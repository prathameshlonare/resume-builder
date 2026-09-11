<div align="center">

# 📄 Resume Builder (ATS & Humanized Engineering)

**An evidence-backed Agent Skill that crafts, humanizes, and audits technical resumes.**  
*Combines modern ATS semantic search realities, recruiter F-pattern scan rules, and structural debiasing to eliminate AI tells.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Tests](https://github.com/prathameshlonare/resume-builder/actions/workflows/test.yml/badge.svg)](https://github.com/prathameshlonare/resume-builder/actions/workflows/test.yml)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](scripts/validate_bullets.py)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Anthropic%20%7C%20Antigravity-purple)](SKILL.md)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-green)](scripts/validate_bullets.py)
[![Research-Backed](https://img.shields.io/badge/Research-Sept%202026%20ATS%20Audit-orange)](references/ats-detection-research.md)

<br>

> **Not an AI-detector bypass trick.**  
> The goal is unassailable technical credibility: bullets grounded in real codebase metrics, verified git artifacts, and active engineering phrasing that survives both semantic ATS parsers and rigorous technical interview screens.

</div>

---

## ⚡ Quick Install

Install directly into your agent environment (Claude Code, Antigravity, Cursor, Codex):

```bash
# Using skills CLI 
npx skills add prathameshlonare/resume-builder
```

**Or install manually via Git:**

```bash
# Global Agent Skills store
git clone https://github.com/prathameshlonare/resume-builder.git ~/.agents/skills/resume-builder

# Or directly in your workspace
git clone https://github.com/prathameshlonare/resume-builder.git .agents/skills/resume-builder
```

---

## 🧠 Why This Exists (The Problem)

When job seekers ask generic LLMs (ChatGPT, Claude, Gemini) to write or polish their resumes, the output defaults to high-probability tokens:
1. **Recurring Tell Vocabulary**: Words like *"spearheaded"*, *"leveraged"*, *"orchestrated"*, *"results-driven"*, and *"fostered cross-functional collaboration"* cluster unnaturally across thousands of applications.
2. **Machine-Like Verb-Shape Uniformity**: Every bullet rigidly follows `[Verb] + [Activity] + [Result]` with zero sentence structure variation.
3. **Suspicious Metric Symmetry**: Fabricating clean round-number metrics for every single bullet (e.g., *"improved efficiency by 40%"*) without baselines or mechanisms.
4. **Orphan Skills**: Listing 30 tools in a "Skills" box that have zero supporting evidence sentences in the project bullets.

### Ground Truth from Industry Audits (Sept 2026)
- **ATS Does NOT Detect Watermarks**: Independent audits across 10 major enterprise ATS platforms (Workday, Greenhouse, Taleo, iCIMS, Lever, Ashby) confirm that platforms do **not** run AI text detectors or watermark sniffers. Doing so would trigger legal and compliance liability under EEOC guidelines and the EU AI Act due to massive false-positive rates on non-native English speakers.
- **The Real Threat is Human Recruiter Recognition**: Recruiters perform a **6 to 7.4-second F-pattern scan** (The Ladders eye-tracking study). When a recruiter spots generic AI templates and ungrounded buzzwords, the resume gets binned immediately.
- **Modern ATS Uses Semantic Embeddings**: Platforms like Eightfold.ai and Ashby use deep learning ontologies and citation-based reviews. They search for **evidence sentences** inside project bullets to validate claimed skills.

---

## 🏗️ Architecture & How It Works

`resume-builder` operates as a dual-flow system governed by a shared standards layer:

```mermaid
flowchart TD
    A["User Request"] --> B{"Skill Router\nSKILL.md"}
    
    B -->|"Build from Scratch"| C["Generate Flow\nflows/generate.md"]
    B -->|"Review Existing Resume"| D["Audit Flow\nflows/audit.md"]
    
    subgraph Standards ["Shared Standards Layer"]
        S1["Bullet Standards\nScope + Outcome + Ownership"]
        S2["ATS Parsing Rules\nMechanical & Header Hygiene"]
        S3["Semantic Match Rules\nEmbeddings & DevOps Reference"]
        S4["Resume Phrasing Rules\nAI-Pattern & Credibility Risk"]
        S5["Codebase Fact-Mining\nDocker, Terraform, CI/CD, DB Metrics"]
    end
    
    C --> Standards
    D --> Standards
    
    C --> E["Deterministic Quality Gate\nscripts/validate_bullets.py"]
    D --> E
    
    E --> F["Validated Output\nSingle-Column Clean ATS / LaTeX"]

    style A fill:#1e293b,color:#fff,stroke:#3b82f6
    style B fill:#312e81,color:#fff,stroke:#6366f1
    style C fill:#065f46,color:#fff,stroke:#10b981
    style D fill:#831843,color:#fff,stroke:#f43f5e
    style Standards fill:#0f172a,color:#fff,stroke:#64748b
    style E fill:#431407,color:#fff,stroke:#f97316
    style F fill:#064e3b,color:#fff,stroke:#34d399
```

---

## 📊 The 4-Axis Evaluation Framework

Both flows grade and validate content across four independent axes:

| Axis | Weight | What It Measures |
| :--- | :---: | :--- |
| **1. Traditional ATS Parsing** | **30%** | Plain-text extraction, single-column layout, standard headers (`Experience`, `Education`), unambiguous dates (`MM/YYYY`), visible URLs. |
| **2. AI-Semantic Search** | **25%** | Vector embedding alignment, conceptual synonym mapping ($\text{Terraform} \approx \text{IaC}$), contextual keyword integration, anti-orphan skill enforcement. |
| **3. Recruiter F-Pattern Scan** | **25%** | 6–7.4s triage glance, outcome vs. scope ratio (target: 60%+ outcome bullets), team vs. solo ownership language, interview defensibility. |
| **4. AI-Pattern & Credibility** | **20%** | Zero banned tell words, verb-shape variety across sections, avoiding suspicious 100% metric symmetry, real baseline plausibility. |

---

## 🛠️ CLI Linter: `validate_bullets.py`

The repository includes a standalone, zero-dependency Python linter enforcing 8 deterministic quality gates.

### The 8 Hard Quality Gates
1. **`no_participial_opener`**: Forbids bullets opening with an `-ing` verb (*"Leveraging..."*, *"Building..."*). Enforces past-tense active verbs (*"Built"*, *"Configured"*).
2. **`no_trailing_fluff`**: Catches and flags trailing participial fluff (*"..., facilitating seamless scalability"*).
3. **`no_banned_words`**: Regex scan against a dictionary of 35+ corporate buzzwords and AI tells.
4. **`mechanical_hygiene`**: Forbids em/en dashes (`—`, `–`), curly quotes (`“”`), and decorative emojis.
5. **`word_count`**: Validates length between 15 and 38 words (optimal scannability).
6. **`metric_present`**: Checks for numbers, percentages, latencies, capacities, line counts, or multipliers.
7. **`active_voice`**: Flags weak ownership phrases (*"was responsible for"*, *"assisted with"*).
8. **`verb_uniformity`**: Warns if 3+ consecutive bullets start with the identical verb stem.

### Usage

```bash
# Validate a single bullet
python scripts/validate_bullets.py --bullet "Built automated GitHub Actions pipeline running Bandit SAST and 34 unit tests."

# Validate a full text/markdown file of bullets
python scripts/validate_bullets.py --file path/to/bullets.md

# Output structured JSON for automation
python scripts/validate_bullets.py --file path/to/bullets.md --json

# Run built-in self-test suite
python scripts/validate_bullets.py --test
```

---

## 🔍 Codebase Fact-Mining Protocol

When technical candidates don't know what metrics to provide, the skill extracts exact facts directly from git commits, Dockerfiles, and cloud templates:

* **Docker Optimization**: `docker images --format "{{.Repository}}:{{.Tag}} - {{.Size}}"`
  * *Outcome*: *"Reduced Docker build artifact from 350MB (`node:22`) to 25MB (`nginx:alpine`), a 93% image size reduction."*
* **Infrastructure as Code**: Count lines of modular Terraform / CloudFormation:
  * *Outcome*: *"Authored 650+ lines of modular Terraform provisioning 5 DynamoDB tables, Cognito, and API Gateway."*
* **CI/CD & Security**: Count automated tests and linters:
  * *Outcome*: *"Configured GitHub Actions CI/CD pipeline running Bandit SAST and 34 unit tests on every pull request."*
* **Concurrency & Database**:
  * *Outcome*: *"Implemented DynamoDB conditional write expressions (`attribute_not_exists`) to guarantee idempotency and prevent double-voting."*

---

## 🔄 Real-World Transformation Showcase

| Stage | Content | Analysis |
| :--- | :--- | :--- |
| **Raw Candidate Input** | *"I used Docker and GitHub actions for CI/CD in my voting system project."* | Honest, but lacks scope, ownership, and measurable impact. |
| **Standard AI Output** *(ChatGPT / Claude)* | *"Leveraging Docker and GitHub Actions, spearheaded the implementation of modern CI/CD pipelines, facilitating seamless automated testing and enhancing overall operational efficiency."* | ❌ Participial opener (`Leveraging`)<br>❌ 3 Banned tell words (`spearheaded`, `facilitating`, `seamless`)<br>❌ Participial tail fluff (`enhancing efficiency`)<br>❌ Zero concrete metrics |
| **`resume-builder` Output** *(Grounded + Humanized)* | *"Built automated GitHub Actions CI/CD pipeline running Bandit SAST and 34 unit tests, cutting Docker image size from 350MB to 25MB using a multi-stage `node:22-alpine` to `nginx:alpine` build."* | ✅ Direct active verb (`Built`)<br>✅ Exact technical entities (`Bandit SAST`, `nginx:alpine`)<br>✅ Concrete baseline vs. outcome (`350MB to 25MB`)<br>✅ **Score: 7/7 on validate_bullets.py** |

---

## 📁 Repository Structure

```
resume-builder/
├── SKILL.md                             # Main router & agent instructions (<50 lines)
├── LICENSE                              # MIT License
├── README.md                            # Complete documentation & usage guide
├── .gitignore                           # Git ignore rules
│
├── flows/                               # Execution flows
│   ├── generate.md                      # Build from scratch protocol
│   └── audit.md                         # 4-axis audit & severity-coding protocol
│
├── shared/                              # Shared standards layer
│   ├── bullet-standards.md              # Scope + Outcome + Ownership rules
│   ├── ats-parsing-rules.md             # Mechanical parsing & formatting rules
│   ├── semantic-match-rules.md          # Vector embedding & DevOps keyword reference
│   ├── resume-phrasing-rules.md         # AI-pattern signal set & tell vocabulary
│   └── codebase-mining.md               # Terminal commands for metric fact-mining
│
├── references/                          # Deep research & evidence base
│   ├── ats-detection-research.md        # Sept 2026 10-platform ATS research
│   ├── phrasing-research.md             # Why prose thresholds don't transfer
│   └── methodology.md                   # Severity coding & DevOps failure patterns
│
├── examples/                            # End-to-end walkthroughs & reference output
│   ├── before-after-bullets.md          # 10 bullet transformations across all 8 gates
│   └── devops-fresher/                  # Complete intake -> audit report -> final resume
│       ├── input-raw-notes.md           # Raw unpolished candidate input
│       ├── audit-report.md              # 4-axis severity-coded audit report
│       └── final-resume.md              # Validated single-column ATS markdown resume
│
└── scripts/                             # Deterministic code tools
    └── validate_bullets.py              # Zero-dependency Python bullet linter
```

---

## 🤝 Contributing

Contributions are welcome! Whether you want to add new engineering domains (Frontend, Data, ML), add fact-mining commands, or improve the deterministic linter:

* Please read our **[Contributing Guidelines (CONTRIBUTING.md)](CONTRIBUTING.md)** for quality standards, zero-dependency rules, and development workflows.
* Check out existing keyword taxonomies in `shared/semantic-match-rules.md` to see the structure for new domains.
* Open a PR or submit an issue to start a discussion.

---

## 📜 License

Distributed under the [MIT License](LICENSE).
