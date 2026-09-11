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

## 4. AI & Generative AI Engineering (RAG, Agents & LLMOps)

| Target Metric | Inspection Command / Source | Example Grounded Bullet Data |
| :--- | :--- | :--- |
| **RAG Ingestion & Chunking** | Inspect text splitter config in `rag/` or `ingest.py` for `chunk_size` and `chunk_overlap` | Built RAG pipeline chunking 1,200 technical documentation files into 512-token segments with 64-token overlap, indexed in Qdrant. |
| **Token Cost & Semantic Cache** | Check Redis / GPTCache integration and token tracking logs | Implemented Redis semantic cache for frequent query embeddings, cutting LLM token consumption by 42% and API spend by ₹25,000/month. |
| **RAG Evaluation (Ragas / TruLens)** | Inspect evaluation script or CI eval runs (`ragas.evaluate`) | Evaluated retrieval pipeline using Ragas, boosting answer faithfulness from 0.68 to 0.91 and context precision by adding Cohere re-ranking. |
| **Streaming & Time-to-First-Token** | Inspect async streaming generator in FastAPI / LiteLLM | Configured asynchronous SSE token streaming behind FastAPI, cutting user-perceived time-to-first-token (TTFT) from 2.4s to 380ms. |

---

## 5. Data & Analytics Engineering (dbt, Airflow & Warehousing)

| Target Metric | Inspection Command / Source | Example Grounded Bullet Data |
| :--- | :--- | :--- |
| **dbt Models & Schema Tests** | Linux: `find models/ -name "*.sql" \| wc -l`<br>PowerShell: `(Get-ChildItem -Recurse models\*.sql).Count`<br>Check `dbt test` output | Authored 18 modular dbt models transforming 1.5M raw event records into a dimensional star schema with 42 automated schema tests. |
| **Pipeline Runtime & Batch Volume** | Inspect Airflow DAG execution logs or Prefect flow run history | Scheduled daily Apache Airflow DAG processing 250k customer records, reducing batch pipeline runtime from 45 min to 14 min via PySpark partitioning. |
| **Analytical Query Optimization** | Run `EXPLAIN ANALYZE` or inspect BigQuery/Snowflake slot time | Optimized analytical SQL transformations using window functions and partition pruning, reducing warehouse query scan volume from 12GB to 450MB. |

---

## 6. Modern Backend & High-Throughput Systems

| Target Metric | Inspection Command / Source | Example Grounded Bullet Data |
| :--- | :--- | :--- |
| **Database Indexing & Query Latency** | Inspect migration scripts for B-Tree / GIN indexes and run `EXPLAIN (ANALYZE, BUFFERS)` | Added composite B-Tree indexes on user lookup queries, reducing PostgreSQL P95 query execution time from 850ms to 45ms across 500k rows. |
| **Connection Pooling & Concurrency** | Inspect `pgbouncer.ini` or database pool settings (`pool_size`, `max_overflow`) | Configured PgBouncer connection pooling with 20 persistent connections, preventing database connection exhaustion under 1,200 concurrent user requests. |
| **API Throughput & Rate Benchmarks** | Run `wrk -t4 -c100 -d30s http://localhost:8000/api/v1/...` or check load test reports | Engineered asynchronous FastAPI endpoints sustaining 1,800 req/s with zero dropped connections during load testing. |

---

## 7. Verification Checklist Before Bullet Drafting

- [ ] Is there an exact tool or technology name mentioned (e.g. `Qdrant`, `dbt test`, `Cohere Rerank`, `PgBouncer`, `Bandit`, `CloudFront OAI`)?
- [ ] Is there a measurable baseline vs outcome (e.g. `350MB to 25MB`, `2.4s to 380ms`, `45 min to 14 min`, `₹95,000 to ₹28,000`)?
- [ ] Could any other candidate copy-paste this bullet unchanged? If yes, dig deeper into the codebase for unique constraints or architectural choices.
