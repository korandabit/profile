# Analysis Scoping Criteria

## Problem: Semantic Drift and False Positives

**What happens without scoping:**
- 217-word technical how-to gets same treatment as 2000-word cultural essay
- Zero-domain posts get "domain_barrier: none" (clutters data)
- Standalone posts get empty dependency arrays (noise)
- Serialized posts need different metrics than standalone

## Core Principle: Only Measure What Differentiates

### Post Type Detection (First Pass)

Run this decision tree on every post:

```
1. Word count < 400?
   → SCOPE: minimal (lightweight metrics only)
   → SKIP: domain analysis, dependency analysis
   
2. Has internal references (post_url)?
   → SCOPE: network (include dependency metrics)
   → OTHERWISE: skip dependency section
   
3. Has citations [^N]?
   → SCOPE: evidence-based (include citation metrics)
   → OTHERWISE: skip citation analysis
   
4. Opening is narrative/scene?
   → SCOPE: narrative (sentence variance matters)
   → FOCUS: max/min sentence length, paragraph rhythm
   
5. Opening is definition/framework?
   → SCOPE: conceptual (concept density matters)
   → FOCUS: concept rate, terms defined
   
6. Contains cultural terms (ASL, CODA, veteran, etc.)?
   → SCOPE: cultural (cultural barrier matters)
   → FOCUS: cultural prerequisites, perspective shift
   
7. Otherwise:
   → SCOPE: standard (all applicable metrics)
```

### Metric Applicability Matrix

| Metric | When to Apply | When to Skip |
|--------|---------------|--------------|
| **word_count** | Always | Never |
| **sentence_metrics** | Word count > 400 OR narrative structure | Word count < 400 AND framework structure |
| **opening_structure** | Always | Never |
| **domain_term_density** | Has specialized terms | Zero domain terms (mark as 0, not n/a) |
| **domains** | Has domain terms | No domains (empty array, not skip) |
| **cultural_terms** | Has cultural context | No cultural terms (empty array) |
| **terms_defined_inline** | Has domain or cultural terms | No specialized terms (skip) |
| **concepts_introduced** | Framework/analysis posts | Pure narrative, how-to (skip) |
| **concept_rate** | concepts_introduced exists | Skip if concepts skipped |
| **entities_named** | References people/orgs | Universal/abstract posts (skip) |
| **citation_count** | Has citations | No citations (mark as 0) |
| **has_footnotes** | Always | Never |
| **structure_type** | Always | Never |
| **prerequisites.domains** | Has domain-specific content | Universal posts (empty array) |
| **prerequisites.cultural** | Has cultural-specific content | Universal posts (empty array) |
| **signals_prerequisites** | Has prerequisites | No prerequisites (skip) |
| **references.internal** | Has internal refs | No refs (empty array) |
| **dependency_score** | Has internal refs | No refs (skip) |
| **accessibility.barriers** | Always (but can be "none") | Never |
| **actionability** | Framework/how-to posts | Pure narrative/analysis (skip) |
| **read_next** | Always | Never |

### Specific Rules

**Rule 1: Short Posts (<400 words)**
```yaml
analysis:
  word_count: 355
  opening_structure: definition
  structure_type: framework
  
  accessibility:
    linguistic_barrier: none
    domain_barrier: none
    cultural_barrier: none
  
  read_next: [slug1, slug2]

# SKIP: sentence_metrics, terminology deep-dive, referential_density
```

**Rule 2: Pure Narrative (no frameworks)**
```yaml
analysis:
  word_count: 1947
  
  sentence_metrics:
    avg_sentence_length: 22.3
    max_sentence_length: 68  # narrative variance matters
    min_sentence_length: 4
  
  opening_structure: scene
  structure_type: narrative
  
  # SKIP: concepts_introduced, concept_rate (not framework post)
  # INCLUDE: entities_named (people/places in story)
```

**Rule 3: Universal Posts (no domain/cultural context)**
```yaml
analysis:
  word_count: 355
  
  terminology:
    domain_term_density: 0
    domains: []              # empty, not skipped
    cultural_terms: []       # empty, not skipped
    terms_defined_inline: 2  # BUT still count defined terms (Point, Tangent)
  
  prerequisites:
    domains: []              # empty array = universal
    cultural: []             # empty array = universal
    # SKIP: signals_prerequisites (none to signal)
  
  accessibility:
    linguistic_barrier: none
    domain_barrier: none     # "none" not empty
    cultural_barrier: none
```

**Rule 4: Hub Posts (many internal references)**
```yaml
analysis:
  references:
    internal:
      - slug: post-1
        type: prerequisite
      - slug: post-2
        type: continuation
      # ... (list all)
    
    external: 6
    
    referenced_by: []  # filled during corpus scan, not this session
  
  dependency_score: high  # >3 references
  
  # MUST include read_before for prerequisite-type refs
  read_before: [post-1]
```

**Rule 5: Evidence-Based Posts (citations)**
```yaml
analysis:
  content_markers:
    citation_count: 6
    has_footnotes: true
  
  # If citations exist, note type in comments:
  # academic | blog | news | internal
```

## Decision Flow for Each Post

```
START
  ↓
Read post
  ↓
Compute word_count, count citations, grep for post_url
  ↓
Determine scope (minimal|network|narrative|conceptual|cultural|standard)
  ↓
Apply only relevant metrics from matrix above
  ↓
Skip non-applicable metrics entirely (don't write them)
  ↓
Mark universal posts with empty arrays (not skipped sections)
  ↓
END
```

## Anti-Patterns to Avoid

**DON'T:**
- Analyze sentence variance for 300-word posts
- Mark every post with empty `read_before: []`
- List domains for universal posts as `domains: [general]` (use empty array)
- Apply concept_rate to pure narratives
- Create placeholder values for skipped metrics

**DO:**
- Skip entire metric if not applicable
- Use empty arrays for "none" (domains, cultural_terms)
- Use "none" for barriers when appropriate
- Use 0 for counts when truly zero
- Comment why metric skipped if ambiguous

## Validation Rules

After analysis, check:

1. **Short posts (<400w) should NOT have:**
   - Detailed sentence_metrics
   - Deep terminology analysis
   - Referential_density section

2. **Universal posts MUST have:**
   - Empty arrays for domains, cultural_terms
   - Barriers marked "none" (not empty)

3. **Framework posts MUST have:**
   - concepts_introduced (count)
   - structure_type: framework

4. **Narrative posts should NOT have:**
   - concepts_introduced
   - concept_rate

5. **All posts MUST have:**
   - word_count
   - opening_structure
   - structure_type
   - accessibility.barriers (can be "none")
   - read_next

## Session Workflow Integration

**Pre-analysis:** Run scope detection
**During analysis:** Apply only relevant metrics
**Post-analysis:** Validate against rules above
**Commit:** Only if validation passes

