# Content Improvement Roadmap

Generated from Sessions 11-12 corpus analysis of 35 posts.

## Overview

Three categories of improvements identified:

1. **Strategic Tasks** (`improvement-tasks.md`) - New content, entry points, series completions
2. **Post-Specific Edits** (`post-specific-improvements.md`) - Targeted improvements to existing posts
3. **Network Optimization** - Linking and reference improvements

**Total actionable items:** 31 (12 strategic tasks + 19 post edits)

---

## Phase 1: Quick Wins (Week 1)

**Goal:** Fix broken references and low-hanging accessibility improvements

### Tasks (Est. 4-5 hours total)

- [ ] **ACCESS-001**: Add prerequisite signal to "the-definition-of-deaf" (30-60m)
- [ ] **SERIES-001**: Analyze and link "not-the-point" post (15-30m)
- [ ] **LINK-002**: Connect "awakening-ai" to related posts (30-45m)
- [ ] **LINK-003**: Connect "read-receipts-irl" to communication posts (30-45m)
- [ ] **LINK-004**: Connect "introduction-to-empirical-pragmatism" to philosophy posts (30-45m)
- [ ] Fix 6 broken "read_next" recommendations (see `post-specific-improvements.md`)

**Impact:** Immediate improvement to navigation and accessibility

---

## Phase 2: Content Creation (Weeks 2-3)

**Goal:** Fill critical gaps in the corpus

### High Priority (Est. 6-8 hours)

- [ ] **CONTENT-001**: Create promised AI self-reflection workshop post (4-6h)
  - Title suggestion: "AI-Assisted Self-Reflection Workshop"
  - Link from: stop-avoiding-yourself-the-ai-in-you
  - Structure: How-to with exercises
  - Target: 800-1200w

### Strategic Entry Points (Est. 12-16 hours)

Identify which domains need entry points based on:
- Number of posts in domain (5+)
- Current barrier levels
- Reader demand

Candidate domains for entry posts:
- [ ] **ENTRY-001**: Military theme (17 posts, mostly medium barriers)
- [ ] **ENTRY-002**: War/deployment theme (16 posts, narrative heavy)
- [ ] Consider: AI overview (7 posts, some high barriers)

**Impact:** Makes corpus more accessible to new readers

---

## Phase 3: Post Enhancement (Weeks 3-4)

**Goal:** Improve quality of existing high-traffic posts

### Add Structure (6 posts)

Long narratives that need section breaks or summaries:
- [ ] 7-a-christmas-special (1748w)
- [ ] 9-emotional-warfare (1678w)
- [ ] 15-lead-me-home (1955w)
- [ ] a-need-for-combat (2304w)
- [ ] 12-grenades-cigarettes-or-melons (1940w)
- [ ] 14-everyday (1653w)

**Action:** Add section headers, consider summary bullets at end

### Expand Protocols (4 posts)

Posts with actionable content that could be expanded:
- [ ] right-click-for-ai (280w) - Expand practical steps
- [ ] say-less-and-more (280w) - Add more examples
- [ ] the-agreement-between-reader-and-writer (290w) - Elaborate framework
- [ ] the-fear-and-power-of-singularity (350w) - Add actionable recommendations

**Impact:** Higher value for readers seeking practical guidance

### Add Citations (3 posts)

Framework posts that need academic grounding:
- [ ] awakening-ai - Add sources for AI/consciousness claims
- [ ] read-receipts-irl - Cite communication research
- [ ] the-intellectual-boot-camp - Add pedagogy references

**Impact:** Increased credibility and depth

---

## Phase 4: Network Optimization (Week 5)

**Goal:** Strengthen internal connections

### Domain Bridges (3 posts)

Enhance multi-domain posts to serve as connectors:
- [ ] **BRIDGE-001**: Enhance "awakening-ai" (ai + cognitive-science + ML)
- [ ] **BRIDGE-002**: Enhance "say-less-and-more" (ai + education + communication)
- [ ] **BRIDGE-003**: Enhance "introduction-to-empirical-pragmatism" (philosophy + epistemology + science)

**Action:** Add "further reading" sections organized by domain

### Orphan Rescue

Create meaningful connections for isolated high-value posts:
- [ ] awakening-ai → link to ai-zombie, stop-avoiding-yourself
- [ ] read-receipts-irl → link to agreement-between-reader-and-writer, say-less-and-more
- [ ] introduction-to-empirical-pragmatism → link to words-youve-never-heard

**Impact:** Better discovery, longer reading sessions

---

## Phase 5: Analysis Extension (Ongoing)

**Goal:** Analyze remaining 41 posts

The current analysis framework is solid. Continue with sessions 13-20:
- Session 13-15: Analyze next 15 posts (5 posts each)
- Session 16-18: Analyze next 15 posts
- Session 19-20: Final 11 posts + corpus update

After each batch:
1. Update `post_analysis.json`
2. Regenerate `corpus-index.md`, `dependency-graph.md`, `reading-paths.md`
3. Add YAML to new posts
4. Identify new improvement opportunities

---

## Success Metrics

Track improvement impact:

1. **Accessibility**
   - Increase posts with "none/low" barriers from 5 to 10+
   - Create 2-3 entry points per major domain

2. **Connectivity**
   - Reduce orphaned posts from 26 to <15
   - Increase avg internal references from 0.26 to 0.5+ per post

3. **Quality**
   - Add citations to 50%+ of framework posts
   - Add structure aids to all posts >1500w
   - Define terms in all posts with medium+ domain barriers

4. **Completeness**
   - Analyze all 76 posts (currently 35/76 = 46%)
   - Create promised/referenced posts (1 identified so far)
   - Complete all series with proper bidirectional links

---

## File Reference

All improvement documents in `_analysis/`:

- **improvement-roadmap.md** (this file) - Overall plan
- **improvement-tasks.md** - 12 strategic tasks with acceptance criteria
- **post-specific-improvements.md** - 19 posts with specific edits
- **improvement-findings.json** - Raw data from analysis

Use these alongside:
- **corpus-index.md** - Domain and accessibility index
- **dependency-graph.md** - Reference network
- **reading-paths.md** - Recommended sequences

---

## Getting Started

**Recommended first steps:**

1. Review `improvement-tasks.md` - filter by HIGH/MEDIUM priority
2. Pick 2-3 "Quick Wins" from Phase 1
3. Complete them in a single session
4. Commit with: `feat(content): [describe improvements]`
5. Move to Phase 2 content creation

**Time investment:**
- Phase 1: 4-5 hours (high ROI)
- Phases 2-4: 20-25 hours (comprehensive improvement)
- Phase 5: Ongoing as posts are analyzed

This roadmap assumes ~2-4 hours per week of focused content work.
