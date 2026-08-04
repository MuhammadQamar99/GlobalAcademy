# 🎓 Global Academy — Official Website

Professional, mobile-friendly website for **Global Academy, Rawalpindi** — built with free tools only (PKR 0 hosting via GitHub Pages).

**Theme:** Navy Blue `#0A2540` + White + Red `#E5323E` · **Stack:** HTML5, Bootstrap 5, Vanilla JS, Font Awesome, Google Fonts

---

## 📁 Folder Structure

```
GlobalAcademy/
├── index.html                  # Homepage (hero, stats, courses, results, testimonials)
├── about.html                  # Story, mission, vision, founder, facilities
├── courses.html                # All courses + upcoming
├── course-basic-computer.html  # Flagship course detail page
├── admission.html              # Google Form embed + WhatsApp apply form
├── results.html                # Position holders + result cards
├── gallery.html                # Filterable photo gallery + lightbox
├── blog.html                   # Blog listing
├── blog-ai-tools.html          # Sample article
├── teachers.html               # Faculty + weekly lesson plans
├── testimonials.html           # Reviews
├── faq.html                    # Accordion FAQs
├── contact.html                # Forms + Google Map
├── privacy.html / terms.html   # Legal pages
├── 404.html                    # Error page (auto-served by GitHub Pages)
├── assets/
│   ├── css/style.css           # Full theme
│   ├── js/main.js              # Counters, reveal, filters, WhatsApp forms
│   └── images/                 # Logo + illustrations
├── forms/  pdf/  certificates/  uploads/   # Ready-to-use working folders
├── build.py                    # Site generator (edit once → rebuilds all pages)
├── sitemap.xml  robots.txt     # SEO files
└── README.md                   # This file
```

## 🔧 The ONE file to edit: `build.py`

All global details live in the `TOKENS` dictionary at the top of `build.py`.
Change them **once**, then run `python3 build.py` to regenerate every page:

| Token | Current Value | Replace With |
|---|---|---|
| `@PHONE@` | +92 300 5084669 | Academy phone (already set) |
| `@WA@` | 923005084669 | WhatsApp in international format |
| `@EMAIL@` | globalacademypk@gmail.com | Your real Gmail (Phase 1) |
| `@ADDR@` | Main Murree Road, Rawalpindi | Your exact street address |
| `@HOURS@` | Mon–Sat 3–8 PM | Your real timings |
| `@FB@` `@IG@` `@YT@` | placeholder URLs | Real social links after creating accounts |
| `SITE` (top of file) | YOUR-USERNAME.github.io | Real URL after GitHub setup |

> Prefer editing HTML directly? That works too — just edit the `.html` files and don't re-run `build.py`.

## 🚀 Launch Steps (Phase 1 + Deploy)

1. **Gmail** — create `globalacademypk@gmail.com` (or your chosen name).
2. **GitHub** — sign up at github.com with that Gmail (free).
3. **New repository** — name it `GlobalAcademy`, set **Public**.
4. **Upload** — click *Add files → Upload files*, drag everything inside this folder (not the folder itself), then *Commit changes*.
5. **Enable Pages** — repo → **Settings → Pages → Source: main branch → /(root) → Save**.
6. ✅ Your site is live at `https://YOUR-USERNAME.github.io/GlobalAcademy/` in ~2 minutes (HTTPS is automatic — Phase 20 ✓).
7. Now update `SITE` in `build.py`, `robots.txt` and `sitemap.xml` with your real URL and re-upload changed files.

## 📋 Connect the Free Tools (Phase 12)

| Tool | Where on site | Setup |
|---|---|---|
| **Google Forms → Sheets** | `admission.html` button | forms.google.com → build form with the fields on the admission page → **Send → 🔗 link tab → Shorten URL** → copy the link → set it as `@FORM_URL@` in `build.py` → run `python3 build.py` → re-upload `admission.html`. In the form: **Responses → Link to Sheets** (your student database) and **⋮ → Get email notifications** |
| **Google Sheets** | Student database | Created automatically from the form's "Link to Sheets" |
| **Google Maps** | `contact.html` iframe | maps.google.com → search your exact location → *Share → Embed a map* → replace the iframe `src` |
| **Google Calendar** | Timetable (optional) | calendar.google.com → *Settings → Embed* code → paste on a new `timetable.html` |
| **Google Drive** | Notes/PDF folders | Upload PDFs to Drive → *Share → anyone with link* → add links to `pdf/` section pages |
| **YouTube / FB / IG** | Footer + gallery + testimonials | Create channels/pages with the academy Gmail, then update `@FB@ @IG@ @YT@` tokens |

## 🛠️ Troubleshooting

**"Actions is currently unavailable… requires a Jekyll build step"**
→ Repo → **Settings → Actions → General → Actions permissions → "Allow all actions and reusable workflows"** → Save. GitHub Pages deploys every site (even static ones) through a built-in Actions workflow (`pages-build-deployment`), so Pages cannot build while Actions are disabled. The `.nojekyll` file in this repo also makes GitHub skip Jekyll entirely — the banner disappears after enabling Actions.

**Site shows 404 at the URL** → wait 2–3 min after enabling Pages; check **Actions tab** for a green ✓ on `pages-build-deployment`.

**Styles broken / 404 on assets** → make sure you uploaded the *contents* of the GlobalAcademy folder to the repo root (`index.html` must be at the top level, not inside a subfolder).

## 📈 SEO & Analytics (Phase 18)

- [x] Meta descriptions, Open Graph tags, canonical URLs — done on every page
- [x] JSON-LD `EducationalOrganization` schema — on homepage
- [x] `sitemap.xml` + `robots.txt` — included
- [ ] Create free account at **search.google.com/search-console** → verify site → submit sitemap
- [ ] Create free **GA4** at analytics.google.com → paste the `G-XXXX` tag where marked `EDIT: Google Analytics` in `build.py` (`head()` function)

## ✏️ Content Checklist Before Going Public

- [ ] Replace sample **stats** on homepage (counter targets in `index.html`)
- [ ] Replace sample **result cards & position holders** with real students
- [ ] Replace sample **testimonials** with real reviews
- [ ] Add real **fee** on `course-basic-computer.html`
- [ ] Add **founder name** and real story on `about.html`
- [ ] Add **teacher names/photos** on `teachers.html`
- [ ] Replace `YOUR_FORM_ID` with real Google Form embed
- [ ] Update Google Maps iframe to your exact location
- [ ] Update social links + email + address tokens in `build.py`
- [ ] Replace illustration photos with real photos as you take them (same filenames, keep under ~300 KB each for speed — compress free at squoosh.app)

## 🔮 Later Phases (already scaffolded in design)

- **Phase 13–15 (Portals):** "Coming Soon" cards on homepage → later connect Google Apps Script (free) or Firebase free tier for logins, attendance & marks.
- **Phase 21 (Future):** QR certificates, online tests (Google Forms quizzes first!), fee payments, AI chatbot.
- **Custom domain:** buy `globalacademy.pk` later → add a `CNAME` file with the domain → done, no rebuild needed.

---
© 2026 Global Academy, Rawalpindi · Made with ❤️ and PKR 0 hosting cost.
