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

## DevOps-Specific Keyword Reference

Cross-reference resume vocabulary against the JD (or, if none given, these high-frequency DevOps JD terms):

**Primary (must appear if claimed as a skill):**
Cloud — AWS (EC2, S3, Lambda, EKS, ECS, RDS, CloudFormation, IAM, VPC, CloudWatch), Azure, GCP. IaC — Terraform, CloudFormation, Ansible, Pulumi. CI/CD — GitHub Actions, GitLab CI, Jenkins, ArgoCD, Azure DevOps. Containers — Docker, Kubernetes/EKS/AKS/GKE, Helm. Monitoring — Prometheus, Grafana, CloudWatch, Datadog, ELK. Scripting — Python, Bash, Go. Security — IAM, Vault, SAST/DAST, Trivy, Snyk.

**Secondary (contextual, strengthens if present):**
GitOps, FinOps, Service Mesh (Istio/Linkerd), Observability (OpenTelemetry), Cost Optimization.

**Tertiary (supporting):**
Agile/Scrum, Networking (DNS, VPN, Load Balancing), Database Administration.

Flag/avoid any primary keyword claimed with zero project evidence anywhere in the document — this is a keyword-stuffing risk under the ML-detection note above, not just a gap.
