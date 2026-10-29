/* Enquiry form. Posts to Formspree (formspree.io/f/<id>), which emails it to
   the business. This shows the result next to the form instead of leaving the
   page. Without JavaScript the form still posts and Formspree shows its own
   thank-you page. _honey is our old honeypot name, sent on as Formspree's
   _gotcha so bots that fill it are dropped. */
(function () {
  var forms = document.querySelectorAll('form[action*="formspree.io/f/"]');
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
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var d = new FormData(f);
      if (d.has('_honey')) { d.set('_gotcha', d.get('_honey')); d.delete('_honey'); }
      d.delete('_next'); d.delete('_template');
      var b = f.querySelector('[type=submit], button:not([type])');
      if (b) b.disabled = true;
      fetch(f.action, { method: 'POST', headers: { Accept: 'application/json' }, body: d })
        .then(function (r) { return r.ok; }, function () { return false; })
        .then(function (ok) { if (b) b.disabled = false; if (ok) f.reset(); note(ok); });
    });
  });
})();
