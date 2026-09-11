# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-09-11

### Added
- Complete walkthrough library in `examples/`:
  - `examples/before-after-bullets.md`: 10 real-world transformations covering all 8 quality gates.
  - `examples/devops-fresher/`: End-to-end walkthrough from raw intake (`input-raw-notes.md`) to 4-axis audit (`audit-report.md`) and single-column ATS resume (`final-resume.md`).

### Fixed
- Fixed percentage regex matching in `scripts/validate_bullets.py` where word boundary `\b` following non-word character `%` prevented standalone percentages (e.g. `80%`) from matching when followed by whitespace.

## [1.0.0] - 2026-09-11

### Added
- Dual-flow resume building and auditing architecture (`flows/generate.md`, `flows/audit.md`).
- Core shared standards layer:
  - `shared/bullet-standards.md`: Scope, outcome, ownership, and verifiability rules.
  - `shared/ats-parsing-rules.md`: Mechanical parsing and 2026 enterprise ATS checklist.
  - `shared/semantic-match-rules.md`: Vector embedding alignment and DevOps keyword reference.
  - `shared/resume-phrasing-rules.md`: Human-recognized AI pattern signals and tell vocabulary.
  - `shared/codebase-mining.md`: Fact-mining terminal commands for Docker, Terraform, CI/CD, and databases.
- Deterministic bullet linter (`scripts/validate_bullets.py`) enforcing 8 hard quality gates with zero external dependencies.
- Sourced research and methodology papers in `references/`:
  - 10-platform enterprise ATS audit (Sept 2026).
  - Phrasing research contrasting prose humanizer tools with resume conventions.
  - Severity-coding methodology and fresher/DevOps failure patterns.
- Automated GitHub Actions CI workflow running multi-version matrix tests (Python 3.10, 3.11, 3.12).
- Extended metric regex matching for Indian currency and denominations (`₹95,000`, `₹12 Lakhs`, `Rs. 45,000/month`, `INR 1.5 Cr`, `10 LPA`), rate/throughput metrics (`1,500 req/s`, `500 QPS`), and SLA/uptime metrics (`99.95% uptime`).

### Fixed
- Fixed off-by-one boundary condition in `scripts/validate_bullets.py` where bullets under 15 words were incorrectly permitted if at 14 words.
