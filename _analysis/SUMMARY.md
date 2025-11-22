# Systematic Post Analysis: Sample Complete

## What Was Done

Analyzed 4 representative posts across 2013-2025:
1. bot-therapy (framework, citations, actionable)
2. not-the-point (compressed, universal)
3. deafhood-unheard (cultural advocacy)
4. veteran-war-story (narrative, bridge-building)

Developed repeatable analysis framework identifying:
- Readability dimensions
- Knowledge prerequisites
- Inter-post dependencies
- Audience granularity

## Key Findings

### Pattern 1: Compression vs. Universality
- Shortest post (not-the-point, 355w) = highest accessibility (9/10)
- Cultural bridge posts (veteran, deafhood) = lower accessibility, higher word counts
- No correlation between length and impact

### Pattern 2: Network Effects
- Some posts act as hubs (veteran-story contextualizes 2013 serialization)
- Stand-alone completeness ranges 6-10/10
- Posts with internal references trade independence for network value

### Pattern 3: Audience Variance
- deafhood-unheard: 30-95% comprehension depending on reader background
- not-the-point: 90-100% comprehension (universal)
- Cultural specificity creates high variance

### Pattern 4: Bridge-Building Posts
- Require more words to translate between worldviews
- Lower stand-alone scores
- Higher narrative pull
- Unique value in portfolio

## Proposed Schema

See: proposed-schema.yaml

Core dimensions:
- Structural: word_count, concepts_introduced
- Readability: hook_strength, accessibility, narrative_pull (1-10 scales)
- Prerequisites: domain_knowledge, cultural_context, perspective_shift_required
- Audience: comprehension estimates by reader type
- Network: references, stand_alone_score, read_next suggestions

## Storage Recommendation

Hybrid approach:
- Minimal YAML in each post (for Jekyll access)
- Full analysis in _data/post_analysis.json (for regeneration)

Rationale:
- Jekyll can filter/sort by key metrics
- Full analysis separate = easy to regenerate without touching 76 files
- Version controlled together

## Multi-Session Workflow

**This session:** Developed framework with 4 posts
**Next sessions:** Batch analyze remaining 72 posts (8-10 per session)
**Final session:** Generate derived insights (reading paths, concept glossary, etc.)

Estimated: 8-10 sessions for full corpus

## Opportunities You Might Not See

### Immediate Value (no additional work)
1. Related posts widget (using read_next field)
2. Filter by accessibility on landing page
3. "New reader" vs "Deep dive" sections

### Medium Effort
4. Reading path recommendations (prerequisite chains)
5. Concept glossary (terms across posts)
6. Citation network (academic-backed posts)

### High Effort (but high value)
7. Network visualization (graph of references)
8. Content gap analysis (what's missing)
9. Audience-specific collections

## Next Steps (Your Decision)

1. Review proposed schema - too much? too little? wrong dimensions?
2. Choose storage approach (YAML / separate / hybrid)
3. Decide session pacing (how many posts per session)
4. Identify use cases to prioritize

Or: Pause here, use insights from sample for immediate blog improvements

## Files Generated This Session

/tmp/post-analysis/analysis-framework.md  - Full analysis of 4 posts
/tmp/post-analysis/proposed-schema.yaml   - Proposed metadata structure
/tmp/post-analysis/workflow-proposal.md   - Multi-session plan + opportunities
/tmp/post-analysis/example-analyzed-post.md - Concrete example
/tmp/post-analysis/SUMMARY.md             - This file

