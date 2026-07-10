# Firebean EDM System — Master Prompt & Handover Document
**Version:** 1.0 | **Prepared by:** Manus AI | **Date:** July 2026
**Handover Target:** Perplexity AI (or any capable AI agent)

---

## 1. PROJECT OVERVIEW & MISSION

You are continuing the production of **Firebean's weekly EDM series** titled **"公關市場解碼"** (PR Market Decoded). This is a professional B2G (Business-to-Government) email newsletter targeting **Hong Kong Government officers and procurement decision-makers**.

**The core objective:** Position Firebean Limited as the most reputable, creative, and budget-efficient PR and events agency for government departments to include on their approved contractor lists. The EDM must NOT feel like a promotional mailer. It must feel like a **professional industry briefing** that government officers actually want to read.

**Firebean Limited:**
- Website: https://www.firebean.net
- Portfolio: https://firebean.net/work.html
- Contact: hello@firebean.net | +852 3622 2784
- Address: Unit A, 23/F, Morrison Plaza, 5-9A Morrison Hill Rd, Wan Chai, Hong Kong
- GitHub (EDM hosting): https://github.com/dickson-crypto/Firebean-Profile-Website
- Live EDM index: https://dickson-crypto.github.io/Firebean-Profile-Website/edm/index.html

---

## 2. DATA SOURCES

### 2A. Master Project Database (Google Sheet)
**URL:** https://docs.google.com/spreadsheets/d/1Ms1Q1i7uJg0ilvW4g1PezBm7mTCNKcYJT_c5-weUBNc/edit

**Sheet: "Basic Info"** — Contains all 104 Firebean project profiles with these columns:
| Column | Description |
|---|---|
| Client Name | Client organisation name |
| Project Name | Project/event name |
| Event Date | Date of event (e.g. "2026 Apr") |
| Category (Who we help) | GOVERNMENT & PUBLIC SECTOR / LIFESTYLE & CONSUMER / F&B & HOSPITALITY / MALLS & VENUES |
| Scope of Work | Comma-separated list of services delivered |
| Web EN | Full English website content (HTML) — use this as the primary source for S1 and S2 content |
| LinkedIn Post | LinkedIn-formatted post — use as secondary reference for tone |
| Drive Folder Link | Google Drive folder containing project photos |
| Hero Photo Picker | "PHOTO 1", "PHOTO 2", etc. — indicates which photo to use as hero |
| Project_id | Unique ID e.g. "FB2026048" — used in profile URLs |

**Sheet: "EDM_Database"** — Your completed EDM content database (Issues #1–#24 already done). Each row = one EDM issue with 36 columns (A–AJ). When generating new issues, append new rows here.

### 2B. Firebean Website Profile URLs
- Profile page format: `https://firebean.net/profile.html?id=fb[PROJECT_ID_LOWERCASE]`
- Example: `https://firebean.net/profile.html?id=fb2026048`
- Work listing: `https://firebean.net/work.html#[PROJECT_ID]`

### 2C. Drive Photo URL Format
To get a direct-display URL from a Google Drive file ID:
```
https://drive.google.com/uc?id=[FILE_ID]&export=view
```
The file ID is extracted from the Drive Folder Link. List files in the folder and find `photo_N.jpg` where N matches the Hero Photo Picker number.

### 2D. Existing EDM HTML Files (Reference Templates)
All 24 issues already exist in the GitHub repo. Use Issue #1 as the canonical template:
- **Web version:** https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001.html
- **Gmail version:** https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001_gmail.html
- **Raw HTML (web):** https://raw.githubusercontent.com/dickson-crypto/Firebean-Profile-Website/main/edm/edm_001.html
- **Raw HTML (gmail):** https://raw.githubusercontent.com/dickson-crypto/Firebean-Profile-Website/main/edm/edm_001_gmail.html

---

## 3. EDM STRUCTURE — 4 SECTIONS PER ISSUE

Every EDM issue contains exactly these 4 sections in this order:

### SECTION 1 — Featured Government Project (Case Study)
**Purpose:** Showcase a recent Firebean government project. Demonstrate capability, creativity, and execution excellence to procurement officers.
**Source:** Pull from "Basic Info" sheet, filter `Category = GOVERNMENT & PUBLIC SECTOR`, sort by date descending. Never repeat a project already used.
**Content rules:**
- **Catchy Title:** 8–12 words. Action-oriented, outcome-focused. E.g. "When a Tram Becomes a Classroom: Reimagining Civic Education"
- **Punchline:** 1 italic sentence (15–20 words). The hook that makes a government officer keep reading.
- **Body content:** 150–200 words. Structure: Challenge → Firebean Solution → Key Outcomes (3 bullet points using → arrows). Write in third person. Past tense. No promotional language. Focus on methodology and results.
- **Hero image:** Use the Drive photo URL from the project's folder (Hero Photo Picker column). Format: `https://drive.google.com/uc?id=[FILE_ID]&export=view`
- **CTA link:** `https://firebean.net/profile.html?id=fb[project_id_lowercase]`
- **Category tag:** "GOVERNMENT & PUBLIC SECTOR" (red badge)

### SECTION 2 — Cross-Industry Inspiration (Non-Gov Project, Gov-Relevant Angle)
**Purpose:** Show commercial-grade methodology that is directly transferable to government campaigns. Broaden the reader's thinking about what's possible.
**Source:** Pull from "Basic Info" sheet, filter `Category ≠ GOVERNMENT & PUBLIC SECTOR`, sort by date descending. Never repeat a project already used.
**Content rules:**
- **Catchy Title:** 8–12 words. Frame the commercial project as a lesson for government. E.g. "The Gamification Formula: How a Beauty Brand Cracked Public Participation"
- **Punchline:** 1 italic sentence. Must directly reference the government application. E.g. "If a cosmetics booth can drive civic-style engagement, imagine what it can do for your next departmental campaign."
- **Body content:** 150–200 words. Structure: Commercial challenge → Firebean solution → **Government Takeaway** section (3–4 bullet points). The Government Takeaway is the most important part — explicitly connect the commercial methodology to government use cases (public health, road safety, civic education, environmental campaigns, etc.).
- **Hero image:** Drive photo URL from the project folder.
- **CTA link:** `https://firebean.net/profile.html?id=fb[project_id_lowercase]`
- **Category tag:** Use the project's actual category (e.g. "LIFESTYLE & CONSUMER") — dark/black badge

### SECTION 3 — Market Insight & Trend Watch
**Purpose:** Provide genuine value to the government officer. Make them feel informed, not sold to. This is the section that prevents the EDM from being treated as spam.
**Source:** Research fresh market data from credible sources. Each issue must cover a UNIQUE topic not covered in previous issues.
**Content rules:**
- **Insight Topic Tag:** 5–8 words (red badge). E.g. "Phygital Civic Engagement / Hybrid Events Market Growth"
- **Catchy Title:** 8–12 words. Data-forward. E.g. "Trend Watch: The 'Phygital' Revolution Is Reshaping How Governments Communicate"
- **Punchline:** 1 italic sentence. The data hook.
- **Body content:** 150–180 words. MUST include: (1) Opening statistic with source, (2) Trend explanation, (3) 3–4 bullet points of implications specifically for HK government departments, (4) Source citation line at the bottom.
- **Image:** AI-generated image relevant to the topic. 16:9 ratio. Professional editorial style. Navy blue / teal colour palette. No text overlay.
- **Credible sources to use:** McKinsey, Deloitte, PwC, HKSAR Policy Addresses, Digital Policy Office HK, MarketIntelo, Statista, academic journals (Tandfonline, MDPI), industry reports.

### SECTION 4 — Why Firebean (Agency CTA)
**Purpose:** Reinforce Firebean's credentials and invite the reader to connect. Keep it concise and confident — not pushy.
**Content rules:**
- **Title:** Rotate between 3–4 variants. E.g. "53 Government Projects. One Agency. A Track Record That Speaks for Itself." / "Your Strategic Partner for High-Impact Civic Campaigns" / "Commercial-Grade Innovation. Public Sector Accountability."
- **Punchline:** 1 italic sentence.
- **Body:** 100–150 words. Key stats: 53+ gov projects, 104+ case studies, 18+ years experience, 360+ completed projects, 1.5M+ participants reached. End with portfolio link.
- **Image:** AI-generated image. Professional agency/team scene. No text overlay.
- **CTA button:** "Explore Our Work →" → links to https://firebean.net
- **Contact box:** hello@firebean.net

---

## 4. BRAND DESIGN SYSTEM

### Colour Palette
| Token | Hex | Usage |
|---|---|---|
| Firebean Red | `#E8291C` | Primary accent, section dividers, CTA buttons, bullet arrows, tags |
| Black | `#111111` | Headlines, logo text, dark tags |
| Dark Grey | `#444444` | Body text |
| Medium Grey | `#666666` | Punchlines, secondary text |
| Light Grey | `#AAAAAA` | Meta text, labels |
| Off-White | `#FAFAFA` | Section backgrounds (S3) |
| White | `#FFFFFF` | Main card background |
| Outer BG | `#EBEBEB` | Email outer wrapper background |

### Typography
- **Primary font:** `'Helvetica Neue', Arial, sans-serif` (email-safe fallback)
- **Web font (Gmail version only):** `'Noto Sans TC'` from Google Fonts (supports Traditional Chinese)
- **Headline sizes:** H1 = 26px (hero), H2 = 20–22px (section titles), H3 = 18px
- **Body text:** 13px, line-height 1.75
- **Meta/labels:** 10–11px, letter-spacing 0.15–0.2em, UPPERCASE

### Logo
- Icon: `https://files.manuscdn.com/user_upload_by_module/session_file/310519663437368766/OXsmmaNIDdCdSALu.png` (36×36px)
- Wordmark: "FIREBEAN" in font-weight 300, letter-spacing 0.25em
- Tagline (red, uppercase): "公關市場解碼"

---

## 5. HTML TECHNICAL SPECIFICATIONS

### Two Output Files Per Issue
Every EDM issue requires TWO HTML files:

#### File 1: Web Version (`edm_NNN.html`)
- **Purpose:** Hosted on GitHub Pages as a browser-viewable webpage
- **Rendering:** Table-based HTML (MSO/Outlook-safe) with VML fallback for background images
- **Pre-header link:** `https://firebean.net/edm/edm_NNN.html`
- **Hero image technique:** `background` attribute on `<td>` with VML fallback for Outlook
- **Bullet lists:** Use `<table>` with `→` arrow in first `<td>` (18px wide, red, bold)
- **Container width:** 620px max, centered
- **File naming:** `edm_001.html`, `edm_002.html`, ... `edm_024.html`

#### File 2: Gmail/Email Version (`edm_NNN_gmail.html`)
- **Purpose:** Paste-ready HTML for Gmail, Mailchimp, Klaviyo, or any ESP
- **Rendering:** Div-based with inline CSS (no `<style>` blocks except for `@media` queries and `::before` pseudo-elements)
- **Pre-header link:** `https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_NNN.html`
- **Hero image technique:** `<img>` tag with absolute-positioned overlay div
- **Bullet lists:** `<ul>` with `list-style:none` and CSS `::before` pseudo-element (→ for case studies, ▸ for insights)
- **Mobile responsive:** `@media (max-width: 640px)` breakpoints for font sizes and layout
- **File naming:** `edm_001_gmail.html`, `edm_002_gmail.html`, ... `edm_024_gmail.html`

### Shared HTML Structure (Both Versions)
```
[Pre-header bar] — "View in browser" link
[Header] — Logo + Issue number + Date + "公關市場解碼" tagline
[Hero] — Full-width image (340px height) + gradient overlay + title
[Issue Intro] — 2–3 sentence welcome paragraph
[Section 01] — Gov case study card
[Red divider line]
[Section 02] — Non-gov case study card
[Stats strip] — Black background: 53+ Gov Projects | 18+ Years | 360+ Projects | 1.5M+ Participants
[Section 03] — Industry insight (grey background #FAFAFA)
[Section 04] — Why Firebean CTA (white background, top border 4px red)
[Footer] — Logo + links + address + legal + unsubscribe
```

### Section 01 & 02 Card HTML Pattern
```html
<!-- Category tag (red for gov, black for non-gov) -->
<!-- Client name (grey, small) -->
<!-- Hero image: 100% width, 240px height, object-fit:cover -->
<!-- Title: 20px, font-weight 900, #111 -->
<!-- Punchline: 13px, italic, #666, left border 3px #E8291C -->
<!-- Body: paragraphs + bullet table with → arrows -->
<!-- CTA button: border 1.5px solid #111, 11px uppercase text -->
```

### Stats Strip HTML Pattern
```html
<table bgcolor="#111111" width="100%">
  <tr>
    <td align="center">53<span color="#E8291C">+</span> Gov't Projects</td>
    <td align="center">18<span color="#E8291C">+</span> Years Experience</td>
    <td align="center">360<span color="#E8291C">+</span> Completed Projects</td>
    <td align="center">1.5<span color="#E8291C">M+</span> Participants Reached</td>
  </tr>
</table>
```

### Footer Constants (Use Exactly)
```
Firebean Limited · Unit A, 23/F, Morrison Plaza, 5-9A Morrison Hill Rd, Wan Chai, Hong Kong
Tel: +852 3622 2784 · hello@firebean.net
Unsubscribe: https://firebean.net/edm/unsubscribe.html?email=
```

---

## 6. CONTENT WRITING METHODOLOGY & TONE

### Target Reader Profile
- **Who:** Hong Kong Government department heads, procurement officers, PR/communications managers
- **Seniority:** D2–D4 civil service grade, or equivalent in statutory bodies
- **Pain points:** Tight budgets (70% marketing / 30% technical split in tenders), need for reputable contractors, pressure to justify creative spend, risk-averse decision-making
- **What they DON'T want:** Sales pitches, event invitations, generic promotions
- **What they DO want:** Industry intelligence, peer validation, data-backed insights, proof of track record

### Writing Principles
1. **Insight-first, promotion-second.** The reader should gain value from Section 3 even if they never hire Firebean.
2. **Specificity over generality.** Name the department, the project, the methodology. Vague claims lose credibility.
3. **Data anchors every claim.** Every market insight must cite a source. Every outcome bullet must be concrete.
4. **Government empathy.** Always frame commercial examples through the lens of "what this means for your department." Bridge the gap explicitly.
5. **Confident, not boastful.** Firebean's track record speaks. State facts, don't oversell.
6. **Short sentences, high density.** Government readers are busy. Every sentence must earn its place.
7. **No jargon without explanation.** If using "phygital" or "KOL," briefly define it.

### Subject Line Formula
- Must be insight-driven, not promotional
- 6–10 words
- Options: Data-led ("The 12.8% Growth Trend Reshaping Gov Campaigns") / Question ("Is Your Department Ready for AI-Powered Citizen Engagement?") / Statement ("53 Gov Projects. Here's What We Learned.")
- Always provide 3 subject line options per issue

### Punchline Formula
- 15–20 words
- Must create cognitive tension or surprise
- Examples: "If a cosmetics booth can drive civic-style engagement, imagine what it can do for your next departmental campaign." / "Static exhibitions are yesterday's strategy. Here's what the data says."

---

## 7. ALREADY COMPLETED — DO NOT REPEAT

Issues #1–#24 are complete. The following projects and topics have been used:

### Used Government Projects (S1)
FB2026048, FB2026010, FB2026009, FB2026067, FB2026012, FB2025999, FB2025771, FB2026004, FB2025013, FB2026047, FB2025012, FB2025017, FB2026065, FB2026011, FB2026074, FB2026062, FB2026008, FB2026037, FB2026070, FB2026050, FB2024005, FB2026002, FB2024016, FB2024018

### Used Non-Gov Projects (S2)
FB2026059, FB2026058, FB2026057, FB2024001, FB2026019, FB2024002, FB2023998, FB2026022, FB2026043, FB2026055, FB2026056, FB2026049, FB2026053, FB2026042, FB2026006, FB2026051, FB2026052, FB2021040, FB2026023, FB2026060, FB2026054, FB2026046, FB2021999, FB2026020

### Used Market Insight Topics (S3)
1. Phygital Civic Engagement / Hybrid Events Market Growth
2. AI in HK Gov Communications 2026
3. Experiential Marketing for Public Engagement
4. Green Governance: ESG & Public Trust
5. Influencer Marketing for HK Government Youth Outreach
6. Smart City Tech in HK Gov 2025-2026
7. Citizen Co-creation: Boosting Trust & Policy Outcomes
8. Data Privacy & Digital Trust in Gov Communications
9. Event Technology & Live Streaming for Public Engagement
10. Mental Health Awareness Campaigns & Public Sector
11. Inclusive Design & Accessibility in Gov Campaigns
12. Cultural Tourism & Heritage Promotion
13. Workplace Safety & OSH Campaign Effectiveness
14. Anti-Drug & Substance Abuse Prevention Campaigns
15. Building Safety & Urban Maintenance Public Awareness
16. Electoral Participation & Civic Education
17. Cross-Border Collaboration & Greater Bay Area Promotion
18. Public Health Campaign Design & Behavioural Change
19. Youth Entrepreneurship & Innovation Promotion
20. Smart Retail & Consumer Technology Trends
21. Sports & Wellness Promotion
22. Media Relations & Press Conference Strategy
23. Roving Exhibition Effectiveness for Gov Outreach
24. Brand Reputation Management & Crisis Communications

---

## 8. GITHUB DEPLOYMENT INSTRUCTIONS

### Repository
- **Repo:** `dickson-crypto/Firebean-Profile-Website`
- **EDM folder:** `/edm/`
- **File naming:** `edm_NNN.html` (web) and `edm_NNN_gmail.html` (email)
- **Index file:** `/edm/index.html` — must be updated with each new issue card

### Index Card Format (add to `/edm/index.html`)
```html
<div class="card">
  <div class="card-issue">Issue NNN</div>
  <div class="card-date">DD Month YYYY</div>
  <div class="card-title">[SUBJECT LINE / EDM TITLE]</div>
  <div class="card-links">
    <a class="btn-web" href="edm_NNN.html" target="_blank">Web</a>
    <a class="btn-gmail" href="edm_NNN_gmail.html" target="_blank">Gmail</a>
  </div>
</div>
```

### Deployment Steps
1. Create `edm_NNN.html` (web version) in `/edm/` folder
2. Create `edm_NNN_gmail.html` (Gmail version) in `/edm/` folder
3. Add new card to `/edm/index.html` grid
4. Commit and push to `main` branch
5. GitHub Pages auto-deploys to `https://dickson-crypto.github.io/Firebean-Profile-Website/edm/`

### Git Commands
```bash
gh repo clone dickson-crypto/Firebean-Profile-Website
cd Firebean-Profile-Website
# Add your new files to /edm/
git add edm/edm_NNN.html edm/edm_NNN_gmail.html edm/index.html
git commit -m "Add EDM Issue NNN — [TITLE]"
git push origin main
```

---

## 9. IMAGE SOURCING RULES

| Section | Image Source | Method |
|---|---|---|
| S1 Hero (Gov project) | Google Drive (from Master DB) | Get folder ID from "Drive Folder Link" column → list files → find `photo_N.jpg` matching "Hero Photo Picker" → use `https://drive.google.com/uc?id=[FILE_ID]&export=view` |
| S2 Hero (Non-gov project) | Google Drive (from Master DB) | Same as S1 |
| S3 Hero (Market insight) | AI-generated | Generate 16:9 image. Professional editorial style. Navy blue/teal palette. No text overlay. Topic-relevant scene. |
| S4 Hero (Agency CTA) | AI-generated | Generate 16:9 image. Professional agency/team scene. Warm lighting. No text overlay. |
| Logo icon | CDN | `https://files.manuscdn.com/user_upload_by_module/session_file/310519663437368766/OXsmmaNIDdCdSALu.png` |

**Alternative website image URL format** (if Drive URL doesn't render):
`https://firebean.net/data/images/[project_id_lowercase]-photo-[N].webp`
Example: `https://firebean.net/data/images/fb2026048-photo-2.webp`

---

## 10. GOOGLE SHEET UPDATE INSTRUCTIONS

After generating each new EDM, append a row to the **"EDM_Database"** sheet in the Master DB Google Sheet:
`https://docs.google.com/spreadsheets/d/1Ms1Q1i7uJg0ilvW4g1PezBm7mTCNKcYJT_c5-weUBNc/edit`

**Column mapping (A–AJ, 36 columns):**
```
A: Issue_ID (e.g. EDM_025)
B: Issue_Date
C: Subject_Line
D: Status (DRAFT / APPROVED / SENT)
E: Send_Date
F: S1_Project_ID
G: S1_Client
H: S1_Project_Name
I: S1_Event_Date
J: S1_Scope_of_Work
K: S1_Catchy_Title
L: S1_Punchline
M: S1_Content
N: S1_Hero_Photo_URL
O: S1_Profile_URL
P: S2_Project_ID
Q: S2_Client
R: S2_Project_Name
S: S2_Category
T: S2_Scope_of_Work
U: S2_Catchy_Title
V: S2_Punchline
W: S2_Content
X: S2_Hero_Photo_URL
Y: S2_Profile_URL
Z: S3_Insight_Topic
AA: S3_Catchy_Title
AB: S3_Punchline
AC: S3_Content
AD: S3_AI_Image_URL
AE: S4_Catchy_Title
AF: S4_Punchline
AG: S4_Content
AH: S4_AI_Image_URL
AI: S4_CTA_Link
AJ: Notes
```

---

## 11. QUALITY CHECKLIST (Run Before Publishing)

Before committing any EDM to GitHub, verify:

- [ ] Subject line is insight-driven, not promotional
- [ ] S1 project is a GOVERNMENT project not used in Issues #1–#24
- [ ] S2 project is a NON-GOV project not used in Issues #1–#24
- [ ] S3 topic is unique and not covered in Issues #1–#24
- [ ] S1 & S2 hero images are from Google Drive (not AI-generated)
- [ ] S3 & S4 images are AI-generated (not from Drive)
- [ ] All content is ≤200 words per section (S1, S2) and ≤180 words (S3)
- [ ] S3 includes at least one statistic with a named source
- [ ] All CTA links resolve correctly (`firebean.net/profile.html?id=fb[id]`)
- [ ] Both `edm_NNN.html` and `edm_NNN_gmail.html` files created
- [ ] Index card added to `/edm/index.html`
- [ ] EDM_Database Google Sheet row appended
- [ ] No content repeated from previous issues
- [ ] Footer constants correct (address, phone, email)
- [ ] Logo icon URL correct

---

## 12. EXAMPLE ISSUE FOR REFERENCE

**Issue #1 — Complete Reference**
- Web: https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001.html
- Gmail: https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001_gmail.html
- Subject: "Beyond Information: How HK's Best Campaigns Turn Policy into Experience"
- S1: Education Bureau — A Voyage with Books (FB2026048)
- S2: K-palette Summer Festival Pop-up (FB2026059)
- S3: Phygital Engagement / Hybrid Events Market Growth
- S4: "53 Government Projects. One Agency. A Track Record That Speaks for Itself."

---

## 13. NEXT ISSUES TO GENERATE (Starting from Issue #25)

Issues #25 onwards should continue from the remaining unused projects in the Master DB Google Sheet. Suggested approach:
1. Query the "Basic Info" sheet for all projects NOT in the "Used" lists above
2. Sort by date descending for freshness
3. Pair each Gov project with a thematically complementary Non-Gov project
4. Research a fresh market insight topic relevant to HK government communications
5. Generate AI images for S3 and S4
6. Draft both HTML files
7. Push to GitHub and update the index
8. Append row to EDM_Database sheet

The Master DB contains approximately 53 Government projects and 51 Non-Gov projects. With 24 issues already generated, approximately **29 more issues** can be produced before any project repetition.

---

*End of Master Prompt Document*
*Prepared by Manus AI for Firebean Limited — July 2026*
