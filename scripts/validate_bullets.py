#!/usr/bin/env python3
"""
validate_bullets.py - Deterministic Resume Bullet Linter & Quality Gate

Validates resume bullet points against ATS, recruiter F-pattern, and
AI-tell phrasing rules. Uses only standard library modules.

Security: stdlib-only (argparse, re, json, sys, pathlib). No network,
no subprocess, no shell, no eval/exec, no file writes. Read-only —
reads bullets via --file or stdin only. Never pass untrusted resume
text as a shell argument; always write to a file first and use --file.

Checks:
  [1] No Participial Opener (no starting with '-ing' word)
  [2] No Trailing Participial Fluff (no trailing ', ...ing...')
  [3] Zero Banned Tell Words / Register Inflation Buzzwords
  [4] Mechanical Hygiene (no em/en dashes, curly quotes, decorative unicode, emoji)
  [5] Word Count Bounds (15 to 38 words per bullet)
  [6] Metric Presence (numbers, percentages, latencies, capacities, line counts)
  [7] Passive Voice Detection (no 'was responsible for', 'assisted in', etc.)
  [8] Consecutive Verb-Shape Uniformity across bullet sets
"""

import sys
import re
import argparse
import json
from pathlib import Path

# Ensure UTF-8 output across Windows, Unix, and CI environments
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
if hasattr(sys.stderr, "reconfigure"):
    try:
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Banned register-inflation buzzwords and classic AI tells
BANNED_TELL_WORDS = [
    r"\bspearhead(?:ed|ing|s)?\b",
    r"\bleverage(?:d|ing|s)?\b",
    r"\bsynerg(?:y|ized|izing|ies)\b",
    r"\bresults?-driven\b",
    r"\bdynamic professional\b",
    r"\bproven track record\b",
    r"\borchestrat(?:ed|ing|es)?\b",
    r"\bchampion(?:ed|ing|s)?\b",
    r"\bcatalyz(?:ed|ing|es)?\b",
    r"\bcross-functional collaboration\b",
    r"\bstreamlin(?:ed|ing|es)?\b",
    r"\bdelv(?:e|ed|ing|es)?\b",
    r"\bfoster(?:ed|ing|s)?\b",
    r"\butiliz(?:e|ed|ing|es)?\b",
    r"\bfacilitat(?:e|ed|ing|es)?\b",
    r"\bempower(?:ed|ing|s)?\b",
    r"\brobust\b",
    r"\bcutting-edge\b",
    r"\bparadigm shift\b",
    r"\bgame changer\b",
    r"\btapestry\b",
    r"\brealm\b",
    r"\bbeacon\b",
    r"\bmultifaceted\b",
    r"\bmeticulous(?:ly)?\b",
    r"\bintricate\b",
    r"\bparamount\b",
    r"\btransformative\b",
    r"\belevat(?:e|ed|ing|es)?\b",
    r"\bharness(?:ed|ing|es)?\b",
    r"\bever-evolving\b",
    r"\btestament to\b",
    r"\bpivotal\b",
    r"\bgroundbreaking\b",
    r"\bholistic\b",
    r"\bseamless(?:ly)?\b",
    r"\bpassionate\b",
    r"\bmeticulous\b",
]

COMPILED_BANNED = [(pattern, re.compile(pattern, re.IGNORECASE)) for pattern in BANNED_TELL_WORDS]

METRIC_PATTERNS = [
    r"(?:₹|Rs\.?|INR|\$)\s*\d+(?:,\d{2,3})*(?:\.\d+)?\s*(?:k|lakhs?|crores?|cr|l|m|b|billion|million)?(?:\s*/\s*(?:mo|month|yr|year|annum))?\b", # Financial: ₹95,000, ₹25,000/month, ₹12 Lakhs, Rs. 50,000, INR 1.5 Cr
    r"\b\d+(?:,\d{2,3})*(?:\.\d+)?\s*(?:lakhs?|crores?|cr|lpa)\b",                                   # Indian denominations: 12 Lakhs, 1.5 Crore, 10 LPA
    r"\b\d+(?:\.\d+)?\s*(?:req/s|rps|qps|tps|ops/s|requests/sec)\b",                       # Throughput/rates: 1,500 req/s, 500 QPS
    r"\b\d+(?:\.\d+)?\s*[kKmMbB]?\s+(?:\w+\s+){0,2}(?:tokens?/s|tokens?|records?/s|records?|rows?/s|rows?|events?|queries)\b", # AI & Data volume: 1.5M raw event records, 4k tokens, 250k rows
    r"\b\d+(?:\.\d+)?%\s*(?:uptime|sla|availability)\b",                                               # Uptime & SLA: 99.95% uptime
    r"\b\d+(?:\.\d+)?%(?!\w)",                                                                         # Percentages: 93%, 99.9%, 80%
    r"\b\d+(?:\.\d+)?\s*(?:ms|sec|min|hours?)\b",                                                       # Latency/time: 120ms, 3 min
    r"\b\d+(?:\.\d+)?\s*(?:MB|GB|TB|KB)\b",                                                             # Storage/memory: 25MB, 350MB
    r"\b\d+\+?\s+(?:\w+\s+){0,2}(?:microservices?|services?|endpoints?|lambdas?|tables?|tests?|repos?|pipelines?|models?|dags?|chunks?|files?)\b", # Counts: 34 unit tests, 18 modular dbt models
    r"\b(?:faithfulness|precision|recall|relevan(?:ce|cy)|accuracy|f1[-\s]*score)\s*(?:from|to|of|:)?\s*0?\.\d+\b", # AI/RAG evaluation metrics: faithfulness from 0.68 to 0.91
    r"\b\d+x\b",                                                                                         # Multipliers: 2x, 10x
    r"\b\d+\s*lines?\b",                                                                                # Line counts: 650 lines
    r"\b(?:[<>]|less than|more than)\s*\d+(?:\.\d+)?%?\b",                                              # General numbers with comparison context
]

COMPILED_METRICS = [re.compile(p, re.IGNORECASE) for p in METRIC_PATTERNS]

PASSIVE_PHRASES = [
    re.compile(r"\bwas responsible for\b", re.IGNORECASE),
    re.compile(r"\bwere responsible for\b", re.IGNORECASE),
    re.compile(r"\bassisted (?:with|in)\b", re.IGNORECASE),
    re.compile(r"\bhelped (?:with|to)\b", re.IGNORECASE),
    re.compile(r"\btasked with\b", re.IGNORECASE),
    re.compile(r"\bworked on\b", re.IGNORECASE),
]

def clean_bullet_text(text: str) -> str:
    """Strip leading list markers, dashes, or bullets."""
    return re.sub(r"^\s*[-*•–—\d\.]+\s*", "", text).strip()

def check_participial_opener(text: str) -> tuple[bool, str]:
    """Gate 1: Never start a bullet with an '-ing' word."""
    words = text.split()
    if not words:
        return False, "Empty bullet"
    first_word = re.sub(r"[^\w]", "", words[0]).lower()
    if first_word.endswith("ing") and first_word not in ("spring", "ring", "string", "ping"):
        return False, f"Starts with participial opener '{words[0]}'. Use past-tense active verb (e.g. 'Built', 'Configured', 'Authored')."
    return True, "Passed"

def check_trailing_participial_fluff(text: str) -> tuple[bool, str]:
    """Gate 2: Never end a bullet with trailing participial fluff (', ...ing...')."""
    match = re.search(r",\s+([a-zA-Z]+ing\b[^.]*)\.?$", text)
    if match:
        fluff_clause = match.group(1).strip()
        first_ing = fluff_clause.split()[0].lower()
        if first_ing in ("enhancing", "facilitating", "ensuring", "driving", "boosting", "fostering", "streamlining", "improving", "allowing"):
            return False, f"Trailing participial fluff detected: ', {fluff_clause}'. Cut the clause or convert it into a concrete measured outcome."
    return True, "Passed"

def check_banned_words(text: str) -> tuple[bool, list[str]]:
    """Gate 3: Check for banned register inflation words."""
    found = []
    for raw_pattern, regex in COMPILED_BANNED:
        matches = regex.findall(text)
        if matches:
            found.extend(matches)
    if found:
        return False, list(set(found))
    return True, []

def check_mechanical_hygiene(text: str) -> tuple[bool, list[str]]:
    """Gate 4: Mechanical hygiene (no em/en dashes, curly quotes, emoji)."""
    issues = []
    if "—" in text or "–" in text:
        issues.append("Contains em/en dash (— or –). Use standard comma, colon, or parentheses.")
    if "“" in text or "”" in text or "‘" in text or "’" in text:
        issues.append("Contains curly quotes. Use straight ASCII quotes (' or \").")
    # Check for emoji/unicode symbols
    for char in text:
        if ord(char) > 10000:
            issues.append(f"Non-ASCII / emoji character detected: '{char}'")
            break
    if issues:
        return False, issues
    return True, []

def check_word_count(text: str) -> tuple[bool, str]:
    """Gate 5: Word count bounds (15 to 38 words)."""
    word_count = len(text.split())
    if word_count < 15:
        return False, f"Too brief ({word_count} words). Good technical bullets typically require 15-38 words to detail tool, action, and metric."
    if word_count > 38:
        return False, f"Too long ({word_count} words). Exceeds 38 words; hard to parse in a 6-second scan. Split into two points or cut fluff."
    return True, f"{word_count} words (optimal)"

def check_metric_presence(text: str) -> tuple[bool, str]:
    """Gate 6: Check for quantified impact/metric."""
    for regex in COMPILED_METRICS:
        match = regex.search(text)
        if match:
            return True, f"Found metric: '{match.group(0)}'"
    return False, "No quantified metric found (no %, ms, MB, line count, or numerical scale). Add real baseline/outcome if available, or mark [SUPPLY NUMBER]."

def check_passive_voice(text: str) -> tuple[bool, str]:
    """Gate 7: Check for passive / weak ownership phrasing."""
    for regex in PASSIVE_PHRASES:
        match = regex.search(text)
        if match:
            return False, f"Passive or weak ownership phrase: '{match.group(0)}'. Lead with direct active verb."
    return True, "Passed"

def validate_bullet(bullet: str) -> dict:
    """Run all checks on a single bullet point."""
    cleaned = clean_bullet_text(bullet)
    results = {}
    
    # 1. Participial Opener
    p_open_ok, p_open_msg = check_participial_opener(cleaned)
    results["no_participial_opener"] = {"pass": p_open_ok, "detail": p_open_msg}
    
    # 2. Trailing Participial Fluff
    t_fluff_ok, t_fluff_msg = check_trailing_participial_fluff(cleaned)
    results["no_trailing_fluff"] = {"pass": t_fluff_ok, "detail": t_fluff_msg}
    
    # 3. Banned Words
    bw_ok, bw_matches = check_banned_words(cleaned)
    results["no_banned_words"] = {"pass": bw_ok, "detail": f"Found: {', '.join(bw_matches)}" if not bw_ok else "Passed"}
    
    # 4. Mechanical Hygiene
    mech_ok, mech_issues = check_mechanical_hygiene(cleaned)
    results["mechanical_hygiene"] = {"pass": mech_ok, "detail": "; ".join(mech_issues) if not mech_ok else "Passed"}
    
    # 5. Word Count
    wc_ok, wc_msg = check_word_count(cleaned)
    results["word_count"] = {"pass": wc_ok, "detail": wc_msg}
    
    # 6. Metric Presence
    met_ok, met_msg = check_metric_presence(cleaned)
    results["metric_present"] = {"pass": met_ok, "detail": met_msg}
    
    # 7. Passive Voice
    pass_ok, pass_msg = check_passive_voice(cleaned)
    results["active_voice"] = {"pass": pass_ok, "detail": pass_msg}
    
    all_passed = all(check["pass"] for check in results.values())
    passed_count = sum(1 for check in results.values() if check["pass"])
    
    return {
        "text": cleaned,
        "passed": all_passed,
        "score": f"{passed_count}/{len(results)}",
        "checks": results
    }

def check_verb_uniformity(bullets: list[str]) -> list[str]:
    """Check for 3+ consecutive bullets opening with the same verb stem."""
    warnings = []
    openers = []
    for b in bullets:
        c = clean_bullet_text(b)
        words = c.split()
        if words:
            verb = re.sub(r"[^\w]", "", words[0]).lower()
            openers.append(verb)
        else:
            openers.append("")
            
    for i in range(len(openers) - 2):
        v1, v2, v3 = openers[i], openers[i+1], openers[i+2]
        if v1 and v1 == v2 == v3:
            warnings.append(f"Bullets {i+1}, {i+2}, {i+3} all start with identical verb '{v1}'. Vary the opening verbs to avoid machine-like uniformity.")
    return warnings

def run_tests():
    """Run internal test cases verifying detection on bad vs good bullets."""
    test_cases = [
        {
            "name": "Bad AI Bullet: participial opener, buzzwords, trailing fluff, em-dash",
            "text": "Leveraging Docker and Terraform, spearheaded the implementation of modern CI/CD pipelines — facilitating seamless integration and enhancing overall operational efficiency.",
            "expect_pass": False,
        },
        {
            "name": "Good Humanized Bullet: active verb, metrics, exact tools, no fluff",
            "text": "Built automated GitHub Actions CI/CD pipeline running Bandit SAST and 34 unit tests, cutting Docker image size from 350MB to 25MB using a multi-stage node:22-alpine to nginx:alpine build.",
            "expect_pass": True,
        },
        {
            "name": "Bad AI Bullet: passive voice, vague metric, robust buzzword",
            "text": "Was responsible for building robust cloud infrastructure on AWS, improving system speed significantly.",
            "expect_pass": False,
        },
        {
            "name": "Good Humanized Bullet: DynamoDB conditional writes, concurrency metric",
            "text": "Authored 650 lines of modular Terraform provisioning 5 DynamoDB tables and API Gateway, implementing composite primary keys to prevent double-voting under concurrent load.",
            "expect_pass": True,
        },
        {
            "name": "Good Humanized Bullet: financial savings metric in Indian currency (₹)",
            "text": "Reduced monthly AWS infrastructure spend from ₹95,000 to ₹28,000 by right-sizing EC2 instances and migrating non-critical batch jobs to Spot.",
            "expect_pass": True,
        },
        {
            "name": "Good Humanized Bullet: rate metric and high-availability SLA",
            "text": "Scaled backend ingestion pipeline to handle 1,500 req/s while sustaining 99.95% uptime across 3 AWS availability zones.",
            "expect_pass": True,
        },
        {
            "name": "Good Humanized Bullet: AI RAG pipeline, token chunking and faithfulness eval metric",
            "text": "Built RAG pipeline chunking 1,200 documentation files into 512-token segments in Qdrant and improved answer faithfulness from 0.68 to 0.91 using Cohere re-ranking.",
            "expect_pass": True,
        },
        {
            "name": "Good Humanized Bullet: Data engineering dbt models, row volume, and automated tests",
            "text": "Authored 18 modular dbt models transforming 1.5M raw event records into a dimensional star schema with 42 automated schema tests.",
            "expect_pass": True,
        },
        {
            "name": "Bad Bullet: too brief boundary check (14 words, fails 15-word threshold)",
            "text": "Configured automated GitHub Actions CI pipeline running 34 unit tests on every pull request.",
            "expect_pass": False,
        }
    ]
    
    print("==================================================")
    print("RUNNING VALIDATE_BULLETS TEST SUITE")
    print("==================================================")
    all_ok = True
    for i, tc in enumerate(test_cases, 1):
        res = validate_bullet(tc["text"])
        passed = res["passed"]
        if passed == tc["expect_pass"]:
            status = "PASSED"
        else:
            status = "FAILED"
            all_ok = False
        print(f"\n[Test {i}] {tc['name']} -> {status} (Score: {res['score']})")
        if status == "FAILED" or not passed:
            for check_name, check_data in res["checks"].items():
                if not check_data["pass"]:
                    print(f"   [FAIL] {check_name}: {check_data['detail']}")
                    
    print("\n==================================================")
    if all_ok:
        print("ALL TESTS PASSED SUCCESSFULLY.")
        sys.exit(0)
    else:
        print("SOME TESTS FAILED.")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Validate resume bullets against ATS and AI-tell rules.")
    parser.add_argument("--bullet", type=str, help="Single bullet text to validate.")
    parser.add_argument("--file", type=str, help="Path to text/markdown file containing bullets.")
    parser.add_argument("--test", action="store_true", help="Run self-test suite.")
    parser.add_argument("--json", action="store_true", help="Output results in JSON format.")
    
    args = parser.parse_args()
    
    if args.test:
        run_tests()
        return

    bullets_to_check = []
    if args.bullet:
        bullets_to_check.append(args.bullet)
    elif args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: file not found at {args.file}", file=sys.stderr)
            sys.exit(1)
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                stripped = line.strip()
                if stripped.startswith(("-", "*", "•")) or (len(stripped) > 20 and not stripped.startswith("#")):
                    bullets_to_check.append(stripped)
    else:
        # Read from stdin if no args provided
        if not sys.stdin.isatty():
            for line in sys.stdin:
                s = line.strip()
                if s:
                    bullets_to_check.append(s)
        else:
            parser.print_help()
            sys.exit(1)
            
    if not bullets_to_check:
        print("No bullets found to validate.", file=sys.stderr)
        sys.exit(1)
        
    results = [validate_bullet(b) for b in bullets_to_check]
    uniformity_warnings = check_verb_uniformity(bullets_to_check)
    
    output_data = {
        "bullets": results,
        "uniformity_warnings": uniformity_warnings,
        "summary": {
            "total": len(results),
            "passed": sum(1 for r in results if r["passed"]),
            "failed": sum(1 for r in results if not r["passed"]),
        }
    }
    
    if args.json:
        print(json.dumps(output_data, indent=2))
        return
        
    print(f"\nVALIDATION REPORT ({output_data['summary']['passed']}/{output_data['summary']['total']} Bullets Passed All Gates)")
    print("-" * 60)
    for i, r in enumerate(results, 1):
        status_symbol = "✓" if r["passed"] else "✗"
        print(f"\nBullet {i} [{status_symbol}] ({r['score']} checks passed):")
        print(f"  \"{r['text']}\"")
        if not r["passed"]:
            for check_name, data in r["checks"].items():
                if not data["pass"]:
                    print(f"    - FAIL [{check_name}]: {data['detail']}")
                    
    if uniformity_warnings:
        print("\nUniformity Warnings:")
        for w in uniformity_warnings:
            print(f"  ! {w}")
            
    if output_data["summary"]["failed"] > 0:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
