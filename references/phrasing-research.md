# Resume Phrasing Baselines — generic-LLM patterns vs. good resume writing

Purpose: derive resume-genre-specific structural baselines before building `resume-phrasing-rules.md`. This is NOT a port of Not-Ai's essay/prose thresholds — resume bullets are a different genre with different norms, and applying prose baselines directly would flag correct resume convention as a problem.

---

## Why Not-Ai's thresholds don't transfer directly

Not-Ai measures (nominalization density, participial-clause openers, sentence burstiness, engagement markers) against **essay/prose norms**. Resume bullets structurally violate several of those norms *by design*, in ways that are correct, not AI-like:

| Not-Ai signal | Prose norm | Resume norm | Why the resume norm differs |
|---|---|---|---|
| Nominalization density | 25–40/1,000 words = human | Resumes run naturally higher | Bullets compress verbs into outcome nouns on purpose ("led migration" → "migration lead"); this is standard resume economy, not an AI tell |
| Sentence burstiness (variation in length) | High variation = human | Deliberately **low** variation is fine | Bullets are meant to be scannable and parallel — uniform length is a *feature* for a 6-second scan, not a defect |
| Engagement markers (reader address, first-person, hedges) | Expected in essays | Actively wrong in resumes | Resumes never use "I", never hedge ("might have"), never address the reader — this is universal resume convention, not an AI signature |
| Participial-clause openers ("Leveraging the power of...") | Overused by LLMs in prose | Different manifestation in resumes | Resumes don't open sentences this way at all normally — but LLMs still produce a resume-specific version of this problem (see below) |

**Conclusion: the phrasing-rules module needs its own resume-specific signal set, not Not-Ai's numeric thresholds.** Its structural *philosophy* (measure specific, falsifiable patterns; never optimize for detector-dodging; never invent facts to increase specificity) still applies and should be kept.

---

## What the research actually converges on (high confidence — corroborated across 10+ independent 2026 sources)

Unlike the ATS-detection claims (contradictory), these patterns show strong, consistent agreement across career-advice sites, recruiter-facing blogs, and hiring-manager surveys:

### 1. A specific, recurring "tell" vocabulary
The same words appear across nearly every source as recruiter-recognized AI markers: **"spearheaded," "leveraged," "synergy/synergized," "results-driven," "dynamic professional," "proven track record," "orchestrated," "championed," "catalyzed," "cross-functional collaboration," "streamlined," "optimized," "drove strategic initiatives."** One source frames the mechanism precisely: these cluster at high frequency because <cite index="38-1">resumes drafted with AI assistance cluster around these verbs because the training data over-represents them</cite>.

### 2. Uniform bullet structure (the single most-cited signal)
This is the most consistently named pattern, described the same way by multiple independent sources: <cite index="40-1">ChatGPT tends to produce bullets in a rigid [verb] + [activity] + [result] format with almost no variation, while real resume bullets have natural variation in length and structure — a wall of perfectly parallel bullet points looks machine-generated</cite>. A second source frames it as the diagnostic recruiters actually use: <cite index="41-1">bullets that all start with the same verb shape, and opening lines that are identical across applicants from the same prompt, are what actually gets a resume caught — not the fact that AI was used</cite>.

### 3. "Suspicious symmetry" — every bullet has a clean metric
<cite index="45-1">AI resumes often create suspicious symmetry: every bullet has a metric, every project has perfect impact, and every skill appears in the job description — real careers are messier</cite>. This matters directly for your job-search context: it means the fix isn't "add a number to every bullet," it's "add real numbers where they exist and leave bullets without one alone rather than inventing symmetry."

### 4. Round, suspiciously convenient numbers
A more technical framing from a recruiter-facing source: <cite index="38-1">when every bullet has a round-number outcome, at least half of them are likely invented — the giveaway is a claim that is internally consistent but externally impossible for the stated role or company size</cite>. This connects to `resume-ats-audit`'s existing "never invent a metric" guardrail — worth carrying that same discipline into the generation flow, not just the audit flow.

### 5. The actual mechanism recruiters use — pattern recognition, not detection tools
Convergent and important for how the skill should frame its own goal: <cite index="39-1">most major ATS platforms do not run AI-detection models on resume text, but recruiters reading the output do catch AI-tell patterns like "leveraged," "results-driven," repeated phrasing across candidates, and vague metrics — the practical risk is human pattern recognition, not algorithmic detection</cite>. This directly confirms the earlier research doc's conclusion and should be stated plainly in the skill: **the goal is passing human pattern recognition, not evading a detector that mostly doesn't exist for this purpose.**

### 6. Specificity is the actual fix, not vocabulary substitution alone
Multiple sources converge on the same fix, and it matches what our own earlier conclusion said: swapping "leveraged" for a synonym without adding real detail doesn't work. <cite index="36-1">A resume built entirely from AI without your specifics will read like every other template in the applicant pool — the fix is feeding the tool real accomplishments, metrics, and career details, then using it to improve language, structure, and keyword alignment, not the reverse</cite>. One source gives a concrete test for whether a bullet is specific enough: <cite index="47-1">your bullets need to survive a "so what?" test — if the result could apply to anyone, it's not strong enough</cite>.

### 7. One large-scale-survey-style data point (treat with appropriate caution)
One source cites hiring-manager self-report figures: <cite index="47-1">a survey of 1,000 U.S. hiring managers found 80% say they can spot an AI-written resume, and 77% say many resumes now appear partially or fully AI-generated</cite>. Flag this as a single-source, self-reported perception statistic (recruiters *believing* they can spot AI is not the same as being right — this is a known bias in the same family as the unreliable-detector finding from the earlier research doc) — useful as directional color, not as a hard number to repeat as fact.

---

## Derived resume-specific signal set (for `resume-phrasing-rules.md`)

Unlike Not-Ai's numeric density thresholds, these are pattern checks appropriate to resume length/structure:

| Signal | Check | Flag when |
|---|---|---|
| Tell-word density | Count occurrences of the recurring tell vocabulary (list above) across the resume | Any tell word appears more than once, or 2+ different tell words appear across the bullet set |
| Verb-shape uniformity | Look at the first word of every bullet | 3+ consecutive or 50%+ of bullets in a section open with structurally identical verb-tense/shape ("Led... Managed... Drove... Spearheaded...") |
| Metric symmetry | Check ratio of bullets with a quantified metric to bullets without | 100% of bullets having a clean round-number metric, especially across unrelated bullets, is itself a flag — not a strength |
| Round-number plausibility | For each metric, sanity-check magnitude against stated scope (team size, company size, role seniority, project duration) | A fresher/intern bullet claiming enterprise-scale impact ("$20M budget," "team of 40") without team/project context to support it |
| Anachronism check | Cross-reference any named tool/tech against the stated project timeframe | Tool referenced before its public release, or used in a context inconsistent with its actual capabilities at that time |
| Genuine specificity | Does the bullet name a real system, tool, dataset, constraint, or decision — or could it describe any candidate in the role? | Bullet passes the "so what — could this describe literally anyone in this job title" test |

---

## What this means for the two flows

**Generate flow:** apply these as constraints *while drafting*, not as a post-hoc filter — i.e., never let a first draft use the tell vocabulary or produce uniform verb-shape bullets in the first place, rather than generating generic text and then "humanizing" it after. This also sidesteps the whole watermark/detector question entirely, since the point is genuine specificity from real candidate input, not disguising generated text.

**Audit flow (absorbing old resume-ats-audit):** add this as a fourth axis alongside the existing three (ATS parsing / semantic match / human skimmability) — call it **"AI-pattern / credibility risk"** — reported the same way as the others: severity-coded, with before/after rewrites, never blended into the other three scores.

## Research credibility note

Sources section removed to reduce external-link supply-chain surface. Patterns above synthesize a Sept 2026 multi-source review (recruiter blogs, hiring-manager surveys, detector-accuracy studies) — convergent signals only, single-source stats flagged inline. See README Ground Truth summary. No external downloads required.
