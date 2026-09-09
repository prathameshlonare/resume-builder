# Codebase Fact-Mining Protocol for Technical Resumes

A developer or DevOps engineer's strongest defense against generic AI phrasing is **unassailable technical grounding** pulled directly from git commits, configuration files, and architecture artifacts.

When drafting bullets in `generate.md` or repairing weak bullets in `audit.md`, use these exact inspection commands to extract real metrics and architectures rather than guessing or padding.

---

## 1. Container & Image Optimization

| Target Metric | Inspection Command / Source | Example Grounded Bullet Data |
| :--- | :--- | :--- |
| **Image Size Reduction** | `docker images --format "{{.Repository}}:{{.Tag}} - {{.Size}}"` | Reduced build artifact from 350MB (`node:22`) to 25MB (`nginx:alpine`), a **93% reduction in image size**. |
| **Multi-Stage Build Architecture** | Inspect `Dockerfile` for `FROM ... AS builder` and runtime copy | Implemented multi-stage Docker build separating frontend compiler from production Nginx server. |
| **Local Dev Composition** | Inspect `docker-compose.yml` for services, ports, and volumes | Configured 4-service Docker Compose stack simulating DynamoDB Local, backend API, and SPA runtime. |

---

## 2. Infrastructure as Code (Terraform / CloudFormation / SAM)

| Target Metric | Inspection Command / Source | Example Grounded Bullet Data |
| :--- | :--- | :--- |
| **IaC Code Volume** | PowerShell: `(Get-Content -Path (Get-ChildItem -Recurse -Filter *.tf).FullName \| Measure-Object -Line).Lines`<br>Linux: `git ls-files "*.tf" \| xargs wc -l` | Authored **650+ lines of modular Terraform** provisioning 5 DynamoDB tables, Cognito, and API Gateway. |
| **Resource Breadth** | Inspect `main.tf` / `template.yaml` for provisioned resource blocks | Provisioned S3 origin with CloudFront Origin Access Identity (OAI) enforcing encrypted HTTPS delivery. |
| **IAM Least-Privilege** | Inspect IAM policy statements for specific resource ARNs | Authored least-privilege IAM execution roles scoping Lambda access to specific DynamoDB table ARNs. |

---

## 3. CI/CD Pipelines & DevSecOps

| Target Metric | Inspection Command / Source | Example Grounded Bullet Data |
| :--- | :--- | :--- |
| **Automated Test Volume** | Check test output runner (e.g. `pytest`, `npm test`, `vitest`) | Integrated GitHub Actions pipeline running **34 unit tests** on every pull request prior to deployment. |
| **Static Security Scans (SAST)** | Inspect `.github/workflows/` for linters and scanners | Automated Bandit static application security testing (SAST) and ESLint within CI pull request gates. |
| **Zero-Downtime Cache Invalidation** | Inspect deployment workflow for CDN sync | Configured AWS CLI deployment step to invalidate CloudFront cache automatically following S3 static asset sync. |

---

## 4. Backend Microservices & Database Architecture

| Target Metric | Inspection Command / Source | Example Grounded Bullet Data |
| :--- | :--- | :--- |
| **Microservice Count** | Count handler files in `lambdas/` or `controllers/`: `(Get-ChildItem -Recurse *.py).Count` | Maintained **12 Python 3.9 Lambda microservices** handling authentication, vote ingestion, and tallying. |
| **Concurrency & Race Conditions** | Inspect database write queries for conditional constraints | Used DynamoDB conditional write expressions (`attribute_not_exists`) to guarantee idempotency and prevent double-voting. |
| **Access Control (RBAC)** | Check Cognito user groups or JWT claims verification | Enforced role-based access control (RBAC) across Student, Faculty, and Admin personas using Cognito user pool groups. |
| **API Latency & Media Offloading** | Inspect file upload logic for presigned S3 URLs | Offloaded media uploads from backend compute via S3 presigned URLs, cutting API gateway payload overhead. |

---

## 5. Verification Checklist Before Bullet Drafting

- [ ] Is there an exact tool or technology name mentioned (e.g. `Bandit`, `CloudFront OAI`, `DynamoDB conditional writes`)?
- [ ] Is there a measurable baseline vs outcome (e.g. `350MB to 25MB`, `34 unit tests`, `650+ lines`)?
- [ ] Could any other candidate copy-paste this bullet unchanged? If yes, dig deeper into the codebase for unique constraints or architectural choices.
