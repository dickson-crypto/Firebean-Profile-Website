# Firebean EDM Generation Instruction — Handover Document

**Project:** Firebean weekly EDM series "PR MARKET DECODED"
**Audience:** Hong Kong Government officers & procurement decision-makers (B2G, cold list)
**Purpose:** Detailed build spec for generating / transforming EDM issue HTML files. Follow this end-to-end.
**Reference template (finalized):** Issue 001 (`edm/edm_001.html`)
**Last updated:** July 2026

---

## 1. Project Overview

Firebean is a Hong Kong PR/creative agency. "PR MARKET DECODED" is a weekly EDM series (24 issues) sent to a **cold list** of government civil servants sourced from public government websites — recipients have **not** subscribed. Therefore the EDM must feel like a **professional industry briefing, NOT a promotional mailer or spam**. Value-first: lead with genuinely useful public information, keep Firebean self-promotion to the final section.

### Branding rules (non-negotiable)
- Newsletter name: **PR MARKET DECODED** (English tagline only — do NOT use the Chinese translation 公關市場解碼)
- Issuer: **Firebean**
- Tone: reputable, creative, budget-efficient PR agency; insider briefing voice
- Language of body content: **English** (Chinese allowed only in bilingual section labels and bilingual news item titles where natural)
- The word **"welcome" must NOT appear anywhere** (cold-list strategy — never imply the recipient subscribed or was welcomed). The editorial intro opens with **"Inside PR Market Decoded —"** instead.
- **No personal greeting / no recipient name** anywhere.

---

## 2. Repository & Access

- **GitHub repo:** `dickson-crypto/Firebean-Profile-Website`
- **EDM folder:** `/edm/`
- **Live base URL (GitHub Pages):** `https://dickson-crypto.github.io/Firebean-Profile-Website/edm/`
- **Files per issue (two variants):**
  - `edm_XXX.html` — web preview version (modern browsers, used for "view in browser")
  - `edm_XXX_gmail.html` — legacy-email-safe version (Outlook Express, Apple Mail/OS X, Thunderbird, Yahoo Mail). **Generated from the web version** via `build_legacy_gmail.py` (see §9).
- `index.html` — EDM landing/index page listing all issues.
- **GitHub Pages deploy delay:** ~60 seconds after `git push` before changes are live. Always wait ~60s before verifying a live URL.

### Git workflow
- Identity: `dickson@firebean.net` / Dickson Chan
- Work on `main` branch directly (this project does not use feature branches).
- Commit message convention: short imperative sentence, e.g. `Restructure Issue 005: value-first layout per Issue 001 template`.
- After editing web files, **always regenerate the gmail files** (`python3 build_legacy_gmail.py` from the `edm/` dir), commit both, then push.

---

## 3. Finalized Template Structure (Issue 001 is the canonical reference)

Every issue must follow this top-to-bottom order. The only things that change per issue are the **variable content** (§7): issue number, intro summary, the 2 news items, the market insight, the case study, and project image IDs.

| # | Block | Notes |
|---|-------|-------|
| 1 | **View-in-browser pre-header bar** | Light grey bar, bilingual link only. **No unsubscribe here.** |
| 2 | **Header** | Firebean logo + "PR MARKET DECODED" + "Issue XXX" |
| 3 | **Editorial intro** | Red left accent bar, "Inside PR Market Decoded — …" summary |
| 4 | **Section 01 — 本期資訊 / WHAT'S ON** | 2 news items, each with 30% right-floated thumbnail |
| 5 | **Section 02 — 市場洞察 / MARKET INSIGHT** | Feature story: full-width photo on top, then text + bullets + source |
| 6 | **Section 03 — CASE STUDY** | Dept label → hero banner ("Beyond Information…") → case study article |
| 7 | **Stats strip** | 53+ / 18+ / 360+ / 1.5M+ |
| 8 | **Section 04 — WHY FIREBEAN + CTA** | Agency capability + contact box + "Explore Our Work" button |
| 9 | **Footer** | Logo, links, address, copyright, Unsubscribe/Privacy/Terms |

### What was removed vs. the old layout (issues 002–024 original state)
The original issues 002–024 have an **old layout** that must be transformed to the new template:
- OLD: standalone HERO image at top + "Welcome" intro → SECTION 01 CASE STUDY → SECTION 02 CASE STUDY (a second/non-gov profile) → SECTION 03 INDUSTRY INSIGHT → SECTION 04 WHY FIREBEAN.
- NEW: delete the top standalone hero + welcome; **delete the old Section 02** (the second/non-gov event profile — e.g. Issue 001's was "K-palette"); promote the industry insight to its own numbered section; add the 2 news items as the new opening Section 01; move the hero design into the Case Study section as its banner.

---

## 4. Section-by-Section Spec

### Global wrapper & container
- Outer `<table>` `bgcolor="#EBEBEB"`, centered cell with `padding:32px 16px`.
- Email container `<table>` `bgcolor="#FFFFFF"`, `max-width:620px;width:100%`, `border:1px solid #E0E0E0`.
- Body font stack: `'Helvetica Neue',Arial,sans-serif` on **every** text element (inline).
- Brand red: `#E8291C`. Body text dark grey `#333333`/`#444444`. Muted grey `#666666`/`#888888`/`#AAAAAA`/`#BBBBBB`.
- Head `<meta charset="utf-8"/>`, viewport meta, `<meta content="IE=edge" http-equiv="X-UA-Compatible"/>`, and the MSO OfficeDocumentSettings comment block (keep it — needed for Outlook VML).

### Block 1 — View-in-browser pre-header bar
- `bgcolor="#F0F0F0"`, `padding:9px 24px`, centered, `border-bottom:1px solid #E4E4E4`.
- One link: `View this email in your browser &nbsp;|&nbsp; 在瀏覽器中查看`, `font-size:11px`, `color:#666666`, `text-decoration:none`.
- href = the issue's own live URL, e.g. `https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001.html`, `target="_blank"`.
- **No unsubscribe link in this bar.**

### Block 2 — Header
- `bgcolor="#FFFFFF"`, `padding:22px 32px 18px`, `border-bottom:3px solid #E8291C`.
- Left: logo image (36×36, `object-fit:contain`) + `<span>` "FIREBEAN" (`font-size:18px;font-weight:300;letter-spacing:0.25em`).
- Right: "PR MARKET DECODED" (`color:#E8291C;font-size:12px;font-weight:700;letter-spacing:0.12em`) + "Issue XXX" (`color:#999999;font-size:11px`).
- Logo icon URL: `https://files.manuscdn.com/user_upload_by_module/session_file/310519663437368766/OXsmmaNIDdCdSALu.png`

### Block 3 — Editorial intro
- `bgcolor="#FFFFFF"`, `padding:24px 32px`. Inner table `max-width:556px`.
- `<td>` with `padding-left:14px;border-left:4px solid #E8291C;` (the red accent bar).
- `<p>` `font-size:14px;color:#333333;line-height:1.6`.
- Opens: **"Inside <strong>PR Market Decoded</strong> — <strong>Firebean</strong>'s insider briefing on what's actually working in Hong Kong's PR and experiential marketing. This issue: <SUMMARY>.**
- Bold "PR Market Decoded" and "Firebean".
- **Per-issue variable:** the `<SUMMARY>` after "This issue:" changes each issue (see §7). Keep it to one sentence summarizing the issue's contents.

### Block 4 — Section 01: WHAT'S ON (2 news items)
- Section label row: `<td>` "SECTION 01 — 本期資訊 / WHAT'S ON" (`font-size:10px;font-weight:700;letter-spacing:0.2em;text-transform:uppercase;color:#BBBBBB`) + a `<td>` with `border-top:1px solid #E8E8E4;` (the trailing divider line).
- Each news item in its own `<tr>` with `bgcolor="#FAFAFA"`.
- **Per news item structure (magazine-wrap):**
  1. Tag row: red box `<td bgcolor="#E8291C">` with category (e.g. `GOVERNMENT · EXHIBITION`, `GOVERNMENT · FAMILY`) + grey source text (e.g. `Chinese Culture Promotion Office (LCSD)`).
  2. Thumbnail `<img align="right" ... width="170" style="float:right;display:block;width:170px;max-width:170px;height:auto;margin:4px 0 12px 18px;border:0;">` — **30% of content width (~170px)**, right-floated.
  3. `<h2>` catchy bilingual title, `font-size:18px;font-weight:900`.
  4. Punchline: italic grey text in a `<div>` with `border-left:3px solid #E8291C`.
  5. Body `<p>` `font-size:12px;color:#444444;line-height:1.7`.
  6. "Learn More →" button: `<td>` with `border:1.5px solid #111111;padding:9px 18px;` + link.
  7. Clear div: `<div style="clear:both;height:0;line-height:0;font-size:0;">&nbsp;</div>` (REQUIRED after each floated item).
- Between the two news items: a 1px divider `<td style="border-top:1px solid #E8E8E4;height:1px;font-size:0;line-height:0;">&nbsp;</td>`.

### Block 5 — Section 02: MARKET INSIGHT (feature story)
- Section label "SECTION 02 — 市場洞察 / MARKET INSIGHT".
- `bgcolor="#FAFAFA"`, `border-bottom:1px solid #EEEEEE`.
- Red pill label (e.g. "Phygital Civic Engagement / Hybrid Events Market Growth"): `<div style="display:inline-block;background-color:#E8291C;color:#FFFFFF;font-size:10px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;padding:4px 10px;">`.
- **Full-width feature photo on top:** `<img style="display:block;width:100%;max-width:556px;height:auto;margin-bottom:18px;object-fit:cover;" width="556">` — NOT floated.
- `<h2>` insight title (e.g. "Trend Watch: The 'Phygital' Revolution Is Reshaping Gov Comms"), `font-size:18px;font-weight:900`.
- Punchline (italic, red left bar) + body paragraphs.
- Bullet list using a `<table>` with `→` arrows in red (`color:#E8291C;font-weight:bold`) in the first column.
- Source line at the bottom: italic `font-size:11px;color:#888888`, citing the data sources with real publication names.
- After this section: a red divider `<tr><td bgcolor="#E8291C" style="height:2px;font-size:0;line-height:0;">&nbsp;</td></tr>`.

### Block 6 — Section 03: CASE STUDY
**Internal order (IMPORTANT — matches user's finalized sequence):**
1. Section label "SECTION 03 — CASE STUDY".
2. **Dept label (top):** red box "GOVERNMENT" + grey dept name (e.g. `Education Bureau — Curriculum Development Institute`). `bgcolor="#FFFFFF"`, `padding:16px 32px 0`.
3. **Hero banner:** the big exhibition-style photo with overlay. Uses `background-image` on a `<td>` **plus** VML (`<!--[if gte mso 9]> <v:rect>...<v:fill type="tile" src="..."/> <v:textbox>`) for Outlook. Inside: a spacer row (`height:220px`) + a dark gradient overlay row (`background:linear-gradient(to top,rgba(0,0,0,0.82) 0%,rgba(0,0,0,0) 100%);background-color:rgba(0,0,0,0.7)`) containing the red "GOVERNMENT & PUBLIC SECTOR" pill + the headline "Beyond Information: How HK's Best Campaigns Turn Policy into Experience" (`font-size:24px;font-weight:900;color:#FFFFFF`). The hero headline is the **issue theme** — it can vary per issue but must be a policy→experience style statement.
4. **Case study article (bottom):**
   - Tram/project photo as a **30% right-floated thumbnail** (`width="170"`, magazine-wrap, same pattern as news thumbnails).
   - `<h2>` case study title (e.g. "When a Tram Becomes a Classroom: Reimagining Civic Education for the Public"), `font-size:20px;font-weight:900`.
   - Punchline (italic, red left bar).
   - Body paragraphs (`font-size:13px;color:#444444;line-height:1.75`).
   - "Key Outcomes:" bullets (red `→` arrows table).
   - "VIEW FULL CASE STUDY →" button (`border:1.5px solid #111111`), linking to `https://firebean.net/profile.html?id={PROJECT_ID}`.
   - Clear div after the floated thumbnail.

### Block 7 — Stats strip
- `bgcolor="#111111"`, `padding:28px 16px`. 4-column `<table width="100%">`, each `width="25%"` centered.
- Values: **53+ Gov't Projects · 18+ Years Experience · 360+ Completed Projects · 1.5M+ Participants Reached** (the `+`/`M+` in red `#E8291C`).
- These stats are **constant across all issues** — do not change.

### Block 8 — Section 04: WHY FIREBEAN + CTA
- `bgcolor="#FFFFFF"`, `border-top:4px solid #E8291C`.
- Label "SECTION 04 — WHY FIREBEAN" in red.
- Agency photo as right-floated thumbnail `width="250"` (larger than news thumbs).
- `<h2>` headline "53 Government Projects. One Agency. A Track Record That Speaks for Itself."
- Punchline + body + 4 value-prop bullets (red arrows).
- Clear div.
- Contact box: `<table>` `bgcolor="#F8F8F6;border-left:3px solid #E8291C"`, "READY TO TALK?" + `hello@firebean.net →` (mailto link).
- CTA button: `<td bgcolor="#E8291C">` "Explore Our Work →" linking to `https://firebean.net`.

### Block 9 — Footer
- `bgcolor="#F5F5F3"`, `border-top:3px solid #E8291C"`, `padding:28px 32px 24px`.
- Logo (28×28) + "FIREBEAN".
- Divider, then links row: Website | Our Work | Contact Us | PR Market Decoded.
- Address: `Firebean Limited · Unit A, 23/F, Morrison Plaza, 5-9A Morrison Hill Rd, Wan Chai, Hong Kong` + `Tel: +852 3622 2784 · hello@firebean.net`.
- Divider, then legal.
- **MUST contain:** `© 2026 Firebean Limited. All rights reserved.` and an **Unsubscribe** link (see §10) + Privacy Policy + Terms of Service.
- **MUST NOT contain** the old "You are receiving this newsletter because you subscribed… / please add hello@firebean.net to your address book" paragraph — this was deleted (cold list, never subscribed; claiming subscription is misleading and a PDPO risk).

---

## 5. Styling Rules — Legacy Email Compatibility (CRITICAL)

The EDM must render in Outlook Express, Apple Mail (OS X), Thunderbird/Mozilla, and Yahoo Mail. Rules:

- **Table-based layout only.** Use nested `<table>`, `<tr>`, `<td>` with `align`, `valign`, `width`, `bgcolor`, `cellpadding="0"`, `cellspacing="0"`, `border="0"`.
- **All CSS inline** on each element. No `<style>` blocks for layout (only the MSO comment is allowed). No external CSS, no `<link>`.
- **Forbidden CSS** (do NOT use): `flex`, `grid`, `position` (`absolute`/`relative`/`fixed`), `float` is OK for web version but converted to nested tables for gmail (see §9), CSS pseudo-elements (`:before`/`:after`), `transform`, `animation`.
- **`object-fit` is OK in the web version** but is stripped in the gmail version. Always also set explicit `width`/`height` attributes so sizing holds when object-fit is removed.
- **Images:** always set `display:block;` to avoid gaps; always include `width` and `height` attributes; always provide `alt`.
- **Buttons:** build with `<table><tr><td style="border:1.5px solid #111111;padding:9px 18px;"><a...>`. Do NOT use `<button>` or CSS background-only buttons.
- **Hero/banner background images:** use `background` on a `<td>` **plus** VML `<!--[if gte mso 9]> <v:rect>...` for Outlook. The gmail version replaces the `linear-gradient` overlay with a solid dark block (`background-color:#111111`).
- **Magazine-wrap thumbnails:** web version uses `<img align="right" style="float:right;...">`; gmail version converts these to `<table align="right" width="170"><tr><td><img.../></td></tr></table>`.
- **No WebP** in the gmail version — convert to JPEG (see §8).
- Use HTML entities for special chars: `&mdash;`, `&ndash;`, `&rarr;`, `&middot;`, `&rsquo;`, `&copy;`, `&amp;`, `&nbsp;`.
- Keep `<tr>`/`</tr>` and `<table>`/`</table>` tags balanced (verify counts in QA).

---

## 6. Image Handling

### Allowed image hosts
1. **manuscdn (primary for this project's assets):** `https://files.manuscdn.com/user_upload_by_module/session_file/310519663437368766/{HASH}.jpg` — all `.jpg` work in browsers and email.
2. **GitHub Pages (committed images):** `https://dickson-crypto.github.io/Firebean-Profile-Website/edm/email-img/{NAME}.jpg` — use for any newly-sourced/converted images (e.g. news photos). Commit the file into `edm/email-img/`.
3. **Google Drive CDN:** `https://lh3.googleusercontent.com/d/{FILE_ID}=w1600` — reliable for Drive-hosted assets.
4. **firebean.net WebP:** `https://firebean.net/data/images/{project_id_lowercase}-photo-{N}.webp` — **WebP does NOT render in legacy email clients.** If used in the web version, the gmail build script converts the URL to a committed JPEG in `edm/email-img/`. You must pre-convert and commit the JPEG yourself (name it `{project_id_lowercase}-photo-{N}.jpg`).

### Rules
- **Never hotlink external gov/venue images directly in the final EDM** — download them, commit to `edm/email-img/`, and reference the GitHub Pages URL. (Hotlinks break and gov sites may block hotlinking.)
- For each new issue's case study, the project images come from firebean.net (`{project_id}-photo-N.webp`) — convert to JPG and commit, or use the manuscdn equivalent.
- News item photos: source from official venues (e.g. HK Museum of History, LCSD/EKCC), download, commit to `edm/email-img/`, reference via GitHub Pages URL.
- Logo icon (constant): `https://files.manuscdn.com/user_upload_by_module/session_file/310519663437368766/OXsmmaNIDdCdSALu.png`

---

## 7. Per-Issue Variable Content

For each issue `edm_XXX.html`, these elements change:

| Variable | What to set |
|----------|-------------|
| **Issue number** | "Issue XXX" in header; "Issue XXX" in `<title>`; filename `edm_XXX.html` |
| **`<title>`** | `Firebean EDM — Issue XXX | {issue theme headline}` |
| **Intro summary** | The sentence after "This issue:" in the editorial intro — summarize this issue's 2 campaigns + trend + Firebean case |
| **News items (2)** | Two real, current Hong Kong government / LCSD / public-sector events or exhibitions. Research online (see §11). Each needs: category tag, source org, bilingual title, punchline, body, photo (committed JPEG), Learn More link (official URL) |
| **Market insight** | A trend + real data point with cited source (e.g. MarketIntelo report, journal). Title, punchline, body, 3–4 bullets, source line |
| **Case study** | From the Firebean project for that issue (project ID below). Dept label, hero headline (issue theme), case study title, body, outcomes, VIEW FULL CASE STUDY link `https://firebean.net/profile.html?id={PROJECT_ID}` |
| **Hero headline** | The issue theme statement (policy→experience style), e.g. Issue 001: "Beyond Information: How HK's Best Campaigns Turn Policy into Experience" |
| **Project image IDs** | The case study's images (firebean.net WebP → convert to JPEG) |

### Project IDs per issue (case study source)
```
001: FB2026048   002: FB2026010   003: FB2026009   004: FB2026067
005: FB2026012   006: FB2025999   007: FB2025771   008: FB2026004
009: FB2025013   010: FB2026047   011: FB2025012   012: FB2025017
013: FB2026065   014: FB2026011   015: FB2026074   016: FB2026062
017: FB2026008   018: FB2026037   019: FB2026070   020: FB2026050
021: FB2024005   022: FB2026002   023: FB2024016   024: FB2024018
```
Case study link format: `https://firebean.net/profile.html?id={lowercase_id}` (e.g. `fb2026048`).

### Constant elements (do NOT change across issues)
- Stats strip (53+ / 18+ / 360+ / 1.5M+)
- Section 04 (Why Firebean) body text and value props
- Footer address, phone, links
- Logo, brand colors, typography

---

## 8. Generating the Gmail / Legacy Variant

After finishing (or editing) each `edm_XXX.html`, regenerate ALL gmail files:

```bash
cd /home/user/workspace/Firebean-Profile-Website/edm
python3 build_legacy_gmail.py
```

`build_legacy_gmail.py` reads each `edm_001.html`…`edm_024.html` and writes `edm_001_gmail.html`…`edm_024_gmail.html`, applying:
1. **WebP → JPEG** on GitHub Pages (`firebean.net/.../*.webp` → `.../email-img/*.jpg`). You must have pre-committed the JPEGs.
2. **Strip `object-fit`** (unsupported; sizing kept via width/height attrs).
3. **Hero `linear-gradient` overlay → solid `background-color:#111111`** (readable fallback).
4. **Magazine-wrap `<img align="right" style="float:right">` → nested `<table align="right" width="250">`** (most legacy-safe wrap).

If you add new transformation needs (e.g. a new CSS feature legacy clients choke on), extend `build_legacy_gmail.py` rather than hand-editing each gmail file.

---

## 9. QA / Verification Checklist (run before pushing each issue)

Open the live URL (after ~60s deploy delay) and verify:

- [ ] **Structure order:** View-in-browser bar → header → intro → S01 (2 news) → S02 (insight) → S03 (case study: dept label → hero → article) → stats → S04 (why firebean) → footer.
- [ ] **No "welcome"** anywhere (case-insensitive search = 0). Intro opens with "Inside PR Market Decoded —".
- [ ] **No "公關市場解碼"** (must use English "PR MARKET DECODED" only).
- [ ] **No personal greeting / recipient name.**
- [ ] **Footer:** has "© 2026 Firebean Limited" + Unsubscribe link; does NOT have "because you subscribed" / "add to your address book".
- [ ] **Top bar** has only "View in browser", no unsubscribe.
- [ ] **2 news items** each have: thumbnail (~170px, right-floated), title, punchline, body, Learn More link (live official URL).
- [ ] **Market insight** has full-width photo, cited source line, bullets.
- [ ] **Case study** internal order: dept label → hero banner → article; tram/project photo is 30% right-floated thumbnail; VIEW FULL CASE STUDY links to correct project ID.
- [ ] **Stats strip** shows 53+ / 18+ / 360+ / 1.5M+.
- [ ] **0 broken images** (all image URLs return HTTP 200).
- [ ] **HTML tags balanced** (count `<table>`=`</table>`, `<tr>`=`</tr>`, `<td>`=`</td>`).
- [ ] **Forbidden CSS = 0** in gmail version (no flex/grid/position/object-fit/pseudo).
- [ ] **Gmail version regenerated** (`build_legacy_gmail.py`) and committed alongside the web version.
- [ ] Render-check in a browser at ~720px width; no text overflow, no black boxes, no broken layout.

---

## 10. Unsubscribe Handling

- The **footer Unsubscribe link** is the only unsubscribe mechanism. Current href: `https://firebean.net/edm/unsubscribe.html?email=` (the recipient email is appended at send time by the sending tool).
- The dedicated unsubscribe page / Google Form wiring (feeding the "Unsubscribe Responses" sheet in the master Google Sheet) is a separate pending task — not yet built. Until built, keep the footer unsubscribe link pointing at `https://firebean.net/edm/unsubscribe.html?email=`.
- **Never** add an unsubscribe link to the top pre-header bar (removed by design).

---

## 11. Content Sourcing Guidance (for the 2 news items + market insight)

- **News items** must be real, current, Hong Kong government / LCSD / public-sector events or exhibitions (e.g. museum exhibitions, the International Arts Carnival, government-organised public programmes). Source from official `.gov.hk` sites: `lcsd.gov.hk`, `ccpo.gov.hk`, `hk.history.museum`, `ekcc.hk`, `hkiac.gov.hk`, `gov.hk` press releases. Always cite the official Learn More URL.
- **Market insight** must include a real, citable data point (market size + CAGR from a named report, or a named journal). Cite the source in the italic source line. Do not fabricate statistics.
- Download event/exhibition photos from official venues, commit to `edm/email-img/`, reference via GitHub Pages URL. Do not hotlink.
- Keep news items text-only-friendly: a thumbnail + short punchline + one body paragraph is enough.

---

## 12. PDPO Compliance Notes (context — do not ignore)

- The recipient list is a **cold list** sourced from public government civil-servant websites; recipients have **not consented** to receive marketing.
- Under Hong Kong's Personal Data (Privacy) Ordinance (PDPO) Part VI A, direct marketing requires the data subject's consent; consent cannot be inferred from silence, and there is no general exemption for public-domain data.
- Therefore: **never imply subscription** (no "welcome", no "you are receiving this because you subscribed"). Always include a working **Unsubscribe** option in the footer. Keep the content value-first and informational to reduce spam-complaint risk.
- This is a compliance risk the user has accepted; the EDM design mitigates (value-first, no subscription claims, unsubscribe present). Do not add wording that claims or implies consent.

---

## 13. Quick Reference — Issue 001 Live URLs

- EDM index: https://dickson-crypto.github.io/Firebean-Profile-Website/edm/index.html
- Issue 001 (template reference, web): https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001.html
- Issue 001 (gmail/legacy): https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001_gmail.html
- Firebean website: https://www.firebean.net
- Master Google Sheet ID: `1Ms1Q1i7uJg0ilvW4g1PezBm7mTCNKcYJT_c5-weUBNc` (sheets: Basic Info, EDM_Database, Email list, Unsubscribe Responses, GBP_AutoPost)

---

## 14. Definition of Done (per issue)

An issue is complete when:
1. `edm_XXX.html` matches the Issue 001 template structure with that issue's variable content.
2. `edm_XXX_gmail.html` regenerated via `build_legacy_gmail.py`.
3. All QA checklist items pass (structure, no welcome, no 公關市場解碼, footer correct, 0 broken images, tags balanced, forbidden CSS=0 in gmail).
4. Both files committed and pushed to `main`; live URL verified after ~60s.
5. `index.html` lists/links the issue if needed.
