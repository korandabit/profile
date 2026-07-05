# Essay Reading Notes — Structural Frames (e1–e5)

**Status note (v1 recommendation, declinable):** This file is the durable home chosen for MKC-001
(`../../backlog-tickets/MKC-001-durable-home-essay-reading-notes.md`), relocated 2026-07-05. essay_linter
authored a v1 set of structural reading-notes on a breadth sample of Mark's published essays and parked
them in a project `inbox/` that has since been retired (ADR-0013); that inbox copy no longer exists. This
file is reconstructed from the still-live upstream source — `essay_linter/bench/parse-derivation/
derivation-notes.txt` (Mark's raw framing notes, verbatim) plus the structural findings essay_linter
derived from them in `essay_linter/bench/parse-derivation/derivation.md` and `essay_linter/PARSE_SPEC.md`
(the resolutions, marked `[resolved:]` below). The shape (a single `_analysis/` companion file vs.
per-post annotations) is Mark's call to keep, split, or move — nothing here is final.

## How to read this

Each essay below has two layers:
- **Mark's raw framing** — his own reading notes: frames, registers, stances, open questions, as first
  written (lightly reformatted, content unchanged).
- **`[resolved:]`** — essay_linter's structural answer to that framing, drawn from the comparative parse
  in `derivation.md` and the two-axis facet spec in `PARSE_SPEC.md` (MOVE: `FUNCTION`/`GROUNDING`/`STANCE`;
  CONTENT: `ENTITY`/`ROLE`/`RELATION`). Where a question has no upstream answer, it's left open and
  flagged.

---

## e1 — Reader and Writer

- **Post:** `_posts/2022-04-18-the-agreement-between-reader-and-writer.md`
- **Permalink:** `/blog/2022/04/18/the-agreement-between-reader-and-writer/`

### Mark's raw framing

> is almost a gold standard essay in form. i want the elinter to be able to measure it in the senses as
> follows: first, its argumentative components, are meant to be atomic, pragmatic, critical and universal.
> in their execution they emit a topology of relevance that any imaginative reader should be able to yield.
> the problem is it does ZERO to model, implement, claim inductively or empirically its pragmatic
> relevance. what i've just described are, i believe the intersection of two things: *registers* and
> frames?

Frames noticed (not corroborated at time of writing):
- frame 1: epistemological minima — reader vs. writer; have vs. no info, etc.
- frame 2: 3rd-person experience — "which way," etc.
- frame 3: 1st-person narrator, discursive — "i'm going away"
- frame 4 (maybe distinct from frame 1?): phenomenological — lies in word choice, extensional scopes,
  "a disagreement is" — toward an empirical grounding of phenomenological high-value.
- frame 5: meta? — is 2nd person its signal? contract, binding, like frame 4 but a more specific purpose:
  "if you (likely event)" then "it's (strong, implicating inference/generalization)."

Extra: elinter, for frames legible without top-down (LLM) inference, would attempt to parse them
directly; nlp4llm could supply an LLM-parsed "gold standard" for the rest (backlogged there, not here —
see Drift note below).

**`[resolved:]`** e1 is the essay with the *least* grounding of the five (`derivation.md` §1, §3):
grounding ≈ 0/14 — six `DEFINE` moves ground meaning only, never claim/fact. The `FUNCTION` spine
(`DEFINE → CLAIM → DIRECT`, Axis 1 of `PARSE_SPEC.md`) loops three times with no `GROUND` move at all.
`STANCE` is function-locked: 2nd person → `DIRECT`, 1st person → closing, 3rd person → `CLAIM`/`DEFINE` —
this is the empirical shape of the "registers and frames" intersection Mark names above; the 2p/3p split
*is* the frame-vs-register seam. The thesis-bearing entity, WORDS, is the one dangling node — claimed
load-bearing (`enables → AGREEMENT`) but never defined or grounded, which is the structural form of "does
ZERO to model... its pragmatic relevance." Frame 5's 2nd-person contract/binding read ("if you [likely
event] then it's [strong generalization]") corresponds to the `role-flip` at READER: `SCENE[agent:asks] →
DEFINE → CLAIM → DIRECT[patient:"go away"]` — a role-flip that is, notably, **ungrounded** (the one
ungrounded flip among all five essays).

### Open / not yet resolved
- Whether frames 1–5 as individually enumerated survive as distinct `ENTITY`/`RELATION` tracks, or
  collapse into the STANCE-locked FUNCTION spine above, is not settled by `derivation.md` — it gives the
  aggregate profile, not a frame-by-frame reconciliation. Flagged as a gap, not answered here (see
  drift note).

---

## e2 — Standards

- **Post:** `_posts/2021-09-17-standards.md`
- **Permalink:** `/blog/2021/09/17/standards/`

### Mark's raw framing

> its funny, my memory tagline for this is quite cringe, but as far as format-power goes, this essay
> performs its own extreme. in [htttw] sense, it is a plain high-roi legibility instruction embedded in
> personal lived value that attempts to maximize irl-quality word-leverage.

Frames noticed:
- frame 1: 1st-person personal material values, universal
- frame 2: 1st-person communicative values, pedagogical, maximal (pragmatic empiricism)
- frame 3: standards as they are, and their 1st-person relevances (standards normalized as regulatory
  noise)
- frame 4: distributed effects of standards in reality, proportionate to their communicative value

Potential recalibration (Mark's own second-guess): "there's something different going on... this essay
performs synthesis of frames, formats. we MIGHT get similar mileage if we stuck strictly to the register
game" — technical/opaque registers embedded in personal/familiar, with a scientific register as the
argumentative arc, the whole subsetted in a self-report/narrative/in-real-time register ("so far this is
the record"). Tangent: a future revision, in the right register, would ask for updates (originally
imagined as a regularly ratified ledger — out of scope here, see drift note).

**`[resolved:]`** e2 is the structural inverse of e1 (`derivation.md` §2–3): grounding is **high and
external** (NSF citation, Brita/Pur, PPM, $10/$100 figures) — the plain high-ROI legibility instruction
Mark names is exactly high `grounded[cite|spec]` density on Axis 1. But relational **continuity is low**:
entities are concrete and their relations point *outward* rather than to each other, producing a
**shallow star/list** graph shape with no role-flip. This is the structural signature of "the register
game" recalibration Mark reaches for on his own — synthesis-of-frames reads, in parse terms, as high
grounding + low internal continuity, the opposite tradeoff from e1 (low grounding, high internal
continuity). The self-report/in-real-time register Mark flags as the outer "record" frame is not itself
one of the six PARSE_SPEC facets — it sits above the sentence-level tag, at the document-coordinate level
(`grounding ratio × relational continuity`, `PARSE_SPEC.md` "The product").

---

## e3 — Bot Therapy

- **Post:** `_posts/2025-11-12-bot-therapy.md` (title: *"From Silence to Bot Therapy: Yes, You Can and
  Should Talk to Bots for Help"*)
- **Permalink:** `/blog/2025/11/12/bot-therapy/`

### Mark's raw framing

> this one is probably the clearest/cleanest implement of what i'm after. there are at least 2 macro
> frames that are interleaved. the other bot essays do this too.

Frames:
1. motivation via hypothesis — normative dismissing views vs. the thesis to fill the delta (from 2)
2. impact — population-estimated relevance
3. intervention — instruction to procedural spec
4. signal detection — spec for those that can't read themselves

Ambitious wants: "the magic of this essay is its falsifiable surfaces and ambition."

**`[resolved:]`** e3 is the structural high point of the sample (`derivation.md` §2–3, the essay singled
out as "cleanest," now made judgment-free): grounding is **highest of all five** — citation + scope-zones-
before-instruction + a "you verify" check — and it has the sample's only **grounded** role-flip: user goes
patient → agent, and that flip is discharged by the check, not just asserted. The graph is dense and
anchored outward. This is the parse-level form of "falsifiable surfaces": `GROUNDING` on `PARSE_SPEC.md`'s
Axis 1 is typed, not binary (`grounded[cite|example|check|spec|testimony]`), and e3 is the essay that
uses the `check` discharge type — the 2nd-person-imperative-question cue ("you verify") that is exactly
Mark's frame 4, "signal detection: spec for those that can't read themselves." Frames 1–3 (motivation →
impact → intervention) read as the `FUNCTION` spine `CLAIM → GROUND → DIRECT`; frame 4 is the grounding
check on the DIRECT that closes the loop the other essays leave open.

---

## e4 — Dealing with Deaf at the party

- **Post:** `_posts/2013-12-07-dealing-with-deaf-at-the-party.md`
- **Permalink:** `/blog/2013/12/07/dealing-with-deaf-at-the-party/`

### Mark's raw framing

> at first i didnt catch it, maybe overfitting, but the frames are subtle in the first paragraph. the
> elinter would surface their consistency internal and in parallel.

On paragraph 1:
- frame 1: (familiar scene/theme in) 2nd person, to set reader-self-identifying stakes
- frame 2: 1st person at the precise decision-stake, to alleviate burden
- frame 3: 3rd person, to claim normative reality
- "Hold up repeat it please" could be 1 or 2, implied reasonable example of 3
- late frame: "But the Deaf dont need you to..."

Additional: the word that sticks out is "perspectives" — Mark wants it at highest resolution, i.e. a
perspectives × events (scenarios, illustrations) array, each scenario a series of events, with the
possibility space explicitly mapped to each perspective (not all permutations exist). Later scenarios/
perspectives would each be scoped and mapped so the scenario facet is visible (e.g. "Tyler, Jon, etc.").
The last frame is a latent critical thesis performed — elinter doesn't need to know this role, but the
value is in capturing this level of grouping.

**`[resolved:]`** e4 is the sample's continuity ceiling (`derivation.md` §2–3): grounding is **mid-high by
example/testimony** (no citation), and it has **very high** relational continuity plus **multiple grounded
role-flips** — the most stance-variance of the five. This is the structural cash-out of Mark's
"perspectives × events" request: the 2p/1p/3p alternation he tracks by hand in paragraph 1 is `STANCE`
(Axis 1) cycling across a **persons × scene-beats matrix**, which `derivation.md` names directly as "the
native shape" for this essay — i.e. Mark's requested array is not a hoped-for feature, it is the structure
already there, unformalized. Each "perspective" is an `ENTITY` on Axis 2; each grounded role-flip is a
point where that entity moves agent↔patient with a `grounded[example|testimony]` discharge, which is what
makes "Hold up repeat it please" legible as a specific, checkable instance rather than a generic 1p/2p
gesture. The late frame ("But the Deaf dont need you to...") is the one ungrounded-to-grounded pivot that
carries the essay's critical thesis — the multi-perspective payoff Mark is already reaching for by naming
"perspectives" as the highest-resolution unit.

---

## e5 — Know thAIself

- **Post:** `_posts/2023-11-14-know-thaiself.md`
- **Permalink:** `/blog/2023/11/14/know-thaiself/`

### Mark's raw framing

Frames:
1. the headers — a specific conversational tone at the front edge of implicating the reader
2. more like a frame-chain — AI-made visual art, with trope references (Frankenstein), to capture the
   emotive/evocative thesis
3. 1st-person stakes
4. 2nd-person stakes
5. theoretical / mechanical context
6. instruction/spec — feature? frame-chain? spans practical abstractions
7. strategic? adversarial? generative? — postures or frameworks, e.g. the "triangulation" method

Extra: "the frame chaining i'm not sure what to call that. i might be conflating things here and in other
places."

**`[resolved:]`** e5 is the sample's outlier shape (`derivation.md` §2–3): grounding is **bimodal** — the
method is grounded via transcripts and a worked example, but the lyric close ungrounds — and it has a
**carrier-node**: one entity whose relation-set accretes monotonically with document position, with the
reader as sustained agent and no role-flip. This gives Mark's "frame-chain" (frame 2, and his own
uncertainty about the term at the end) a name: `derivation.md` §3.4 states plainly that "carrier" is a
measurable shape, not a vibe — an entity whose `RELATION` set grows as the document proceeds. The
chaining Mark senses across frames 3–7 (1p stakes → 2p stakes → theory → instruction → strategic posture)
is the carrier entity accreting new relation types at each step rather than a sequence of independent
frames; the "triangulation" method he flags in frame 7 is one of those accreted relations, not a separate
track. Frame 1 (headers, front-edge conversational tone) sits outside the six PARSE_SPEC facets — it is
presentational/structural (headers as a device) rather than a MOVE or CONTENT tag on a sentence.

---

## Comparative note (all five, from `derivation.md` §3)

The five essays fixed essay_linter's facet set precisely because they land at five distinct points on two
orthogonal axes — **grounding** (none → bimodal → high → highest) and **relational continuity**
(internal-only → low → high+connected → very high → carrier) — with **role-flip** (none / 1 ungrounded /
1 grounded / multiple grounded) as the discriminating cross-axis signal. e1 and e3 are the poles: same
kind of structural move (a role-flip on the central entity), opposite grounding outcome. This is the
empirical basis of `PARSE_SPEC.md`'s "document coordinate" diagnostic (grounding ratio × relational
continuity) and is why the facet set has three axis-2 facets (`ENTITY`/`ROLE`/`RELATION`) rather than two
— the agent↔patient flip on `ROLE` is what makes e1 vs. e3 vs. e4 vs. {e2, e5} separable at all.

## In scope here / drift (do not extend this file with)

Per MKC-001: this file curates and cross-links Mark's authored framing notes and essay_linter's already-
published structural findings. It does not, and should not be extended to:
- build or tune essay_linter to *measure* these frames (that's essay_linter's `PARSE_SPEC.md` build,
  tracked in its own `ROADMAP.md`);
- run LLM-gold parsing via nlp4llm (parked upstream, gated on the LLM-assist-vs-detector-independence
  fork per `PARSE_SPEC.md`'s closing line);
- build essay_linter's linter-as-revision-tool feature (Mark's "elinter the revision tool" aside on e1).

Any of the above, if it needs doing, is essay_linter's or nlp4llm's ticket, not this file's.

## Sources

- Raw verbatim notes: `essay_linter/bench/parse-derivation/derivation-notes.txt`
- Structural resolution: `essay_linter/bench/parse-derivation/derivation.md` (§1–3, the e1–e5 derivation)
- Facet spec: `essay_linter/PARSE_SPEC.md`
- Originating ticket: `../../backlog-tickets/MKC-001-durable-home-essay-reading-notes.md`
