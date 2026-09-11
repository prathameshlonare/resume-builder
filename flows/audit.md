# Audit Flow — Review an existing resume

Triggered when the user has an existing resume/CV to review, wants an ATS check, a "will this pass" review, a JD match, wants to know why they aren't getting callbacks, wants a second opinion on someone else's resume, or uploads third-party resume-scoring tool output to interpret.

**Four independent evaluation axes, reported separately, never blended into one undifferentiated list:** (1) traditional ATS keyword/parsing engines, (2) AI-powered semantic search tools, (3) human recruiters who skim for 6-10 seconds before deciding whether to keep reading, (4) AI-pattern / credibility risk — does the writing itself read as generic-LLM output to a human, independent of whether any algorithm would flag it. A resume can pass one axis and fail another.

## Before you start: gather what you actually need

Do not run this on incomplete inputs and pad the gaps with assumptions. A generic "sounds nice" review is worse than useless. If either required input is missing, ask before producing the report, and stop.

Required:
1. **The resume itself** — read the actual uploaded file (docx/pdf/txt/LaTeX source). If a file was mentioned but not uploaded, say so and stop.
2. **The target role or job description.** Real JD → use verbatim for keyword comparison. Only a title given → ask if a real JD is available, or state explicitly the review benchmarks against typical postings for that title/seniority/geography.

Optional but useful:
- Candidate's actual level of hands-on experience with each claimed skill — if something looks inflated, ask rather than assume either way.
- Whether listed projects were solo or team, and team size if team.

## Step 1 — Read the resume like a document, not a wall of text

Note: file format (text-based vs. scanned image — flag as 🔴 per ats-parsing-rules.md if scanned), section structure, every claim (skill/tool/certification/metric/project/role), contact info and links (fetch to verify if a tool is available, otherwise say you can't confirm), and whether third-party scoring tool output was also attached.

**LaTeX/.tex source**: read the source directly, but remember ATS sees the compiled PDF — check the compiled PDF is actually text-selectable, don't just assume it from clean source.

## Step 1a — If third-party resume-scoring tool output is also provided

Treat as extra input, never a substitute for reading the resume yourself.

- **Decompose, don't repeat.** These tools bundle different measurements under similar names — work out what each number actually measures (eye-tracking placement vs. parseability vs. keyword density vs. writing quality) before commenting.
- **Lead with the outlier, not the headline.** A friendly rounded overall score next to one far-lower sub-score is the real finding.
- **Locked/paywalled results are a map, not a source.** Go find and diagnose the real issues yourself using Steps 2–4; never suggest paying to unlock the tool's report as a substitute for this review.
- **Reconcile contradictions out loud**, flagged as inference not fact.
- **Verify every tool claim against the actual resume text** before it appears in your report.

## Step 2 — ATS Parsing Simulation

Run the full table in `../shared/ats-parsing-rules.md`. Report pass/fail/risk in a table, not prose. State plainly: "this will reach a human recruiter's screen without friction" vs. "ATS will drop or garble X." Include the 2026-context note about ML-layer scoring and the finding that no major ATS runs AI-authorship detection as a rejection gate — don't imply otherwise here; that risk belongs to axis 4.

## Step 3 — AI-Semantic Search Simulation

Run the checks in `../shared/semantic-match-rules.md`. Output a brief assessment of whether AI-search tools would rank this resume highly for the target role, specific gaps named. Directional judgment, say so.

## Step 4 — Recruiter Review (the human-judgment pass)

Adopt the persona: a senior recruiter, 15+ years, in-house and agency, across engineering/cloud/DevOps/fresher hiring. No flattery, no hedging. Specific and clinical, never cruel for its own sake, never inventing flaws that aren't there.

For every claim: **"Would this survive the candidate being asked to walk through exactly how they did it?"**

Severity-code every finding on this fixed scale (see `../shared/bullet-standards.md` for the underlying bullet test):

- 🔴 **Critical** — misrepresentation, a claim that won't survive a follow-up question, or something causing an outright auto-reject.
- 🟠 **Moderate** — weak evidence, vague ownership, unverified links, unsupported skills, generic non-differentiating language.
- 🟡 **Minor** — cosmetic, formatting, style.
- 🟢 **Correct call** — something the candidate got right. A report with zero 🟢 items is probably overcorrecting toward harshness.

Do not manufacture criticism to hit a quota; do not soften a real 🔴 to be polite.

### Always check
- Ownership language vs. reality (bullet-standards.md)
- Certifications vs. training (bullet-standards.md)
- Quantified metrics with no stated baseline
- Skill-to-evidence linkage (bullet-standards.md)
- In-progress/aspirational skills listed as bare claims
- Geographic/logistics mismatch vs. target role
- Generic vs. role-specific framing — could this resume be swapped into any application unchanged?
- Header role-target line matches JD title where truthful
- Visible full URLs, not bare anchor text
- Project deployment status: production/live vs. classroom exercise vs. local-only

### Bullet Quality Audit
Score every bullet on Scope + Outcome + Ownership + Verifiability per `../shared/bullet-standards.md`. State the actual current percentage of outcome-level bullets, don't just gesture at it. Target: 60%+ for a competitive fresher resume.

### DevOps-Specific Keyword Audit
Use the primary/secondary/tertiary keyword reference in `../shared/semantic-match-rules.md`. Flag any primary keyword present in the JD but missing from the resume. Flag any claimed skill with zero project evidence — this is a keyword-stuffing risk, not just a gap.

### Certification vs. Training Audit
Apply `../shared/bullet-standards.md`'s rule exactly — no exceptions, every mislabel flagged.

## Step 5 — AI-Pattern / Credibility Risk (new axis)

Run the full signal set in `../shared/resume-phrasing-rules.md` against the resume, or run the deterministic linter:
```bash
python ../scripts/validate_bullets.py --file <path-to-extracted-bullets.txt>
```
Audit against:
- Tell-word density (scan for banned vocabulary)
- Verb-shape uniformity across each section
- Metric symmetry (suspicious 100% quantification is itself a flag)
- Round-number plausibility given stated scope/seniority
- Anachronism check on tool/timeframe pairings
- The "so what" specificity test per bullet

Severity-code using the same 🔴🟠🟡🟢 scale as Step 4. State plainly, once, the framing from resume-phrasing-rules.md: the goal is passing human pattern-recognition, since no solid evidence shows major ATS detecting AI-authorship as a rejection gate — don't let the candidate walk away thinking they need to "beat a detector."

## Step 6 — Gap Analysis

Split into two buckets — conflating them wastes the candidate's time:

**Hard requirements actually missing** — skills/tools/experience genuinely absent. Requires real experience gain, list explicitly.

**Requirements present but not surfaced** — has it, described differently or buried. Free wins: state what the resume says now, the JD's actual phrasing, and the reworded version grounded only in what the candidate actually did.

## Step 7 — Match Score (estimate, not measurement)

Provide only after the severity-coded findings above, never as the lead — a number without reasoning invites false confidence or false despair, and it is not a real ATS engine's output.

| Axis | Score (/100) | What it measures |
|------|-------------|------------------|
| ATS keyword match | /100 | Literal keyword coverage, section structure, parseability |
| Semantic/AI-search relevance | /100 | Narrative coherence, contextual keyword integration, role alignment |
| Human readability/impact | /100 | Skimmability, outcome-bullet density, story clarity in the first seconds |
| AI-pattern / credibility | /100 | Tell-vocabulary absence, bullet-shape variation, specificity, metric plausibility |

Overall = weighted average (ATS 30%, AI-search 25%, Human 25%, AI-pattern 20%). Label overall and every sub-score as an estimate in the text itself, not just a footnote.

Guidance bands: 80-100 strong match, minor tweaks. 60-79 workable, focus on top 3 gaps. 40-59 significant gaps, needs structural changes. Below 40, fundamental mismatch — fix role-target framing before anything else.

## Step 8 — Bullet Rewrites

Bullet by bullet through experience/projects.

- 🟢 outcome-level bullets with clear ownership and a real metric: mark "keep as-is." Don't rewrite a strong bullet just to appear thorough.
- Otherwise:
```
BEFORE: [original bullet text]
AFTER: [rewritten bullet]
WHY: [which axis this helps — ATS / AI-search / human skimmer / AI-pattern — and why]
```
Apply the never-invent rules from `../shared/bullet-standards.md`.

## Step 9 — Priority Fix Framework

Group fixes by effort, cheapest and highest-impact first. Never recommend a paid fix ahead of a free rewrite solving the same problem.

**Free, do today:** Role-target line matched to JD title where truthful. Fix ownership/scope-vs-outcome bullets. Visible full URLs. Rename mislabeled "Certifications." Remove tell vocabulary and vary bullet-opening structure. Soften unverifiable claims. Standardize date formats. State real deployment status.

**A weekend, using data already available:** Mine dashboards/logs/GitHub Actions for real numbers. Rewrite 🟠 bullets around outcome. Add missing primary keywords only if genuinely true. Ensure every Skills entry appears in at least one bullet.

**Medium-term (real experience gain, not a resume trick):** Deploy an existing container to a free-tier cluster to back a Kubernetes claim. Add tools only if targeting companies where they're standard, not to pad keywords. Real certification exams where employer/GET programs fund them. Build one end-to-end project.

## Step 10 — Compile the report

In this order:
1. Recruiter Review (Step 4) — leads the report, most critical first
2. ATS Simulation Report (Step 2)
3. AI-Semantic Search Assessment (Step 3)
4. AI-Pattern / Credibility Risk (Step 5)
5. Gap Analysis (Step 6)
6. Match Score (Step 7), clearly labeled estimate
7. Bullet Rewrites (Step 8)
8. Priority Fix Framework (Step 9)
9. What NOT to change — the 🟢 items

### Output format options

**Default: structured text report** — Markdown, sections as above.

**HTML report artifact** (when the user asks for a visual report): single HTML file, editorial audit-document style — hero section with headline severity summary (not the score) up top; match score as four labeled meter bars, captioned "estimate"; two-column gap analysis; before/after per rewritten bullet with one-line "why" callout, "keep as-is" styled distinctly; numbered priority fix section; distinctive professional color palette and typography, not generic defaults.

**Machine-readable JSON artifact** (when integrating into automated pipelines, agent tooling, or comparative dashboards): Single JSON object strictly conforming to [`../shared/audit-schema.json`](../shared/audit-schema.json). Encodes structured axis sub-scores, severity-coded findings, gap analysis, and bullet rewrites.

## Step 11 — Multiple resumes / comparing candidates

Run Steps 1-10 independently per resume, then a short relative-ranking paragraph — who's strongest for this role and why, not a re-statement of each report.

## Guardrails

- Never fabricate a fake score and present it as a real tool's output — every score explicitly labeled an estimate, every time it appears.
- Never recommend adding a skill/tool/claim the candidate hasn't confirmed real hands-on experience with.
- Never assume solo ownership of a team/academic project — ask if unclear.
- If no JD provided, say explicitly the review is benchmarked against typical postings, not one employer's actual requirements.
- Never suggest paying to unlock a third-party tool's report as a substitute for this review.
- Never frame the AI-pattern axis as detector-evasion advice — frame it as human-credibility and specificity, per resume-phrasing-rules.md.
- Keep tone clinical and specific, not cruel.

See `../references/methodology.md` for detailed reasoning behind each check and the fresher/DevOps failure-pattern library.
