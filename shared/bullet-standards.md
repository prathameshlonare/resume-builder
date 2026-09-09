# Bullet Quality Standards

Shared by both flows: `generate.md` applies these while drafting; `audit.md` applies them while scoring existing bullets. Keep this the single source of truth — do not let either flow redefine "good bullet" independently.

## The core test

For every bullet, ask: **"Would this survive the candidate being asked to walk through exactly how they did it?"**

## Scope + Outcome + Ownership + Verifiability

- 🟢 **Outcome bullet**: "Reduced deploy time from 12 min to 3 min via GitHub Actions pipeline" — has a number, a mechanism, and implied ownership.
- 🟠 **Scope bullet**: "Built CI/CD pipeline with GitHub Actions" — states what, not what changed or what it achieved.
- 🔴 **Vague/fluff**: "Optimized performance at scale" — no number, no baseline, unfalsifiable.

Target for a competitive fresher resume: at least 60% of bullets should be outcome-level.

## Never invent

- Never invent a metric. Where a bullet needs a number the candidate hasn't given, write `[SUPPLY NUMBER: what to measure and where to find it]` rather than a plausible-sounding guess.
- Never rewrite scope into false outcome — "Built CI/CD pipeline" cannot become "Reduced deploy time by 70%" unless the candidate actually has that number.
- Never assume solo ownership of a project described in group/academic/team context — ask if unclear, don't default either direction.

## Ownership language vs. reality

Group/academic/team projects described with solo-sounding verbs ("I designed and deployed...") without team size disclosed is the single most common fresher-resume issue. Actively check for it in both flows — during intake for generation, during review for audit.

## Skill-to-evidence linkage

Every Skills-section entry should be backed by at least one bullet elsewhere. In generation, don't add a skill to the Skills list unless it appears in at least one project bullet (or the candidate confirms real hands-on exposure even if small). In audit, flag unsupported entries — don't recommend outright removal, recommend adding evidence or being ready to speak to real exposure.

## Certification vs. Training

- **Certification** = proctored exam with a verifiable credential ID (AWS Certified Cloud Practitioner, CKA, Terraform Associate, etc.)
- **Training/Course** = self-paced, no exam, no verifiable badge (AWS Skill Builder, Coursera, bootcamp completions)
- The section header must match reality: "Certifications" vs. "Training & Courses." A free course is never a certification — no exceptions, in generation or audit.
- Exam-scheduled certifications: list as "Certification (Exam Scheduled: MM YYYY)" — never presented as already earned.

## AI-pattern / credibility risk (see resume-phrasing-rules.md for the full signal set)

Applies to both flows equally — this is not a separate afterthought pass, it's part of what makes a bullet "good" in the first place:

- Never use tell-vocabulary: "spearheaded," "leveraged," "synergy/synergized," "results-driven," "dynamic professional," "proven track record," "orchestrated," "championed," "catalyzed," "cross-functional collaboration," "streamlined," "optimized" (as a standalone claim with no mechanism).
- Never let 3+ consecutive bullets, or 50%+ of a section, open with the same verb tense/shape.
- Don't force a metric onto every single bullet just for symmetry — a bullet without a real number is better than an invented one. "Suspicious symmetry" (every bullet having a clean round number) is itself a credibility risk, not a strength.
- Sanity-check metric magnitude against stated scope — a fresher/intern bullet claiming enterprise-scale impact needs the team/project context to support it, or it reads as implausible.
- Cross-reference named tools/tech against the project timeframe for anachronism risk.
- The "so what" test: could this bullet describe literally any candidate with this job title, or does it name a real system, tool, dataset, constraint, or decision that's specific to this person?
