# Resume Phrasing Rules — AI-Pattern / Credibility Risk

Derived from resume-genre-specific research, NOT ported from prose/essay humanizer tools (their numeric thresholds — nominalization density, burstiness, engagement markers — don't transfer to resumes, which are correctly dense, uniform, and reader-address-free by convention). Full derivation and sourcing in `references/phrasing-research.md`.

**Framing, stated plainly to the candidate when this comes up**: the goal is passing human recruiter pattern-recognition, not evading an AI-detector. Research found no solid evidence major ATS run AI-authorship detection as a rejection gate — the real risk is a human reader recognizing generic phrasing, not an algorithm flagging a watermark. Optimizing to "beat a detector" would target the wrong problem and can hurt real scannability. This module's job is: genuine specificity from real candidate input, not disguised generated text.

## The signal set

| Signal | Check | Flag when |
|---|---|---|
| Tell-word density | Scan for the tell vocabulary below | Any tell word appears more than once, or 2+ different tell words appear across the bullet set |
| Verb-shape uniformity | Look at the first word/tense of every bullet in a section | 3+ consecutive bullets, or 50%+ of a section, open with structurally identical verb-tense/shape |
| Metric symmetry | Ratio of bullets with a clean quantified metric to bullets without | 100% of bullets having a clean round-number metric, especially spanning unrelated bullets, is itself a flag |
| Round-number plausibility | Sanity-check metric magnitude against stated scope (team size, company size, seniority, project duration) | A fresher/intern bullet claiming enterprise-scale impact without supporting context |
| Anachronism check | Cross-reference named tool/tech against stated project timeframe | Tool referenced before its public release or used inconsistent with its actual capability then |
| Genuine specificity | Could this bullet describe literally any candidate with this job title? | Bullet fails the "so what" test — no real system, tool, dataset, constraint, or decision named |

## Tell vocabulary (avoid; flag if present)

spearheaded, leveraged, synergy / synergized, results-driven, dynamic professional, proven track record, orchestrated, championed, catalyzed, cross-functional collaboration, streamlined, optimized (as a bare claim with no mechanism), drove strategic initiatives, passionate, meticulous.

Note: some of these are legitimate words in the right context (e.g. "optimized query performance from 800ms to 120ms" is fine — the word plus a real mechanism and number is not the problem; "optimized workflows" alone with nothing after it is). Judge by whether a real mechanism/number follows, not by the word in isolation.

## How this applies per flow

**Generate flow**: these are hard constraints applied *while drafting*, not a filter run after. Never produce a first draft containing tell vocabulary or uniform verb-shape bullets — draft directly from real candidate specifics instead. This sidesteps the detection question entirely: there's nothing to disguise if the output was never generic in the first place.

**Audit flow**: report as a fourth axis, alongside ATS parsing / semantic match / human skimmability — labeled "AI-pattern / credibility risk." Severity-code using the same 🔴🟠🟡🟢 scale as the recruiter-review axis (see bullet-standards.md), never blended into the other three scores. Rewrite flagged bullets using the same BEFORE/AFTER/WHY format as Step 5 bullet rewrites.

## What NOT to do (from Not-Ai's stance, still correct here)

- Never optimize for a detector score — there's no reliable resume-authorship detector to optimize against, and trying to would trade away real scannability for nothing.
- Never add fake imperfection (inconsistent formatting, deliberate typos, uneven polish) to "seem more human" — a resume should look clean; the fix for generic-sounding content is real specificity, not manufactured roughness.
- Never invent a detail to pass the specificity test — an honestly generic bullet flagged as `[SUPPLY DETAIL: what makes this specific to you]` is correct; a fabricated specific detail is not.
