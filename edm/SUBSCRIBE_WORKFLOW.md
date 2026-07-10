# PR MARKET DECODED — Subscribe & Welcome Email Workflow (Issue 001 Example)

## What's been built (live demo)

A working example of the Issue 001 welcome email has been sent to **dickson@firebean.net** via Zapier Gmail. Check your inbox for:

> **Subject:** Welcome to PR MARKET DECODED — Issue 001 inside
> **From:** Firebean (reply-to: hello@firebean.net)
> **Gmail message ID:** `19f4c9f55a219be5`

The email is a branded HTML welcome with the Issue 001 hero, title, summary, and a red "Read Issue 001 →" button linking to the GitHub-hosted EDM.

## Architecture

```
[Google Form]  →  [Google Sheet: "Email list"]  →  [Zapier trigger]  →  [Gmail: send welcome email]
   (subscribe)        (master DB)                (new row = new sub)      (HTML welcome + EDM link)
                                                                          │
                            [GitHub Pages] ← hosts the EDM HTML ←─────────┘
```

### The three services
- **Google Forms** — public subscription page (Name, Email, Department, Title)
- **GitHub** (Pages) — hosts the EDM HTML at `https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001.html`
- **Zapier MCP** — Gmail "Send Email" action sends the welcome email (HTML body) when a new subscriber row appears

### Master spreadsheet
- Spreadsheet ID: `1Ms1Q1i7uJg0ilvW4g1PezBm7mTCNKcYJT_c5-weUBNc`
- Sheet: **Email list** (worksheetId 1378192939)
- Columns: Email, Name, Date Added, Source, Department, Title, Phone, Sub-Department, Status, Polite Greeting

## Welcome email HTML
- Committed to repo: `edm/welcome_001.html` (commit `393c56a`)
- Live URL: `https://dickson-crypto.github.io/Firebean-Profile-Website/edm/welcome_001.html`
- Links to EDM: `https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001.html`

---

## Remaining manual step: create the persistent Zap trigger

The Zapier MCP connector can execute Gmail's "Send Email" action on demand (which is how the test email was sent), but it **cannot create a persistent, always-on trigger Zap**. That must be done once in the Zapier dashboard. Here's the exact setup:

### Step 1 — Create the Google Form
1. Go to https://forms.new (logged into dickson@firebean.net)
2. Title: `Firebean — PR MARKET DECODED Subscription`
3. Description: `Subscribe to Firebean's weekly briefing on Hong Kong government PR & experiential marketing. We respect your privacy.`
4. Add questions:
   - **Name** — Short answer — Required
   - **Email** — Short answer — Required — set Response validation → Email address
   - **Department** — Short answer — Optional
   - **Title / Position** — Short answer — Optional
5. Settings → Responses → Presentation → Confirmation message: `Thank you for subscribing to PR MARKET DECODED. Your welcome issue is on its way — check your inbox.`
6. Copy the published form URL (Send → link icon)

### Step 2 — Link the form to the master spreadsheet
1. In the form editor, go to **Responses** tab → click the green **Link to Sheets** icon
2. Choose **Select existing spreadsheet** → pick the master DB (`1Ms1Q1i7uJg0ilvW4g1PezBm7mTCNKcYJT_c5-weUBNc`)
3. Select the **Email list** sheet
4. Form responses will now append rows to "Email list", with columns: Timestamp, Name, Email, Department, Title/Position

> Note: Google Forms creates its own response sheet. To land responses directly in the existing "Email list" sheet with the exact column order, map fields with a Zapier Formatter step (Step 3 below).

### Step 3 — Create the Zap (the trigger that sends the welcome email)
1. Go to https://zapier.com → **Create a Zap**
2. **Trigger:** Google Forms → **New Response in Spreadsheet**
   - Select the form/spreadsheet from Step 1–2
3. **Action 1 (optional):** Google Sheets → **Create Spreadsheet Row**
   - Spreadsheet: master DB (`1Ms1Q1i7uJg0ilvW4g1PezBm7mTCNKcYJT_c5-weUBNc`)
   - Worksheet: `Email list`
   - Map: Email ← form Email, Name ← form Name, Department ← form Department, Title ← form Title/Position, Source = "Google Form", Status = "ACTIVE", Date Added = `{{zap_meta_human_now}}`, Polite Greeting ← form Name
4. **Action 2:** Gmail → **Send Email**
   - To: `{{email}}` (from form)
   - From Name: `Firebean`
   - Reply To: `hello@firebean.net`
   - Subject: `Welcome to PR MARKET DECODED — Issue 001 inside`
   - Body type: **HTML**
   - Body: paste the full HTML from `edm/welcome_001.html` (or use a public URL). Replace any personalization as needed.
   - Tip: To send the latest issue each week, store the welcome HTML body in a Google Doc or a Zapier Storage value and reference it, so you update one place per issue.
5. **Publish** the Zap

### Step 4 — Test
1. Open the form URL and submit a test entry with an inbox you control
2. Confirm: a new row appears in the "Email list" sheet, and the welcome email arrives

---

## Reproducibility

The welcome email HTML can be regenerated/edited in `edm/welcome_001.html` and re-committed. For future issues, duplicate `welcome_001.html` → `welcome_0XX.html`, swap the hero image URL and title/summary, and update the "Read Issue 0XX" button link to the new EDM page.

## Live URLs
- EDM index: https://dickson-crypto.github.io/Firebean-Profile-Website/edm/index.html
- Issue 001 web: https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001.html
- Issue 001 Gmail (legacy-safe): https://dickson-crypto.github.io/Firebean-Profile-Website/edm/edm_001_gmail.html
- Welcome email HTML: https://dickson-crypto.github.io/Firebean-Profile-Website/edm/welcome_001.html
