# Systematic Post Analysis Workflow

## Phase 1: Sample Complete ✓
Analyzed 4 representative posts to develop schema

## Phase 2: Schema Refinement (Next)
1. Get user feedback on proposed dimensions
2. Decide: YAML front matter vs. separate analysis file
3. Decide: Manual vs. AI-assisted scoring

## Phase 3: Full Corpus Analysis (Multi-session)
Systematic iteration through 76 posts:
- Batch size: 8-10 posts per session (token conscious)
- Order: By theme or chronological
- Output: Either update YAML or generate analysis.json

## Phase 4: Derived Insights
Once all posts analyzed, generate:

### A. Reading Path Maps
"If you read X, you'll get more from Y"
Example: veteran-story → 2013 serialization

### B. Entry Point Recommendations
By reader background:
- New to AI: [right-click-for-ai] → [stop-avoiding] → [bot-therapy]
- Academic philosophy: [empirical-pragmatism] → [words-never-heard]
- Quickest value: [not-the-point] → [questions-books]

### C. Concept Glossary
Terms appearing across multiple posts:
- "Cognitive mirror" (bot-therapy, stop-avoiding)
- "Point vs Tangent" (not-the-point, reader-and-writer)

### D. Citation Network
Posts with academic backing:
- bot-therapy (6 sources)
- empirical-pragmatism (philosophical framework)

### E. Dependency Graphs
Prerequisite chains:
- 2013 serialization ← veteran-story (contextualizes)

## Storage Options

### Option 1: YAML Front Matter (Recommended)
**Pros:**
- Single source of truth
- Human readable
- Jekyll can use for filtering/sorting
- Version controlled with content

**Cons:**
- Clutters post files
- 76 files to update

### Option 2: Separate Analysis File
**Pros:**
- Clean separation
- Easy to regenerate
- One file to manage

**Cons:**
- Can drift from content
- Not accessible to Jekyll templates

### Option 3: Hybrid
**Pros:**
- Key metrics in YAML (for Jekyll)
- Full analysis in separate file

**Example:**
```yaml
# In post YAML (minimal)
analysis:
  accessibility: 7
  content_type: framework
  read_next: [post-slug-1, post-slug-2]
```

```json
// In _data/post_analysis.json (full)
{
  "bot-therapy": {
    "detailed_analysis": "...",
    "hook_strength": 9,
    ...
  }
}
```

## Automation Potential

### What Can Be Automated
- Word count (already have)
- Citation count (grep for footnotes)
- Internal reference count (grep for post_url)
- Reading time estimates

### What Requires Human/AI Judgment
- Hook strength
- Accessibility
- Narrative pull
- Audience comprehension estimates
- Reading recommendations

## Use Cases You Might Not See Yet

### 1. Dynamic Landing Page Sections
"Posts for readers new to [topic]"
"Deep dives requiring background"

### 2. Related Posts Widget
At end of each post:
"If this resonated, try: [X, Y, Z]"
"For more on [concept]: [A, B]"

### 3. Search/Filter by Difficulty
"Show me accessible posts on AI"
"Show me posts requiring military context"

### 4. Content Gap Analysis
"You have 0 accessible posts on empirical pragmatism"
"Communication theme lacks narrative posts"

### 5. Network Visualization
Graph showing which posts reference which
Identify hub posts vs. leaf posts

### 6. Audience-Specific Collections
"Reading path for psychologists"
"Reading path for veterans"
(Based on prerequisite knowledge, not essentialist categories)

