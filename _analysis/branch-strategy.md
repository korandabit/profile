# Branch & Checkout Strategy

Ensures no conflicting work across sessions.

## Branch Naming Convention

```
claude/analysis-session-{N}
```

Examples:
- `claude/analysis-session-3`
- `claude/analysis-session-4`

## Checkout Protocol (Step 0 in /analyze)

Before analyzing, check:

### 1. Check for existing session branches

```bash
git fetch origin
git branch -r | grep "claude/analysis-session"
```

### 2. Determine session branch status

For the next session (e.g., session 3):

**Check remote:**
- `origin/claude/analysis-session-3` exists?
  - YES → checkout and pull that branch
  - NO → create new branch from current

**Check progress.json on that branch:**
- Session status = "completed"?
  - YES → This session is done, move to next
  - NO → Continue work on this session

**Check for in-progress markers:**
- Look for `.analysis-lock-session-3` file
- If exists and timestamp < 2 hours ago → session in progress elsewhere, HALT
- If exists and timestamp > 2 hours → stale lock, safe to proceed

### 3. Create or checkout branch

**If branch doesn't exist:**
```bash
git checkout -b claude/analysis-session-3
```

**If branch exists:**
```bash
git checkout claude/analysis-session-3
git pull origin claude/analysis-session-3
```

### 4. Create lock file (optional safety)

```bash
echo "$(date -Iseconds)" > .analysis-lock-session-3
git add .analysis-lock-session-3
```

This prevents two Claude sessions from working on same batch concurrently.

### 5. After completion

```bash
rm .analysis-lock-session-3  # if used
git add -A
git commit -m "..."
git push -u origin claude/analysis-session-3
```

## Multi-Session Workflow

**Option A: One branch per session (RECOMMENDED)**
```
Session 3 → claude/analysis-session-3 → PR #1 → merge
Session 4 → claude/analysis-session-4 → PR #2 → merge
Session 5 → claude/analysis-session-5 → PR #3 → merge
```

Benefits:
- Clean separation
- Easy to review incrementally
- Can run multiple sessions in parallel (different people)
- Clear progress tracking

**Option B: Single long-running branch**
```
All sessions → claude/systematic-analysis → one big PR → merge at end
```

Benefits:
- Simpler
- Fewer PRs to manage

Drawbacks:
- Can't review incrementally
- Risk of conflicts if restarting
- Harder to track progress

## Conflict Resolution

**If you start a session and realize it's in progress elsewhere:**

1. Check the lock file timestamp
2. If recent (<2 hours), STOP and notify
3. If stale (>2 hours), verify no one's working on it
4. If truly abandoned, delete lock and proceed

**If branches diverge:**

1. Pull latest from main
2. Rebase your session branch
3. Resolve conflicts (usually just in post_analysis.json)
4. Force push if needed (safe on feature branch)

## Recommended: Lock File System

Add to `/analyze` workflow:

**Before starting:**
```bash
# Check for lock
if [ -f .analysis-lock-session-3 ]; then
  timestamp=$(cat .analysis-lock-session-3)
  age=$(($(date +%s) - $(date -d "$timestamp" +%s)))
  if [ $age -lt 7200 ]; then  # 2 hours
    echo "Session 3 in progress elsewhere (locked $age seconds ago)"
    exit 1
  fi
fi

# Create lock
echo "$(date -Iseconds)" > .analysis-lock-session-3
git add .analysis-lock-session-3
git commit -m "lock: start session 3"
git push
```

**After completion:**
```bash
rm .analysis-lock-session-3
git add .analysis-lock-session-3
git commit --amend --no-edit  # remove from final commit
git push -f
```

## Status Check Command

Add this to check what's safe to work on:

```bash
# Show all analysis branches and their status
git fetch origin
git branch -r | grep analysis-session | while read branch; do
  session=$(echo $branch | grep -o 'session-[0-9]*')
  echo "Checking $session..."

  # Check if locked
  git show $branch:.analysis-lock-$session 2>/dev/null && echo "  🔒 LOCKED" || echo "  ✓ Available"

  # Check progress.json
  status=$(git show $branch:_analysis/progress.json | jq -r ".sessions.\"$session\".status" 2>/dev/null)
  echo "  Status: $status"
done
```

## Simple Rule

**Before `/analyze`:**
1. Check current branch
2. If not on `claude/analysis-session-{next}`, create/checkout that branch
3. Check for lock file
4. Proceed if safe

This ensures:
- ✓ No duplicate work
- ✓ Clean branch history
- ✓ Easy to review
- ✓ Safe for parallel work (if multiple people)
