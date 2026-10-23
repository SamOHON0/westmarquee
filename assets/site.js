
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

/* product photo gallery: thumbnails swap the main photo */
document.querySelectorAll('.pd .gal').forEach(function (g) {
  var main = g.querySelector('.main');
  g.querySelectorAll('.thumbs button').forEach(function (b) {
    b.addEventListener('click', function () {
      main.src = b.dataset.src;
      g.querySelectorAll('.thumbs button').forEach(function (x) { x.classList.toggle('on', x === b); });
    });
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

/* ---------------------------------------------------------------- availability
   Date-first availability on the home page. Asks PartyOps what is free on a
   given day and lists it. Products flagged price_on_request come back from the
   API as unavailable, so while the catalogue is unpriced this correctly shows
   the empty state instead of inventing an answer. */
(function () {
  var grid = document.getElementById('avGrid');
  if (!grid) return;

  var API = 'https://partyops.app/api/day-availability';
  var BIZ = 'cb395296-bd08-492a-a0fa-162f5fe5227b';
  var PHONE_TEXT = '085 269 6628';
  var PHONE_HREF = '+353852696628';
  var MAX_MONTHS_AHEAD = 12;

  var monthLabel = document.getElementById('avMonth');
  var result = document.getElementById('avResult');
  var prevBtn = document.getElementById('avPrev');
  var nextBtn = document.getElementById('avNext');

  var today = new Date(); today.setHours(0, 0, 0, 0);
  var view = new Date(today.getFullYear(), today.getMonth(), 1);
  var selected = null;
  var cache = {};

  function ymd(d) {
    return d.getFullYear() + '-' + String(d.getMonth() + 1).padStart(2, '0') +
           '-' + String(d.getDate()).padStart(2, '0');
  }

  function callLine(lead) {
    return lead + ' Give us a ring on <a href="tel:' + PHONE_HREF + '">' + PHONE_TEXT + '</a>.';
  }

  function render() {
    var year = view.getFullYear(), month = view.getMonth();
    monthLabel.textContent = view.toLocaleDateString('en-IE', { month: 'long', year: 'numeric' });
    var minView = new Date(today.getFullYear(), today.getMonth(), 1);
    var maxView = new Date(today.getFullYear(), today.getMonth() + MAX_MONTHS_AHEAD, 1);
    prevBtn.disabled = view <= minView;
    nextBtn.disabled = view >= maxView;

    grid.innerHTML = '';
    ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'].forEach(function (d) {
      var el = document.createElement('div');
      el.className = 'avail-dow';
      el.textContent = d;
      grid.appendChild(el);
    });

    var lead = (new Date(year, month, 1).getDay() + 6) % 7; /* Monday-first */
    for (var i = 0; i < lead; i++) {
      var blank = document.createElement('div');
      blank.className = 'avail-day blank';
      grid.appendChild(blank);
    }

    var daysIn = new Date(year, month + 1, 0).getDate();
    for (var d = 1; d <= daysIn; d++) {
      var date = new Date(year, month, d);
      var iso = ymd(date);
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'avail-day' + (selected === iso ? ' sel' : '');
      btn.textContent = d;
      if (date < today) {
        btn.disabled = true;
      } else {
        btn.addEventListener('click', (function (isoDate) {
          return function () { selected = isoDate; render(); load(isoDate); };
        })(iso));
      }
      grid.appendChild(btn);
    }
  }

  function load(iso) {
    var pretty = new Date(iso + 'T12:00').toLocaleDateString('en-IE',
      { weekday: 'long', day: 'numeric', month: 'long' });
    if (cache[iso]) { show(pretty, cache[iso]); return; }
    result.innerHTML = '<div class="avail-load">Checking ' + pretty + '...</div>';
    fetch(API + '?business_id=' + BIZ + '&date=' + iso)
      .then(function (r) { if (!r.ok) throw new Error('bad response'); return r.json(); })
      .then(function (data) { cache[iso] = data; show(pretty, data); })
      .catch(function () {
        result.innerHTML = '<div class="avail-err">' +
          callLine('We could not check that date just now.') + '</div>';
      });
  }

  function show(pretty, data) {
    var all = data.products || [];
    var items = all.filter(function (p) { return p.available; });
    var gone = all.length - items.length;

    var html = '<div class="avail-date-label">' + pretty + '</div>';
    if (!items.length) {
      /* Neutral, not an error: an unpriced catalogue also lands here, and
         "booked out" would be the wrong thing to tell someone. */
      html += '<div class="avail-hint">' +
        callLine('We cannot confirm that date online just yet.') + '</div>';
      result.innerHTML = html;
      return;
    }

    html += '<div class="avail-count">' + items.length + ' available' +
            (gone > 0 ? ' &middot; ' + gone + ' already booked' : '') + '</div><div class="avail-list">';
    items.forEach(function (p) {
      var img = p.image_url
        ? '<img src="' + encodeURI(p.image_url) + '" alt="" loading="lazy">'
        : '<span class="avail-noimg"></span>';
      var price = (p.price_on_request || !Number(p.price_per_day))
        ? '<div class="pr pr-req">Price on request</div>'
        : '<div class="pr">&euro;' + Math.round(Number(p.price_per_day)) + '</div>';
      var href = p.slug ? '/hire/' + encodeURIComponent(p.slug) + '/' : '/book/';
      html += '<div class="avail-item">' + img +
              '<div class="avail-meta"><div class="nm"></div>' + price + '</div>' +
              '<a class="bk" href="' + href + '">Book</a></div>';
    });
    html += '</div>';
    result.innerHTML = html;

    /* Names come from the API and are set as text, never markup. */
    var nms = result.querySelectorAll('.avail-item .nm');
    items.forEach(function (p, i) { if (nms[i]) nms[i].textContent = p.name; });
  }

  prevBtn.addEventListener('click', function () {
    view = new Date(view.getFullYear(), view.getMonth() - 1, 1); render();
  });
  nextBtn.addEventListener('click', function () {
    view = new Date(view.getFullYear(), view.getMonth() + 1, 1); render();
  });
  render();
})();
