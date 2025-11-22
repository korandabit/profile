---
description: Run automated blog post analysis for the next batch
---

# Automated Blog Post Analysis Workflow

You are executing an automated blog post analysis session. Follow this procedure exactly:

## Step 0: Branch Checkout & Safety Check

**CRITICAL: Do this before any analysis work**

1. **Read progress.json** to determine next session number (or use session number from command)

2. **Check current branch:**
   ```bash
   git branch --show-current
   ```

3. **Determine target branch:** `claude/analysis-session-{N}`

4. **Check if target branch exists remotely:**
   ```bash
   git fetch origin
   git branch -r | grep "claude/analysis-session-{N}"
   ```

5. **Branch logic:**
   - **If branch exists remotely:**
     ```bash
     git checkout claude/analysis-session-{N}
     git pull origin claude/analysis-session-{N}
     ```
     Then check progress.json on this branch - if session already complete, move to next

   - **If branch doesn't exist:**
     ```bash
     git checkout -b claude/analysis-session-{N}
     ```

6. **Verify we're on correct branch** before proceeding

If any branch checkout fails, HALT and report error to user.

## Step 1: Read Configuration Files

Read these files to understand the current state:
- `_analysis/progress.json` - current progress and next session number
- `_analysis/batches.json` - batch definitions
- `_analysis/schema.yaml` - analysis schema
- `_analysis/scoping.md` - scoping criteria

## Step 2: Determine Next Batch

From `progress.json`, identify `next_session` number.
From `batches.json`, get the post list for that session.

If a specific session number was provided with the command (e.g., `/analyze 5`), use that instead.

## Step 3: Validate Posts Exist

For each post slug in the batch:
- Search for the post file in `_posts/` using Glob
- If any post is missing, report and halt

## Step 4: Analyze All Posts

For each post in the batch:

1. **Read the post file**
2. **Run scope detection:**
   - Count words (exclude YAML front matter)
   - Check for citations (footnotes)
   - Check for internal references (post_url)
   - Identify opening structure
3. **Determine scope type** (minimal/standard/network/narrative/conceptual)
4. **Apply metrics** according to `scoping.md` rules:
   - ALWAYS: word_count, opening_structure, structure_type, accessibility, read_next
   - CONDITIONAL: sentence_metrics, terminology, concepts, citations, dependencies
   - SKIP: non-applicable metrics for minimal scope posts
5. **Generate analysis object** following `schema.yaml` structure

## Step 5: Update post_analysis.json

Read current `_data/post_analysis.json`.
Add all new post analyses.
Update `_meta` section:
- Increment `total_posts_analyzed`
- Update `sessions_completed`
- Update `last_updated` to today's date

Write the updated JSON file.

## Step 6: Update Progress Tracking

Update `_analysis/progress.json`:
- Mark current session as "completed"
- Add to `completed_sessions` array
- Set `next_session` to current + 1
- Update `total_posts_analyzed`
- Add session entry with completion details

## Step 7: Append to Session Log

Append to `_analysis/session-log.md`:
```markdown
---

## Session N: [Batch Name]
**Date:** [today]
**Branch:** [current branch]
**Commit:** [will be added]
**Status:** Completed
**Posts analyzed:** [count]

**Posts:**
[list with word counts and types]

**Key findings:**
[2-3 bullet points]

**Validation:** [passed/issues found]

---
```

## Step 8: Generate Summary Report

Output to user:

### Session [N] Complete: [Batch Name]

**Posts analyzed:** [count]

```
Post                    | Words | Type      | Scope    | Domains | Barriers
------------------------|-------|-----------|----------|---------|----------
[table rows]
```

**Key patterns:**
- [finding 1]
- [finding 2]
- [finding 3]

**Edge cases:**
- [any edge cases encountered]

**Validation:**
- [ ] Short posts (<400w) have minimal scope
- [ ] Framework posts include concept metrics
- [ ] All required fields present
- [ ] No placeholder values

**Files updated:**
- ✓ _data/post_analysis.json
- ✓ _analysis/progress.json
- ✓ _analysis/session-log.md

## Step 9: Commit and Push

Create commit with message:
```
feat(analysis): session N - [batch name]

Analyzed [count] posts: [theme]
- [post 1 slug] ([words]w, [type])
- [post 2 slug] ([words]w, [type])
[...]

Key findings:
- [finding 1]
- [finding 2]

Total posts analyzed: [total] / 76
```

Push to current branch with:
```bash
git push -u origin [current-branch-name]
```

## Step 10: Offer Next Steps

Ask user:
1. Continue to next session?
2. Review this session's output?
3. Create pull request?
4. Stop here?

---

## Important Notes

- **Do NOT update individual post YAML** - that comes in final session
- **Apply scoping rules strictly** - see scoping.md
- **No placeholder values** - skip fields rather than fake data
- **Validate continuously** - check rules after each post
- **Empty arrays vs skip** - use `[]` for "none", omit field if not applicable
- **Commit only when complete** - all posts must be analyzed successfully

## Error Handling

If any post analysis fails:
1. Report the error
2. Do NOT update any files
3. Do NOT commit
4. Ask user how to proceed

## Token Consciousness

- Read posts in parallel when possible
- Use efficient search patterns
- Don't re-read files unnecessarily
- Summary report should be concise
