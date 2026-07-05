# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository. (Parent directory has no CLAUDE.md — the project root *is* `profile/`; the parent `D:/code/markkorandacom/` is just a container.)

## Project Overview
This is a Jekyll-based personal website/blog for Mark Koranda (markkoranda.com), hosted on GitHub Pages. The site features academic and personal writing on AI, psychology, communication, language science, deaf culture, and military experience.

## Site Structure
- **Main site root**: `profile/` directory contains all Jekyll files
- **Content**: Blog posts in `_posts/` with YAML frontmatter and Markdown content
- **Layouts**: `_layouts/default.html` and `_layouts/post.html` for page templates  
- **Theme**: Uses `jekyll-theme-minimal` with custom CSS overrides
- **Navigation**: `index.md` (homepage), `blog.md` (curated theme-based blog), `nerds.md` (academic focus)

## Development Commands
Since this is a Jekyll site, common development tasks include:

```bash
# Serve locally (if Jekyll installed)
bundle exec jekyll serve

# Build site
bundle exec jekyll build

# GitHub Pages automatically builds on push to main branch
```

## Content Architecture
### Blog Structure (`blog.md`)
- **Featured Themes**: 6 curated theme sections (post counts verified 2026-05-26 against `blog.md` lines 162-241):
  - Discovering AI Chatbots (6 posts)
  - Communication (4 posts)
  - Language Science (3 posts)
  - Cognitive Growth (3 posts)
  - Deaf Culture (9 posts; expanded 2026 per commit `b16afb2`)
  - Military (2 retrospective posts + 9 in "Afghanistan 2013: Real-Time Deployment" sub-section = 11 total)
- **Adjacent collection** (not a theme box; in a `<details>` element after Military): "Dear_" letter series — 3 posts forming a Human→Love / Human→AI / AI→Human triptych.
- **All Posts**: Chronological listing with date and tags

### Post Format
Blog posts use YAML frontmatter with required fields:
```yaml
---
author: Mark Koranda
categories: [category1, category2]
date: 'YYYY-MM-DD HH:MM:SS'
excerpt: Brief description for previews
layout: post
tags: [tag1, tag2, tag3]
title: Post Title
---
```

## Key Configuration
- **_config.yml**: Jekyll configuration with minimal theme, kramdown markdown, rouge syntax highlighting
- **Permalinks**: `/blog/:year/:month/:day/:title/` format
- **Plugins**: jekyll-feed for RSS

## Custom Styling
- `blog.md` contains extensive CSS overrides to disable floating sidebar layout
- Responsive theme boxes for featured content sections
- Mobile-first responsive design for theme containers

## Content Strategy
Based on BLOG_PROJECT_ASSESSMENT.md, the site emphasizes:
- Quality curation over quantity (200-word assessment method)
- Interdisciplinary expertise showcase (Military → Academia → Tech → AI)
- AI content as flagship theme reflecting recent focus
- Academic credibility through Language Science theme

## File Locations
- Configuration: `profile/_config.yml`
- Layouts: `profile/_layouts/`
- Posts: `profile/_posts/` (date-prefixed .md files)
- Assets: `profile/images/`, `profile/assets/css/`
- Pages: `profile/index.md`, `profile/blog.md`, `profile/nerds.md`

## Theory Analysis Protocol (2025-08-16)
**Source**: Compression synthesis session across 128 claims from 48+ theory files

### Epistemic Requirements
- **Evidence format**: e-empirical data, i-interpretive analysis, data-quantitative measures
- **Attribution**: Single global notice, avoid repetitive "author claims"  
- **Sources**: Cite actual files, not meta-analyses or frequency analyses
- **Speculation**: Preserve uncertainty markers, distinguish proposals from facts
- **Instances**: Keep single events single, don't aggregate across sources

### Citation Standards  
- **Valid**: Specific filenames with .txt/.md/.Rmd extensions
- **Invalid**: "terminology analysis", "frequency analysis", meta-analysis files
- **Evidence**: What the text contains, not quotes or interpretive summaries
- **Verification**: All empirical claims require source file validation

### Quality Indicators
- **Good**: "proposes X framework" with file citation and specific evidence  
- **Bad**: "X framework enables optimization" without source or empirical backing
- **Best**: e-specific data points, i-theoretical connections, minimal copula usage

## Historical moves

| Date | What | Where it went | Manifest |
|---|---|---|---|
| 2026-07-05 | essay_linter's v1 structural reading-notes on 5 published essays (e1–e5), parked in a now-retired project `inbox/` (ADR-0013; original artifact no longer exists) | `profile/_analysis/essay-reading-notes.md`, reconstructed from the still-live upstream source (`essay_linter/bench/parse-derivation/derivation-notes.txt`, `derivation.md`, `PARSE_SPEC.md`) | MKC-001 (`../backlog-tickets/MKC-001-durable-home-essay-reading-notes.md`) is the sole record; no separate manifest file |

## Session Start
- Read the backlog: `../backlog-tickets/` (one `# CATALOG:`-blocked .md per ticket; the project's standardized queue). The dir sits at the container root `D:/code/markkorandacom/`, alongside `inbox/`. Scan `inbox/` for new work-asks; durable queue lives in `backlog-tickets/`.