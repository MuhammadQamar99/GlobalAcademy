/* ============================================================
   GLOBAL ACADEMY — main.js
   ============================================================ */
(function () {
  'use strict';

  /* Current year in footer */
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  /* Navbar shrink on scroll */
  var nav = document.querySelector('.ga-navbar');
  function navScroll() {
    if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
  }
  navScroll();
  window.addEventListener('scroll', navScroll, { passive: true });

  /* Animated stat counters */
  function animateCounter(el) {
    var target = parseInt(el.getAttribute('data-target'), 10) || 0;
    var suffix = el.getAttribute('data-suffix') || '';
    var dur = 1500, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.floor(eased * target).toLocaleString();
      if (p < 1) requestAnimationFrame(step);
      else el.innerHTML = target.toLocaleString() + '<span class="suffix">' + suffix + '</span>';
    }
    requestAnimationFrame(step);
  }
  var counters = document.querySelectorAll('.stat-num[data-target]');
  if ('IntersectionObserver' in window && counters.length) {
    var io1 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { animateCounter(e.target); io1.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (c) { io1.observe(c); });
  } else {
    counters.forEach(function (c) { c.textContent = c.getAttribute('data-target'); });
  }

  /* Scroll-reveal */
  var rev = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && rev.length) {
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io2.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    rev.forEach(function (r) { io2.observe(r); });
  } else {
    rev.forEach(function (r) { r.classList.add('in'); });
  }

  /* Gallery filter */
  var filterBtns = document.querySelectorAll('[data-filter]');
  var galleryItems = document.querySelectorAll('[data-cat]');
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      filterBtns.forEach(function (b) { b.classList.remove('active'); });
      btn.classList.add('active');
      var f = btn.getAttribute('data-filter');
      galleryItems.forEach(function (item) {
        var show = (f === 'all' || item.getAttribute('data-cat') === f);
        item.classList.toggle('d-none', !show);
      });
    });
  });

  /* Gallery lightbox (Bootstrap modal) */
  var lbImg = document.getElementById('lightboxImg');
  document.querySelectorAll('a.gallery-item').forEach(function (a) {
    a.addEventListener('click', function () {
      if (lbImg) lbImg.src = a.getAttribute('href');
    });
  });

  /* WhatsApp form builder — forms with [data-wa] submit via wa.me (works with zero setup) */
  var waForms = document.querySelectorAll('form[data-wa]');
  waForms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var num = form.getAttribute('data-wa-num') || '923005084669';
      var title = form.getAttribute('data-wa') || 'Website Enquiry';
      var lines = [];
      var handledRadio = {};
      form.querySelectorAll('[data-label]').forEach(function (inp) {
        var label = inp.getAttribute('data-label');
        if (inp.type === 'radio') {
          if (handledRadio[inp.name]) return;
          handledRadio[inp.name] = true;
          var sel = form.querySelector('input[name="' + inp.name + '"]:checked');
          if (sel) lines.push('*' + label + ':* ' + sel.value);
          return;
        }
        if (inp.type === 'checkbox') return;
        if (inp.type === 'file') {
          lines.push('*' + label + ':* (will send photo on WhatsApp)');
          return;
        }
        if (inp.value) lines.push('*' + label + ':* ' + inp.value);
      });
      var text = 'Assalam-o-Alaikum! *' + title + '*%0A%0A' +
        lines.map(function (l) { return encodeURIComponent(l).replace(/%20/g, '+'); }).join('%0A');
      // Encode message but keep %0A newlines readable
      text = 'Assalam-o-Alaikum! ' + '*' + title + '*\n\n' + lines.join('\n');
      window.open('https://wa.me/' + num + '?text=' + encodeURIComponent(text), '_blank');
      var done = form.querySelector('.sent-msg');
      if (done) done.classList.remove('d-none');
    });
  });

  /* Back to top */
  var toTop = document.getElementById('toTop');
  window.addEventListener('scroll', function () {
    if (toTop) toTop.classList.toggle('show', window.scrollY > 450);
  }, { passive: true });
  if (toTop) toTop.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
})();
