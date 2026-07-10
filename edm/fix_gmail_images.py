#!/usr/bin/env python3
"""Fix two pre-existing template bugs in the Gmail EDM files only.

BUG 1: Section 04 `class="agency-cta-image"` <img> has a corrupted src
       (URL-encoded body copy instead of a real image URL). Replace it with
       the corresponding web file's S04 agency image src (the <img alt="Firebean
       Agency"> manuscdn URL).

BUG 2: Some case-image <img> tags have alt text with unescaped double quotes,
       which the HTML parser split into garbage attributes. Rebuild those tags
       cleanly, restoring the alt from the web file (internal " replaced by ').

Only *_gmail.html files are modified. Idempotent.
"""
import re
import sys
from pathlib import Path
from html import escape
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
WHITELIST = ("align", "alt", "class", "src", "style", "width", "height")
ORDER = ("align", "alt", "class", "height", "src", "style", "width")
AGENCY_STYLE = ("float:right;display:block;width:250px;max-width:250px;"
                "height:auto;margin:4px 0 14px 18px;border:0;")


def build_tag(attrs):
    parts = []
    for k in ORDER:
        if k in attrs and attrs[k] is not None:
            v = escape(str(attrs[k]), quote=True).replace("&#x27;", "'")
            parts.append(f'{k}="{v}"')
    return "<img " + " ".join(parts) + "/>"


def surviving(tag_html):
    """Whitelisted attributes that survived on a (possibly mangled) tag."""
    img = BeautifulSoup(tag_html, "html.parser").find("img")
    out = {}
    for k in WHITELIST:
        if img.has_attr(k):
            val = img[k]
            out[k] = " ".join(val) if isinstance(val, list) else val
    return out


def web_reference(num):
    soup = BeautifulSoup((HERE / f"edm_{num:03d}.html").read_text("utf-8"),
                         "html.parser")
    agency = soup.find("img", alt="Firebean Agency")
    agency_src = agency["src"] if agency else None
    # Candidate S02/case alts: exclude logos (alt="Firebean") and the agency img.
    cand = []
    for img in soup.find_all("img"):
        alt = img.get("alt", "")
        if alt and alt not in ("Firebean", "Firebean Agency"):
            cand.append(alt)
    return agency_src, cand


def best_alt(garbage_names, candidates):
    """Pick the web alt whose words best overlap the garbage attribute names."""
    words = {re.sub(r'[^0-9a-z]', '', g.lower()) for g in garbage_names}
    words.discard("")
    best, score = None, -1
    for alt in candidates:
        aw = {re.sub(r'[^0-9a-z]', '', w.lower()) for w in alt.split()}
        s = len(words & aw)
        if s > score:
            best, score = alt, s
    return best


def clean_alt(alt):
    return alt.replace('"', "'")


def fix_file(num):
    gpath = HERE / f"edm_{num:03d}_gmail.html"
    html = gpath.read_text("utf-8")
    agency_src, candidates = web_reference(num)
    changed = False

    # --- BUG 1: agency-cta-image src ---
    m = re.search(r'<img[^>]*class="agency-cta-image"[^>]*>', html)
    if m and agency_src:
        attrs = surviving(m.group(0))
        needs = not str(attrs.get("src", "")).startswith("http") or \
            any(a not in WHITELIST
                for a in BeautifulSoup(m.group(0), "html.parser").find("img").attrs)
        if needs:
            attrs["src"] = agency_src
            attrs["alt"] = "Firebean Agency"
            attrs["class"] = "agency-cta-image"
            attrs.setdefault("align", "right")
            attrs.setdefault("style", AGENCY_STYLE)
            attrs.setdefault("width", "250")
            html = html[:m.start()] + build_tag(attrs) + html[m.end():]
            changed = True

    # --- BUG 2: mangled case-image tags ---
    def fix_case(match):
        nonlocal changed
        tag = match.group(0)
        img = BeautifulSoup(tag, "html.parser").find("img")
        garbage = [a for a in img.attrs if a not in WHITELIST]
        if not garbage:
            return tag  # already clean
        attrs = surviving(tag)
        alt = best_alt(garbage, candidates)
        if alt:
            attrs["alt"] = clean_alt(alt)
        attrs["class"] = "case-image"
        changed = True
        return build_tag(attrs)

    html = re.sub(r'<img[^>]*class="case-image"[^>]*>', fix_case, html)

    if changed:
        gpath.write_text(html, "utf-8")
    return changed


def main():
    touched = []
    for n in range(1, 25):
        if fix_file(n):
            touched.append(n)
    print("Modified:", [f"{n:03d}" for n in touched] or "none")


if __name__ == "__main__":
    main()
