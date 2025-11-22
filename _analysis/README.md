# Blog Post Analysis Automation

Complete automation system for systematic blog post analysis.

## Quick Start

In any new Claude Code session, simply run:

```
/analyze
```

That's it. Claude will automatically:
1. ✓ Detect which session to work on next
2. ✓ Analyze all posts in that batch
3. ✓ Update all tracking files
4. ✓ Commit and push changes
5. ✓ Ask if you want to continue

## How It Works

### Files

**Configuration:**
- `batches.json` - Defines all 10 analysis sessions and their post lists
- `schema.yaml` - Analysis schema (objective metrics)
- `scoping.md` - Rules for applying metrics selectively

**Tracking:**
- `progress.json` - Current progress, next session, completion status
- `session-log.md` - Append-only log of all sessions

**Output:**
- `_data/post_analysis.json` - Full analysis results for all posts

**Command:**
- `.claude/commands/analyze.md` - Slash command that triggers automation

### Workflow

```
User types: /analyze
      ↓
Read progress.json → next_session = 3
      ↓
Read batches.json → get post list for session 3
      ↓
Analyze each post using schema.yaml + scoping.md rules
      ↓
Update _data/post_analysis.json with new analyses
      ↓
Update progress.json (mark session 3 complete, next = 4)
      ↓
Append to session-log.md
      ↓
Commit & push to current branch
      ↓
Ask user: Continue to session 4?
```

## Commands

### Analyze next batch (automatic)
```
/analyze
```

### Analyze specific session
```
/analyze 5
```

### Check current progress
Just read `progress.json`:
```
cat _analysis/progress.json
```

## Session Overview

| Session | Name | Posts | Status |
|---------|------|-------|--------|
| 1 | Framework Development | 4 | ✓ Completed |
| 2 | AI Theme - Test | 3 | ✓ Completed |
| 3 | AI Theme - Full | 4 | Pending |
| 4 | Communication | 3 | Pending |
| 5 | Language Science | 3 | Pending |
| 6 | Cognitive Growth | 3 | Pending |
| 7 | Deaf Culture | 2 | Pending |
| 8 | Military - Retrospective | 1 | Pending |
| 9 | Military - Serialization 1 | 10 | Pending |
| 10 | Military - Serialization 2 | 6 | Pending |

**Total:** 76 posts across 10 sessions

## Branch Strategy

**Automated per-session branches (IMPLEMENTED):**

Each session gets its own branch:
```
Session 3 → claude/analysis-session-3 → PR → merge
Session 4 → claude/analysis-session-4 → PR → merge
Session 5 → claude/analysis-session-5 → PR → merge
```

The `/analyze` command automatically:
1. ✓ Determines next session number
2. ✓ Checks if branch exists remotely
3. ✓ Creates or checks out the appropriate branch
4. ✓ Verifies no duplicate work in progress
5. ✓ Commits and pushes to that branch

**Safety:** If branch exists, it pulls latest. If session already complete on that branch, moves to next.

See `branch-strategy.md` for detailed protocol.

## Quality Controls

Each session validates:
- [x] Short posts (<400w) get minimal scope
- [x] Framework posts include concept metrics
- [x] No placeholder/fake values
- [x] All required fields present
- [x] JSON is valid

## Troubleshooting

**"Post file not found"**
- Check post slug in `batches.json` matches filename
- Post might be in different format (check `_posts/` directory)

**"Session already completed"**
- Check `progress.json` - session might be marked complete
- To re-run: manually edit `progress.json` to set status to "pending"

**"Validation failed"**
- Claude will report which validation rule failed
- Fix the issue in analysis
- Don't commit until validation passes

## Adding New Sessions

To add more posts to analyze:

1. Edit `batches.json`:
   ```json
   {
     "session": 11,
     "name": "New Theme",
     "status": "pending",
     "posts": ["slug1", "slug2"],
     "theme": "theme-name"
   }
   ```

2. The automation will automatically pick it up when session 10 completes

## Manual Override

If you need to manually analyze posts without the automation:

1. Read the post
2. Follow `schema.yaml` structure
3. Apply `scoping.md` rules
4. Update `_data/post_analysis.json` manually
5. Update `progress.json` manually
6. Append to `session-log.md` manually
7. Commit and push

But really, just use `/analyze` - it's easier.

## Estimated Completion

- **7 posts done** (sessions 1-2)
- **69 posts remaining** (sessions 3-10)
- **~8-10 Claude sessions** to complete all posts
- **~15-20 minutes per session** (including review)
- **Total time: 2-3 hours** of active work spread across sessions

## What Happens After All Sessions?

Session 11 (not yet defined):
- Corpus-wide analysis
- Dependency graphs
- Reading path recommendations
- Concept glossary

Session 12 (final):
- Add minimal YAML to each post's front matter
- Validate Jekyll can read it
- Test filtering/sorting on blog
