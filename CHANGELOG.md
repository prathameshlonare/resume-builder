# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.3.1] - 2026-09-23

### Security
- Removed external references to flagged domain `resumeoptimizerpro.com`.
- Hardened bullet validator execution guidelines (`validate_bullets.py`) with strict stdlib-only restrictions.
- Added input sanitization boundaries in `flows/audit.md` and `flows/generate.md` against indirect prompt injection.

## [1.3.0] - 2026-09-11

### Added
- **Structured Audit Schema (`shared/audit-schema.json`)**:
  - Formal JSON Schema conforming to JSON Schema Draft 2020-12 defining structured, machine-readable audit report artifacts.
  - Enforces schemas for candidate metadata, benchmark type, estimate overall score with guidance bands, 4-axis sub-scores, severity-coded findings (`critical`, `moderate`, `minor`, `correct_call`), gap analysis, and before/after bullet rewrites with gates fixed.
- **Machine-Readable JSON Output in Audit Flow (`flows/audit.md`)**:
  - Added JSON artifact output specification under Step 10 for programmatic agent workflows, automated CI gates, and dashboard integrations.
- **Documentation & Standards Sync**:
  - Added `shared/audit-schema.json` to the file tree in `README.md` and shared standards list in `SKILL.md`.

## [1.2.0] - 2026-09-11

### Added
- **2026 Booming Fresher Domain Taxonomies** in `shared/semantic-match-rules.md`:
  - AI & Generative AI Engineering (RAG architecture, vector databases, LangChain/LlamaIndex, evaluation frameworks, model serving).
  - Data & Analytics Engineering (dbt models and tests, Apache Airflow, PySpark, star schema, SQL window functions, Great Expectations).
  - Modern Backend & Distributed Systems (FastAPI, Go, PostgreSQL indexing, Redis caching, connection pooling, concurrency).
- **Codebase Fact-Mining Protocols** in `shared/codebase-mining.md`:
  - AI/GenAI: Chunk size/overlap, token cost reduction, Ragas evaluation metrics, streaming TTFT.
  - Data Engineering: dbt model counts, Airflow DAG runtime reduction, analytical query profiling.
  - Backend Systems: PostgreSQL `EXPLAIN ANALYZE` index cost, PgBouncer pooling, API throughput load testing.
- **Extended Linter Regexes** in `scripts/validate_bullets.py`:
  - Matches AI tokens (`tokens/s`, `4k tokens`), dataset volumes (`1.5M records`, `250k rows`), and evaluation metrics (`faithfulness from 0.68 to 0.91`).
  - Added self-tests for AI RAG pipelines and Data Engineering dbt models (all 9 tests passing).

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
