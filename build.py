#!/usr/bin/env python3
# ============================================================
#  GLOBAL ACADEMY — Static site generator
#  Run:  python3 build.py
#  It writes all HTML pages with a shared header/footer.
#  Tokens like @PHONE@ are replaced globally — edit the
#  TOKENS dict below ONCE and the whole site updates.
# ============================================================
import os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
TODAY = "2026-08-03"
SITE = "https://YOUR-USERNAME.github.io/GlobalAcademy"   # EDIT after GitHub setup

TOKENS = {
    "@SITE@": SITE,
    "@PHONE@": "+92 300 5084669",                        # EDIT: academy phone
    "@PHONE_TEL@": "+92300508466 9".replace(" ", ""),
    "@WA@": "92300508466" + "9",                         # WhatsApp intl format
    "@EMAIL@": "globalacademypk@gmail.com",              # EDIT: academy email
    "@ADDR@": "Main Murree Road, Rawalpindi, Punjab, Pakistan",  # EDIT
    "@HOURS@": "Mon – Sat, 3:00 PM – 8:00 PM",           # EDIT
    "@FB@": "https://www.facebook.com/globalacademypk",  # EDIT
    "@IG@": "https://www.instagram.com/globalacademypk", # EDIT
    "@YT@": "https://www.youtube.com/@GlobalAcademyPK",  # EDIT
}

NAV = [
    ("index.html", "Home"), ("about.html", "About"), ("courses.html", "Courses"),
    ("admission.html", "Admissions"), ("results.html", "Results"),
    ("gallery.html", "Gallery"), ("blog.html", "Blog"), ("contact.html", "Contact"),
]

def head(title, desc, fname, extra=""):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>""" + title + """ | Global Academy</title>
<meta name="description" content=\"""" + desc + """\">
<meta name="robots" content="index, follow">
<link rel="canonical" href="@SITE@/""" + fname + """\">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Global Academy">
<meta property="og:title" content=\"""" + title + """ | Global Academy\">
<meta property="og:description" content=\"""" + desc + """\">
<meta property="og:url" content="@SITE@/""" + fname + """\">
<meta property="og:image" content="@SITE@/assets/images/hero.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="assets/images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" rel="stylesheet">
<link href="assets/css/style.css" rel="stylesheet">
<!-- EDIT: Google Analytics (Phase 18) — paste your GA4 tag here after creating a free account
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
-->
""" + extra + """
</head>
<body>
"""

def header(active):
    links = ""
    for href, label in NAV:
        cls = 'nav-link active' if href == active else 'nav-link'
        aria = ' aria-current="page"' if href == active else ''
        links += '<li class="nav-item"><a class="' + cls + '" href="' + href + '"' + aria + '>' + label + '</a></li>\n'
    return """
<nav class="navbar navbar-expand-lg navbar-dark ga-navbar sticky-top" aria-label="Main navigation">
  <div class="container">
    <a class="navbar-brand d-flex align-items-center gap-2" href="index.html">
      <img src="assets/images/logo.png" alt="Global Academy logo" width="46" height="46" class="rounded-circle bg-white p-1" loading="lazy">
      <span><span class="brand-text">GLOBAL <em>ACADEMY</em></span><br><span class="brand-sub">Learn &middot; Grow &middot; Succeed</span></span>
    </a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
    <div class="collapse navbar-collapse" id="mainNav">
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
      """ + links + """
      </ul>
      <div class="d-flex align-items-center gap-2 ms-lg-3 mt-3 mt-lg-0">
        <a class="btn btn-outline-light btn-sm px-3" href="tel:@PHONE_TEL@" aria-label="Call academy"><i class="fa-solid fa-phone"></i></a>
        <a class="btn btn-red btn-sm px-4" href="admission.html"><i class="fa-solid fa-pen-to-square me-1"></i> Apply Now</a>
      </div>
    </div>
  </div>
</nav>
"""

def footer():
    return """
<footer class="ga-footer pt-5">
  <div class="container">
    <div class="row g-4 pb-4">
      <div class="col-lg-4 col-md-6">
        <div class="d-flex align-items-center gap-2 mb-3">
          <img src="assets/images/logo.png" alt="Global Academy logo" width="44" height="44" class="rounded-circle bg-white p-1" loading="lazy">
          <span class="brand-text">GLOBAL <em>ACADEMY</em></span>
        </div>
        <p class="small mb-3">Building confident learners with modern computer skills, quality teaching, and career guidance — from classroom to career.</p>
        <div class="d-flex gap-2">
          <a class="social-ic" href="@FB@" target="_blank" rel="noopener" aria-label="Facebook"><i class="fa-brands fa-facebook-f"></i></a>
          <a class="social-ic" href="@IG@" target="_blank" rel="noopener" aria-label="Instagram"><i class="fa-brands fa-instagram"></i></a>
          <a class="social-ic" href="@YT@" target="_blank" rel="noopener" aria-label="YouTube"><i class="fa-brands fa-youtube"></i></a>
          <a class="social-ic" href="https://wa.me/@WA@" target="_blank" rel="noopener" aria-label="WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
      </div>
      <div class="col-lg-2 col-md-6 col-6">
        <h5>Quick Links</h5>
        <ul class="list-unstyled small d-grid gap-2">
          <li><a href="about.html"><i class="fa-solid fa-angle-right me-2"></i>About Us</a></li>
          <li><a href="admission.html"><i class="fa-solid fa-angle-right me-2"></i>Admissions</a></li>
          <li><a href="results.html"><i class="fa-solid fa-angle-right me-2"></i>Results</a></li>
          <li><a href="teachers.html"><i class="fa-solid fa-angle-right me-2"></i>Our Teachers</a></li>
          <li><a href="testimonials.html"><i class="fa-solid fa-angle-right me-2"></i>Testimonials</a></li>
          <li><a href="faq.html"><i class="fa-solid fa-angle-right me-2"></i>FAQs</a></li>
        </ul>
      </div>
      <div class="col-lg-3 col-md-6 col-6">
        <h5>Our Courses</h5>
        <ul class="list-unstyled small d-grid gap-2">
          <li><a href="course-basic-computer.html"><i class="fa-solid fa-angle-right me-2"></i>Basic Computer Course</a></li>
          <li><a href="courses.html"><i class="fa-solid fa-angle-right me-2"></i>Web Development</a></li>
          <li><a href="courses.html"><i class="fa-solid fa-angle-right me-2"></i>Graphic Design</a></li>
          <li><a href="courses.html"><i class="fa-solid fa-angle-right me-2"></i>Python Programming</a></li>
          <li><a href="courses.html"><i class="fa-solid fa-angle-right me-2"></i>Digital Marketing</a></li>
          <li><a href="courses.html"><i class="fa-solid fa-angle-right me-2"></i>AI Tools</a></li>
        </ul>
      </div>
      <div class="col-lg-3 col-md-6">
        <h5>Contact Us</h5>
        <div class="contact-line"><i class="fa-solid fa-location-dot"></i><span>@ADDR@</span></div>
        <div class="contact-line"><i class="fa-solid fa-phone"></i><a href="tel:@PHONE_TEL@">@PHONE@</a></div>
        <div class="contact-line"><i class="fa-brands fa-whatsapp"></i><a href="https://wa.me/@WA@" target="_blank" rel="noopener">@PHONE@</a></div>
        <div class="contact-line"><i class="fa-solid fa-envelope"></i><a href="mailto:@EMAIL@">@EMAIL@</a></div>
        <div class="contact-line"><i class="fa-solid fa-clock"></i><span>@HOURS@</span></div>
      </div>
    </div>
  </div>
  <div class="footer-bottom py-3">
    <div class="container d-flex flex-wrap justify-content-between align-items-center gap-2">
      <span>&copy; <span id="year">2026</span> Global Academy, Rawalpindi. All rights reserved.</span>
      <span class="d-flex gap-3">
        <a href="privacy.html">Privacy Policy</a><a href="terms.html">Terms</a><a href="sitemap.xml">Sitemap</a>
      </span>
    </div>
  </div>
</footer>

<a class="wa-float" href="https://wa.me/@WA@?text=Assalam-o-Alaikum!%20I%20want%20details%20about%20Global%20Academy%20courses." target="_blank" rel="noopener" aria-label="Chat on WhatsApp"><i class="fa-brands fa-whatsapp"></i></a>
<button id="toTop" aria-label="Back to top"><i class="fa-solid fa-arrow-up"></i></button>

<div class="modal fade" id="lightbox" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered modal-lg">
    <div class="modal-content bg-transparent border-0">
      <button type="button" class="btn-close btn-close-white ms-auto me-1" data-bs-dismiss="modal" aria-label="Close"></button>
      <img id="lightboxImg" class="w-100 rounded-3" alt="Gallery image enlarged">
    </div>
  </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
<script src="assets/js/main.js"></script>
</body>
</html>
"""

def page_header(title, crumb, active):
    return """
<section class="page-header breadcrumb-bg">
  <div class="container position-relative">
    <nav aria-label="breadcrumb"><ol class="breadcrumb mb-2">
      <li class="breadcrumb-item"><a href="index.html">Home</a></li>
      <li class="breadcrumb-item active">""" + crumb + """</li>
    </ol></nav>
    <h1 class="mb-0">""" + title + """</h1>
  </div>
</section>
"""

def render(fname, title, desc, active, body, extra_head=""):
    html = head(title, desc, fname, extra_head) + header(active) + body + footer()
    for k, v in TOKENS.items():
        html = html.replace(k, v)
    with open(os.path.join(BASE, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓ " + fname)

JSONLD = """
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "EducationalOrganization",
  "name": "Global Academy",
  "url": "@SITE@/",
  "logo": "@SITE@/assets/images/logo.png",
  "telephone": "@PHONE@",
  "email": "@EMAIL@",
  "address": {"@type": "PostalAddress", "streetAddress": "@ADDR@", "addressLocality": "Rawalpindi", "addressRegion": "Punjab", "addressCountry": "PK"},
  "sameAs": ["@FB@", "@IG@", "@YT@"]
}
</script>
"""

PAGES = []

# ============================ HOME ============================
PAGES.append(("index.html",
"Global Academy Rawalpindi — Computer Courses & Quality Education",
"Global Academy Rawalpindi offers affordable computer courses, expert teachers and certified training. Join our Basic Computer Course today — admissions open.",
"index.html", """

<!-- ================= HERO ================= -->
<section class="hero">
  <div class="container py-5">
    <div class="row align-items-center">
      <div class="col-lg-7 reveal in">
        <span class="hero-badge"><i class="fa-solid fa-bolt"></i> Admissions Open — New Batch 2026</span>
        <h1 class="mb-3">Learn <span class="accent">Computer Skills</span>,<br>Build Your <span class="accent">Career</span>.</h1>
        <p class="lead mb-4">Join Global Academy today. Practical, career-focused computer education in Rawalpindi — from MS Office and internet skills to AI tools and freelancing basics.</p>
        <div class="d-flex flex-wrap gap-3">
          <a href="admission.html" class="btn btn-red btn-lg px-4"><i class="fa-solid fa-pen-to-square me-2"></i>Apply Now</a>
          <a href="https://wa.me/@WA@?text=Assalam-o-Alaikum!%20I%20want%20admission%20details." target="_blank" rel="noopener" class="btn btn-wa btn-lg px-4"><i class="fa-brands fa-whatsapp me-2"></i>WhatsApp</a>
          <a href="tel:@PHONE_TEL@" class="btn btn-outline-light btn-lg px-4"><i class="fa-solid fa-phone me-2"></i>Call Now</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ================= TRUST BAR ================= -->
<div class="trust-bar py-3">
  <div class="container">
    <div class="row g-2 text-center small">
      <div class="col-6 col-md-3"><i class="fa-solid fa-user-graduate"></i>Qualified Faculty</div>
      <div class="col-6 col-md-3"><i class="fa-solid fa-desktop"></i>Modern Computer Lab</div>
      <div class="col-6 col-md-3"><i class="fa-solid fa-certificate"></i>Certificates on Completion</div>
      <div class="col-6 col-md-3"><i class="fa-solid fa-briefcase"></i>Career Guidance</div>
    </div>
  </div>
</div>

<!-- ================= STATS ================= -->
<section class="stats-strip section-sm">
  <div class="container">
    <!-- EDIT: update these numbers to your real academy statistics -->
    <div class="row text-center g-4">
      <div class="col-6 col-md"><div class="stat-ico"><i class="fa-solid fa-users"></i></div><div class="stat-num" data-target="500" data-suffix="+">0</div><div class="stat-label">Students Enrolled</div></div>
      <div class="col-6 col-md"><div class="stat-ico"><i class="fa-solid fa-book-open"></i></div><div class="stat-num" data-target="8" data-suffix="+">0</div><div class="stat-label">Courses</div></div>
      <div class="col-6 col-md"><div class="stat-ico"><i class="fa-solid fa-chalkboard-user"></i></div><div class="stat-num" data-target="6" data-suffix="+">0</div><div class="stat-label">Expert Teachers</div></div>
      <div class="col-6 col-md"><div class="stat-ico"><i class="fa-solid fa-chart-line"></i></div><div class="stat-num" data-target="95" data-suffix="%">0</div><div class="stat-label">Success Rate</div></div>
      <div class="col-6 col-md"><div class="stat-ico"><i class="fa-solid fa-award"></i></div><div class="stat-num" data-target="300" data-suffix="+">0</div><div class="stat-label">Certificates Issued</div></div>
    </div>
  </div>
</section>

<!-- ================= ABOUT PREVIEW ================= -->
<section class="section">
  <div class="container">
    <div class="row align-items-center g-5">
      <div class="col-lg-6 reveal">
        <img src="assets/images/about.jpg" alt="Global Academy campus illustration" class="rounded-4 shadow w-100" loading="lazy">
      </div>
      <div class="col-lg-6 reveal">
        <span class="eyebrow">About Global Academy</span>
        <h2 class="section-title">Quality Education,<br>Practical Skills, Real Results</h2>
        <div class="section-bar"></div>
        <p class="mt-4 text-secondary">Global Academy is a learning institute in Rawalpindi focused on modern, practical education. We combine experienced teachers, a fully equipped computer lab, and a friendly environment so every student can learn at their own pace.</p>
        <ul class="list-check my-4">
          <li><i class="fa-solid fa-circle-check"></i>Experienced, caring teachers with lesson plans for every class</li>
          <li><i class="fa-solid fa-circle-check"></i>Hands-on computer training — every student practices on a PC</li>
          <li><i class="fa-solid fa-circle-check"></i>Regular tests, transparent result cards &amp; progress reports</li>
          <li><i class="fa-solid fa-circle-check"></i>Freelancing &amp; career guidance for every student</li>
        </ul>
        <a href="about.html" class="btn btn-navy px-4">Read Our Story <i class="fa-solid fa-arrow-right ms-2"></i></a>
      </div>
    </div>
  </div>
</section>

<!-- ================= COURSES PREVIEW ================= -->
<section class="section soft-bg">
  <div class="container">
    <div class="text-center mb-5 reveal">
      <span class="eyebrow">Our Courses</span>
      <h2 class="section-title">Career-Focused Programs</h2>
      <div class="section-bar mx-auto"></div>
      <p class="text-secondary mt-3 col-lg-6 mx-auto">Start with our flagship Basic Computer Course — more professional courses are launching soon.</p>
    </div>
    <div class="row g-4">
      <div class="col-lg-3 col-md-6 reveal">
        <div class="ga-card p-4">
          <span class="badge-red mb-3 d-inline-block">Enrolling Now</span>
          <div class="icon-circle"><i class="fa-solid fa-laptop-code"></i></div>
          <h5 class="text-navy">Basic Computer Course</h5>
          <p class="small text-secondary mb-3">MS Word, Excel, PowerPoint, Internet, Email, AI Basics &amp; Freelancing — 2 Months.</p>
          <a href="course-basic-computer.html" class="text-red fw-semibold small">View Details <i class="fa-solid fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="col-lg-3 col-md-6 reveal">
        <div class="ga-card p-4">
          <span class="badge-grey mb-3 d-inline-block">Coming Soon</span>
          <div class="icon-circle"><i class="fa-brands fa-python"></i></div>
          <h5 class="text-navy">Python Programming</h5>
          <p class="small text-secondary mb-3">Learn programming from zero — logic, problem solving and real projects.</p>
          <a href="courses.html" class="text-red fw-semibold small">Learn More <i class="fa-solid fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="col-lg-3 col-md-6 reveal">
        <div class="ga-card p-4">
          <span class="badge-grey mb-3 d-inline-block">Coming Soon</span>
          <div class="icon-circle"><i class="fa-solid fa-pen-nib"></i></div>
          <h5 class="text-navy">Graphic Design</h5>
          <p class="small text-secondary mb-3">Posters, social media design and branding with Canva &amp; pro tools.</p>
          <a href="courses.html" class="text-red fw-semibold small">Learn More <i class="fa-solid fa-arrow-right"></i></a>
        </div>
      </div>
      <div class="col-lg-3 col-md-6 reveal">
        <div class="ga-card p-4">
          <span class="badge-grey mb-3 d-inline-block">Coming Soon</span>
          <div class="icon-circle"><i class="fa-solid fa-code"></i></div>
          <h5 class="text-navy">Web Development</h5>
          <p class="small text-secondary mb-3">HTML, CSS, JavaScript — build real websites, step by step.</p>
          <a href="courses.html" class="text-red fw-semibold small">Learn More <i class="fa-solid fa-arrow-right"></i></a>
        </div>
      </div>
    </div>
    <div class="text-center mt-5 reveal"><a href="courses.html" class="btn btn-red px-5">View All Courses <i class="fa-solid fa-arrow-right ms-2"></i></a></div>
  </div>
</section>

<!-- ================= WHY CHOOSE US ================= -->
<section class="section">
  <div class="container">
    <div class="text-center mb-5 reveal">
      <span class="eyebrow">Why Choose Us</span>
      <h2 class="section-title">The Global Academy Difference</h2>
      <div class="section-bar mx-auto"></div>
    </div>
    <div class="row g-4">
      <div class="col-lg-4 col-md-6 reveal"><div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-user-tie"></i></div><h5>Qualified Teachers</h5><p class="small text-secondary mb-0">Experienced instructors who follow structured weekly lesson plans and give personal attention to every student.</p></div></div>
      <div class="col-lg-4 col-md-6 reveal"><div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-computer"></i></div><h5>Modern Computer Lab</h5><p class="small text-secondary mb-0">Every student gets dedicated PC time — learning by doing, not just watching.</p></div></div>
      <div class="col-lg-4 col-md-6 reveal"><div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-wallet"></i></div><h5>Affordable Fees</h5><p class="small text-secondary mb-0">Quality education at fees every family can manage, with easy monthly installments.</p></div></div>
      <div class="col-lg-4 col-md-6 reveal"><div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-users-line"></i></div><h5>Small Batches</h5><p class="small text-secondary mb-0">Limited seats per class so teachers can focus on each learner's progress.</p></div></div>
      <div class="col-lg-4 col-md-6 reveal"><div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-certificate"></i></div><h5>Certificates</h5><p class="small text-secondary mb-0">Receive a certificate on course completion — a valuable addition to your CV.</p></div></div>
      <div class="col-lg-4 col-md-6 reveal"><div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-rocket"></i></div><h5>Career &amp; Freelancing</h5><p class="small text-secondary mb-0">Guidance on Fiverr, Upwork and AI tools so your skills start earning for you.</p></div></div>
    </div>
  </div>
</section>

<!-- ================= RESULTS PREVIEW ================= -->
<section class="section soft-bg">
  <div class="container">
    <div class="d-flex flex-wrap justify-content-between align-items-end mb-4 reveal">
      <div><span class="eyebrow">Student Results</span><h2 class="section-title mb-0">Our Stars Shine Bright</h2><div class="section-bar"></div></div>
      <a href="results.html" class="btn btn-outline-red mt-3 mt-md-0">View All Results <i class="fa-solid fa-arrow-right ms-1"></i></a>
    </div>
    <!-- EDIT: replace sample result cards with real position holders -->
    <div class="row g-4">
      <div class="col-md-4 reveal">
        <div class="result-card">
          <div class="rc-ribbon">1st Position</div>
          <div class="rc-head"><div class="rc-avatar">AK</div><div><h6 class="mb-0 text-white">Areeba Khan</h6><small>SSC — Science Group</small></div></div>
          <div class="rc-body">
            <div class="rc-marks"><div><strong>1023</strong><span>Obtained</span></div><div><strong>1100</strong><span>Total</span></div><div><strong class="grade">93%</strong><span>Grade A+</span></div></div>
            <p class="small text-secondary mb-0"><i class="fa-solid fa-award text-red me-2"></i>Board Exams 2026 — Academy Topper</p>
          </div>
        </div>
      </div>
      <div class="col-md-4 reveal">
        <div class="result-card">
          <div class="rc-ribbon">2nd Position</div>
          <div class="rc-head"><div class="rc-avatar">MA</div><div><h6 class="mb-0 text-white">Muhammad Ahmed</h6><small>HSSC — Pre-Engineering</small></div></div>
          <div class="rc-body">
            <div class="rc-marks"><div><strong>986</strong><span>Obtained</span></div><div><strong>1100</strong><span>Total</span></div><div><strong class="grade">89%</strong><span>Grade A+</span></div></div>
            <p class="small text-secondary mb-0"><i class="fa-solid fa-award text-red me-2"></i>Board Exams 2026</p>
          </div>
        </div>
      </div>
      <div class="col-md-4 reveal">
        <div class="result-card">
          <div class="rc-ribbon">Top Scorer</div>
          <div class="rc-head"><div class="rc-avatar">SF</div><div><h6 class="mb-0 text-white">Sara Fatima</h6><small>Basic Computer Course</small></div></div>
          <div class="rc-body">
            <div class="rc-marks"><div><strong>96</strong><span>Obtained</span></div><div><strong>100</strong><span>Total</span></div><div><strong class="grade">96%</strong><span>Grade A+</span></div></div>
            <p class="small text-secondary mb-0"><i class="fa-solid fa-award text-red me-2"></i>Final Assessment 2026</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ================= PORTALS (COMING SOON) ================= -->
<section class="section">
  <div class="container">
    <div class="text-center mb-5 reveal">
      <span class="eyebrow">Digital Campus</span>
      <h2 class="section-title">Portals Launching Soon</h2>
      <div class="section-bar mx-auto"></div>
      <p class="text-secondary mt-3 col-lg-6 mx-auto">We're building dedicated online portals so students, teachers and admins can work smarter — free for all enrolled members.</p>
    </div>
    <div class="row g-4">
      <div class="col-md-4 reveal"><div class="coming-soon"><i class="fa-solid fa-user-graduate"></i><h5 class="text-navy">Student Portal</h5><p class="small text-secondary">Attendance, assignments, results, certificates &amp; downloads — all in one login.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-md-4 reveal"><div class="coming-soon"><i class="fa-solid fa-chalkboard-user"></i><h5 class="text-navy">Teacher Portal</h5><p class="small text-secondary">Upload notes, mark attendance, manage homework and student marks online.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-md-4 reveal"><div class="coming-soon"><i class="fa-solid fa-user-shield"></i><h5 class="text-navy">Admin Panel</h5><p class="small text-secondary">Fee management, exams, reports and certificates — full academy control center.</p><span class="badge-grey">Coming Soon</span></div></div>
    </div>
  </div>
</section>

<!-- ================= TESTIMONIALS ================= -->
<section class="section soft-bg">
  <div class="container">
    <div class="text-center mb-5 reveal">
      <span class="eyebrow">Testimonials</span>
      <h2 class="section-title">What Students &amp; Parents Say</h2>
      <div class="section-bar mx-auto"></div>
    </div>
    <!-- EDIT: replace with real reviews -->
    <div class="row g-4">
      <div class="col-md-4 reveal"><div class="quote-card"><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div><p class="small text-secondary">"I joined with zero computer knowledge. Within two months I was making documents, spreadsheets and even my first CV. The teachers are so patient!"</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">H</div><div><strong class="d-block small text-navy">Hassan R.</strong><small class="text-muted">Basic Computer Course</small></div></div></div></div>
      <div class="col-md-4 reveal"><div class="quote-card"><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div><p class="small text-secondary">"My daughter's confidence has grown so much. Regular tests and result cards keep us informed about her progress every month."</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">N</div><div><strong class="d-block small text-navy">Mrs. Noreen A.</strong><small class="text-muted">Parent</small></div></div></div></div>
      <div class="col-md-4 reveal"><div class="quote-card"><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i></div><p class="small text-secondary">"The freelancing module opened my eyes. I created my Fiverr profile during the course and learned exactly which skills buyers want."</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">U</div><div><strong class="d-block small text-navy">Usman T.</strong><small class="text-muted">Student</small></div></div></div></div>
    </div>
    <div class="text-center mt-4 reveal"><a href="testimonials.html" class="btn btn-outline-red">Read More Reviews</a></div>
  </div>
</section>

<!-- ================= GALLERY PREVIEW ================= -->
<section class="section">
  <div class="container">
    <div class="d-flex flex-wrap justify-content-between align-items-end mb-4 reveal">
      <div><span class="eyebrow">Gallery</span><h2 class="section-title mb-0">Life at Global Academy</h2><div class="section-bar"></div></div>
      <a href="gallery.html" class="btn btn-outline-red mt-3 mt-md-0">View Gallery <i class="fa-solid fa-arrow-right ms-1"></i></a>
    </div>
    <div class="row g-3 reveal">
      <div class="col-6 col-md-3"><a class="gallery-item" href="assets/images/gallery-lab.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/gallery-lab.jpg" alt="Computer lab session" loading="lazy"><span class="gi-cap">Computer Lab</span></a></div>
      <div class="col-6 col-md-3"><a class="gallery-item" href="assets/images/gallery-class.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/gallery-class.jpg" alt="Class activity" loading="lazy"><span class="gi-cap">Class Activity</span></a></div>
      <div class="col-6 col-md-3"><a class="gallery-item" href="assets/images/gallery-awards.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/gallery-awards.jpg" alt="Prize distribution" loading="lazy"><span class="gi-cap">Prize Distribution</span></a></div>
      <div class="col-6 col-md-3"><a class="gallery-item" href="assets/images/gallery-certificates.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/gallery-certificates.jpg" alt="Certificate ceremony" loading="lazy"><span class="gi-cap">Certificates</span></a></div>
    </div>
    <!-- ================= CTA ================= -->
    <div class="cta-band mt-5 p-5 text-center reveal">
      <h2 class="mb-3">Ready to Start Your Learning Journey?</h2>
      <p class="mb-4 opacity-75">Seats are limited per batch. Reserve yours today — apply online in 2 minutes.</p>
      <div class="d-flex flex-wrap justify-content-center gap-3">
        <a href="admission.html" class="btn btn-light btn-lg px-4 text-red fw-bold"><i class="fa-solid fa-pen-to-square me-2"></i>Apply Now</a>
        <a href="https://wa.me/@WA@" target="_blank" rel="noopener" class="btn btn-outline-light btn-lg px-4"><i class="fa-brands fa-whatsapp me-2"></i>Chat With Us</a>
      </div>
    </div>
  </div>
</section>
""", JSONLD))

# ============================ ABOUT ============================
PAGES.append(("about.html",
"About Us",
"Learn about Global Academy Rawalpindi — our history, mission, vision, founder, and campus facilities.",
"about.html", page_header("About Global Academy", "About", "about.html") + """
<section class="section">
  <div class="container">
    <div class="row g-5 align-items-center mb-5">
      <div class="col-lg-6 reveal">
        <span class="eyebrow">Our Story</span>
        <h2 class="section-title">From a Single Classroom to a Center of Excellence</h2>
        <div class="section-bar"></div>
        <!-- EDIT: replace with your real story -->
        <p class="mt-4 text-secondary">Global Academy began with a simple belief: every student in Rawalpindi deserves access to practical, modern education — especially computer skills that open doors to jobs, freelancing and higher studies.</p>
        <p class="text-secondary">Today, our academy runs structured courses with proper lesson plans, regular assessments, transparent result cards and certificates — all in a friendly, disciplined environment where parents can trust the process.</p>
        <div class="d-flex gap-2 flex-wrap mt-3"><span class="chip">Discipline</span><span class="chip">Practical Learning</span><span class="chip">Character Building</span><span class="chip">Career Focus</span></div>
      </div>
      <div class="col-lg-6 reveal">
        <img src="assets/images/about.jpg" alt="Global Academy campus" class="rounded-4 shadow w-100" loading="lazy">
      </div>
    </div>

    <div class="row g-4 mb-5">
      <div class="col-md-6 reveal">
        <div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-bullseye"></i></div>
          <h4 class="text-navy">Our Mission</h4>
          <p class="text-secondary mb-0">To empower students with practical computer skills, strong academics and the confidence to succeed — through quality teaching, honest assessment and personal mentorship at an affordable fee.</p>
        </div>
      </div>
      <div class="col-md-6 reveal">
        <div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-eye"></i></div>
          <h4 class="text-navy">Our Vision</h4>
          <p class="text-secondary mb-0">To become Rawalpindi's most trusted academy — where every graduate leaves with skills, a certificate, and a clear path toward employment, freelancing or higher education.</p>
        </div>
      </div>
    </div>

    <div class="row g-5 align-items-center mb-5">
      <div class="col-lg-4 reveal">
        <div class="ga-card p-4 text-center">
          <img src="assets/images/founder.jpg" alt="Founder of Global Academy" class="rounded-circle shadow mb-3" style="width:170px;height:170px;object-fit:cover" loading="lazy">
          <!-- EDIT: founder's real name & message -->
          <h5 class="text-navy mb-1">Founder &amp; Director</h5>
          <p class="small text-red fw-semibold mb-2">Global Academy, Rawalpindi</p>
          <p class="small text-secondary mb-0">"Our promise is simple: honest teaching, visible progress, and skills that stay with your child for life." <em>(edit about.html)</em></p>
        </div>
      </div>
      <div class="col-lg-8 reveal">
        <span class="eyebrow">Milestones</span>
        <h3 class="section-title fs-3">Our Journey</h3>
        <div class="section-bar mb-4"></div>
        <div class="timeline">
          <div class="t-item"><div class="t-year">Foundation</div><p class="small text-secondary mb-0">Global Academy opens its doors with its first batch of students. <em>(edit year)</em></p></div>
          <div class="t-item"><div class="t-year">Computer Lab</div><p class="small text-secondary mb-0">A dedicated computer lab is set up for hands-on practical training.</p></div>
          <div class="t-item"><div class="t-year">Basic Computer Course</div><p class="small text-secondary mb-0">Our flagship 2-month certified course launches with AI basics &amp; freelancing.</p></div>
          <div class="t-item"><div class="t-year">2026 — Going Digital</div><p class="small text-secondary mb-0">Website launch, online admissions, digital result cards — and student/teacher portals next.</p></div>
        </div>
      </div>
    </div>

    <div class="reveal">
      <div class="text-center mb-4"><span class="eyebrow">Campus</span><h3 class="section-title fs-3">Facilities at Global Academy</h3><div class="section-bar mx-auto"></div></div>
      <div class="row g-3">
        <div class="col-6 col-lg-3"><div class="ga-card p-3 text-center small fw-semibold text-navy"><i class="fa-solid fa-desktop fa-lg d-block mb-2 text-red"></i>Computer Lab</div></div>
        <div class="col-6 col-lg-3"><div class="ga-card p-3 text-center small fw-semibold text-navy"><i class="fa-solid fa-chalkboard fa-lg d-block mb-2 text-red"></i>Smart Classrooms</div></div>
        <div class="col-6 col-lg-3"><div class="ga-card p-3 text-center small fw-semibold text-navy"><i class="fa-solid fa-book fa-lg d-block mb-2 text-red"></i>Notes Library</div></div>
        <div class="col-6 col-lg-3"><div class="ga-card p-3 text-center small fw-semibold text-navy"><i class="fa-solid fa-moon fa-lg d-block mb-2 text-red"></i>Evening Batches</div></div>
        <div class="col-6 col-lg-3"><div class="ga-card p-3 text-center small fw-semibold text-navy"><i class="fa-solid fa-users fa-lg d-block mb-2 text-red"></i>Small Batches</div></div>
        <div class="col-6 col-lg-3"><div class="ga-card p-3 text-center small fw-semibold text-navy"><i class="fa-solid fa-clipboard-check fa-lg d-block mb-2 text-red"></i>Monthly Tests</div></div>
        <div class="col-6 col-lg-3"><div class="ga-card p-3 text-center small fw-semibold text-navy"><i class="fa-solid fa-certificate fa-lg d-block mb-2 text-red"></i>Certificates</div></div>
        <div class="col-6 col-lg-3"><div class="ga-card p-3 text-center small fw-semibold text-navy"><i class="fa-solid fa-handshake fa-lg d-block mb-2 text-red"></i>Career Guidance</div></div>
      </div>
    </div>
  </div>
</section>
"""))

# ============================ COURSES ============================
PAGES.append(("courses.html",
"Courses",
"Explore Global Academy courses — Basic Computer Course enrolling now, plus upcoming Python, Graphic Design, Web Development, Digital Marketing, AI Tools, Data Science and Office Automation.",
"courses.html", page_header("Our Courses", "Courses", "courses.html") + """
<section class="section">
  <div class="container">
    <div class="row justify-content-center mb-5 reveal">
      <div class="col-lg-8 text-center">
        <span class="eyebrow">Programs</span>
        <h2 class="section-title">Learn Skills That Pay</h2>
        <div class="section-bar mx-auto"></div>
        <p class="text-secondary mt-3">Every course includes hands-on practice, notes, tests and a completion certificate.</p>
      </div>
    </div>

    <!-- Featured course -->
    <div class="ga-card overflow-hidden mb-5 reveal">
      <div class="row g-0">
        <div class="col-lg-5"><img src="assets/images/gallery-lab.jpg" class="w-100 h-100" style="object-fit:cover;min-height:280px" alt="Basic Computer Course practice lab" loading="lazy"></div>
        <div class="col-lg-7 p-4 p-lg-5">
          <span class="badge-red mb-3 d-inline-block"><i class="fa-solid fa-fire me-1"></i> Enrolling Now</span>
          <h3 class="text-navy">Basic Computer Course <span class="text-red">— Flagship</span></h3>
          <p class="text-secondary">The complete starter package for students, job-seekers and home users. Go from zero to confident computer user in 2 months — with practical tasks in every class.</p>
          <div class="mb-3">
            <span class="chip">MS Word</span><span class="chip">MS Excel</span><span class="chip">PowerPoint</span><span class="chip">Internet</span><span class="chip">Email</span><span class="chip">AI Basics</span><span class="chip">Freelancing</span>
          </div>
          <ul class="list-check small mb-4">
            <li><i class="fa-solid fa-circle-check"></i>Duration: 2 Months &nbsp; | &nbsp; Classes: 3 days/week &nbsp; | &nbsp; Certificate included</li>
            <li><i class="fa-solid fa-circle-check"></i>No age limit. No prior computer experience needed.</li>
          </ul>
          <div class="d-flex flex-wrap gap-2">
            <a href="course-basic-computer.html" class="btn btn-navy px-4">Full Course Details</a>
            <a href="admission.html" class="btn btn-red px-4"><i class="fa-solid fa-pen-to-square me-1"></i> Apply Now</a>
          </div>
        </div>
      </div>
    </div>

    <h4 class="text-navy mb-4 reveal"><i class="fa-solid fa-layer-group text-red me-2"></i>Upcoming Courses</h4>
    <div class="row g-4">
      <div class="col-lg-3 col-md-6 reveal"><div class="ga-card p-4 text-center"><div class="icon-circle mx-auto"><i class="fa-brands fa-python"></i></div><h6 class="text-navy">Python Programming</h6><p class="small text-secondary">Programming fundamentals &amp; projects.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-lg-3 col-md-6 reveal"><div class="ga-card p-4 text-center"><div class="icon-circle mx-auto"><i class="fa-solid fa-pen-nib"></i></div><h6 class="text-navy">Graphic Design</h6><p class="small text-secondary">Canva, branding &amp; social media design.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-lg-3 col-md-6 reveal"><div class="ga-card p-4 text-center"><div class="icon-circle mx-auto"><i class="fa-solid fa-code"></i></div><h6 class="text-navy">Web Development</h6><p class="small text-secondary">HTML, CSS, JavaScript &amp; real websites.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-lg-3 col-md-6 reveal"><div class="ga-card p-4 text-center"><div class="icon-circle mx-auto"><i class="fa-solid fa-bullhorn"></i></div><h6 class="text-navy">Digital Marketing</h6><p class="small text-secondary">SEO, social media &amp; online business.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-lg-3 col-md-6 reveal"><div class="ga-card p-4 text-center"><div class="icon-circle mx-auto"><i class="fa-solid fa-robot"></i></div><h6 class="text-navy">AI Tools</h6><p class="small text-secondary">ChatGPT, Gemini &amp; productivity AI.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-lg-3 col-md-6 reveal"><div class="ga-card p-4 text-center"><div class="icon-circle mx-auto"><i class="fa-solid fa-chart-pie"></i></div><h6 class="text-navy">Data Science</h6><p class="small text-secondary">Excel to analytics — data careers path.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-lg-3 col-md-6 reveal"><div class="ga-card p-4 text-center"><div class="icon-circle mx-auto"><i class="fa-solid fa-briefcase"></i></div><h6 class="text-navy">Office Automation</h6><p class="small text-secondary">Advanced office &amp; admin workflows.</p><span class="badge-grey">Coming Soon</span></div></div>
      <div class="col-lg-3 col-md-6 reveal">
        <div class="coming-soon"><i class="fa-solid fa-bell"></i><h6 class="text-navy">Get Notified</h6><p class="small text-secondary">WhatsApp us to join the waiting list for any upcoming course.</p><a href="https://wa.me/@WA@?text=Please%20notify%20me%20about%20upcoming%20courses." target="_blank" rel="noopener" class="btn btn-wa btn-sm px-3"><i class="fa-brands fa-whatsapp me-1"></i>Notify Me</a></div>
      </div>
    </div>

    <div class="note-box mt-5 reveal"><i class="fa-solid fa-circle-info me-2"></i><strong>Certificates:</strong> Every completed course includes a Global Academy certificate of completion. Bring your CNIC/B-Form copy and 2 photos when finalizing admission at the campus.</div>
  </div>
</section>
"""))

# ============================ COURSE DETAIL ============================
PAGES.append(("course-basic-computer.html",
"Basic Computer Course — 2 Months",
"Global Academy's flagship 2-month Basic Computer Course in Rawalpindi: MS Word, Excel, PowerPoint, Internet, Email, AI Basics and Freelancing with certificate.",
"courses.html", page_header("Basic Computer Course", "Courses", "course-basic-computer.html") + """
<section class="section">
  <div class="container">
    <div class="row g-5">
      <div class="col-lg-8">
        <div class="reveal">
          <span class="badge-red mb-3 d-inline-block"><i class="fa-solid fa-fire me-1"></i> Enrolling Now — Seats Limited</span>
          <h2 class="section-title">From Zero to Confident Computer User in 2 Months</h2>
          <div class="section-bar"></div>
          <p class="mt-4 text-secondary">Our flagship course is designed for absolute beginners — school students, college students, job seekers, office staff and home users. Everything is taught step-by-step in Urdu-friendly classes with daily hands-on practice on the academy's computers.</p>
        </div>

        <h4 class="text-navy mt-5 mb-3 reveal"><i class="fa-solid fa-list-check text-red me-2"></i>What You Will Learn</h4>
        <div class="row g-3 reveal">
          <div class="col-md-6"><div class="ga-card p-3 d-flex gap-3 align-items-start"><div class="icon-circle mb-0" style="width:48px;height:48px;font-size:1.1rem"><i class="fa-solid fa-file-word"></i></div><div><strong class="text-navy">MS Word</strong><p class="small text-secondary mb-0">Documents, letters, CVs, tables, printing &amp; formatting.</p></div></div></div>
          <div class="col-md-6"><div class="ga-card p-3 d-flex gap-3 align-items-start"><div class="icon-circle mb-0" style="width:48px;height:48px;font-size:1.1rem"><i class="fa-solid fa-file-excel"></i></div><div><strong class="text-navy">MS Excel</strong><p class="small text-secondary mb-0">Sheets, formulas, marks sheets, bills &amp; basic data work.</p></div></div></div>
          <div class="col-md-6"><div class="ga-card p-3 d-flex gap-3 align-items-start"><div class="icon-circle mb-0" style="width:48px;height:48px;font-size:1.1rem"><i class="fa-solid fa-file-powerpoint"></i></div><div><strong class="text-navy">PowerPoint</strong><p class="small text-secondary mb-0">Presentations with animations &amp; professional slides.</p></div></div></div>
          <div class="col-md-6"><div class="ga-card p-3 d-flex gap-3 align-items-start"><div class="icon-circle mb-0" style="width:48px;height:48px;font-size:1.1rem"><i class="fa-solid fa-globe"></i></div><div><strong class="text-navy">Internet Skills</strong><p class="small text-secondary mb-0">Browsing, searching, downloading &amp; safe online habits.</p></div></div></div>
          <div class="col-md-6"><div class="ga-card p-3 d-flex gap-3 align-items-start"><div class="icon-circle mb-0" style="width:48px;height:48px;font-size:1.1rem"><i class="fa-solid fa-envelope"></i></div><div><strong class="text-navy">Email</strong><p class="small text-secondary mb-0">Gmail setup, attachments &amp; professional communication.</p></div></div></div>
          <div class="col-md-6"><div class="ga-card p-3 d-flex gap-3 align-items-start"><div class="icon-circle mb-0" style="width:48px;height:48px;font-size:1.1rem"><i class="fa-solid fa-robot"></i></div><div><strong class="text-navy">AI Basics</strong><p class="small text-secondary mb-0">Using ChatGPT &amp; AI tools for study, work &amp; creativity.</p></div></div></div>
          <div class="col-md-6"><div class="ga-card p-3 d-flex gap-3 align-items-start"><div class="icon-circle mb-0" style="width:48px;height:48px;font-size:1.1rem"><i class="fa-solid fa-laptop-code"></i></div><div><strong class="text-navy">Freelancing Intro</strong><p class="small text-secondary mb-0">Fiverr/Upwork basics — turn your new skills into income.</p></div></div></div>
          <div class="col-md-6"><div class="ga-card p-3 d-flex gap-3 align-items-start"><div class="icon-circle mb-0" style="width:48px;height:48px;font-size:1.1rem"><i class="fa-solid fa-certificate"></i></div><div><strong class="text-navy">Final Project &amp; Exam</strong><p class="small text-secondary mb-0">Practical assessment + certificate of completion.</p></div></div></div>
        </div>

        <h4 class="text-navy mt-5 mb-3 reveal"><i class="fa-solid fa-calendar-week text-red me-2"></i>8-Week Course Outline</h4>
        <div class="table-responsive reveal">
          <table class="table table-ga table-bordered">
            <thead><tr><th>Week</th><th>Module</th><th>Outcome</th></tr></thead>
            <tbody class="small">
              <tr><td>1</td><td>Computer Fundamentals &amp; Typing</td><td>Confident basic operation, faster typing</td></tr>
              <tr><td>2</td><td>MS Word — Basics</td><td>Letters &amp; simple documents</td></tr>
              <tr><td>3</td><td>MS Word — Advanced</td><td>CV, tables, headers, printing</td></tr>
              <tr><td>4</td><td>MS Excel — Basics</td><td>Sheets, marks sheets, simple formulas</td></tr>
              <tr><td>5</td><td>MS Excel — Advanced</td><td>Budgets, bills &amp; charts</td></tr>
              <tr><td>6</td><td>PowerPoint + Internet &amp; Email</td><td>Slides + professional email skills</td></tr>
              <tr><td>7</td><td>AI Basics + Freelancing Intro</td><td>Use AI tools; profile on Fiverr/Upwork</td></tr>
              <tr><td>8</td><td>Final Project, Test &amp; Certificates</td><td>Assessment + result card + certificate</td></tr>
            </tbody>
          </table>
        </div>

        <h4 class="text-navy mt-5 mb-3 reveal"><i class="fa-solid fa-circle-question text-red me-2"></i>Who Should Join?</h4>
        <ul class="list-check reveal">
          <li><i class="fa-solid fa-circle-check"></i>School &amp; college students who want a skill advantage</li>
          <li><i class="fa-solid fa-circle-check"></i>Job seekers preparing for office &amp; government jobs</li>
          <li><i class="fa-solid fa-circle-check"></i>Home users who want to learn computers from the start</li>
          <li><i class="fa-solid fa-circle-check"></i>Anyone planning to start freelancing online</li>
        </ul>
        <div class="note-box mt-4 reveal"><i class="fa-solid fa-lightbulb me-2"></i><strong>Teaching method:</strong> short concept → live demonstration → <em>you practice</em> → weekly quiz. That's why our students actually remember what they learn.</div>
      </div>

      <!-- Sidebar -->
      <div class="col-lg-4">
        <div class="ga-card p-4 sticky-top reveal" style="top:110px">
          <h5 class="text-navy mb-4">Course Summary</h5>
          <div class="d-flex justify-content-between border-bottom py-2 small"><span class="text-muted"><i class="fa-solid fa-clock text-red me-2"></i>Duration</span><strong>2 Months (8 Weeks)</strong></div>
          <div class="d-flex justify-content-between border-bottom py-2 small"><span class="text-muted"><i class="fa-solid fa-calendar text-red me-2"></i>Classes</span><strong>3 Days / Week</strong></div>
          <!-- EDIT: real fee -->
          <div class="d-flex justify-content-between border-bottom py-2 small"><span class="text-muted"><i class="fa-solid fa-tag text-red me-2"></i>Fee</span><strong>Affordable — Contact Us</strong></div>
          <div class="d-flex justify-content-between border-bottom py-2 small"><span class="text-muted"><i class="fa-solid fa-certificate text-red me-2"></i>Certificate</span><strong>Included</strong></div>
          <!-- EDIT: next batch date -->
          <div class="d-flex justify-content-between border-bottom py-2 small"><span class="text-muted"><i class="fa-solid fa-flag-checkered text-red me-2"></i>Next Batch</span><strong>New batch monthly</strong></div>
          <div class="d-flex justify-content-between py-2 small"><span class="text-muted"><i class="fa-solid fa-building text-red me-2"></i>Mode</span><strong>On-Campus, Rawalpindi</strong></div>
          <a href="admission.html" class="btn btn-red w-100 mt-3"><i class="fa-solid fa-pen-to-square me-1"></i> Apply Now</a>
          <a href="https://wa.me/@WA@?text=I%20want%20fee%20and%20timing%20details%20for%20the%20Basic%20Computer%20Course." target="_blank" rel="noopener" class="btn btn-wa w-100 mt-2"><i class="fa-brands fa-whatsapp me-1"></i> Ask on WhatsApp</a>
          <p class="text-center small text-muted mt-3 mb-0"><i class="fa-solid fa-phone me-1"></i> Call: <a href="tel:@PHONE_TEL@">@PHONE@</a></p>
        </div>
      </div>
    </div>
  </div>
</section>
"""))

# ============================ ADMISSION ============================
PAGES.append(("admission.html",
"Admissions — Apply Online",
"Apply for admission at Global Academy Rawalpindi. Fill the online form in 2 minutes — data reaches us instantly via Google Sheets or WhatsApp.",
"admission.html", page_header("Admissions Open", "Admissions", "admission.html") + """
<section class="section">
  <div class="container">
    <div class="row g-3 mb-5 text-center reveal">
      <div class="col-md-4"><div class="ga-card p-4"><div class="icon-circle mx-auto"><i class="fa-solid fa-pen-to-square"></i></div><h6 class="text-navy">Step 1 — Fill the Form</h6><p class="small text-secondary mb-0">Complete the admission form below (2 minutes).</p></div></div>
      <div class="col-md-4"><div class="ga-card p-4"><div class="icon-circle mx-auto"><i class="fa-solid fa-phone-volume"></i></div><h6 class="text-navy">Step 2 — We Contact You</h6><p class="small text-secondary mb-0">Our team confirms your seat, timing &amp; fee details.</p></div></div>
      <div class="col-md-4"><div class="ga-card p-4"><div class="icon-circle mx-auto"><i class="fa-solid fa-graduation-cap"></i></div><h6 class="text-navy">Step 3 — Start Learning</h6><p class="small text-secondary mb-0">Visit the campus, finalize admission and begin!</p></div></div>
    </div>

    <div class="row g-5">
      <div class="col-lg-8">
        <!-- ============ OPTION A: GOOGLE FORM (recommended) ============ -->
        <div class="ga-card p-4 mb-4 reveal">
          <h4 class="text-navy mb-2"><i class="fa-solid fa-file-lines text-red me-2"></i>Admission Form</h4>
          <p class="small text-secondary">Your details go directly to our Google Sheet — we usually reply the same day.</p>
          <div class="note-box small mb-3">
            <strong>Owner note (EDIT):</strong> replace <code>YOUR_FORM_ID</code> below with your real Google Form ID
            (Google Forms → Send → ⚙ Embed). See <code>README.md → Phase 1</code>.
          </div>
          <div class="ratio ratio-4x3" style="max-height:900px">
            <iframe src="https://docs.google.com/forms/d/e/YOUR_FORM_ID/viewform?embedded=true" title="Admission form">Loading…</iframe>
          </div>
        </div>

        <!-- ============ OPTION B: WHATSAPP FORM (works instantly, zero setup) ============ -->
        <div class="form-card p-4 reveal">
          <h4 class="text-navy mb-1"><i class="fa-brands fa-whatsapp text-red me-2"></i>Or Apply via WhatsApp</h4>
          <p class="small text-secondary mb-4">Fill this quick form — it opens WhatsApp with your details ready to send.</p>
          <form data-wa="New Admission Application" data-wa-num="@WA@">
            <div class="row g-3">
              <div class="col-md-6"><label class="form-label">Full Name *</label><input required class="form-control" data-label="Name" placeholder="Student name"></div>
              <div class="col-md-6"><label class="form-label">Father Name *</label><input required class="form-control" data-label="Father Name" placeholder="Father name"></div>
              <div class="col-md-6"><label class="form-label">Phone *</label><input required class="form-control" data-label="Phone" type="tel" placeholder="03xx-xxxxxxx"></div>
              <div class="col-md-6"><label class="form-label">WhatsApp Number</label><input class="form-control" data-label="WhatsApp" type="tel" placeholder="If different from phone"></div>
              <div class="col-md-6"><label class="form-label">Email</label><input class="form-control" data-label="Email" type="email" placeholder="you@example.com"></div>
              <div class="col-md-6"><label class="form-label">Education *</label>
                <select required class="form-select" data-label="Education"><option value="">Choose…</option><option>Middle</option><option>Matric (SSC)</option><option>Intermediate (HSSC)</option><option>Bachelor</option><option>Master</option><option>Other</option></select></div>
              <div class="col-12"><label class="form-label">Address</label><input class="form-control" data-label="Address" placeholder="Area / city"></div>
              <div class="col-md-6"><label class="form-label">Select Course *</label>
                <select required class="form-select" data-label="Course"><option value="">Choose…</option><option>Basic Computer Course (2 Months)</option><option>Python (waiting list)</option><option>Graphic Design (waiting list)</option><option>Web Development (waiting list)</option><option>Other / Not sure</option></select></div>
              <div class="col-md-6"><label class="form-label">Preferred Timing *</label>
                <select required class="form-select" data-label="Timing"><option value="">Choose…</option><option>Morning</option><option>Afternoon</option><option>Evening</option></select></div>
              <div class="col-md-6"><label class="form-label d-block">Gender *</label>
                <div class="btn-group" role="group">
                  <input type="radio" class="btn-check" name="gender" id="g1" value="Male" data-label="Gender"><label class="btn btn-outline-red btn-sm" for="g1">Male</label>
                  <input type="radio" class="btn-check" name="gender" id="g2" value="Female" data-label="Gender"><label class="btn btn-outline-red btn-sm" for="g2">Female</label>
                </div></div>
              <div class="col-md-6"><label class="form-label">Photo (optional)</label><input class="form-control" type="file" accept="image/*" data-label="Photo"><small class="text-muted">Or send your photo on WhatsApp later.</small></div>
              <div class="col-12">
                <button class="btn btn-red px-5" type="submit"><i class="fa-brands fa-whatsapp me-2"></i>Submit Application</button>
                <span class="sent-msg d-none small text-success ms-3"><i class="fa-solid fa-circle-check"></i> Opening WhatsApp… press Send there to finish.</span>
              </div>
            </div>
          </form>
        </div>
      </div>

      <div class="col-lg-4">
        <div class="ga-card p-4 mb-4 reveal">
          <h5 class="text-navy mb-3">Need Help With Admission?</h5>
          <div class="d-flex gap-3 align-items-start mb-3"><i class="fa-solid fa-phone text-red mt-1"></i><div><strong class="small d-block">Call Us</strong><a class="small" href="tel:@PHONE_TEL@">@PHONE@</a></div></div>
          <div class="d-flex gap-3 align-items-start mb-3"><i class="fa-brands fa-whatsapp text-red mt-1"></i><div><strong class="small d-block">WhatsApp</strong><a class="small" href="https://wa.me/@WA@" target="_blank" rel="noopener">@PHONE@</a></div></div>
          <div class="d-flex gap-3 align-items-start mb-3"><i class="fa-solid fa-envelope text-red mt-1"></i><div><strong class="small d-block">Email</strong><a class="small" href="mailto:@EMAIL@">@EMAIL@</a></div></div>
          <div class="d-flex gap-3 align-items-start mb-3"><i class="fa-solid fa-location-dot text-red mt-1"></i><div><strong class="small d-block">Visit Us</strong><span class="small text-secondary">@ADDR@</span></div></div>
          <div class="d-flex gap-3 align-items-start"><i class="fa-solid fa-clock text-red mt-1"></i><div><strong class="small d-block">Office Hours</strong><span class="small text-secondary">@HOURS@</span></div></div>
        </div>
        <div class="ga-card p-4 reveal">
          <h5 class="text-navy mb-3">Documents Required</h5>
          <ul class="list-check small mb-0">
            <li><i class="fa-solid fa-circle-check"></i>CNIC / B-Form copy</li>
            <li><i class="fa-solid fa-circle-check"></i>2 recent passport photos</li>
            <li><i class="fa-solid fa-circle-check"></i>Last educational certificate (copy)</li>
            <li><i class="fa-solid fa-circle-check"></i>First month / admission fee</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>
"""))

# ============================ RESULTS ============================
PAGES.append(("results.html",
"Student Results & Position Holders",
"Global Academy results — SSC, HSSC position holders, academy test results and downloadable result cards.",
"results.html", page_header("Student Results", "Results", "results.html") + """
<section class="section">
  <div class="container">
    <div class="note-box mb-5 reveal"><i class="fa-solid fa-circle-info me-2"></i>Congratulations to all our students! Results below are updated after every board exam and academy assessment. Printed official result cards are issued at the campus. <em>(EDIT: replace sample data with real students)</em></div>

    <h3 class="text-navy mb-4 reveal"><i class="fa-solid fa-trophy text-red me-2"></i>Top Position Holders — 2026</h3>
    <div class="table-responsive mb-5 reveal">
      <table class="table table-ga table-hover">
        <thead><tr><th>#</th><th>Student</th><th>Exam / Course</th><th>Marks</th><th>Percentage</th><th>Grade</th><th>Position</th></tr></thead>
        <tbody class="small">
          <tr><td>1</td><td><i class="fa-solid fa-medal text-danger me-2"></i>Areeba Khan</td><td>SSC — Science Group</td><td>1023 / 1100</td><td>93.0%</td><td>A+</td><td><span class="badge-red">1st</span></td></tr>
          <tr><td>2</td><td><i class="fa-solid fa-medal text-secondary me-2"></i>Muhammad Ahmed</td><td>HSSC — Pre-Engineering</td><td>986 / 1100</td><td>89.6%</td><td>A+</td><td><span class="badge-navy">2nd</span></td></tr>
          <tr><td>3</td><td><i class="fa-solid fa-medal text-warning me-2"></i>Bilal Hussain</td><td>SSC — Computer Science</td><td>965 / 1100</td><td>87.7%</td><td>A</td><td><span class="badge-navy">3rd</span></td></tr>
          <tr><td>4</td><td>Sara Fatima</td><td>Basic Computer Course</td><td>96 / 100</td><td>96.0%</td><td>A+</td><td><span class="badge-grey">Top Scorer</span></td></tr>
          <tr><td>5</td><td>Ali Raza</td><td>Basic Computer Course</td><td>92 / 100</td><td>92.0%</td><td>A+</td><td><span class="badge-grey">Distinction</span></td></tr>
        </tbody>
      </table>
    </div>

    <h3 class="text-navy mb-4 reveal"><i class="fa-solid fa-id-card text-red me-2"></i>Latest Result Cards</h3>
    <div class="row g-4 mb-5">
      <div class="col-md-4 reveal"><div class="result-card"><div class="rc-ribbon">A+</div><div class="rc-head"><div class="rc-avatar">AK</div><div><h6 class="mb-0 text-white">Areeba Khan</h6><small>SSC — Science Group</small></div></div><div class="rc-body"><div class="rc-marks"><div><strong>1023</strong><span>Obtained</span></div><div><strong>1100</strong><span>Total</span></div><div><strong class="grade">93%</strong><span>A+</span></div></div><button class="btn btn-outline-red btn-sm w-100" disabled><i class="fa-solid fa-file-pdf me-1"></i> PDF — available at campus</button></div></div></div>
      <div class="col-md-4 reveal"><div class="result-card"><div class="rc-ribbon">A+</div><div class="rc-head"><div class="rc-avatar">MA</div><div><h6 class="mb-0 text-white">Muhammad Ahmed</h6><small>HSSC — Pre-Engineering</small></div></div><div class="rc-body"><div class="rc-marks"><div><strong>986</strong><span>Obtained</span></div><div><strong>1100</strong><span>Total</span></div><div><strong class="grade">89.6%</strong><span>A+</span></div></div><button class="btn btn-outline-red btn-sm w-100" disabled><i class="fa-solid fa-file-pdf me-1"></i> PDF — available at campus</button></div></div></div>
      <div class="col-md-4 reveal"><div class="result-card"><div class="rc-ribbon">A+</div><div class="rc-head"><div class="rc-avatar">SF</div><div><h6 class="mb-0 text-white">Sara Fatima</h6><small>Basic Computer Course</small></div></div><div class="rc-body"><div class="rc-marks"><div><strong>96</strong><span>Obtained</span></div><div><strong>100</strong><span>Total</span></div><div><strong class="grade">96%</strong><span>A+</span></div></div><button class="btn btn-outline-red btn-sm w-100" disabled><i class="fa-solid fa-file-pdf me-1"></i> PDF — available at campus</button></div></div></div>
    </div>

    <div class="row g-4">
      <div class="col-md-6 reveal">
        <div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-file-arrow-down"></i></div><h5 class="text-navy">Download Your Result</h5><p class="small text-secondary">Digital result cards will be downloadable here once the Student Portal launches. Until then, collect printed result cards from the office during working hours (@HOURS@).</p><a href="https://wa.me/@WA@?text=Please%20share%20my%20result%20card." class="btn btn-wa btn-sm" target="_blank" rel="noopener"><i class="fa-brands fa-whatsapp me-1"></i>Request on WhatsApp</a></div>
      </div>
      <div class="col-md-6 reveal">
        <div class="ga-card p-4 h-100"><div class="icon-circle"><i class="fa-solid fa-clipboard-question"></i></div><h5 class="text-navy">Result Rechecking</h5><p class="small text-secondary">If you believe there is an error in your marks, submit a rechecking request within 7 days of result announcement — at the office or via WhatsApp.</p><a href="contact.html" class="btn btn-outline-red btn-sm"><i class="fa-solid fa-envelope me-1"></i>Contact Office</a></div>
      </div>
    </div>
  </div>
</section>
"""))

# ============================ GALLERY ============================
PAGES.append(("gallery.html",
"Gallery — Photos & Events",
"Global Academy photo gallery — computer lab, classroom activities, events, prize distribution and certificate ceremonies.",
"gallery.html", page_header("Academy Gallery", "Gallery", "gallery.html") + """
<section class="section">
  <div class="container">
    <div class="text-center mb-4 reveal">
      <button class="filter-btn active" data-filter="all">All</button>
      <button class="filter-btn" data-filter="lab">Computer Lab</button>
      <button class="filter-btn" data-filter="class">Classes</button>
      <button class="filter-btn" data-filter="events">Events</button>
      <button class="filter-btn" data-filter="certificates">Certificates</button>
    </div>
    <div class="row g-3 mb-5">
      <div class="col-md-4 col-6" data-cat="lab"><a class="gallery-item" href="assets/images/gallery-lab.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/gallery-lab.jpg" alt="Students practicing in the computer lab" loading="lazy"><span class="gi-cap"><i class="fa-solid fa-desktop me-1"></i>Computer Lab Session</span></a></div>
      <div class="col-md-4 col-6" data-cat="class"><a class="gallery-item" href="assets/images/gallery-class.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/gallery-class.jpg" alt="Interactive class activity" loading="lazy"><span class="gi-cap"><i class="fa-solid fa-chalkboard-user me-1"></i>Class Activity</span></a></div>
      <div class="col-md-4 col-6" data-cat="events"><a class="gallery-item" href="assets/images/gallery-awards.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/gallery-awards.jpg" alt="Prize distribution ceremony" loading="lazy"><span class="gi-cap"><i class="fa-solid fa-trophy me-1"></i>Prize Distribution</span></a></div>
      <div class="col-md-4 col-6" data-cat="certificates"><a class="gallery-item" href="assets/images/gallery-certificates.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/gallery-certificates.jpg" alt="Certificate distribution ceremony" loading="lazy"><span class="gi-cap"><i class="fa-solid fa-certificate me-1"></i>Certificate Ceremony</span></a></div>
      <div class="col-md-4 col-6" data-cat="events"><a class="gallery-item" href="assets/images/hero.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/hero.jpg" alt="Orientation day at Global Academy" loading="lazy"><span class="gi-cap"><i class="fa-solid fa-flag me-1"></i>Orientation Day</span></a></div>
      <div class="col-md-4 col-6" data-cat="events"><a class="gallery-item" href="assets/images/about.jpg" data-bs-toggle="modal" data-bs-target="#lightbox"><img src="assets/images/about.jpg" alt="Global Academy campus" loading="lazy"><span class="gi-cap"><i class="fa-solid fa-school me-1"></i>Our Campus</span></a></div>
    </div>

    <div class="ga-card p-4 text-center reveal">
      <div class="icon-circle mx-auto"><i class="fa-brands fa-youtube"></i></div>
      <h5 class="text-navy">Videos &amp; Event Highlights</h5>
      <p class="small text-secondary col-lg-6 mx-auto">Class videos, event highlights and course introductions are available on our YouTube channel — subscribe to stay updated.</p>
      <!-- EDIT: real channel URL in build.py tokens -->
      <a href="@YT@" target="_blank" rel="noopener" class="btn btn-red px-4"><i class="fa-brands fa-youtube me-2"></i>Visit Our YouTube Channel</a>
    </div>
  </div>
</section>
"""))

# ============================ BLOG ============================
PAGES.append(("blog.html",
"Blog — Learning Tips & Career Guidance",
"Global Academy blog — computer learning tips, AI tools, MS Office guides, study tips and career advice for students in Pakistan.",
"blog.html", page_header("Academy Blog", "Blog", "blog.html") + """
<section class="section">
  <div class="container">
    <div class="row g-4">
      <div class="col-12 reveal">
        <div class="ga-card overflow-hidden">
          <div class="row g-0 align-items-center">
            <div class="col-lg-5"><img src="assets/images/gallery-lab.jpg" class="w-100 h-100 card-img-top" style="min-height:240px" alt="AI tools for students" loading="lazy"></div>
            <div class="col-lg-7 p-4">
              <span class="badge-red mb-2 d-inline-block">Featured</span>
              <div class="post-meta mb-2"><i class="fa-solid fa-calendar"></i>Aug 3, 2026 &nbsp; <i class="fa-solid fa-folder ms-2"></i>AI &amp; Skills</div>
              <h4 class="text-navy">Top 7 Free AI Tools Every Student Should Learn in 2026</h4>
              <p class="small text-secondary">AI is now a basic skill like MS Office. Here are 7 free tools our students use to study faster, write better and work smarter…</p>
              <a href="blog-ai-tools.html" class="btn btn-red btn-sm px-3">Read Article <i class="fa-solid fa-arrow-right ms-1"></i></a>
            </div>
          </div>
        </div>
      </div>

      <div class="col-md-6 col-lg-4 reveal"><div class="ga-card blog-card h-100"><img src="assets/images/gallery-class.jpg" class="card-img-top" alt="How to learn computers" loading="lazy"><div class="p-4"><div class="post-meta mb-2"><i class="fa-solid fa-folder"></i>Guides</div><h6 class="text-navy">How to Learn Computers from Zero — A Beginner's Roadmap</h6><p class="small text-secondary">The exact order we teach: typing → Word → Excel → Internet → AI tools.</p><span class="badge-grey">Coming Soon</span></div></div></div>
      <div class="col-md-6 col-lg-4 reveal"><div class="ga-card blog-card h-100"><img src="assets/images/gallery-certificates.jpg" class="card-img-top" alt="MS Office tips" loading="lazy"><div class="p-4"><div class="post-meta mb-2"><i class="fa-solid fa-folder"></i>MS Office</div><h6 class="text-navy">10 MS Word Shortcuts That Save You an Hour Every Day</h6><p class="small text-secondary">Keyboard shortcuts and formatting tricks every office worker should know.</p><span class="badge-grey">Coming Soon</span></div></div></div>
      <div class="col-md-6 col-lg-4 reveal"><div class="ga-card blog-card h-100"><img src="assets/images/gallery-awards.jpg" class="card-img-top" alt="Study tips" loading="lazy"><div class="p-4"><div class="post-meta mb-2"><i class="fa-solid fa-folder"></i>Study Tips</div><h6 class="text-navy">FBISE Exam Prep: How Our Toppers Study for Boards</h6><p class="small text-secondary">Proven revision schedules and past-paper strategies from position holders.</p><span class="badge-grey">Coming Soon</span></div></div></div>
      <div class="col-md-6 col-lg-4 reveal"><div class="ga-card blog-card h-100"><img src="assets/images/hero.jpg" class="card-img-top" alt="Career guidance" loading="lazy"><div class="p-4"><div class="post-meta mb-2"><i class="fa-solid fa-folder"></i>Careers</div><h6 class="text-navy">From Classroom to Fiverr: Your First Freelancing Steps</h6><p class="small text-secondary">Which skills sell, how to price, and mistakes to avoid as a beginner.</p><span class="badge-grey">Coming Soon</span></div></div></div>
      <div class="col-md-6 col-lg-4 reveal"><div class="ga-card blog-card h-100"><img src="assets/images/about.jpg" class="card-img-top" alt="Scholarships" loading="lazy"><div class="p-4"><div class="post-meta mb-2"><i class="fa-solid fa-folder"></i>Opportunities</div><h6 class="text-navy">Scholarships &amp; Free Courses for Pakistani Students (2026)</h6><p class="small text-secondary">A list of verified scholarships and free learning platforms.</p><span class="badge-grey">Coming Soon</span></div></div></div>
      <div class="col-md-6 col-lg-4 reveal"><div class="ga-card blog-card h-100"><img src="assets/images/gallery-lab.jpg" class="card-img-top" alt="Excel guide" loading="lazy"><div class="p-4"><div class="post-meta mb-1"><i class="fa-solid fa-folder"></i>MS Office</div><h6 class="text-navy">Excel for Beginners: Make Your First Marks Sheet</h6><p class="small text-secondary">Step-by-step project from our Basic Computer Course workbook.</p><span class="badge-grey">Coming Soon</span></div></div></div>
    </div>
  </div>
</section>
"""))

# ============================ BLOG ARTICLE ============================
PAGES.append(("blog-ai-tools.html",
"Top 7 Free AI Tools Every Student Should Learn in 2026",
"7 free AI tools that help students in Pakistan study faster, write better and learn new skills — recommended by Global Academy.",
"blog.html", page_header("Top 7 Free AI Tools Every Student Should Learn in 2026", "Blog", "blog-ai-tools.html") + """
<section class="section">
  <div class="container" style="max-width:860px">
    <div class="post-meta mb-3"><i class="fa-solid fa-calendar"></i>Aug 3, 2026 &nbsp;·&nbsp; <i class="fa-solid fa-user"></i>Global Academy Team &nbsp;·&nbsp; <i class="fa-solid fa-folder"></i>AI &amp; Skills</div>
    <img src="assets/images/gallery-lab.jpg" class="rounded-4 shadow w-100 mb-4" alt="Students learning AI tools in the lab" loading="lazy">
    <div class="reveal in">
      <p>At Global Academy, we teach AI as a <strong>basic skill</strong> — just like MS Word or typing. Students who learn these tools early finish assignments faster, understand topics better, and get a head start in freelancing. Here are the 7 free tools we recommend (and practice with in our Basic Computer Course).</p>
      <h4 class="text-navy mt-4">1. ChatGPT — your 24/7 study partner</h4>
      <p>Use it to explain difficult topics in simple words, practice English, check your grammar, and brainstorm ideas. Tip: <em>ask it to quiz you</em> before exams.</p>
      <h4 class="text-navy mt-4">2. Google Gemini — research with sources</h4>
      <p>Gemini connects with Google Search, so it can summarize current topics and long articles — great for assignments and presentations.</p>
      <h4 class="text-navy mt-4">3. Canva (with AI) — design anything</h4>
      <p>Posters, CVs, presentations and social media posts in minutes. Free for students, and perfect for our graphic-design learners.</p>
      <h4 class="text-navy mt-4">4. NotebookLM — master your own notes</h4>
      <p>Upload your chapter or notes, and it creates summaries, questions and explanations based only on <em>your</em> material.</p>
      <h4 class="text-navy mt-4">5. Grammarly — write mistake-free</h4>
      <p>Fixes spelling, punctuation and tone in emails and assignments — essential for professional communication.</p>
      <h4 class="text-navy mt-4">6. Microsoft Copilot — AI inside Office</h4>
      <p>Draft documents in Word, analyze data in Excel, and turn documents into PowerPoint slides faster.</p>
      <h4 class="text-navy mt-4">7. Coursera / Google certificates (free audit)</h4>
      <p>Not exactly AI, but AI-guided learning: many professional courses can be studied free to build your CV alongside academy certificates.</p>
      <div class="note-box my-4"><i class="fa-solid fa-shield-halved me-2"></i><strong>Safety tip:</strong> Never share passwords, CNIC photos or personal data with any AI tool. Use them for learning and ideas — always verify important information yourself.</div>
      <div class="cta-band p-4 text-center mt-5">
        <h4 class="text-white mb-2">Learn These Tools With Us</h4>
        <p class="mb-3 opacity-75 small">AI Basics is included in our 2-month Basic Computer Course — practice on our lab computers with a teacher's guidance.</p>
        <a href="admission.html" class="btn btn-light px-4 fw-bold text-red"><i class="fa-solid fa-pen-to-square me-1"></i>Apply Now</a>
      </div>
      <div class="mt-4"><a href="blog.html" class="small"><i class="fa-solid fa-arrow-left me-1"></i> Back to all articles</a></div>
    </div>
  </div>
</section>
"""))

# ============================ TEACHERS ============================
PAGES.append(("teachers.html",
"Our Teachers & Weekly Plans",
"Meet Global Academy's qualified faculty and see our structured weekly lesson plans for every class.",
"about.html", page_header("Our Teachers", "Teachers", "teachers.html") + """
<section class="section">
  <div class="container">
    <div class="row g-4 mb-5">
      <!-- EDIT: replace with real teacher names, photos and qualifications -->
      <div class="col-md-6 col-lg-3 reveal"><div class="ga-card p-4 text-center h-100"><div class="t-avatar mx-auto mb-3" style="width:72px;height:72px;font-size:1.4rem"><i class="fa-solid fa-user-tie"></i></div><h6 class="text-navy mb-1">Senior Computer Instructor</h6><p class="small text-red fw-semibold mb-1">Computer Science Dept.</p><p class="small text-secondary mb-0">MS Office, typing, AI tools &amp; freelancing modules. <em>(edit name)</em></p></div></div>
      <div class="col-md-6 col-lg-3 reveal"><div class="ga-card p-4 text-center h-100"><div class="t-avatar mx-auto mb-3" style="width:72px;height:72px;font-size:1.4rem"><i class="fa-solid fa-user"></i></div><h6 class="text-navy mb-1">English Faculty</h6><p class="small text-red fw-semibold mb-1">Languages Dept.</p><p class="small text-secondary mb-0">Spoken English, communication &amp; grammar. <em>(edit name)</em></p></div></div>
      <div class="col-md-6 col-lg-3 reveal"><div class="ga-card p-4 text-center h-100"><div class="t-avatar mx-auto mb-3" style="width:72px;height:72px;font-size:1.4rem"><i class="fa-solid fa-user"></i></div><h6 class="text-navy mb-1">Mathematics Faculty</h6><p class="small text-red fw-semibold mb-1">Science Dept.</p><p class="small text-secondary mb-0">SSC/HSSC math with concept-based teaching. <em>(edit name)</em></p></div></div>
      <div class="col-md-6 col-lg-3 reveal"><div class="ga-card p-4 text-center h-100"><div class="t-avatar mx-auto mb-3" style="width:72px;height:72px;font-size:1.4rem"><i class="fa-solid fa-user"></i></div><h6 class="text-navy mb-1">Junior Lab Assistant</h6><p class="small text-red fw-semibold mb-1">Lab &amp; Support</p><p class="small text-secondary mb-0">Lab sessions, practice supervision &amp; student support. <em>(edit name)</em></p></div></div>
    </div>

    <div class="row g-5 align-items-start">
      <div class="col-lg-7">
        <h3 class="text-navy mb-3 reveal"><i class="fa-solid fa-calendar-days text-red me-2"></i>Sample Weekly Lesson Plan — Basic Computer Course</h3>
        <div class="table-responsive reveal">
          <table class="table table-ga table-bordered small">
            <thead><tr><th>Day</th><th>Topic</th><th>Activity</th><th>Homework</th></tr></thead>
            <tbody>
              <tr><td>Monday</td><td>New concept (e.g., Excel formulas)</td><td>Demo + guided practice</td><td>Practice sheet</td></tr>
              <tr><td>Wednesday</td><td>Hands-on lab practice</td><td>Individual tasks on PC</td><td>Mini project</td></tr>
              <tr><td>Friday</td><td>Quiz + review + freelancing tips</td><td>Weekly test &amp; Q&amp;A</td><td>Revision notes</td></tr>
            </tbody>
          </table>
        </div>
        <div class="note-box mt-3 reveal"><i class="fa-solid fa-circle-info me-2"></i>Every teacher prepares a weekly plan in advance — parents may request a copy of the current class plan at the office.</div>
      </div>
      <div class="col-lg-5">
        <div class="ga-card p-4 reveal">
          <div class="icon-circle"><i class="fa-solid fa-user-plus"></i></div>
          <h5 class="text-navy">Join Our Faculty</h5>
          <p class="small text-secondary">Passionate about teaching? We welcome qualified instructors in computing, English and science subjects. Send your CV via WhatsApp or email.</p>
          <a href="https://wa.me/@WA@?text=I%20want%20to%20apply%20as%20a%20teacher.%20My%20CV%20is%20attached." target="_blank" rel="noopener" class="btn btn-wa btn-sm"><i class="fa-brands fa-whatsapp me-1"></i>Send CV on WhatsApp</a>
          <a href="mailto:@EMAIL@?subject=Teacher%20Application" class="btn btn-outline-red btn-sm"><i class="fa-solid fa-envelope me-1"></i>Email CV</a>
        </div>
      </div>
    </div>
  </div>
</section>
"""))

# ============================ TESTIMONIALS ============================
PAGES.append(("testimonials.html",
"Testimonials — Student & Parent Reviews",
"Reviews from Global Academy students and parents about our computer courses, teachers and results.",
"gallery.html", page_header("Testimonials", "Testimonials", "testimonials.html") + """
<section class="section">
  <div class="container">
    <!-- EDIT: replace with real reviews -->
    <div class="row g-4 mb-5">
      <div class="col-md-4 reveal"><div class="quote-card"><i class="fa-solid fa-quote-left"></i><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div><p class="small text-secondary">"I joined with zero computer knowledge. Within two months I was making documents, spreadsheets and even my first CV. The teachers are so patient!"</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">H</div><div><strong class="d-block small text-navy">Hassan R.</strong><small class="text-muted">Basic Computer Course</small></div></div></div></div>
      <div class="col-md-4 reveal"><div class="quote-card"><i class="fa-solid fa-quote-left"></i><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div><p class="small text-secondary">"My daughter's confidence has grown so much. Regular tests and result cards keep us informed about her progress every month."</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">N</div><div><strong class="d-block small text-navy">Mrs. Noreen A.</strong><small class="text-muted">Parent</small></div></div></div></div>
      <div class="col-md-4 reveal"><div class="quote-card"><i class="fa-solid fa-quote-left"></i><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i></div><p class="small text-secondary">"The freelancing module opened my eyes. I created my Fiverr profile during the course and learned exactly which skills buyers want."</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">U</div><div><strong class="d-block small text-navy">Usman T.</strong><small class="text-muted">Student</small></div></div></div></div>
      <div class="col-md-4 reveal"><div class="quote-card"><i class="fa-solid fa-quote-left"></i><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div><p class="small text-secondary">"Small batches mean the teacher actually has time for you. I asked questions freely and never felt left behind."</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">A</div><div><strong class="d-block small text-navy">Ayesha M.</strong><small class="text-muted">Student</small></div></div></div></div>
      <div class="col-md-4 reveal"><div class="quote-card"><i class="fa-solid fa-quote-left"></i><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i></div><p class="small text-secondary">"Fee is very reasonable for the quality. The AI tools section alone was worth it — my son now uses them for his college assignments."</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">T</div><div><strong class="d-block small text-navy">Mr. Tariq S.</strong><small class="text-muted">Parent</small></div></div></div></div>
      <div class="col-md-4 reveal"><div class="quote-card"><i class="fa-solid fa-quote-left"></i><div class="stars"><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star-half-stroke"></i></div><p class="small text-secondary">"Result card culture keeps students serious. Weekly quizzes in the computer course made sure I practiced at home too."</p><div class="d-flex align-items-center gap-3 mt-3"><div class="t-avatar">B</div><div><strong class="d-block small text-navy">Bilal H.</strong><small class="text-muted">Student</small></div></div></div></div>
    </div>

    <div class="text-center mb-4 reveal"><span class="eyebrow">Video Testimonials</span><h3 class="section-title fs-3">Hear It From Them</h3><div class="section-bar mx-auto"></div></div>
    <div class="row g-4">
      <div class="col-md-4 reveal"><div class="coming-soon"><i class="fa-brands fa-youtube"></i><p class="small text-secondary">Student review video</p><span class="badge-grey">Coming Soon on YouTube</span></div></div>
      <div class="col-md-4 reveal"><div class="coming-soon"><i class="fa-brands fa-youtube"></i><p class="small text-secondary">Parent review video</p><span class="badge-grey">Coming Soon on YouTube</span></div></div>
      <div class="col-md-4 reveal"><div class="coming-soon"><i class="fa-brands fa-youtube"></i><p class="small text-secondary">Campus tour video</p><span class="badge-grey">Coming Soon on YouTube</span></div></div>
    </div>
  </div>
</section>
"""))

# ============================ FAQ ============================
PAGES.append(("faq.html",
"FAQs — Frequently Asked Questions",
"Answers about admissions, fees, timings, certificates, computer lab access and results at Global Academy Rawalpindi.",
"contact.html", page_header("Frequently Asked Questions", "FAQ", "faq.html") + """
<section class="section">
  <div class="container" style="max-width:860px">
    <div class="accordion" id="faqAcc">
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button" data-bs-toggle="collapse" data-bs-target="#q1">How do I take admission?</button></h2><div id="q1" class="accordion-collapse collapse show" data-bs-parent="#faqAcc"><div class="accordion-body small">Fill the <a href="admission.html">online admission form</a> or visit the campus. We'll confirm your seat, timing and fee on call/WhatsApp — then you visit once to submit documents and start classes.</div></div></div>
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q2">What is the fee for the Basic Computer Course?</button></h2><div id="q2" class="accordion-collapse collapse" data-bs-parent="#faqAcc"><div class="accordion-body small">We keep fees affordable with monthly installments. Contact us on <a href="https://wa.me/@WA@" target="_blank" rel="noopener">WhatsApp</a> or call <a href="tel:@PHONE_TEL@">@PHONE@</a> for the current fee plan.</div></div></div>
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q3">What are the class timings?</button></h2><div id="q3" class="accordion-collapse collapse" data-bs-parent="#faqAcc"><div class="accordion-body small">Classes run @HOURS@ with multiple batches. You can choose morning, afternoon or evening slots in the admission form.</div></div></div>
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q4">Is there an age limit?</button></h2><div id="q4" class="accordion-collapse collapse" data-bs-parent="#faqAcc"><div class="accordion-body small">No age limit for computer courses — school students, college students, job seekers and home users all join. Batches are grouped by level.</div></div></div>
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q5">Do I get a certificate?</button></h2><div id="q5" class="accordion-collapse collapse" data-bs-parent="#faqAcc"><div class="accordion-body small">Yes — every student who completes a course and passes the final assessment receives a Global Academy certificate of completion.</div></div></div>
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q6">Will I get to practice on a computer?</button></h2><div id="q6" class="accordion-collapse collapse" data-bs-parent="#faqAcc"><div class="accordion-body small">Absolutely. Every class includes dedicated hands-on time in our computer lab — learning by doing is our core method.</div></div></div>
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q7">How are results shared?</button></h2><div id="q7" class="accordion-collapse collapse" data-bs-parent="#faqAcc"><div class="accordion-body small">Weekly quizzes plus a final assessment. Printed result cards are issued at the campus and top performers are featured on our <a href="results.html">Results page</a>.</div></div></div>
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q8">Do you offer online classes?</button></h2><div id="q8" class="accordion-collapse collapse" data-bs-parent="#faqAcc"><div class="accordion-body small">Currently our courses are on-campus for maximum practice time. Online/live class options are planned — join the waiting list on WhatsApp.</div></div></div>
      <div class="accordion-item"><h2 class="accordion-header"><button class="accordion-button collapsed" data-bs-toggle="collapse" data-bs-target="#q9">Where is the academy located?</button></h2><div id="q9" class="accordion-collapse collapse" data-bs-parent="#faqAcc"><div class="accordion-body small">@ADDR@. See the map on our <a href="contact.html">Contact page</a> for directions.</div></div></div>
    </div>
    <div class="cta-band p-4 text-center mt-5 reveal">
      <h4 class="text-white mb-2">Still Have a Question?</h4>
      <p class="small opacity-75 mb-3">Message us on WhatsApp — we usually reply within an hour during office timing.</p>
      <a href="https://wa.me/@WA@" target="_blank" rel="noopener" class="btn btn-light px-4 fw-bold text-red"><i class="fa-brands fa-whatsapp me-1"></i>Ask on WhatsApp</a>
    </div>
  </div>
</section>
"""))

# ============================ CONTACT ============================
PAGES.append(("contact.html",
"Contact Us",
"Contact Global Academy Rawalpindi — phone, WhatsApp, email, campus address, opening hours and location map.",
"contact.html", page_header("Contact Us", "Contact", "contact.html") + """
<section class="section">
  <div class="container">
    <div class="row g-4 mb-5">
      <div class="col-md-6 col-lg-3 reveal"><a href="tel:@PHONE_TEL@" class="ga-card p-4 text-center d-block"><div class="icon-circle mx-auto"><i class="fa-solid fa-phone"></i></div><h6 class="text-navy">Call Us</h6><p class="small text-secondary mb-0">@PHONE@</p></a></div>
      <div class="col-md-6 col-lg-3 reveal"><a href="https://wa.me/@WA@" target="_blank" rel="noopener" class="ga-card p-4 text-center d-block"><div class="icon-circle mx-auto"><i class="fa-brands fa-whatsapp"></i></div><h6 class="text-navy">WhatsApp</h6><p class="small text-secondary mb-0">@PHONE@</p></a></div>
      <div class="col-md-6 col-lg-3 reveal"><a href="mailto:@EMAIL@" class="ga-card p-4 text-center d-block"><div class="icon-circle mx-auto"><i class="fa-solid fa-envelope"></i></div><h6 class="text-navy">Email</h6><p class="small text-secondary mb-0">@EMAIL@</p></a></div>
      <div class="col-md-6 col-lg-3 reveal"><div class="ga-card p-4 text-center"><div class="icon-circle mx-auto"><i class="fa-solid fa-clock"></i></div><h6 class="text-navy">Opening Hours</h6><p class="small text-secondary mb-0">@HOURS@</p></div></div>
    </div>

    <div class="row g-5">
      <div class="col-lg-6">
        <div class="form-card p-4 reveal">
          <h4 class="text-navy mb-1">Send Us a Message</h4>
          <p class="small text-secondary mb-4">Fill this form and it opens in your WhatsApp — press send and we receive it instantly.</p>
          <form data-wa="Website Contact Message" data-wa-num="@WA@">
            <div class="row g-3">
              <div class="col-md-6"><label class="form-label">Your Name *</label><input required class="form-control" data-label="Name"></div>
              <div class="col-md-6"><label class="form-label">Phone *</label><input required class="form-control" type="tel" data-label="Phone"></div>
              <div class="col-12"><label class="form-label">Subject</label>
                <select class="form-select" data-label="Subject"><option>Admission enquiry</option><option>Fee details</option><option>Result enquiry</option><option>Teaching job</option><option>Other</option></select></div>
              <div class="col-12"><label class="form-label">Message *</label><textarea required class="form-control" rows="4" data-label="Message"></textarea></div>
              <div class="col-12"><button class="btn btn-red px-4" type="submit"><i class="fa-brands fa-whatsapp me-2"></i>Send via WhatsApp</button>
              <span class="sent-msg d-none small text-success ms-2"><i class="fa-solid fa-circle-check"></i> Opening WhatsApp…</span></div>
            </div>
          </form>
        </div>
      </div>
      <div class="col-lg-6">
        <div class="reveal">
          <h4 class="text-navy mb-3">Find Us on the Map</h4>
          <!-- EDIT: replace q= with your exact academy location -->
          <iframe class="maps-embed mb-3" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Global Academy location map"
            src="https://maps.google.com/maps?q=Murree%20Road%20Rawalpindi%20Punjab%20Pakistan&t=&z=14&ie=UTF8&iwloc=&output=embed"></iframe>
          <div class="ga-card p-3 d-flex gap-3 align-items-start">
            <i class="fa-solid fa-location-dot text-red fa-lg mt-1"></i>
            <div><strong class="text-navy">@ADDR@</strong><p class="small text-secondary mb-0">Open @HOURS@. Sunday closed. Call before visiting to avoid waiting.</p></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
"""))

# ============================ PRIVACY ============================
PAGES.append(("privacy.html",
"Privacy Policy",
"Global Academy privacy policy — how we collect, use and protect student information submitted through our website forms.",
"", page_header("Privacy Policy", "Privacy", "privacy.html") + """
<section class="section"><div class="container" style="max-width:860px">
  <p class="text-secondary small">Last updated: August 2026</p>
  <h4 class="text-navy mt-4">1. Information We Collect</h4>
  <p class="small text-secondary">When you fill our admission or contact forms, we collect your name, father's name, phone/WhatsApp number, email, address, education, course selection and preferred timing — only to process your admission or enquiry.</p>
  <h4 class="text-navy mt-4">2. How We Use It</h4>
  <p class="small text-secondary">Contacting you about admissions, classes, fees and results; maintaining student records; improving our courses. We do <strong>not</strong> sell or share your data with third-party advertisers.</p>
  <h4 class="text-navy mt-4">3. Where Data Is Stored</h4>
  <p class="small text-secondary">Form submissions are stored in the academy's private Google account (Sheets) and official WhatsApp — accessible only to authorized staff.</p>
  <h4 class="text-navy mt-4">4. Photos & Testimonials</h4>
  <p class="small text-secondary">We publish student photos, results and reviews only with the student's/parent's consent. Contact us anytime to remove your content.</p>
  <h4 class="text-navy mt-4">5. Website Analytics</h4>
  <p class="small text-secondary">We may use Google Analytics (anonymous statistics) to understand website visitors. No personal identity is tracked.</p>
  <h4 class="text-navy mt-4">6. Your Rights</h4>
  <p class="small text-secondary">You may request correction or deletion of your data by emailing <a href="mailto:@EMAIL@">@EMAIL@</a> or messaging us on WhatsApp.</p>
  <h4 class="text-navy mt-4">7. Contact</h4>
  <p class="small text-secondary">Global Academy, @ADDR@ · Phone: <a href="tel:@PHONE_TEL@">@PHONE@</a> · Email: <a href="mailto:@EMAIL@">@EMAIL@</a></p>
</div></section>
"""))

# ============================ TERMS ============================
PAGES.append(("terms.html",
"Terms & Conditions",
"Terms and conditions for using the Global Academy website and enrolling in courses.",
"", page_header("Terms & Conditions", "Terms", "terms.html") + """
<section class="section"><div class="container" style="max-width:860px">
  <p class="text-secondary small">Last updated: August 2026</p>
  <h4 class="text-navy mt-4">1. General</h4>
  <p class="small text-secondary">This website provides information about Global Academy's courses, admissions and results. Content may be updated without notice; please confirm fees and timings with the office before enrolling.</p>
  <h4 class="text-navy mt-4">2. Admissions & Fees</h4>
  <p class="small text-secondary">Admission is confirmed only after form submission, office verification and fee payment. Fees once paid are generally non-refundable; special cases are reviewed by management.</p>
  <h4 class="text-navy mt-4">3. Certificates</h4>
  <p class="small text-secondary">Certificates are awarded upon completing course requirements (attendance, assessments, final project). Academy certificates attest to skills training at Global Academy; they are not a substitute for government board degrees.</p>
  <h4 class="text-navy mt-4">4. Attendance & Conduct</h4>
  <p class="small text-secondary">Students should maintain regular attendance and respectful conduct. The academy may suspend enrollment for serious misconduct.</p>
  <h4 class="text-navy mt-4">5. Results & Photos</h4>
  <p class="small text-secondary">With consent, top results and event photos may be published on this website and our social media for recognition purposes.</p>
  <h4 class="text-navy mt-4">6. External Links</h4>
  <p class="small text-secondary">Links to Google Forms, WhatsApp, YouTube, Facebook and Instagram are provided for convenience; their own terms apply on those platforms.</p>
  <h4 class="text-navy mt-4">7. Contact</h4>
  <p class="small text-secondary">Global Academy, @ADDR@ · Phone: <a href="tel:@PHONE_TEL@">@PHONE@</a> · Email: <a href="mailto:@EMAIL@">@EMAIL@</a></p>
</div></section>
"""))

# ============================ 404 ============================
PAGES.append(("404.html",
"Page Not Found",
"The page you are looking for does not exist. Return to Global Academy homepage.",
"", """
<section class="hero" style="min-height:70vh">
  <div class="container text-center py-5">
    <h1 style="font-size:6rem" class="mb-0"><span class="accent">4</span>0<span class="accent">4</span></h1>
    <h4 class="mb-3">Oops! Page Not Found</h4>
    <p class="lead mb-4 col-lg-6 mx-auto">The page you're looking for moved or never existed. Let's get you back on track.</p>
    <div class="d-flex justify-content-center gap-3 flex-wrap">
      <a href="index.html" class="btn btn-red px-4"><i class="fa-solid fa-house me-2"></i>Go Home</a>
      <a href="courses.html" class="btn btn-outline-light px-4">View Courses</a>
      <a href="contact.html" class="btn btn-outline-light px-4">Contact Us</a>
    </div>
  </div>
</section>
"""))

# ============================ BUILD ============================
if __name__ == "__main__":
    print("Building Global Academy website...")
    for p in PAGES:
        render(*p)
    # Keep empty working folders in git
    for d in ["forms", "pdf", "certificates", "uploads", "assets/icons", "assets/fonts"]:
        os.makedirs(os.path.join(BASE, d), exist_ok=True)
        open(os.path.join(BASE, d, ".gitkeep"), "a").close()
    print("Done — " + str(len(PAGES)) + " pages written.")
