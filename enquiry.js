/* Enquiry form. Posts to SquareTwo's enquiry service (squaretwo.ie/api/enquiry),
   which emails it to the business. This shows the result next to the form
   instead of leaving the page. Without JavaScript the form still posts and
   the service sends the visitor back here with ?enquiry=sent. */
(function () {
  var forms = document.querySelectorAll('form[action*="squaretwo.ie/api/enquiry"]');
  Array.prototype.forEach.call(forms, function (f) {
    function note(ok) {
      var p = f.querySelector('.enquiry-note') || document.createElement('p');
      p.className = 'enquiry-note';
      p.setAttribute('role', 'status');
      p.style.cssText = 'margin:14px 0 0;font-weight:600;color:' + (ok ? '#15803d' : '#b91c1c');
      p.textContent = ok ? 'Thanks, your enquiry has been sent. We will be in touch soon.'
                         : 'Sorry, that did not send. Please ring us instead.';
      f.appendChild(p);
    }
    if (/[?&]enquiry=sent/.test(location.search)) note(true);
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var b = f.querySelector('[type=submit], button:not([type])');
      if (b) b.disabled = true;
      fetch(f.action, { method: 'POST', headers: { Accept: 'application/json' },
                        body: new URLSearchParams(new FormData(f)) })
        .then(function (r) { return r.ok; }, function () { return false; })
        .then(function (ok) { if (b) b.disabled = false; if (ok) f.reset(); note(ok); });
    });
  });
})();
