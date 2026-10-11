#!/usr/bin/env python3
"""Static site generator for westmarqueesandinflatables.ie"""
import os, shutil, html
from data import *

OUT = os.environ.get("SITE_OUT") or os.path.join(os.path.dirname(__file__), "..")

# ---------------------------------------------------------------- logo -------
LOGO_MARK = """<svg viewBox="0 0 64 64" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <g stroke-linejoin="round" stroke-linecap="round">
    <rect x="31" y="4" width="2" height="12" rx="1" fill="#0a5c48"/>
    <path d="M33 5h12l-4.5 3.5L45 12H33z" fill="#ffb31a"/>
    <path d="M32 14 C 18 20, 10 28, 7 36 L 17.3 36 A 5.2 5.2 0 0 0 27.6 36 L 36.4 36 A 5.2 5.2 0 0 0 46.7 36 L 57 36 C 54 28, 46 20, 32 14 Z" fill="#0e7a5f"/>
    <path d="M32 14 C 26 21, 21 28, 19.5 36 L 27.6 36 C 28.5 27, 30 20, 32 14 Z" fill="#ffffff" opacity=".9"/>
    <path d="M32 14 C 38 21, 43 28, 44.5 36 L 36.4 36 C 35.5 27, 34 20, 32 14 Z" fill="#ffffff" opacity=".9"/>
    <path d="M13 38 h38 l-3 20 a 3 3 0 0 1 -3 2.6 H 19 a 3 3 0 0 1 -3 -2.6 Z" fill="#0a5c48"/>
    <path d="M32 44 c -5 0 -7 4 -7 8 v 8.6 h 14 V 52 c 0 -4 -2 -8 -7 -8 Z" fill="#ffb31a"/>
    <circle cx="52" cy="52" r="7" fill="#f4694b"/>
    <path d="M48.5 52 a 3.5 3.5 0 0 1 7 0" fill="none" stroke="#ffffff" stroke-width="1.8"/>
  </g>
</svg>"""

def logo_lockup(h=46, dark=False):
    name_fill = "#ffffff" if dark else "#0a5c48"
    sub_fill = "#ffd57a" if dark else "#d98f00"
    return f"""<svg viewBox="0 0 268 64" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="West Marquees and Inflatables" style="height:{h}px;width:auto">
  <g stroke-linejoin="round" stroke-linecap="round">
    <rect x="31" y="4" width="2" height="12" rx="1" fill="{'#9cc4b6' if dark else '#0a5c48'}"/>
    <path d="M33 5h12l-4.5 3.5L45 12H33z" fill="#ffb31a"/>
    <path d="M32 14 C 18 20, 10 28, 7 36 L 17.3 36 A 5.2 5.2 0 0 0 27.6 36 L 36.4 36 A 5.2 5.2 0 0 0 46.7 36 L 57 36 C 54 28, 46 20, 32 14 Z" fill="#0e7a5f"/>
    <path d="M32 14 C 26 21, 21 28, 19.5 36 L 27.6 36 C 28.5 27, 30 20, 32 14 Z" fill="#ffffff" opacity=".92"/>
    <path d="M32 14 C 38 21, 43 28, 44.5 36 L 36.4 36 C 35.5 27, 34 20, 32 14 Z" fill="#ffffff" opacity=".92"/>
    <path d="M13 38 h38 l-3 20 a 3 3 0 0 1 -3 2.6 H 19 a 3 3 0 0 1 -3 -2.6 Z" fill="#0a5c48"/>
    <path d="M32 44 c -5 0 -7 4 -7 8 v 8.6 h 14 V 52 c 0 -4 -2 -8 -7 -8 Z" fill="#ffb31a"/>
    <circle cx="52" cy="52" r="7" fill="#f4694b"/>
    <path d="M48.5 52 a 3.5 3.5 0 0 1 7 0" fill="none" stroke="#ffffff" stroke-width="1.8"/>
  </g>
  <text x="72" y="32" font-family="Fredoka, sans-serif" font-weight="600" font-size="24" fill="{name_fill}">West Marquees</text>
  <text x="73" y="52" font-family="Nunito, sans-serif" font-weight="800" font-size="12.5" letter-spacing="3.2" fill="{sub_fill}">&amp; INFLATABLES</text>
</svg>"""

# ------------------------------------------------------------ shared bits ----
CHECK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>'
WA_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.15-1.7-.85-2-.95-.27-.1-.46-.15-.65.15-.2.3-.75.95-.92 1.14-.17.2-.34.22-.63.07-.3-.15-1.25-.46-2.38-1.47-.88-.78-1.47-1.75-1.64-2.05-.17-.3-.02-.46.13-.6.13-.13.3-.34.45-.5.15-.18.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.65-1.57-.9-2.15-.23-.56-.47-.48-.65-.5h-.55c-.2 0-.5.07-.76.37-.27.3-1 1-1 2.42s1.03 2.8 1.17 3c.15.2 2.02 3.08 4.9 4.32.68.3 1.22.47 1.63.6.69.22 1.31.19 1.8.12.55-.08 1.7-.7 1.94-1.36.24-.67.24-1.24.17-1.36-.07-.12-.27-.2-.56-.34ZM12 2a10 10 0 0 0-8.5 15.3L2 22l4.8-1.5A10 10 0 1 0 12 2Z"/></svg>'
FB_SVG = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.5 9.9v-7H8v-2.9h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6v1.9h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 22 12Z"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.81.36 1.6.7 2.34a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.74.34 1.53.57 2.34.7A2 2 0 0 1 22 16.92z"/></svg>'
MAIL_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 7 10 6 10-6"/></svg>'
PIN_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0Z"/><circle cx="12" cy="10" r="3"/></svg>'

NAV_ITEMS = [
    ("/", "Home"),
    ("/hire/", "The Range"),
    ("/areas/", "Areas We Cover"),
    ("/about/", "About"),
    ("/faqs/", "FAQs"),
    ("/contact/", "Contact"),
]

def head(title, desc, path, og_image=None, extra=""):
    og_image = og_image or f"{DOMAIN}{IMG}2026/05/pub-home.jpg"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{DOMAIN}{path}">
<meta property="og:type" content="website">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">
{{
  "@context":"https://schema.org","@type":"EntertainmentBusiness",
  "name":"West Marquees and Inflatables",
  "url":"{DOMAIN}/",
  "telephone":"{PHONE_INTL}",
  "email":"{EMAIL}",
  "image":"{DOMAIN}{IMG}2026/05/pub-home.jpg",
  "description":"Local hire of obstacle courses, combi bouncy castles, foot darts, marquees and the unique Pub Inflatable across Galway, Mayo, Roscommon, Clare and Limerick. Fully insured.",
  "address":{{"@type":"PostalAddress","addressLocality":"Oranmore","addressRegion":"Co Galway","addressCountry":"IE"}},
  "areaServed":["Galway","Mayo","Roscommon","Clare","Limerick"]
}}
</script>
{extra}
</head>
<body>
"""

def navbar(active=""):
    on = ' class="on"'
    links = "".join(
        f'<a href="{href}"{on if href == active else ""}>{label}</a>'
        for href, label in NAV_ITEMS)
    mlinks = "".join(f'<a href="{href}">{label}</a>' for href, label in NAV_ITEMS)
    return f"""
<div class="topbar">
  <div class="wrap">
    <div>Serving Galway, Mayo, Roscommon, Clare &amp; Limerick</div>
    <div><a href="tel:{PHONE.replace(' ', '')}">Call {PHONE}</a></div>
  </div>
</div>
<header class="nav">
  <div class="wrap">
    <a href="/" class="brand" aria-label="West Marquees and Inflatables home">{logo_lockup(46)}</a>
    <nav class="navlinks">{links}</nav>
    <a href="/book/" class="btn btn-amber nav-cta">Book online</a>
    <button class="burger" id="burger" aria-label="Menu"><span></span><span></span><span></span></button>
  </div>
  <div class="mobile-menu" id="mobileMenu">{mlinks}<a href="/book/">Book online</a></div>
</header>
"""

def footer():
    range_links = "".join(f'<a href="/hire/{p["slug"]}/">{p["name"]}</a>' for p in PRODUCTS[:6])
    county_links = "".join(f'<a href="/areas/{c["slug"]}/">Hire in {c["name"]}</a>' for c in COUNTIES)
    return f"""
<footer>
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        {logo_lockup(52, dark=True)}
        <p style="max-width:38ch">Obstacle course, combi castle, marquee, foot dart and Pub Inflatable hire based in Oranmore, Co Galway. Fully insured, delivered and set up across the west of Ireland.</p>
        <div class="socials">
          <a href="{FACEBOOK}" target="_blank" rel="noopener" aria-label="Facebook">{FB_SVG}</a>
          <a href="{WHATSAPP}" target="_blank" rel="noopener" aria-label="WhatsApp">{WA_SVG}</a>
        </div>
      </div>
      <div class="foot-col">
        <h4>The Range</h4>
        {range_links}
        <a href="/hire/">View everything</a>
      </div>
      <div class="foot-col">
        <h4>Areas</h4>
        {county_links}
        <a href="/areas/">All areas</a>
      </div>
      <div class="foot-col">
        <h4>Get in touch</h4>
        <a href="tel:{PHONE.replace(' ', '')}">{PHONE}</a>
        <a href="mailto:{EMAIL}">Email us</a>
        <a href="/book/">Book online</a>
        <a href="/contact/">Contact page</a>
        <span style="display:block;padding:4px 0;font-size:14.5px">Oranmore, Co Galway</span>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; <span id="yr"></span> West Marquees and Inflatables. All rights reserved.</span>
      <span><a href="/privacy/">Privacy &amp; cookies</a> &middot; Site by <a href="https://squaretwo.ie" target="_blank" rel="noopener">SquareTwo</a></span>
    </div>
  </div>
</footer>
<a href="{WHATSAPP}" target="_blank" rel="noopener" class="wa-float" aria-label="Chat on WhatsApp">{WA_SVG}</a>
<div class="cookiebar" id="cookiebar">
  <p>We use essential cookies to make this site work. See our <a href="/privacy/">privacy notice</a>.</p>
  <button class="btn btn-green" id="cookieOk">Grand, got it</button>
</div>
<script src="/assets/site.js" defer></script>
<script src="{PARTYOPS}/price-sync.js" data-business-id="{BUSINESS_ID}" defer></script>
</body>
</html>
"""

def page_hero(title, sub, crumbs=None, img=None):
    crumb_html = ""
    if crumbs:
        parts = " &rsaquo; ".join(f'<a href="{h}">{t}</a>' if h else t for h, t in crumbs)
        crumb_html = f'<div class="crumbs">{parts}</div>'
    bg = f'<div class="ph-bg"><img src="{img}" alt="" loading="eager"></div>' if img else ""
    cls = "page-hero with-img" if img else "page-hero"
    return f"""
<section class="{cls}">
  {bg}
  <div class="wrap">
    {crumb_html}
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</section>
<div class="stripe" aria-hidden="true"></div>
"""

def img_url(p, absolute=False):
    """Product images are old WordPress upload paths (served from IMG) unless they start with "/"."""
    path = p["img"] if p["img"].startswith("/") else IMG + p["img"]
    return (DOMAIN if absolute else "") + path

def product_card(p):
    return f"""
<a class="pcard" href="/hire/{p['slug']}/" data-cat="{p['cat']}" data-reveal>
  <div class="pcard-img"><span class="pcard-tag">{p['tag']}</span><img src="{img_url(p)}" alt="{html.escape(p['name'])}" loading="lazy"></div>
  <div class="pcard-body">
    <h3>{p['name']}</h3>
    <p>{p['short']}</p>
    <div class="pcard-foot"><div class="card-price">Call for price</div><span class="pcard-cta">View &amp; book</span></div>
  </div>
</a>"""

def widget_embed(item=None):
    item_attr = f' data-item="{item}"' if item else ""
    return f"""
<div class="book-shell">
  <script src="{PARTYOPS}/widget.js" data-business-id="{BUSINESS_ID}"{item_attr}></script>
  <p class="book-note">Send a booking request and we confirm availability and price, usually the same day. No card needed.</p>
</div>"""

def cta_band(h, p):
    return f"""
<section class="ctaband">
  <div class="wrap">
    <h2>{h}</h2>
    <p>{p}</p>
    <div class="acts">
      <a href="/book/" class="btn btn-amber">Book online</a>
      <a href="tel:{PHONE.replace(' ', '')}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>"""

def write(path, content):
    full = os.path.join(OUT, path.lstrip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)

def trustband():
    items = ["Fully insured", "Delivered &amp; set up", "Cleaned between hires", "Day, midweek &amp; weekend hire"]
    spans = "".join(f"<span>{CHECK_SVG}{t}</span>" for t in items)
    return f'<div class="trustband"><div class="wrap">{spans}</div></div>'

def faq_html(faqs):
    out = []
    for q, a in faqs:
        out.append(f'<div class="faq-item"><button class="faq-q">{q}<span class="pm"></span></button><div class="faq-a"><p>{a}</p></div></div>')
    return f'<div class="faq-wrap">{"".join(out)}</div>'
