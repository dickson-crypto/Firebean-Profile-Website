#!/usr/bin/env python3
"""Deterministic EDM transformer.

Applies four changes to every EDM issue file in this directory:
  1. Magazine text-wrap (right-floated 250px thumbnail) for Sections 02, 03, 04.
  2. Remove the date from the header issue label (keep "Issue 0XX" only).
  3. Replace the Chinese tagline 公關市場解碼 with "PR MARKET DECODED".
  4. Rewrite broken drive.google.com image URLs to the lh3.googleusercontent.com CDN.

Idempotent: sections already carrying a float:right thumbnail are skipped.
Run:  python3 transform_layout.py
"""

import glob
import os
import re
import sys

from bs4 import BeautifulSoup, Comment, Tag

HERE = os.path.dirname(os.path.abspath(__file__))

TAGLINE_CN = "公關市場解碼"  # 公關市場解碼
TAGLINE_EN = "PR MARKET DECODED"

CLEAR_STYLE = "clear:both;height:0;line-height:0;font-size:0;"
FLOAT_STYLE = ("float:right;display:block;width:250px;max-width:250px;"
               "height:auto;margin:{margin};border:0;")

stats = {
    "web_transformed": 0,
    "gmail_transformed": 0,
    "index_transformed": 0,
    "floated_imgs": 0,
    "sections_skipped_idempotent": 0,
    "drive_rewritten": 0,
    "problems": [],
}


# ---------------------------------------------------------------------------
# Change 1 helpers
# ---------------------------------------------------------------------------
def _resize_style(style):
    """Shrink body/bullet/punchline font sizes and line-heights to golden sizes.

    Order matters: 12->11 must run before 13->12 so a size is never stepped
    twice in a single pass.
    """
    style = style.replace("font-size:12px", "font-size:11px")
    style = style.replace("font-size:13px", "font-size:12px")
    style = style.replace("line-height:1.75", "line-height:1.7")
    style = style.replace("line-height:1.6", "line-height:1.55")
    return style


def _resize_subtree(node):
    if isinstance(node, Tag):
        if node.has_attr("style"):
            node["style"] = _resize_style(node["style"])
        for el in node.find_all(True):
            if el.has_attr("style"):
                el["style"] = _resize_style(el["style"])


def _make_clear(soup):
    div = soup.new_tag("div")
    div["style"] = CLEAR_STYLE
    div.append(" ")
    return div


def _float_img(img, margin, alt_default=None):
    img["align"] = "right"
    img["width"] = "250"
    if img.has_attr("height"):
        del img["height"]
    img["style"] = FLOAT_STYLE.format(margin=margin)


def transform_web_section(soup, td, h2_size, img_margin):
    """Magazine-wrap one web section cell. Returns True if transformed."""
    img = td.find("img")
    if img is None:
        return False
    if "float:right" in img.get("style", ""):
        stats["sections_skipped_idempotent"] += 1
        return False

    h2 = td.find("h2")
    if h2 is None:
        return False

    # Float the section image (already positioned before the title).
    _float_img(img, img_margin)
    stats["floated_imgs"] += 1

    # Resize the title.
    old, new = h2_size
    h2["style"] = h2["style"].replace("font-size:" + old, "font-size:" + new)

    # Content region: title + following siblings up to the first CTA/contact
    # table (a direct-child <table> that contains an <a>).
    insertion = None
    content_nodes = [h2]
    for sib in h2.next_siblings:
        if isinstance(sib, Tag):
            if sib.name == "table" and sib.find("a") is not None:
                insertion = sib
                break
            content_nodes.append(sib)

    for node in content_nodes:
        _resize_subtree(node)

    clear = _make_clear(soup)
    if insertion is not None:
        insertion.insert_before(clear)
    else:
        td.append(clear)
    return True


def transform_web(soup):
    specs = [
        ("CASE STUDY 02", ("20px", "18px"), "4px 0 12px 18px"),
        ("SECTION 03", ("20px", "18px"), "4px 0 12px 18px"),
        ("SECTION 04", ("22px", "20px"), "4px 0 14px 18px"),
    ]
    changed = False
    for anchor, h2_size, margin in specs:
        comment = None
        for c in soup.find_all(string=lambda t: isinstance(t, Comment) and anchor in t):
            comment = c
            break
        if comment is None:
            stats["problems"].append("web: anchor '%s' not found" % anchor)
            continue
        tr = comment.find_next("tr")
        if tr is None:
            stats["problems"].append("web: no <tr> after '%s'" % anchor)
            continue
        td = tr.find("td", recursive=False)
        if td is None:
            stats["problems"].append("web: no content <td> after '%s'" % anchor)
            continue
        if transform_web_section(soup, td, h2_size, margin):
            changed = True
    return changed


def transform_gmail_section(soup, container, img_selector, title_cls,
                            title_size, img_margin, trailing_selector,
                            unwrap_selector=None):
    if container is None:
        return False
    img = container.select_one(img_selector)
    if img is None:
        return False
    if "float:right" in img.get("style", ""):
        stats["sections_skipped_idempotent"] += 1
        return False

    # For the case card the image sits inside a full-width wrapper div; unwrap
    # it so the float takes effect against the flowing text.
    if unwrap_selector:
        wrap = container.select_one(unwrap_selector)
        if wrap is not None and img in wrap.descendants:
            wrap.replace_with(img)

    _float_img(img, img_margin)
    stats["floated_imgs"] += 1

    title = container.select_one(title_cls)
    if title is not None and title.has_attr("style"):
        old, new = title_size
        title["style"] = title["style"].replace("font-size:" + old,
                                                 "font-size:" + new)

    # Resize punchline + body (everything that flows around the float).
    for cls in container.select('[class*="punchline"], [class*="body"]'):
        _resize_subtree(cls)

    clear = _make_clear(soup)
    trailing = container.select_one(trailing_selector) if trailing_selector else None
    if trailing is not None:
        trailing.insert_before(clear)
    else:
        container.append(clear)
    return True


def transform_gmail(soup):
    changed = False

    # Section 02 — case card following the "SECTION 02" comment.
    s2_comment = None
    for c in soup.find_all(string=lambda t: isinstance(t, Comment) and "SECTION 02" in t):
        s2_comment = c
        break
    s2 = s2_comment.find_next("div", class_="case-card") if s2_comment else None
    if s2 is None:
        stats["problems"].append("gmail: section 02 case-card not found")
    elif transform_gmail_section(
            soup, s2, "img.case-image", ".case-title", ("20px", "18px"),
            "4px 0 12px 18px", "a.case-cta", unwrap_selector=".case-image-wrap"):
        changed = True

    # Section 03 — industry insight.
    s3 = soup.select_one(".insight-section")
    if s3 is None:
        stats["problems"].append("gmail: insight-section not found")
    elif transform_gmail_section(
            soup, s3, "img.insight-image", ".insight-title", ("20px", "18px"),
            "4px 0 12px 18px", None):
        changed = True

    # Section 04 — why firebean.
    s4 = soup.select_one(".agency-cta-section")
    if s4 is None:
        stats["problems"].append("gmail: agency-cta-section not found")
    elif transform_gmail_section(
            soup, s4, "img.agency-cta-image", ".agency-cta-title", ("22px", "20px"),
            "4px 0 14px 18px", ".contact-box"):
        changed = True

    return changed


# ---------------------------------------------------------------------------
# Change 2 / 3 / 4 (string-level, run on serialized output)
# ---------------------------------------------------------------------------
HEADER_DATE_RE = re.compile(
    r"(Issue\s*\d+)"
    r"(?:\s|&nbsp;| )*"
    r"(?:&middot;|·|‧)"
    r"(?:\s|&nbsp;| )*"
    r"\d{4}-\d{2}-\d{2}"
)

DRIVE_RE = re.compile(r"https?://drive\.google\.com/[^\s\"'<>)]+")


def _drive_repl(match):
    url = match.group(0)
    m = re.search(r"/file/d/([A-Za-z0-9_-]+)", url)
    if not m:
        m = re.search(r"[?&](?:amp;)?id=([A-Za-z0-9_-]+)", url)
    if not m:
        return url
    return "https://lh3.googleusercontent.com/d/%s=w1600" % m.group(1)


def apply_text_changes(html):
    html = HEADER_DATE_RE.sub(r"\1", html)          # Change 2
    html = html.replace(TAGLINE_CN, TAGLINE_EN)      # Change 3
    html, n = DRIVE_RE.subn(_drive_repl, html)       # Change 4
    return html, n


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def process(path):
    with open(path, "r", encoding="utf-8") as fh:
        raw = fh.read()

    name = os.path.basename(path)
    soup = BeautifulSoup(raw, "html.parser")

    if name == "index.html":
        # Layout untouched; only tagline + any drive URLs.
        pass
    elif name.endswith("_gmail.html"):
        if transform_gmail(soup):
            stats["gmail_transformed"] += 1
    else:
        if transform_web(soup):
            stats["web_transformed"] += 1

    html = soup.decode(formatter="html")
    html, drive_n = apply_text_changes(html)
    stats["drive_rewritten"] += drive_n

    if name == "index.html" and (drive_n or TAGLINE_EN in html):
        stats["index_transformed"] += 1

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(html)

    return drive_n


def main():
    files = sorted(glob.glob(os.path.join(HERE, "*.html")))
    per_file_drive = {}
    for path in files:
        before = stats["drive_rewritten"]
        process(path)
        per_file_drive[os.path.basename(path)] = stats["drive_rewritten"] - before

    print("=== TRANSFORM SUMMARY ===")
    print("Web files transformed:   %d" % stats["web_transformed"])
    print("Gmail files transformed: %d" % stats["gmail_transformed"])
    print("Index files touched:     %d" % stats["index_transformed"])
    print("Floated thumbnails added:%d" % stats["floated_imgs"])
    print("Sections skipped (idempotent): %d" % stats["sections_skipped_idempotent"])
    print("Drive URLs rewritten:    %d" % stats["drive_rewritten"])
    print("--- per-file Drive rewrites ---")
    for k in sorted(per_file_drive):
        if per_file_drive[k]:
            print("  %-24s %d" % (k, per_file_drive[k]))
    if stats["problems"]:
        print("--- PROBLEMS ---")
        for p in stats["problems"]:
            print("  " + p)
    else:
        print("No problems.")


if __name__ == "__main__":
    main()
