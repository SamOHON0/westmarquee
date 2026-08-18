
/* West Marquees site JS */
document.getElementById('yr') && (document.getElementById('yr').textContent = new Date().getFullYear());

var burger = document.getElementById('burger');
if (burger) burger.addEventListener('click', function () {
  document.getElementById('mobileMenu').classList.toggle('open');
});

/* reveal on scroll */
if ('IntersectionObserver' in window) {
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (en) {
      if (en.isIntersecting) { en.target.style.opacity = '1'; en.target.style.transform = 'translateY(0)'; io.unobserve(en.target); }
    });
  }, { threshold: .08 });
  document.querySelectorAll('[data-reveal]').forEach(function (el, i) {
    el.style.transitionDelay = (i % 4 * 50) + 'ms'; io.observe(el);
  });
  /* safety net: never leave content hidden */
  setTimeout(function () {
    document.querySelectorAll('[data-reveal]').forEach(function (el) {
      el.style.opacity = '1'; el.style.transform = 'translateY(0)';
    });
  }, 1600);
} else {
  document.querySelectorAll('[data-reveal]').forEach(function (el) { el.style.opacity = '1'; el.style.transform = 'none'; });
}

/* area checker (home) */
var areaBtn = document.getElementById('areaBtn');
if (areaBtn) areaBtn.addEventListener('click', function () {
  var sel = document.getElementById('areaSel'), out = document.getElementById('areaOut');
  var v = sel.value, label = sel.options[sel.selectedIndex] ? sel.options[sel.selectedIndex].text : '';
  if (!v) { out.textContent = 'Pick your town first.'; out.style.color = 'var(--ink-faint)'; return; }
  if (v === '__other__') {
    out.innerHTML = 'Not listed? <a href="tel:0852696628" style="color:var(--green);text-decoration:underline">Give us a call</a>, we may still reach you.';
    out.style.color = 'var(--ink-soft)';
  } else {
    out.innerHTML = 'Yes! We deliver to ' + label + '. <a href="/book/" style="color:var(--green);text-decoration:underline">Book online now</a> or <a href="/areas/' + v + '/" style="color:var(--green);text-decoration:underline">see your area page</a>.';
    out.style.color = 'var(--green)';
  }
});

/* catalogue filters (hire index) */
var filters = document.getElementById('filters');
if (filters) {
  var setFilter = function (cat) {
    document.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.toggle('active', b.dataset.cat === cat); });
    document.querySelectorAll('#grid .pcard').forEach(function (c) {
      c.style.display = (cat === 'all' || c.dataset.cat === cat) ? '' : 'none';
    });
  };
  filters.addEventListener('click', function (e) {
    var b = e.target.closest('.filter-btn'); if (!b) return; setFilter(b.dataset.cat);
  });
  var params = new URLSearchParams(location.search);
  if (params.get('cat')) setFilter(params.get('cat'));
}

/* FAQ accordion */
document.querySelectorAll('.faq-q').forEach(function (q) {
  q.addEventListener('click', function () {
    var item = q.parentElement, a = item.querySelector('.faq-a'), open = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(function (i) { i.classList.remove('open'); i.querySelector('.faq-a').style.maxHeight = null; });
    if (!open) { item.classList.add('open'); a.style.maxHeight = a.scrollHeight + 'px'; }
  });
});

/* cookie notice */
try {
  if (!localStorage.getItem('wm-cookie-ok')) document.getElementById('cookiebar').classList.add('show');
  document.getElementById('cookieOk').addEventListener('click', function () {
    localStorage.setItem('wm-cookie-ok', '1');
    document.getElementById('cookiebar').classList.remove('show');
  });
} catch (e) { /* storage unavailable */ }
