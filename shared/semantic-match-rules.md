# AI-Semantic Search Rules

Modern recruiter tools increasingly use vector embeddings and LLM-based semantic matching, not just keyword density. This is the real, well-evidenced mechanism worth designing around (unlike AI-authorship detection).

| Check | What to look for |
|-------|------------------|
| Semantic role alignment | Would a semantic search for "[target role] with [core stack]" surface this resume? The role-target line and summary must match the domain even where exact keywords differ |
| Contextual keyword integration | Keywords woven into project bullets score higher than keywords dumped in a skills list alone. ML models can detect and penalize keyword stuffing |
| Experience narrative coherence | Does the resume read as a coherent story of someone who does this role, or as scattered keywords without narrative context? |
| LinkedIn cross-reference signal | Some ATS platforms cross-reference LinkedIn data — is the resume's role-target line consistent with the candidate's LinkedIn headline, if known? |
| Synonym coverage | Semantic search catches synonyms ("infrastructure as code" vs. "Terraform/CloudFormation"). Does the resume use both the tool name and the domain concept, where genuinely applicable? |
| Skills extraction confidence | Recruiters increasingly see extracted skills next to confidence scores — a skill mentioned once ambiguously scores much lower than one clearly demonstrated across multiple bullets. Concentrate real evidence on the skills that matter most for the target role, don't spread thin. |

Output: a brief assessment of whether AI-search tools would rank this resume highly for the target role, with specific gaps named. This is directional judgment, not a lab measurement — say so, in both flows.

## 1. DevOps & Cloud Keyword Reference

Cross-reference resume vocabulary against the JD (or, if none given, these high-frequency DevOps JD terms):

**Primary (must appear if claimed as a skill):**
Cloud — AWS (EC2, S3, Lambda, EKS, ECS, RDS, CloudFormation, IAM, VPC, CloudWatch), Azure, GCP. IaC — Terraform, CloudFormation, Ansible, Pulumi. CI/CD — GitHub Actions, GitLab CI, Jenkins, ArgoCD, Azure DevOps. Containers — Docker, Kubernetes/EKS/AKS/GKE, Helm. Monitoring — Prometheus, Grafana, CloudWatch, Datadog, ELK. Scripting — Python, Bash, Go. Security — IAM, Vault, SAST/DAST, Trivy, Snyk.

**Secondary (contextual, strengthens if present):**
GitOps, FinOps, Service Mesh (Istio/Linkerd), Observability (OpenTelemetry), Cost Optimization.

**Tertiary (supporting):**
Agile/Scrum, Networking (DNS, VPN, Load Balancing), Database Administration.

---

## 2. AI & Generative AI Engineering Keyword Reference (2026 Trending)

For entry-level AI Engineer, GenAI Developer, and LLM Applications Engineer roles:

**Primary (must appear if claimed as a skill):**
RAG Architecture — Chunking strategies, Vector Embeddings (text-embedding-3, BGE, Cohere), Vector Databases (pgvector, Qdrant, Pinecone, ChromaDB), Hybrid Search (Dense + Sparse/BM25). LLM Frameworks — LangChain, LlamaIndex, Haystack, LiteLLM. Model APIs & Local Inference — OpenAI API, Anthropic Claude API, HuggingFace, Ollama, vLLM. Evaluation & Guardrails — Ragas, TruLens, DeepEval, NeMo Guardrails, Prompt Injection Defense.

**Secondary (contextual, strengthens if present):**
Agentic Workflows (Tool calling, LangGraph, CrewAI, Autogen), Semantic Caching (GPTCache, Redis), Token & Cost Optimization, Function Calling, Re-ranking (Cohere Rerank), Context Window Management.

**Tertiary (supporting):**
PyTorch basics, LoRA / QLoRA fine-tuning concepts, Prompt Versioning (LangSmith, Phoenix, W&B), Dockerized model serving, FastAPI streaming endpoints.

---

## 3. Data & Analytics Engineering Keyword Reference (High-Volume Fresher Intake)

For entry-level Data Engineer, Analytics Engineer, and Associate Pipeline Developer roles:

**Primary (must appear if claimed as a skill):**
Data Transformations & Warehouses — SQL (advanced CTEs, window functions, partitioning), dbt (models, tests, snapshots, docs), Snowflake, BigQuery, Databricks, PostgreSQL. Workflow Orchestration — Apache Airflow (DAGs, TaskFlow API, Operators), Prefect, Dagster. Data Processing — PySpark, Python (Pandas, Polars, DuckDB). Data Quality — Great Expectations, dbt test assertions, schema validation.

**Secondary (contextual, strengthens if present):**
Dimensional Modeling (Star Schema, Snowflake Schema, Kimball methodology, SCD Type 1 & 2), ELT/ETL Architecture, CDC (Change Data Capture), Cloud Storage (S3, GCS Data Lakes), Parquet / Iceberg / Delta Lake table formats.

**Tertiary (supporting):**
Kafka / Kinesis event streaming basics, Data Cataloging (DataHub, Atlan), CI/CD for data pipelines (GitHub Actions SQLFluff linting), Cost-efficient query profiling.

---

## 4. Modern Backend & Distributed Systems Keyword Reference (Core SDE Entry Role)

For entry-level Backend Engineer, Software Development Engineer (SDE I), and Cloud Backend Developer roles:

**Primary (must appear if claimed as a skill):**
Languages — Python (FastAPI, Django), Go, Node.js (TypeScript, Express/NestJS), Java (Spring Boot). Relational & NoSQL Databases — PostgreSQL (indexing, query plans, transactions), DynamoDB, MongoDB, Redis (caching, sessions, pub/sub). API Architecture — RESTful APIs, OpenAPI/Swagger, gRPC, WebSocket. System Fundamentals — Concurrency, Idempotency, Rate Limiting, Connection Pooling (PgBouncer, SQLAlchemy pools).

**Secondary (contextual, strengthens if present):**
Event-Driven Architecture (RabbitMQ, Kafka basics, AWS SQS/SNS), Docker containerization, Authentication & AuthZ (JWT, OAuth2, RBAC), Microservices communication, Database Migrations (Alembic, Prisma).

**Tertiary (supporting):**
Load Balancing (Nginx, Caddy), Distributed Tracing (OpenTelemetry), Unit & Integration Testing (pytest, Jest, supertest), Memory profiling, CI/CD automated deployment.

---

Flag/avoid any primary keyword claimed with zero project evidence anywhere in the document — this is a keyword-stuffing risk under the ML-detection note above, not just a gap.
