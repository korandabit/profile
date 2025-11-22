# Multi-Session Analysis Instructions

## Overview

Analyze 76 posts across 8-10 sessions.
Each session: 8-10 posts, systematic, token-conscious.

## Storage Strategy: Hybrid

**Minimal YAML in each post:**
```yaml
analysis:
  word_count: 1274
  opening_structure: definition
  accessibility:
    linguistic_barrier: low
    domain_barrier: medium
    cultural_barrier: none
  read_next: [slug1, slug2]
```

**Full analysis in `_data/post_analysis.json`:**
```json
{
  "post-slug": {
    "word_count": 1274,
    "sentence_metrics": {...},
    "terminology": {...},
    "prerequisites": {...},
    "references": {...},
    "accessibility": {...},
    "actionability": {...},
    "recommendations": {...}
  }
}
```

## Session Template

### Session N: [Theme/Date Range]

**Input to Claude (copy this):**
```
Continue systematic post analysis, Session N.

Analyze the following posts using the objective schema in _analysis/schema.yaml:

[List 8-10 post slugs here]

Apply scoping criteria from _analysis/SCOPING-CRITERIA.md:
- Short posts (<400w): minimal scope
- Framework posts: include concept metrics
- Narrative posts: skip concept metrics, include sentence variance
- Universal posts: empty arrays for domains/cultural
- Posts with citations: note count
- Posts with internal refs: full dependency analysis

For each post:
1. Run scope detection (word count, has citations, has internal refs)
2. Apply only relevant metrics
3. Skip non-applicable metrics entirely
4. Validate against scoping rules

Output:
- Update _data/post_analysis.json with full analysis
- Show summary table of analyzed posts
- Report any scoping edge cases

Do NOT update post YAML yet (wait until all analyzed).
```

**Claude will output:**
- Updated `_data/post_analysis.json` (full analysis for 8-10 posts)
- Summary table
- Edge cases

**You do:**
- Review output
- Commit: `git add _data/post_analysis.json && git commit -m "feat(analysis): batch N - [theme/range]"`
- Move to next session

## Session Breakdown (Proposed)

### Session 1: Sample Complete ✓
- bot-therapy, not-the-point, deafhood-unheard, veteran-story
- Framework developed
- Scoping criteria established

### Session 2: AI Theme (6 posts)
```
2025-11-12-bot-therapy  # already done, validate
2023-10-28-stop-avoiding-yourself-the-ai-in-you
2024-09-16-awakening-ai
2024-09-17-ai-zombie
2024-08-30-ai-the-next-technological-leap
2024-07-13-right-click-for-ai
2024-07-17-the-fear-and-power-of-singularity
2023-11-14-know-thaiself
```

### Session 3: Communication Theme (4 posts)
```
2022-11-20-2-not-the-point  # already done, validate
2023-08-08-read-receipts-irl
2022-04-18-the-agreement-between-reader-and-writer
2024-07-13-say-less-and-more
```

### Session 4: Language Science (3 posts)
```
2024-06-11-introduction-to-empirical-pragmatism
2024-06-06-words-youve-never-heard
2024-07-16-all-the-right-words-youve-said-or-read
```

### Session 5: Cognitive Growth (3 posts)
```
2020-10-26-bet-your-life
2020-10-26-bet-your-life-notes
2024-07-20-questions-books
```

### Session 6: Deaf Culture (3 posts)
```
2014-10-04-deafhood-unheard  # already done, validate
2013-10-26-the-definition-of-deaf
2014-10-10-language-with-a-bionic-ear
```

### Session 7: Military - Retrospective (2 posts)
```
2017-04-08-the-unedited-war-story-of-a-veteran  # already done, validate
2017-07-28-the-intellectual-boot-camp
```

### Session 8: Military - 2013 Serialization Part 1 (10 posts)
```
2013-04-17-preface-one-of-those-guys
2013-04-17-1-it-rained
2013-04-17-2-unfinished-predeployment-sentiments
2013-04-18-3-the-nights-after-the-rain
2013-04-18-4-haircut-hysteria
2013-04-18-5-webcam-starts-to-capture
2013-04-20-6-battle-for-peace-and-quiet
2013-04-20-7-a-christmas-special
2013-04-20-8-the-sweeter-side-of-work
2013-04-23-9-emotional-warfare
```

### Session 9: Military - 2013 Serialization Part 2 + Combat (5 posts)
```
2013-04-25-10-a-fog-of-war
2013-04-26-11-the-superbowl-on-afn
2013-04-27-12-grenades-cigarettes-or-melons
2013-05-12-14-everyday
2013-05-16-15-lead-me-home
2013-05-02-a-need-for-combat
```

### Session 10: Remaining Posts (20-30 posts)
All posts not in themes above. Batch into 2-3 sub-sessions if needed.

### Session 11: Corpus-Wide Analysis
- Generate dependency graph (who references whom)
- Calculate averages by theme
- Identify hubs vs. leaf posts
- Concept glossary (terms across posts)
- Reading path recommendations
- Content gap analysis

### Session 12: YAML Updates
- Add minimal analysis to each post's front matter
- Validate Jekyll can read it
- Test filtering/sorting

## Scoping Quick Reference

**Always measure:**
- word_count
- opening_structure
- structure_type
- accessibility barriers
- read_next

**Measure if applicable:**
- sentence_metrics: word_count > 400 OR narrative
- terminology: has domain/cultural terms
- concepts_introduced: framework/analysis posts only
- citations: if has footnotes
- dependencies: if has internal refs
- actionability: framework/how-to posts only

**Skip entirely:**
- sentence_metrics on short posts
- concepts on pure narrative
- dependency analysis on standalone posts

## Edge Cases to Flag

During analysis, report:
- Posts that don't fit categories (neither framework nor narrative)
- Ambiguous domain classification
- Serialized posts (need special handling)
- Missing prerequisites in opening but needed
- Broken internal references

## Validation Checklist (Each Session)

Before committing:
- [ ] Short posts (<400w) have minimal scope
- [ ] Universal posts have empty arrays (not skipped)
- [ ] Framework posts have concept_introduced
- [ ] Narrative posts skip concepts
- [ ] All posts have required fields
- [ ] No placeholder/fake values
- [ ] JSON is valid

## Output Format (Each Session)

Claude should provide:

1. **Updated JSON file** (paste full or show diff)
2. **Summary table:**
```
Post                    | Words | Type      | Scope     | Domains | Barriers
------------------------|-------|-----------|-----------|---------|----------
bot-therapy            | 1274  | framework | standard  | 2       | L:low D:med
not-the-point          | 355   | framework | minimal   | 0       | all:none
```

3. **Edge cases:**
```
- Post X: Ambiguous type (framework + narrative blend)
- Post Y: Cultural term "Z" - should we add to cultural_terms list?
```

4. **Recommendations for next session**

## File Locations

- Schema: `_analysis/schema.yaml`
- Scoping: `_analysis/SCOPING-CRITERIA.md`
- This file: `_analysis/SESSION-INSTRUCTIONS.md`
- Output: `_data/post_analysis.json` (create if doesn't exist)
- Post YAML: Update in Session 12 only

## Starting a New Session

1. Open new Claude Code session
2. Navigate to repo
3. Checkout analysis branch: `git checkout claude/systematic-post-analysis-013B5xpqWPDTFxrga3Z8So73`
4. Copy template above, fill in post slugs
5. Paste to Claude
6. Review output
7. Commit batch
8. Repeat

