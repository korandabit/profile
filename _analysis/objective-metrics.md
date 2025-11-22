# Objective Metrics for Post Analysis

## Why These Metrics?

Based on actual variance in your corpus, not generic blog metrics.

### What Differentiates Your Posts (From Sample)

**Word count:** 355 - 2064 words
- not-the-point: 355w, single concept, ultra-compressed
- veteran-story: 2064w, narrative + analysis, cultural bridge

**Sentence structure:**
- not-the-point: "Dialog is two people saying words." (6 words, stark)
- deafhood: "There's a poignant sign to start my story if I were telling it in ASL." (15 words, subordinate clause)
- Variance suggests sentence complexity IS a differentiator

**Opening structure:** Actual variance
- Statistic: "Half of Americans with mental illness..." (bot-therapy)
- Definition: "Dialog is two people saying words" (not-the-point)
- Scene: "Pack your shit for two weeks" (veteran-story)
- Sensory/cultural: "There's a poignant sign..." (deafhood)
→ Opening structure predicts what follows

**Domain terminology:**
- bot-therapy: rumination, cognitive mirror, reframing (but all defined)
- deafhood: ASL, CODA, Deafhood, audism (some defined, some assumed)
- not-the-point: Point, Tangent (defined, zero domain terms)
→ Domain term density varies, inline definition varies independently

**Referential density:**
- bot-therapy: 8 distinct concepts in 1274 words = 0.63 per 100w
- not-the-point: 1 concept in 355 words = 0.28 per 100w
- veteran-story: 4 major concepts in 2064 words = 0.19 per 100w
→ Concept density inversely correlates with narrative structure

**Citations:**
- bot-therapy: 6 academic sources
- deafhood: 3 external links
- not-the-point: 0
- veteran-story: 6 references (but to own posts + Marlantes)
→ Citation type/density varies

**Self-reference:**
- veteran-story: References 4 own posts
- deafhood: References 2 own posts
- bot-therapy: 0 references
→ Some posts are hubs, some stand alone

**Cultural context signals:**
- deafhood: Opening paragraph EXPLICITLY signals unfamiliar cultural context
- bot-therapy: Opening paragraph signals problem (mental health gap) but not cultural shift
→ Some posts signal their own prerequisites

## Computable Metrics

### Can automate:
- Word count
- Sentence count → avg sentence length
- Paragraph count → avg paragraph length
- Citation count (grep for footnotes)
- Internal reference count (grep for post_url)
- Has lists/numbered items (regex)
- Domain term count (with dictionary)

### Requires judgment but objective basis:
- Opening structure (categorize: narrative/definition/argument/scene/statistic)
- Domains present (list them: ai, military, deaf-culture, psychology, etc.)
- Cultural contexts (specific: CODA-experience, veteran-civilian-gap, hearing-normative-assumptions)
- Terms defined inline (count vs. assumed)
- Concept introduction rate (count frameworks introduced)

### Can derive:
- Concept density (concepts / word_count * 100)
- Citation density (citations / word_count * 1000)
- Dependency score (internal_references > threshold)

## Key Changes from Original Schema

### REMOVED (too subjective):
- Hook strength 1-10
- Narrative pull 1-10
- Accessibility 1-10 (replaced with 3 independent barriers)

### ADDED (objective differentiators):
- Sentence metrics (avg, max length)
- Opening structure (categorical)
- Domain term density
- Terms defined inline vs. assumed
- Concept introduction rate
- Multiple domains (decomposed)
- Cultural context specificity
- Prerequisites signaled in opening
- Reference type (prerequisite vs. conceptual vs. continuation)

### REFINED:
- Prerequisites: Decomposed into specific domains + levels
- Accessibility: Split into linguistic/domain/cultural barriers
- Variance: Measured by specific dimension (not "general reader")

## What This Enables

### Can now answer:
- "Show me posts with low linguistic barrier, high domain barrier" (technical but clear)
- "Which posts signal their prerequisites in opening paragraph?"
- "Posts with >5 concepts per 1000 words" (dense vs. exploratory)
- "Posts requiring military + psychology domain knowledge"
- "Average sentence length by theme" (are AI posts simpler language?)
- "Which posts are hubs?" (high internal reference count)

### Can't answer (and shouldn't):
- "Which posts are most compelling?" (subjective)
- "Best posts for psychologists" (essentialist)

