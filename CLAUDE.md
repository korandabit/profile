# CLAUDE.md — markkoranda.com site source

Guidance for Claude Code in this repo. **This repo is PUBLIC** (github.com/korandabit/profile) and
every push to `master` deploys markkoranda.com via GitHub Pages. Everything here is site source.

## Public / private — the rule

- **Nothing private is ever committed here** — no backlog tickets, analysis/session notes, agent
  notes, drafts, revision notes, local-machine paths. Private working state lives in the private
  container repo one level up: `D:/code/markkorandacom/` (github.com/korandabit/markkorandacom).
  Its `CLAUDE.md` holds the project protocol, backlog and history; Claude Code loads it as a parent.
- **If that container repo is not present** (e.g. a fresh clone or web session), do not recreate
  working notes in this repo — put findings in the PR description / reply instead.
- Enforced by `tools/check_public_tree.py`: top-level default-deny allowlist + private-path and
  private-content checks. It runs from `.githooks/pre-commit` (enable per clone:
  `git config core.hooksPath .githooks`) and in CI (`.github/workflows/public-guard.yml`).
  A new top-level page (e.g. `talks.md`) fails the guard until it is added to `PUBLIC_TOP` there —
  that is the intended "decide it's public" step.
- Two separate axes: `_config.yml` `exclude` keeps a *public* repo file off the *site*
  (`docs/`, `tools/`, this file). It does not make anything private.

## Site structure

- Jekyll on GitHub Pages, `jekyll-theme-minimal` + `assets/css/style.scss` overrides.
- Pages: `index.md` (home), `blog.md` (curated themes + all posts; carries its own CSS), `nerds.md`
  (talks). GitHub Pages renders front-matter-less `.md` too.
- Posts: `_posts/YYYY-MM-DD-slug.md`, permalinks `/blog/:year/:month/:day/:title/`.
- Layouts: `_layouts/default.html`, `_layouts/post.html` — the post layout reads
  `_data/post_analysis.json` (reading time, structure, read-next) and per-post `analysis:` front
  matter. Both are public site data.
- `photos/` — standalone Lightroom-export gallery (`photos/index.html`).
- `docs/` — white papers, not web-served; link them via their GitHub URL
  (`https://github.com/korandabit/profile/blob/master/docs/...`), never `/docs/...`.

Post front matter:
```yaml
---
author: Mark Koranda
categories: [category1, category2]
date: 'YYYY-MM-DD HH:MM:SS'
excerpt: Brief description for previews
layout: post
tags: [tag1, tag2]
title: Post Title
---
```

## Checks (run before pushing — there is no local Jekyll build)

```bash
python tools/check_public_tree.py      # nothing private in the index
python tools/check_internal_links.py   # source-level stand-in for the CI htmlproofer job
python tools/test_tools.py             # behavioral tests for both
```

CI: `Check Links` (htmlproofer, internal links) and `Public Guard` run on every push to `master`.

## Image optimization

Several WordPress-imported originals shipped at full camera resolution. Optimize before committing
(native Windows Python + Pillow; pass `D:/...` style paths to native exes, not `/d/...`):

```python
from PIL import Image
p = r'D:/code/markkorandacom/profile/images/NAME.jpg'
im = Image.open(p); w, h = im.size
tw = 1600; th = round(h * tw / w)
im.resize((tw, th), Image.LANCZOS).save(p, 'JPEG', quality=82, optimize=True, progressive=True)
```

Check EXIF orientation first and keep `icc_profile`; an opaque PNG can become a JPEG (update refs).
Target: no in-use image over ~400KB without a reason. Originals stay in git history.
