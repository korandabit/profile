# Test Batch: Session 2 Starter

Use this to test the workflow in a new session.

## Instructions for User

1. Open new Claude Code session
2. Navigate to repo
3. Run: `git checkout claude/systematic-post-analysis-013B5xpqWPDTFxrga3Z8So73`
4. Copy the prompt below
5. Paste to Claude
6. Review output

---

## Prompt for Claude (Session 2 Test)

```
Continue systematic post analysis, Session 2 (TEST BATCH).

Context:
- Branch: claude/systematic-post-analysis-013B5xpqWPDTFxrga3Z8So73
- Schema: _analysis/revised-schema.yaml
- Scoping: _analysis/SCOPING-CRITERIA.md
- Instructions: _analysis/SESSION-INSTRUCTIONS.md

Analyze these 3 AI theme posts:

1. 2023-10-28-stop-avoiding-yourself-the-ai-in-you
2. 2024-08-30-ai-the-next-technological-leap
3. 2024-07-13-right-click-for-ai

For each post:
1. Run scope detection:
   - Word count
   - Has citations?
   - Has internal refs?
   - Opening structure type
2. Determine scope (minimal|network|narrative|conceptual|standard)
3. Apply only relevant metrics per scoping criteria
4. Skip non-applicable metrics entirely

Output format:

**1. Create/update `_data/post_analysis.json`** with full analysis for these 3 posts

**2. Summary table:**
```
Post                    | Words | Type      | Scope     | Domains | Barriers
------------------------|-------|-----------|-----------|---------|----------
[fill this in]
```

**3. Edge cases encountered:**
- [Any ambiguous classifications]
- [Questions about scope application]

**4. Validation:**
- [ ] Short posts (<400w) have minimal scope
- [ ] Framework posts include concept metrics
- [ ] Universal posts have empty arrays (not skipped)
- [ ] All required fields present
- [ ] No placeholder values

Do NOT update individual post YAML yet.
Show me the JSON output for review.
```

---

## Expected Output Structure

Claude should create `_data/post_analysis.json`:

```json
{
  "stop-avoiding-yourself-the-ai-in-you": {
    "word_count": 1324,
    "sentence_metrics": {
      "avg_sentence_length": 21.5,
      "max_sentence_length": 45
    },
    "opening_structure": "question",
    "structure_type": "analysis",
    "terminology": {
      "domain_term_density": 2.8,
      "domains": ["ai-chatbots"],
      "terms_defined_inline": 4
    },
    "prerequisites": {
      "domains": [
        {
          "name": "ai-chatbots",
          "level": "basic-usage",
          "critical": true
        }
      ],
      "cultural": []
    },
    "accessibility": {
      "linguistic_barrier": "low",
      "domain_barrier": "medium",
      "cultural_barrier": "none"
    },
    "read_next": [
      "bot-therapy",
      "know-thaiself"
    ]
  },
  
  "ai-the-next-technological-leap": {
    ...
  },
  
  "right-click-for-ai": {
    ...
  }
}
```

## What to Check

1. **Scoping applied correctly?**
   - Short posts use minimal scope
   - Framework posts include concepts
   - Narrative posts skip concepts

2. **No junk metrics?**
   - Sentence variance on 300w posts (BAD)
   - Empty read_before arrays everywhere (BAD)
   - Placeholder domains like "general" (BAD)

3. **Valid JSON?**
   - Paste into JSON validator
   - Check syntax

4. **Makes sense?**
   - Domains match post content
   - Barriers seem reasonable
   - read_next suggestions logical

## If Test Succeeds

Commit:
```bash
git add _data/post_analysis.json
git commit -m "feat(analysis): session 2 test batch - 3 AI posts"
```

Then proceed with full Session 2 (remaining AI posts).

## If Test Fails

Report issues, refine scoping criteria, try again.

