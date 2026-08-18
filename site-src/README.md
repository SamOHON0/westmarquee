# Site generator

Static site generator for westmarqueesandinflatables.ie.

- `data.py` holds all content: products, areas, towns, reviews, FAQs, contact details, the PartyOps business ID.
- `pages.py` builds every page. Run `python3 pages.py` from this folder; output goes to the repo root (or set `SITE_OUT=/path` to build elsewhere).
- `build.py` has the shared layout: nav, footer, logo, page hero, cards, widget embed.

Editing content = edit `data.py`, rebuild, commit. Do not hand-edit the generated HTML at the repo root; it gets overwritten.
