# Provenance Map — Record of Method and Findings

## What exists

- **`tools/provenance_match.py`** — matching script (runs in ~seconds)
- **`_analysis/provenance-sketch.txt`** — first-pass output (raw, noisy, ~930 lines)

## What the script does

Scans four source directories against `_posts/`:

| Dir | Role |
|---|---|
| `D:/Dropbox/3-prod/essays/` | Dated essay pipeline, subdirs by year/theme |
| `D:/Dropbox/3-prod/_DRAFTS or COPIES/` | Active essay drafts (misnamed; not copies of published posts) |
| `D:/Dropbox/2-theory/_chatbot/` | AI/chatbot-specific notes and essays |
| `D:/Dropbox/2-theory/` | Large theory scratch folder (~423 files) |

Matching uses three layers:
1. **Known matches** — hardcoded from manual inspection (high confidence)
2. **Date match** — filename date proximity bonus (caution: filesystem dates unreliable, see below)
3. **Token overlap** — Jaccard on normalized title tokens, threshold 0.18

## Known errors and caveats

**TR does not mean "Transfer Ready."** TR = THOUGHTREPAIR — a prior project/platform name. Files tagged TR in `2-theory/` were associated with that project. Their presence near a post slug is suggestive of source material but the interpretation of TR itself was wrong in earlier analysis.

**War series dates in source files are wrong.** Files in `2009-deployment mkcom/drafts/` have dates that reflect accidental filesystem creation during a file move, not actual draft dates. The chronological draft narrative (v1→v2→v3→v4) may also not hold. Treat date metadata on these files as unreliable; content and filename slugs are the actual signal.

**Score 1.5 = self-match.** The script scans source dirs which include the repo's own `_posts/` copies (via Dropbox sync presumably). These show as fuzzy score 1.5. They are not informative — filter them mentally or add exclusion to script.

**Deduplication not implemented.** Same source file appears multiple times when it matches multiple directories (e.g. a file in both `2-theory/` and `_chatbot/` subdirs). The sketch output reflects this noise.

## What the output tells us (with appropriate hedging)

**72/74 posts have at least one plausible source file** — but many "matches" are weak token overlaps, not confirmed provenance. Treat the "CONFIRMED" section as: *known matches + date-coincident files*. Treat "WEAK/FUZZY" as: *possible, needs a content read to confirm*.

**Genuinely unmatched posts (no surviving draft found):**
- `bet-your-life.md`
- `noauthor.md` (6-word post, expected)

**Floor material — highest-value unmatched source files:**

Unpublished, recent, substantive:
- `marine-book-extracts/` (7 files, Dec 2025) — Laura narratives, RIVER CITY, war/IED — new writing, not yet in any post
- `_chatbot/`: `4o duolingo vs gmaps language-learning-essay.md`, `8 ai interpretability semantic novelty 2025-03-31.txt`, `5o hypercorpus and committee 2025-03-16.txt`, `PSA on polite AI.txt`

Older drafted, never shipped:
- `8essay-techno threat of our future part one/two (2022-04-20)` — two-part AI-as-nukes essay
- `8essay against appropriating (2022-08-01)`
- `8essay gpt-truman veneer in writing and human self-report`
- `8essay human as internet`
- `2013-07-07 inaction is not a reason to scream.txt`
- `2014-07-12 belief is a spaceship.txt`
- Sound-pounder music essays (2013-2014)

Likely a roadmap file:
- `8essay TR-next themes 2024-07-24.txt` — unmatched, dated one day before a posting burst; may contain a list of planned posts (content unread)

## How to use this going forward

**To add a confirmed match:** add an entry to `KNOWN_MATCHES` dict in the script. Key = fragment of source filename, value = fragment of post slug. Re-run to regenerate sketch.

**To find sources for a specific post:** grep `provenance-sketch.txt` for the post slug — all candidate source files are listed under it with scores.

**To find cutting-room-floor material for a theme:** grep sketch for `[draft]` or `[ai-chatbots]` or `[unpublished-new]` in the FLOOR section.

**To improve signal:** read a candidate source file and check content overlap with the published post. If confirmed, add to KNOWN_MATCHES. Over time this tightens the map.

**Not yet done:**
- Reading any source files to verify matches by content
- Deduplicating multi-directory hits
- Mapping version sequences (which draft preceded which)
- `8essay TR-next themes 2024-07-24.txt` content unread
