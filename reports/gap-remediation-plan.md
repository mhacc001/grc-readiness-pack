# Gap Remediation Plan

| Control | Title | Status | Owner | What is missing |
|---|---|---|---|---|
| 5.35 | Independent review of information security | Planned | CISO | First external ISO 27001 readiness audit booked for Q2 2027 |
| 8.12 | Data leakage prevention | Planned | CISO | DLP for email and drive planned for Q1 2027 |
| 5.3 | Segregation of duties | Partial | CISO | Production deploy and approval are split in CI; finance SoD review not yet formalised |
| 5.7 | Threat intelligence | Partial | CISO | Advisory feeds reviewed weekly; no formal threat-intel reporting yet |
| 5.13 | Labelling of information | Partial | CISO | Labels applied to documents in the drive; database fields not yet tagged |
| 5.18 | Access rights | Partial | CISO | Quarterly access reviews run; Q3 review found 1 late removal (see control test CT-01) |
| 5.20 | Addressing information security within supplier agreements | Partial | Legal & Compliance | Standard security addendum exists; 4 supplier contracts lack DORA Art 30 audit or exit clauses (see vendor scorecard) |
| 5.21 | Managing information security in the ICT supply chain | Partial | CTO | Dependency scanning in CI; no SBOM shared with customers yet |
| 5.28 | Collection of evidence | Partial | CISO | Log retention covers evidence; formal chain-of-custody form not yet adopted |
| 5.30 | ICT readiness for business continuity | Partial | IT Operations | Multi-AZ production and a tested restore; full region failover not yet exercised |
| 6.3 | Information security awareness, education and training | Partial | People Lead | Annual training 94% complete; phishing simulations quarterly |
| 8.2 | Privileged access rights | Partial | CISO | Just-in-time AWS admin via SSO; 2 standing admin accounts still being removed |
| 8.8 | Management of technical vulnerabilities | Partial | CISO | Weekly scanning with SLAs; 2 high findings past SLA (see control test CT-04) |
| 8.11 | Data masking | Partial | CTO | Masked datasets in staging; one analytics export still unmasked |
| 8.30 | Outsourced development | Partial | CTO | Offshore QA contractor under NDA; secure-coding clause missing from contract |
| 8.33 | Test information | Partial | CTO | Synthetic data for tests; one analytics export still contains real data |
