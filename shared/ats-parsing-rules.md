# ATS Parsing Rules

Mechanical checks, not judgment calls. Used by `audit.md` to score an existing resume, and by `generate.md` as hard constraints while producing a new one (cheaper to build these in than to catch them after).

| Check | What to look for |
|-------|------------------|
| File type | Text-selectable PDF/DOCX (good) or image/scan (fails silently — most ATS return a blank parse) |
| Section headers | Standard names (Experience, Education, Skills, Certifications) vs. creative headers some parsers fail to map to fields |
| Contact info | Plain text in document body, not inside a text box, image, or header/footer (some ATS skip header/footer content) |
| Date formats | Consistent, parseable ranges (MM/YYYY or Mon YYYY) — ambiguous dates break "years of experience" auto-calc |
| Keyword match | Extract top hard-skill nouns from the JD (or typical postings if no JD given), check literal presence, report the actual gap list — not just "good match" |
| Certification field risk | Courses/training listed under a "Certifications" header — flag explicitly, common false-positive trigger |
| Section presence | Missing "Experience" section entirely (vs. an explicit "N/A — fresher" stub) can null out fields some parsers expect |
| Location risk | Address vs. target role location — flag if a geographic auto-filter is plausible |
| Length/format | 2+ pages for a junior candidate, or dense multi-column layouts some parsers read out of order |
| Link survival | LinkedIn/GitHub/Portfolio as visible full URLs, not just anchor text — anchor-only links can vanish on plain-text extraction |
| Special characters | Unicode bullets, em-dashes, smart quotes, ligatures (fi, fl) that may garble on plain-text extraction |
| Font embedding | Non-standard fonts may not embed in PDF — verify standard fonts (Arial, Calibri, Helvetica) |
| Section order | Skills before Experience, Education before Experience — standard for freshers, non-standard order can confuse parsers |
| ATS platform quirks | Workday: rejects tables/columns/headers-footers/unclear dates. Greenhouse: needs exact keyword match. Lever: fails on over-designed PDFs. iCIMS: ignores nonstandard sections. Taleo: sensitive to file format & section names. |

## 2026 context

A large share of enterprise ATS now layer ML-based scoring (contextual relevance, keyword-manipulation detection, LinkedIn cross-reference) on top of literal parsing. Keyword stuffing or white-text tricks can now actively penalize a resume rather than just fail to help it. Frame as "a growing share" unless you have a current source — don't cite a specific percentage as fact.

**Important, from research (Sept 2026):** independent audits across 10 major ATS platforms (Workday, Greenhouse, Lever, Taleo, SAP SuccessFactors, iCIMS, BambooHR, JazzHR, BreezyHR, SmartRecruiters) found no evidence any of them run AI-authorship detection as a rejection gate. The ML layer is for candidate matching/ranking and keyword-manipulation detection, not for flagging "was this written by AI." Don't imply otherwise in audit output — the real risk downstream of AI-generated text is human pattern recognition (see resume-phrasing-rules.md), not an ATS detector.
