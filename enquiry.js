/* Enquiry form -> WhatsApp handoff (23 Oct 2026). While SquareTwo's enquiry
   service is paused, the form opens WhatsApp to the business with the
   details filled in, and the visitor presses send. WA is set per site. */
(function () {
  var WA = '353852696628';
  var forms = document.querySelectorAll('form[action*="squaretwo.ie/api/enquiry"]');
  Array.prototype.forEach.call(forms, function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var lines = [];
      new FormData(f).forEach(function (v, k) {
        v = String(v).trim();
        if (!v || k.charAt(0) === '_') return;
        var el = f.querySelector('[name="' + k + '"]');
        var lab = el && el.id && f.querySelector('label[for="' + el.id + '"]');
        var name = lab ? lab.textContent.trim() : k.replace(/[_-]+/g, ' ').replace(/^\w/, function (c) { return c.toUpperCase(); });
        lines.push(name + ': ' + v);
      });
      if (!lines.length) return;
      window.open('https://wa.me/' + WA + '?text=' + encodeURIComponent('Website enquiry\n' + lines.join('\n')), '_blank', 'noopener');
      var p = f.querySelector('.enquiry-note') || document.createElement('p');
      p.className = 'enquiry-note';
      p.setAttribute('role', 'status');
      p.style.cssText = 'margin:14px 0 0;font-weight:600;color:#15803d';
      p.textContent = 'WhatsApp is opening with your enquiry. Press send in WhatsApp and we will be in touch.';
      f.appendChild(p);
    });
  });
})();
