# IRP-01 Incident Response Plan

| Owner | Approved by | Version | Effective | Next review |
|---|---|---|---|---|
| CISO | CEO | 1.0 | 2026-11-01 | 2027-11-01 |

Annex A: 5.24 to 5.28, 6.8. SOC 2: CC7.3 to CC7.5. DORA: Art 17 to 19 (our bank clients' reporting duties).

## Severity

| Severity | Examples | Customer notice |
|---|---|---|
| SEV-1 | Restricted data exposed, platform unavailable for more than 2 hours, compromise of production | Initial notice to affected banks within **4 hours** of classification |
| SEV-2 | Contained compromise of a corporate account, degraded service | Within 24 hours if customer data or service is affected |
| SEV-3 | Malware blocked, phishing reported, single-user issue | Not required |

Why 4 hours: DORA requires our bank clients to send an initial report on a *major* ICT incident within 4 hours of classifying it, and no later than 24 hours after becoming aware of it. They can only meet that deadline if we tell them fast. Our severity matrix mirrors the DORA classification criteria (Art 18 and the related technical standards):
- clients affected
- duration
- geographic spread
- data losses
- criticality of the services affected
- economic impact

## Process

1. **Report.** Anyone reports in #security-report or with the report button.
2. **Triage.** The on-call security engineer (24/7 through the MDR provider) assigns a severity within 30 minutes.
3. **Contain.** Follow the runbooks for account takeover, data exposure or ransomware. Preserve logs as evidence.
4. **Notify.**
   - Legal notifies affected bank clients according to the table above.
   - The DPO assesses whether the GDPR 72-hour notification to the CNPD applies.
5. **Recover.** Restore from backup if needed (control 8.13, tested quarterly in CT-02).
6. **Learn.** Hold a blameless post-incident review within 10 business days. Actions go into the risk register.

## Contacts

| Role | Contact |
|---|---|
| Incident commander | CISO, deputy CTO |
| Legal and customer notice | Legal & Compliance |
| Data protection | DPO |
| Authorities | CNPD (data protection), CIRCL (national CERT); CSSF through bank clients where relevant |
