# Resume Audit Methodology

Detailed reasoning behind each check, for re-running without re-explaining.

---

## 1. The lens

Not "is this well-written." The question: **would this survive 6 seconds of hiring-manager attention, then survive an interview where every line gets probed?**

Two filters, in order:
1. **ATS filter** — will parsing software let a human see this?
2. **Human filter** — once seen, does it hold up under follow-up?

Most fresher resumes fail filter 2 first.

---

## 2. Severity coding

| Tag | Meaning | Consequence if unfixed |
|-----|---------|----------------------|
| 🔴 Critical | Misrepresentation, missing hard filter, or interview-embarrassing claim | Auto-reject or trust breakdown |
| 🟠 Moderate | Weak evidence, vague claims, unverified links | Recruiter skims past; stacks with other issues |
| 🟡 Minor | Cosmetic, formatting, style | Doesn't cost the role by itself |
| 🟢 Correct call | Something done right or confirmed judgment call | No action needed |

Don't soften a 🔴 into a 🟠 to be polite.

---

## 3. Step-by-step checks

**Step 1 — Claims audit**
For every bullet: *if the interviewer asked "walk me through exactly how you did this," could the candidate answer without hesitation?*

**Step 2 — Ownership resolution**
Once team projects are identified, every bullet must be re-classified:
- "I built this" → keep
- "We built this, I don't know which part" → re-scope to defensible claims
- Verification must come from the candidate, not assumption

**Step 3 — ATS parsing simulation**
How common ATS engines (Workday, Greenhouse, Taleo-style) behave:
- Section header matching (need "Experience" even if empty/N-A)
- Certification field string-matching (content under "Certifications" header = checkbox pass)
- Keyword frequency against typical JDs
- Location-radius filtering risk
- File format check (text-based PDF, not rasterized image)

**Step 4 — Keyword-gap analysis**
Compare resume skill/tool vocabulary against actual postings. Note high-frequency terms in JDs but missing from resume. This is a direct diff, not guesswork.

**Step 5 — Geographic/logistics filter**
Address vs target roles concentrated in metro areas. Flag as silent auto-filter risk, fixable with "Open to relocation."

**Step 6 — Skill-to-evidence matching**
Every Skills section line should appear in at least one project bullet. Skills listed only once with no context = weaker signal.

---

## 4. Pattern library

When saying something "reads like inflation" or "is the most common mistake" — pattern-matching against known failure modes:

- Inflated ownership on group/academic projects (most common fresher issue)
- Training courses mislabeled as certifications
- Skills sections padded with unused/unverified tools
- Missing quantifiable scope language
- Geographic mismatch with target roles
- Resumes as features list vs "here's what I did and can defend"

### DevOps/Cloud Fresher Specific Patterns
- **Aspirational tools in Skills**: K8s, Jenkins, Prometheus, Ansible listed but only "practicing" or "learning" in Active Learning — recruiter asks "walk me through your K8s cluster" and candidate has only minikube hello-world
- **CloudFormation vs Terraform confusion**: Listing both without clarifying which was used for what; candidate can't explain state management differences
- **Serverless metrics without context**: "p99 latency 180ms" — but no baseline, no load test methodology, no cost analysis
- **CI/CD "built" without ownership**: "Built pipeline with GitHub Actions" — but didn't write tests, security scans, or deployment strategies
- **Certification header trap**: "AWS Cloud Practitioner Essentials" under Certifications → ATS checkbox passes, recruiter sees "no exam taken" = trust break
- **Multi-cloud buzzwords**: "AWS, Azure, GCP" listed but projects only use AWS → depth vs breadth signal
- **Monitoring without alerting**: "CloudWatch dashboards" but no alarm thresholds, no incident response story

---

## 5. What NOT to do

- Don't add skills/tools user hasn't confirmed hands-on experience with
- Don't recommend paid fixes first if free rewrite solves the problem
- Don't smooth over critical issues for tone

---

## 6. Reusable checklist

- [ ] Every bullet survives "walk me through exactly how you did this"
- [ ] Every group project explicitly states team size
- [ ] Every claimed skill appears in at least one project bullet
- [ ] No training course misread as certification
- [ ] Resume has "Experience" header (even if N-A stub)
- [ ] Location/relocation explicit if targeting metro from smaller town
- [ ] Cross-check skills against 3-5 real JDs for target role
- [ ] File exports as text-based PDF, not flattened image

### DevOps/Cloud Addendum
- [ ] "Certifications" header only contains proctored exams with verifiable IDs
- [ ] Training courses moved to "Training & Courses" or "Active Learning"
- [ ] Aspirational skills (K8s, Jenkins, Prometheus, Terraform Advanced) have clear "learning/practicing" qualifiers
- [ ] Every metric has: baseline → intervention → result → verification method
- [ ] Serverless claims specify: runtime, memory, concurrency, cold start handling
- [ ] IaC claims specify: state backend, module structure, testing approach (Terratest/kitchen-terraform)
- [ ] CI/CD claims specify: test stages, security scans, deployment strategy (blue-green/canary), rollback
- [ ] Cloud services listed with specific services used (not just "AWS" — Lambda, DynamoDB, API Gateway, Cognito, CloudFront, CloudFormation, CloudWatch)
- [ ] Cost awareness mentioned (CloudWatch billing alarms, right-sizing, serverless cost model)
- [ ] Security mentioned with specifics: least-privilege IAM, Bandit scanning, presigned URLs, Cognito JWT validation
