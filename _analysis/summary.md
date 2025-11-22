# Revised Schema: Objective Psycholinguistic Metrics

## Key Changes Based on Feedback

### Removed (Too Subjective)
- Hook strength (1-10)
- Narrative pull (1-10)  
- Accessibility (1-10)

### Added (Objective, Measurable)
- **Sentence metrics:** avg/min/max length (words per sentence)
- **Opening structure:** categorical (definition|narrative|scene|statistic|argument)
- **Domain term density:** specialized terms per 100 words
- **Terms defined inline:** count vs. assumed knowledge
- **Concept rate:** frameworks introduced per 100 words
- **Reference type:** prerequisite|conceptual|continuation|contrast

### Refined (More Specific)
- **Prerequisites:** Decomposed into domain list + cultural list
  - Each domain: name, level (none|awareness|basic-usage|expert), critical (required vs. helpful)
  - Each cultural context: specific name, requires_shift (true/false)
  - Multiple domains allowed (e.g., ai + mental-health)
- **Accessibility:** Split into 3 independent barriers
  - linguistic_barrier (sentence complexity, vocabulary)
  - domain_barrier (specialized knowledge)
  - cultural_barrier (context familiarity)
- **Variance:** By specific dimension, not generic "general reader"

## What These Metrics Expose About Your Corpus

### Measurable Differentiation

**Sentence complexity variance:**
- not-the-point: avg 19.7 words/sentence, stark definitions
- deafhood: longer sentences with subordinate clauses
- Correlates with narrative vs. framework structure

**Concept density spectrum:**
- not-the-point: 0.28 concepts per 100 words (single idea, deep)
- bot-therapy: 0.63 concepts per 100 words (multiple frameworks)
- veteran-story: 0.19 concepts per 100 words (narrative exploration)

**Opening structure patterns:**
- Definition openings → framework posts
- Scene openings → narrative posts
- Statistic openings → evidence-based advocacy

**Domain decomposition:**
- Some posts: zero domains (not-the-point)
- Some posts: multiple domains (bot-therapy = ai + mental-health)
- Allows "low domain_barrier but multiple domains" (bot-therapy explains both)

**Cultural context specificity:**
- deafhood: [hearing-normative-assumptions, CODA-experience]
- veteran-story: [civilian-veteran-gap]
- bot-therapy: [therapy-access-barriers] but doesn't require shift

**Dependency networks:**
- Hub posts (veteran-story → 4 internal references)
- Leaf posts (not-the-point → 0 internal references)
- Series markers (Brief Points on Communication #2)

## Automation vs. Judgment

### Fully Computable
- Word count
- Sentence count → avg/min/max
- Paragraph count
- Citation count (grep for `[^N]`)
- Internal reference count (grep for `post_url`)
- Has lists/code blocks (regex)

### Requires Judgment (But Objective Basis)
- Opening structure (categorical, finite options)
- Domains present (specific list, not generic)
- Cultural contexts (specific, named)
- Terms defined inline (count instances)
- Concepts introduced (count frameworks/ideas)
- Reference type (categorize relationship)

### Derivable
- Concept rate (concepts / word_count * 100)
- Citation density (citations / word_count * 1000)
- Dependency score (internal_references > threshold)
- Domain term density (with domain dictionary)

## Storage Structure

Hybrid recommended:

**In post YAML (minimal, for Jekyll):**
```yaml
analysis:
  word_count: 355
  opening_structure: definition
  accessibility:
    linguistic_barrier: none
    domain_barrier: none
  read_next: [slug1, slug2]
```

**In _data/post_analysis.json (full):**
```json
{
  "not-the-point": {
    "sentence_metrics": {...},
    "terminology": {...},
    "prerequisites": {...}
  }
}
```

## Queries This Enables

**Objective filters:**
- "Posts with avg sentence length < 15 words" (accessible language)
- "Posts with 0 domain prerequisites" (universal entry points)
- "Posts with concept_rate > 0.5" (dense vs. exploratory)
- "Posts requiring [military, psychology] domains"
- "Posts with internal_ref_count > 3" (hub posts)

**Cross-dimensional:**
- "Low linguistic barrier + high domain barrier" (technical but clear)
- "Multiple domains but all defined inline" (accessible expertise)
- "Cultural context that requires perspective shift" (bridge-building posts)

**Network:**
- "Show prerequisite chain for post X"
- "Posts that enhance Y theme"
- "Orphan posts" (no inbound/outbound references)

## Multi-Session Workflow

**Batch 1 (this session):** Framework development, 4 posts analyzed
**Batches 2-9:** 8-10 posts per session, systematic corpus coverage
**Batch 10:** Corpus-wide analysis (avg metrics by theme, dependency graphs, etc.)

Estimated: 9-10 sessions for 76 posts

## Next Steps

1. Validate revised schema on your end
2. Decide storage approach (YAML/JSON/hybrid)
3. Continue or pause at framework stage?

