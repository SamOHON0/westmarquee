#!/usr/bin/env python3
from build import *

# ------------------------------------------------------------------ home -----
def build_home():
    cats_tiles = f"""
<div class="cats">
  <a href="/hire/?cat=obstacle"><img src="{IMG}2026/04/home-danger-zone.jpg" alt="Obstacle course hire" loading="lazy"><div class="lab"><h3>Obstacle Courses</h3><span>Up to 55ft long</span></div></a>
  <a href="/hire/?cat=castle"><img src="{IMG}2026/05/combi-bouncy-castles-for-hire.png" alt="Combi bouncy castle hire" loading="lazy"><div class="lab"><h3>Combi Castles</h3><span>Princess, Barbie, Paw Patrol, Spiderman</span></div></a>
  <a href="/hire/marquee-hire/"><img src="{IMG}2026/04/marquees-galway-for-hire-rent.jpg" alt="Marquee hire" loading="lazy"><div class="lab"><h3>Marquees</h3><span>Weddings, parties &amp; events</span></div></a>
  <a href="/hire/pub-inflatable/"><img src="{IMG}2026/05/pub-home.jpg" alt="The Pub Inflatable" loading="lazy"><div class="lab"><h3>The Pub Inflatable</h3><span>Our signature piece</span></div></a>
  <a href="/hire/foot-dart-board/"><img src="{IMG}2026/04/home-foot-dart-board.jpg" alt="Foot darts hire" loading="lazy"><div class="lab"><h3>Foot Darts</h3><span>Giant 4 metre board</span></div></a>
</div>"""

    featured = "".join(product_card(p) for p in [PRODUCTS[0], PRODUCTS[3], PRODUCTS[4], PRODUCTS[10], PRODUCTS[9], PRODUCTS[11]])

    county_opts = "".join(f'<option value="{c["slug"]}">{t}</option>'
                          for c in COUNTIES for t in c["towns"])
    reviews = "".join(
        f'<div class="review" data-reveal><div class="stars">{"&#9733;" * r["stars"]}</div><p>&ldquo;{r["text"]}&rdquo;</p><div class="who">{r["who"]}<span>{r["where"]}</span></div></div>'
        for r in REVIEWS)

    body = f"""
{navbar("/")}
<section class="hero">
  <div class="hero-bg"><img src="{IMG}2026/05/pub-home.jpg" alt="The Pub Inflatable set up at an event" loading="eager" fetchpriority="high"></div>
  <div class="wrap">
    <div class="hero-inner">
      <div class="hero-copy">
        <h1>Inflatable and <em>marquee hire</em> across the west</h1>
        <p>Obstacle courses, combi castles, marquees, foot darts and the Pub Inflatable. Based in Oranmore, delivered and set up across Galway, Mayo, Roscommon, Clare and Limerick.</p>
        <div class="hero-actions">
          <a href="/book/" class="btn btn-amber">Book online</a>
          <a href="/hire/" class="btn btn-ghost">See the range</a>
        </div>
      </div>
    </div>
  </div>
</section>
{trustband()}

<div class="wrap">
  <div class="checker" data-reveal>
    <h3>Check your area</h3>
    <p>We cover Galway, Mayo, Roscommon, Clare and Limerick from our base in Oranmore.</p>
    <div class="checker-row">
      <select id="areaSel" aria-label="Select your area">
        <option value="">Select your town...</option>
        {county_opts}
        <option value="__other__">My town isn't listed</option>
      </select>
      <button class="btn btn-green" id="areaBtn">Check my area</button>
    </div>
    <div id="areaOut"></div>
  </div>
</div>

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <h2>Browse by type</h2>
      <p class="lede">Castles, courses, marquees and games, all from one local team. Mix and match into a package for the day.</p>
    </div>
    {cats_tiles}
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="sec-head">
      <h2>Most booked</h2>
      <p class="lede">The units that get booked again and again across the west.</p>
    </div>
    <div class="grid-cards">{featured}</div>
    <div style="text-align:center;margin-top:36px"><a href="/hire/" class="btn btn-line">View the full range</a></div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <h2>How booking works</h2>
    </div>
    <div class="steps">
      <div class="step" data-reveal><div class="num">1</div><h3>Pick your unit</h3><p>Browse the range and choose a castle, course, marquee or game.</p></div>
      <div class="step" data-reveal><div class="num">2</div><h3>Choose your date</h3><p>Send a booking request online. No card needed.</p></div>
      <div class="step" data-reveal><div class="num">3</div><h3>We confirm</h3><p>We check availability and come back with your price, usually same day.</p></div>
      <div class="step" data-reveal><div class="num">4</div><h3>Delivery and setup</h3><p>We deliver, set up and collect on the day.</p></div>
    </div>
  </div>
</section>

<section class="sec tint">
  <div class="wrap">
    <div class="split">
      <div class="img" data-reveal><img src="{IMG}2026/05/pub-home.jpg" alt="The Pub Inflatable, styled like a traditional Irish pub" loading="lazy"></div>
      <div data-reveal>
        <h2>The Pub Inflatable</h2>
        <p>Styled like a traditional Irish pub on the outside, marquee style on the inside. Used as a bar, a seating area or the centrepiece at weddings, festivals and garden parties.</p>
        <ul class="checks">
          <li>{CHECK_SVG}Works as a bar area, seating space or centrepiece</li>
          <li>{CHECK_SVG}Pairs brilliantly with a marquee or castle package</li>
          <li>{CHECK_SVG}Delivered and set up anywhere in the west</li>
        </ul>
        <div class="acts">
          <a href="/hire/pub-inflatable/" class="btn btn-green">See the Pub Inflatable</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head center">
      <h2>Reviews</h2>
    </div>
    <div class="reviews">{reviews}</div>
  </div>
</section>

{cta_band("Book or ask a question", "Send a booking request online, or call us and we will put a package together for your date.")}
{footer()}"""

    extra = f"""<script type="application/ld+json">
{{
  "@context":"https://schema.org","@type":"FAQPage","mainEntity":[
    {{"@type":"Question","name":"What can I hire?","acceptedAnswer":{{"@type":"Answer","text":"{FAQS[0][1]}"}}}},
    {{"@type":"Question","name":"What areas do you cover?","acceptedAnswer":{{"@type":"Answer","text":"{FAQS[1][1]}"}}}},
    {{"@type":"Question","name":"How do I book?","acceptedAnswer":{{"@type":"Answer","text":"{FAQS[2][1]}"}}}},
    {{"@type":"Question","name":"Are your inflatables safe?","acceptedAnswer":{{"@type":"Answer","text":"{FAQS[3][1]}"}}}}
  ]
}}
</script>"""
    write("/index.html", head(
        "Bouncy Castle, Obstacle Course & Marquee Hire Galway, Mayo & the West | West Marquees and Inflatables",
        "Book obstacle courses, combi bouncy castles, foot darts, marquees and the unique Pub Inflatable online. Local Oranmore hire serving Galway, Mayo, Roscommon, Clare and Limerick. Fully insured.",
        "/", extra=extra) + body)

# ------------------------------------------------------------- hire index ----
def build_hire_index():
    cards = "".join(product_card(p) for p in PRODUCTS)
    filters = '<button class="filter-btn active" data-cat="all">All</button>' + "".join(
        f'<button class="filter-btn" data-cat="{k}">{v}</button>' for k, v in CATS.items())
    body = f"""
{navbar("/hire/")}
{page_hero("The full range", "Every castle, course, marquee and game we hire out. Tap anything to see details, check dates and book online.",
           crumbs=[("/", "Home"), (None, "The Range")])}
<section class="sec">
  <div class="wrap">
    <div class="filters" id="filters">{filters}</div>
    <div class="grid-cards" id="grid">{cards}</div>
  </div>
</section>
{cta_band("Not sure what suits your day?", "Tell us the occasion, the ages and your area, and we will recommend the right setup and price up a package.")}
{footer()}"""
    write("/hire/index.html", head(
        "Bouncy Castle & Inflatable Hire Range | West Marquees and Inflatables",
        "Browse the full West Marquees hire range: 55ft obstacle courses, themed combi castles, marquees, foot darts and the Pub Inflatable. Book online for Galway, Mayo, Roscommon, Clare and Limerick.",
        "/hire/") + body)

# ---------------------------------------------------------- product pages ----
def build_products():
    for p in PRODUCTS:
        others = [q for q in PRODUCTS if q["cat"] == p["cat"] and q["slug"] != p["slug"]][:3]
        if len(others) < 3:
            others += [q for q in PRODUCTS if q["cat"] != p["cat"] and q not in others][: 3 - len(others)]
        related = "".join(product_card(q) for q in others)
        body = f"""
{navbar("/hire/")}
{page_hero(p["name"], p["short"], crumbs=[("/", "Home"), ("/hire/", "The Range"), (None, p["name"])])}
<section class="sec">
  <div class="wrap">
    <div class="pd">
      <div class="img"><img src="{IMG}{p['img']}" alt="{html.escape(p['name'])}" loading="eager"></div>
      <div>
        <h2>About this unit</h2>
        <p class="desc">{p['long']}</p>
        <div class="spec">
          <div><b>{p['size']}</b><span>Size</span></div>
          <div><b>{p['ages']}</b><span>Ages</span></div>
          <div><b>Included</b><span>Delivery &amp; setup</span></div>
        </div>
        <h2 style="font-size:22px;margin-top:6px">Check dates &amp; book</h2>
        {widget_embed(p['slug'])}
      </div>
    </div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <div class="sec-head"><h2>You might also like</h2></div>
    <div class="grid-cards">{related}</div>
  </div>
</section>
{footer()}"""
        write(f"/hire/{p['slug']}/index.html", head(
            f"{p['name']} Hire, Galway & the West | West Marquees and Inflatables",
            f"{p['short']} Delivered and set up across Galway, Mayo, Roscommon, Clare and Limerick. Check dates and book online.",
            f"/hire/{p['slug']}/", og_image=f"{IMG}{p['img']}") + body)

# ------------------------------------------------------------------ book -----
def build_book():
    body = f"""
{navbar("")}
{page_hero("Book online", "Pick your unit and date and send a booking request. We confirm availability and price, usually the same day. No card needed.",
           crumbs=[("/", "Home"), (None, "Book online")])}
<section class="sec">
  <div class="wrap" style="max-width:860px">
    {widget_embed()}
    <div style="margin-top:34px">
      <div class="sec-head"><h2 style="font-size:24px">Rather talk to a human?</h2></div>
      <div class="contact-list">
        <a href="tel:{PHONE.replace(' ', '')}">{PHONE_SVG}Call {PHONE}</a>
        <a href="{WHATSAPP}" target="_blank" rel="noopener">{WA_SVG}Chat on WhatsApp</a>
        <a href="mailto:{EMAIL}">{MAIL_SVG}{EMAIL}</a>
      </div>
    </div>
  </div>
</section>
{footer()}"""
    write("/book/index.html", head(
        "Book Online | West Marquees and Inflatables",
        "Book bouncy castles, obstacle courses, marquees and the Pub Inflatable online. Serving Galway, Mayo, Roscommon, Clare and Limerick from Oranmore.",
        "/book/") + body)

# ------------------------------------------------------------- area pages ----
def build_areas():
    tiles = "".join(
        f'<a class="area-tile" href="/areas/{c["slug"]}/"><h3>Co {c["name"]}</h3><p>{len(c["towns"])} areas served</p></a>'
        for c in COUNTIES)
    town_tiles = "".join(
        f'<a class="area-tile" href="/areas/{t["slug"]}/"><h3>{t["name"]}</h3><p>Co {t["county"]}</p></a>'
        for t in TOWNS)
    body = f"""
{navbar("/areas/")}
{page_hero("Areas we cover", "Based in Oranmore, Co Galway, we deliver and set up across the west of Ireland. Find your county or town below.",
           crumbs=[("/", "Home"), (None, "Areas")])}
<section class="sec">
  <div class="wrap">
    <div class="sec-head"><h2>By county</h2></div>
    <div class="areas-grid">{tiles}</div>
    <div class="sec-head" style="margin-top:48px"><h2>Popular towns</h2></div>
    <div class="areas-grid">{town_tiles}</div>
  </div>
</section>
{cta_band("Don't see your town?", "We travel further than the list suggests. Give us a call with your Eircode and we will tell you straight away.")}
{footer()}"""
    write("/areas/index.html", head(
        "Delivery Areas: Galway, Mayo, Roscommon, Clare & Limerick | West Marquees and Inflatables",
        "West Marquees and Inflatables delivers bouncy castles, obstacle courses and marquees across Galway, Mayo, Roscommon, Clare and Limerick. Find your area.",
        "/areas/") + body)

    picks = [PRODUCTS[3], PRODUCTS[4], PRODUCTS[10]]
    for c in COUNTIES:
        towns_list = ", ".join(c["towns"])
        cards = "".join(product_card(p) for p in picks)
        body = f"""
{navbar("/areas/")}
{page_hero(f"Bouncy castle &amp; marquee hire in Co {c['name']}",
           c["blurb"], crumbs=[("/", "Home"), ("/areas/", "Areas"), (None, f"Co {c['name']}")])}
<section class="sec">
  <div class="wrap">
    <div class="split">
      <div>
        <h2>Serving all of {c['name']}</h2>
        <p>We regularly deliver to {towns_list} and everywhere in between. Delivery, setup and collection are all handled by our team, and every unit is cleaned and inspected between hires.</p>
        <ul class="checks">
          <li>{CHECK_SVG}Fully insured for inflatable hire</li>
          <li>{CHECK_SVG}Day, midweek and weekend hire</li>
          <li>{CHECK_SVG}Packages across castles, courses, marquees and games</li>
        </ul>
        <div class="acts" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:20px">
          <a href="/book/" class="btn btn-amber">Book online</a>
          <a href="/hire/" class="btn btn-line">See the range</a>
        </div>
      </div>
      <div class="img" data-reveal><img src="{IMG}2026/04/home-danger-zone.jpg" alt="Obstacle course hire in {c['name']}" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <div class="sec-head"><h2>Popular in {c['name']}</h2></div>
    <div class="grid-cards">{cards}</div>
  </div>
</section>
{footer()}"""
        write(f"/areas/{c['slug']}/index.html", head(
            f"Bouncy Castle Hire {c['name']} | West Marquees and Inflatables",
            f"Bouncy castle, obstacle course and marquee hire across Co {c['name']}: {towns_list}. Delivered and set up, fully insured. Book online.",
            f"/areas/{c['slug']}/") + body)

    for t in TOWNS:
        county = next(c for c in COUNTIES if c["name"] == t["county"])
        cards = "".join(product_card(p) for p in picks)
        body = f"""
{navbar("/areas/")}
{page_hero(f"Bouncy castle hire in {t['name']}",
           t["blurb"], crumbs=[("/", "Home"), ("/areas/", "Areas"), (f"/areas/{county['slug']}/", f"Co {t['county']}"), (None, t["name"])])}
<section class="sec">
  <div class="wrap">
    <div class="split">
      <div>
        <h2>What you can hire in {t['name']}</h2>
        <p>The full West Marquees range is available in {t['name']}: 55ft obstacle courses, themed combi castles, the 4M foot dart board, marquees and the Pub Inflatable. Delivery, setup and collection included.</p>
        <ul class="checks">
          <li>{CHECK_SVG}Fully insured, cleaned between every hire</li>
          <li>{CHECK_SVG}Book online</li>
          <li>{CHECK_SVG}Local team based in Oranmore, Co Galway</li>
        </ul>
        <div class="acts" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:20px">
          <a href="/book/" class="btn btn-amber">Book online</a>
          <a href="tel:{PHONE.replace(' ', '')}" class="btn btn-line">Call {PHONE}</a>
        </div>
      </div>
      <div class="img" data-reveal><img src="{IMG}2026/05/Disco-Home.png" alt="Disco obstacle course hire in {t['name']}" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <div class="sec-head"><h2>Popular in {t['name']}</h2></div>
    <div class="grid-cards">{cards}</div>
  </div>
</section>
{footer()}"""
        write(f"/areas/{t['slug']}/index.html", head(
            f"Bouncy Castle Hire {t['name']}, Co {t['county']} | West Marquees and Inflatables",
            f"Bouncy castle, obstacle course and marquee hire in {t['name']}, Co {t['county']}. Delivered, set up and fully insured. Book online with West Marquees and Inflatables.",
            f"/areas/{t['slug']}/") + body)

# ----------------------------------------------------------------- about -----
def build_about():
    body = f"""
{navbar("/about/")}
{page_hero("A local team that shows up", "West Marquees and Inflatables is run from Oranmore, Co Galway, serving families, clubs, schools and businesses across the west of Ireland.",
           crumbs=[("/", "Home"), (None, "About")])}
<section class="sec">
  <div class="wrap">
    <div class="split">
      <div>
        <h2>Why people book us</h2>
        <p>We keep it simple: quality units, honest prices and a team that turns up on time. Every inflatable is cleaned and inspected between hires, and we are fully insured for inflatable hire, so you can book with total peace of mind.</p>
        <p>From a combi castle in a back garden to a marquee and Pub Inflatable at a wedding, we treat every event like it matters, because to you it does.</p>
        <ul class="checks">
          <li>{CHECK_SVG}Fully insured for inflatable hire</li>
          <li>{CHECK_SVG}Over 40 themes across the range</li>
          <li>{CHECK_SVG}Punctual, friendly and clean service</li>
          <li>{CHECK_SVG}Everything from one team: castles, courses, marquees and games</li>
        </ul>
      </div>
      <div class="img" data-reveal><img src="{IMG}2026/04/marquees-galway-for-hire-rent.jpg" alt="Marquee set up by West Marquees" loading="lazy"></div>
    </div>
  </div>
</section>
<section class="sec tint">
  <div class="wrap">
    <div class="sec-head center"><h2>Reviews</h2></div>
    <div class="reviews">{"".join(f'<div class="review" data-reveal><div class="stars">{"&#9733;" * r["stars"]}</div><p>&ldquo;{r["text"]}&rdquo;</p><div class="who">{r["who"]}<span>{r["where"]}</span></div></div>' for r in REVIEWS)}</div>
  </div>
</section>
{cta_band("Have a date in mind?", "Check availability online now, or ring us for a chat about your event.")}
{footer()}"""
    write("/about/index.html", head(
        "About Us | West Marquees and Inflatables",
        "Meet West Marquees and Inflatables: a local, fully insured hire team based in Oranmore, Co Galway, serving Galway, Mayo, Roscommon, Clare and Limerick.",
        "/about/") + body)

# ------------------------------------------------------------------ faqs -----
def build_faqs():
    body = f"""
{navbar("/faqs/")}
{page_hero("Common questions", "Everything people usually ask before they book. Not covered here? Ring or WhatsApp us any time.",
           crumbs=[("/", "Home"), (None, "FAQs")])}
<section class="sec">
  <div class="wrap">
    {faq_html(FAQS)}
  </div>
</section>
{cta_band("Get in touch", "Send a booking request online, or call us on 085 269 6628.")}
{footer()}"""
    faq_ld = ",".join(
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in FAQS)
    extra = f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{faq_ld}]}}</script>'
    write("/faqs/index.html", head(
        "FAQs | West Marquees and Inflatables",
        "Answers to common questions about bouncy castle, obstacle course and marquee hire with West Marquees and Inflatables: areas, safety, setup, weather and booking.",
        "/faqs/", extra=extra) + body)

# --------------------------------------------------------------- contact -----
def build_contact():
    body = f"""
{navbar("/contact/")}
{page_hero("Get in touch", "Questions, quotes or a package for a bigger event: call, WhatsApp, email or drop us a message below.",
           crumbs=[("/", "Home"), (None, "Contact")])}
<section class="sec">
  <div class="wrap">
    <div class="contact-grid">
      <div>
        <h2>Talk to us</h2>
        <p class="lede" style="margin-top:8px">We are quickest on the phone or WhatsApp, and we answer emails every day.</p>
        <div class="contact-list">
          <a href="tel:{PHONE.replace(' ', '')}">{PHONE_SVG}Call {PHONE}</a>
          <a href="{WHATSAPP}" target="_blank" rel="noopener">{WA_SVG}Chat on WhatsApp</a>
          <a href="mailto:{EMAIL}">{MAIL_SVG}{EMAIL}</a>
          <div>{PIN_SVG}Oranmore, Co Galway</div>
        </div>
        <p style="margin-top:18px;font-weight:700;color:var(--ink-soft)">Booking a specific unit for a specific date? The fastest route is the <a href="/book/" style="color:var(--green);text-decoration:underline">online booking page</a>.</p>
      </div>
      <!-- FormSubmit: enquiries go to Sam pre-launch. At handover swap the address for {EMAIL} and Hugh clicks the one-time activation link on first submission. -->
      <form class="enquiry" action="https://formsubmit.co/samohigginsemail@gmail.com" method="POST">
        <input type="hidden" name="_subject" value="Website enquiry: West Marquees and Inflatables">
        <input type="hidden" name="_next" value="{DOMAIN}/contact/thanks/">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">
        <div class="fld"><label for="n">Your name</label><input id="n" name="name" type="text" required></div>
        <div class="fld"><label for="p">Phone</label><input id="p" name="phone" type="tel" required></div>
        <div class="fld"><label for="e">Email</label><input id="e" name="email" type="email"></div>
        <div class="fld"><label for="d">Date of event</label><input id="d" name="date" type="date"></div>
        <div class="fld"><label for="m">What are you after?</label><textarea id="m" name="message" rows="4" placeholder="Castle, marquee, area, guest numbers..."></textarea></div>
        <button type="submit" class="btn btn-amber">Send enquiry</button>
      </form>
    </div>
  </div>
</section>
{footer()}"""
    write("/contact/index.html", head(
        "Contact Us | West Marquees and Inflatables",
        "Contact West Marquees and Inflatables in Oranmore, Co Galway. Call 085 269 6628, WhatsApp us or send an enquiry about bouncy castle, obstacle course and marquee hire.",
        "/contact/") + body)

# ---------------------------------------------------------------- thanks -----
def build_thanks():
    body = f"""
{navbar("")}
{page_hero("Enquiry sent", "Thanks a million. We have your message and we will come back to you shortly, usually the same day.")}
<section class="sec">
  <div class="wrap" style="text-align:center">
    <p class="lede" style="margin:0 auto 26px">In a hurry? Ring or WhatsApp us on {PHONE} and we will sort you out straight away.</p>
    <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a href="/" class="btn btn-green">Back to home</a>
      <a href="/book/" class="btn btn-amber">Book online</a>
    </div>
  </div>
</section>
{footer()}"""
    write("/contact/thanks/index.html", head(
        "Enquiry Sent | West Marquees and Inflatables",
        "Your enquiry has been sent to West Marquees and Inflatables. We usually reply the same day.",
        "/contact/thanks/", extra='<meta name="robots" content="noindex">') + body)

# --------------------------------------------------------------- privacy -----
def build_privacy():
    body = f"""
{navbar("")}
{page_hero("Privacy &amp; cookies", "The short version: we only collect what we need to run your booking, and we never sell your data.",
           crumbs=[("/", "Home"), (None, "Privacy")])}
<section class="sec">
  <div class="wrap" style="max-width:760px">
    <h2 style="font-size:24px">What we collect</h2>
    <p class="lede" style="margin-top:8px">When you book or enquire we collect your name, phone number, email, event date and delivery address. We use these only to manage your booking and to contact you about it.</p>
    <h2 style="font-size:24px;margin-top:30px">Booking system</h2>
    <p class="lede" style="margin-top:8px">Online bookings are processed by PartyOps, our booking software provider, acting as a data processor on our behalf. Your details are stored securely and used solely to manage your booking.</p>
    <h2 style="font-size:24px;margin-top:30px">Cookies</h2>
    <p class="lede" style="margin-top:8px">This site uses essential cookies needed for the site and the booking widget to function. If we add analytics in future, we will ask for your consent first.</p>
    <h2 style="font-size:24px;margin-top:30px">Your rights</h2>
    <p class="lede" style="margin-top:8px">Under GDPR you can ask us at any time what data we hold about you, ask us to correct it, or ask us to delete it. Email {EMAIL} and we will sort it.</p>
  </div>
</section>
{footer()}"""
    write("/privacy/index.html", head(
        "Privacy & Cookies | West Marquees and Inflatables",
        "How West Marquees and Inflatables handles your data: what we collect for bookings, how cookies are used on this site, and your GDPR rights.",
        "/privacy/") + body)

# ---------------------------------------------------------------- assets -----
def build_assets():
    write("/assets/favicon.svg", LOGO_MARK)

    site_js = """
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
"""
    write("/assets/site.js", site_js)

# ------------------------------------------------------- sitemap + robots ----
def build_seo_files():
    paths = ["/", "/hire/", "/book/", "/areas/", "/about/", "/faqs/", "/contact/", "/privacy/"]
    paths += [f"/hire/{p['slug']}/" for p in PRODUCTS]
    paths += [f"/areas/{c['slug']}/" for c in COUNTIES]
    paths += [f"/areas/{t['slug']}/" for t in TOWNS]
    urls = "".join(f"<url><loc>{DOMAIN}{p}</loc></url>" for p in paths)
    write("/sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    write("/robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")

# ------------------------------------------------------------------- 404 -----
def build_404():
    body = f"""
{navbar("")}
{page_hero("That page has floated off", "Like a loose balloon, whatever you were looking for is gone. The good stuff is all still here though.")}
<section class="sec">
  <div class="wrap" style="text-align:center">
    <div class="acts" style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">
      <a href="/" class="btn btn-green">Back to home</a>
      <a href="/hire/" class="btn btn-line">See the range</a>
      <a href="/book/" class="btn btn-amber">Book online</a>
    </div>
  </div>
</section>
{footer()}"""
    write("/404.html", head("Page Not Found | West Marquees and Inflatables",
                            "That page could not be found. Browse the West Marquees and Inflatables hire range or book online.",
                            "/404.html") + body)

# ------------------------------------------------------------------ main -----
if __name__ == "__main__":
    build_home()
    build_hire_index()
    build_products()
    build_book()
    build_areas()
    build_about()
    build_faqs()
    build_contact()
    build_thanks()
    build_privacy()
    build_assets()
    build_seo_files()
    build_404()
    n = sum(len(fs) for _, _, fs in os.walk(OUT))
    print(f"Built site: {n} files in {os.path.abspath(OUT)}")
