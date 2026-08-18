# West Marquees and Inflatables: launch handoff

Multi-page static site + live PartyOps booking for Hugh (westmarqueesandinflatables.ie). Site files live at the repo root; the generator is in `site-src/` (see its README).

## Deploy (5 minutes)

```
# from this folder
git remote add origin git@github.com:<you>/westmarquees-site.git
git push -u origin main
```

Then in Vercel: New Project, import the repo, framework preset "Other", no build command, output directory "." and deploy. Point westmarqueesandinflatables.ie at the project (Vercel > Domains) and update the nameservers/CNAME at the registrar. vercel.json already sets trailing slashes and asset caching; 404.html is picked up automatically.

## Booking system (LIVE in production PartyOps)

- Business ID: `cb395296-bd08-492a-a0fa-162f5fe5227b`
- Owner login: westmarqueesandinflatables@gmail.com / WestMarquees2026!  (change before handing to Hugh)
- 12 products, all price_on_request: request mode, no card, verified live on partyops.app
- Booking alerts currently go to samohigginsemail@gmail.com; switch `notification_email` to Hugh at handover
- Widget embedded on /book/ and every product page (deep links via `data-item` slug)
- price-sync.js runs site-wide: prices entered in the PartyOps admin appear on the site automatically

## Contact form

FormSubmit (no account needed), currently pointed at samohigginsemail@gmail.com. Your first submission triggers a one-time activation email; click it and the form is live. At handover, change the form action in `site-src/pages.py` to Hugh's address, rebuild, and have him click the activation link on the first enquiry. Success redirects to /contact/thanks/.

## Remaining launch steps

1. Push + deploy + DNS (above)
2. Submit the contact form once and click the FormSubmit activation link
3. Do one test booking on /book/ (alert lands in your inbox)
4. Get real prices from Hugh, enter in PartyOps admin (draft email to Hugh is in your Gmail drafts)
5. At handover: change PartyOps password, switch notification_email + form address to Hugh
6. Later: Stripe Connect + payment_required when Hugh wants online payments
7. Optional: swap WP-hosted images for local copies once the old WordPress site is retired
