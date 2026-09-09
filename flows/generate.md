# Generate Flow — Build a resume from scratch

Triggered when the user has no existing resume to audit, or explicitly wants one built/drafted from their information.

Applies `shared/bullet-standards.md`, `shared/ats-parsing-rules.md`, `shared/semantic-match-rules.md`, and `shared/resume-phrasing-rules.md` as constraints from the first draft — never generate generic text and clean it up after. If those constraints mean a bullet can't be written yet, use a `[SUPPLY: ...]` placeholder rather than inventing content.

## Step 1 — Intake

Do not draft anything from assumptions or from a generic template. Gather, in this order, stopping to ask if something critical is missing:

**Required:**
1. **Target role or JD.** Same rule as audit: if a real JD exists, use it verbatim. If only a title/level is given, say plainly the resume is being built against typical postings for that title/seniority/geography, not one employer's specific requirements.
2. **Raw material per project/role/experience**: what was actually built or done, in the candidate's own words — plain description first, polish later. Don't let the candidate skip straight to "make it sound impressive," that's how generic bullets happen.
3. **Team context**: solo or team, and team size if team, for every project. Required before any bullet gets written for it — see ownership rule in bullet-standards.md.
4. **Real numbers, if they exist**: don't ask leadingly ("what % did you improve?") — ask what data exists and where (dashboards, commit history, load tests, before/after comparisons). If no real number exists, that bullet stays unquantified rather than getting an invented one.

**Optional but useful:**
- Tools/skills the candidate has genuine hands-on exposure to, even briefly — vs. tools only read about. Only the former go in Skills.
- Deployment status of each project: production/live vs. local-only vs. classroom exercise. Get this right; it's a credibility-critical distinction (see bullet-standards.md).
- Certifications vs. training courses completed — classify immediately per bullet-standards.md's Certification vs. Training rule; don't let a course get labeled a certification even provisionally.
- For technical / DevOps candidates with GitHub repos or codebases: apply `shared/codebase-mining.md` to extract unassailable metrics (Docker image reductions, Terraform line counts, test quantities, DynamoDB conditional write architectures) directly from repositories.

If the candidate offers polished/buzzword-y self-description instead of raw specifics ("I'm a results-driven professional who leveraged..."), gently redirect: ask what they actually did, in plain terms, before writing anything. This is the intake moment where generic phrasing gets prevented, not caught later.

## Step 2 — Draft structure

Standard sections, in this order (see ats-parsing-rules.md section-order guidance): Contact/Header → Role-target line → Skills → Experience/Projects → Education → Certifications (only if real) / Training & Courses.

- Role-target line under the name: match the JD title where truthful — this drives both ATS semantic match and the first few seconds of human attention.
- One page for a fresher/junior candidate.

## Step 3 — Draft bullets

For each project/role, using the raw intake material:

1. Apply the Scope + Outcome + Ownership + Verifiability test from bullet-standards.md.
2. Vary verb choice and sentence shape across bullets in the same section — don't let 3+ consecutive bullets share the same opening verb tense (resume-phrasing-rules.md).
3. Never reach for tell vocabulary (spearheaded, leveraged, results-driven, etc.) — write what actually happened instead.
4. Weave keywords into bullet context rather than only listing them in Skills (semantic-match-rules.md) — but only keywords genuinely backed by real project work.
5. Where a metric would help but none was supplied, write `[SUPPLY NUMBER: what to measure, where to find it]` — never invent one, even a plausible-sounding one.
6. Don't force a metric onto every bullet for symmetry — an honest unquantified bullet next to quantified ones is fine and normal; forced 100% metric coverage is itself a credibility flag.

## Step 4 — Skills section

Only include an entry if it appears in at least one drafted project bullet, or the candidate has explicitly confirmed real (even small) hands-on exposure. Cross-check against semantic-match-rules.md's DevOps keyword reference if relevant to target role — but never add a keyword the candidate can't back up, even if it would improve match score.

## Step 5 — Self-check before presenting

Run the deterministic linter `scripts/validate_bullets.py` on the drafted bullets:
```bash
python scripts/validate_bullets.py --bullet "bullet text here"
```
Or pipe/pass drafted bullets to verify all 8 quality gates (zero tell words, no participial openers, no trailing fluff, active voice, word count 15-38, metric present).

Also check:
- Verb-shape uniformity across each section (no 3+ consecutive bullets with identical verb stems)
- Metric symmetry — is every single bullet suspiciously quantified?
- Round-number plausibility given stated scope
- Anachronism check on any named tool/timeframe pairing
- Mechanical checks from `ats-parsing-rules.md` (standard section headers, date format consistency, visible full URLs)

## Step 6 — Present with transparency

Show the draft, and separately list:
- Every `[SUPPLY: ...]` placeholder still open, with a plain ask for what's needed to fill it
- Any assumption made (e.g., "benchmarked against typical postings, no JD provided")
- A brief note on what was deliberately left unquantified rather than padded

Offer to output as a file (see main SKILL.md output format options) once the candidate confirms the placeholders are filled or acceptable to leave.

## Iteration

If the candidate wants to tailor an already-generated resume to a new JD, re-run Steps 3–5 against the new JD's language rather than starting over — reuse verified project material, re-map keyword emphasis and role-target line only.
