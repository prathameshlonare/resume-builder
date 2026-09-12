# Contributing to Resume Builder

Thank you for your interest in contributing to `resume-builder`! 

This project aims to help engineers transition away from generic, buzzword-heavy AI resumes and build **unassailable, evidence-backed resumes** grounded in verifiable codebase metrics and clean engineering phrasing.

Whether you want to add a new engineering domain, expand the fact-mining recipes, or add deterministic checks to the linter, this guide explains our standards and contribution process.

---

## 🧭 Core Principles (Our Quality Bar)

Every contribution must align with three non-negotiable principles:

1. **Zero AI Slop & Buzzwords**: We strictly avoid corporate register-inflation words (`spearheaded`, `leveraged`, `orchestrated`, `streamlined`, `fostered`, `results-driven`). If you add bullet templates or examples, they must lead with past-tense active verbs (`Built`, `Configured`, `Authored`, `Reduced`) and concrete mechanisms.
2. **Defensibility First**: Every claim must pass the core interview test: *"Would this survive an engineering manager asking you to walk through exactly how you built it?"*
3. **Zero Dependencies for Scripts**: Any code added to `scripts/validate_bullets.py` must use the **Python 3 Standard Library only** (no `pip install` requirements). This ensures anyone can run the tool in any environment without setup friction.

---

## 🎯 High-Impact Areas to Contribute

### 1. Adding New Domain Keyword Taxonomies
Currently, `shared/semantic-match-rules.md` has a pre-built taxonomy for **Cloud & DevOps**. We actively welcome keyword taxonomies for other disciplines:
* **Frontend Engineering**: React, Next.js, TypeScript, Webpack/Vite, State Management, Core Web Vitals, SSR, Tailwind.
* **Data Engineering & Analytics**: SQL, PySpark, Airflow, dbt, Snowflake, Kafka, Data Modeling, ETL/ELT pipelines.
* **Backend Systems (Go / Java / C++)**: Concurrency primitives, gRPC, Protobuf, Kafka, Distributed Caching (Redis), PostgreSQL tuning.
* **Mobile Engineering (iOS / Android / Flutter)**: Swift, Kotlin, React Native, memory profiling, offline caching, CI/CD with Fastlane.
* **Machine Learning & MLOps**: PyTorch, Model Serving (Triton, vLLM), MLflow, Quantization, RAG pipelines, Evaluation benchmarks.

> **How to format**: Group into **Primary** (mandatory core stack), **Secondary** (contextual concepts), and **Tertiary** (supporting methodologies).

---

### 2. Expanding the Fact-Mining Guide (`shared/codebase-mining.md`)
Help developers extract real numbers from their own codebases by adding terminal commands and inspection recipes. For example:
* **Frontend**: Measuring bundle size reductions (`source-map-explorer`, `bundle-analyzer`) or Core Web Vitals improvements.
* **Backend**: Measuring API response latency cuts, database query optimization with `EXPLAIN ANALYZE`, or memory reduction.
* **Data**: Measuring throughput (events/second), query run-time reductions, or pipeline data volume.

---

### 3. Improving the Deterministic Linter (`scripts/validate_bullets.py`)
You can contribute new quality gates or pattern matches:
* Adding new corporate buzzword patterns to `BANNED_TELL_WORDS`.
* Enhancing metric regex patterns (e.g. recognizing custom units like `req/s`, `rps`, `QPS`, `P99`).
* Adding unit tests to `run_tests()` verifying that the linter catches new failure modes without flagging false positives.

---

## 🛠️ Development & Testing Workflow

### 1. Fork & Clone
```bash
git clone https://github.com/<your-username>/resume-builder.git
cd resume-builder
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/add-frontend-domain
```

### 3. Test Changes Locally
If you modify `scripts/validate_bullets.py`, run the built-in self-test suite to ensure zero regressions:
```bash
python scripts/validate_bullets.py --test
```

You can also test against a custom bullet file:
```bash
python scripts/validate_bullets.py --file my_bullets.txt
```

### 4. Commit using Conventional Commits
Use clean, descriptive commit messages:
* `feat(keywords): add frontend and web performance keyword reference`
* `feat(mining): add webpack bundle analysis commands to codebase-mining.md`
* `fix(linter): avoid false positive on 'spring' as a participial opener`
* `docs: clarify ATS compliance context in ats-detection-research.md`

### 5. Open a Pull Request
Push your branch to GitHub and submit a PR against `main`. Please include:
* A clear summary of what was added or changed.
* Evidence of test verification (e.g., terminal output from `validate_bullets.py --test`).

---

## 📜 Code of Conduct

We are committed to maintaining a welcoming, supportive, and collaborative open-source environment. Be constructive in reviews, respect differing technical backgrounds, and help each other build better engineering careers.
