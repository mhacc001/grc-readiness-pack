# Third-Party Risk Scorecard: Ledgerly

Inherent risk (0-80) measures what the vendor touches: data sensitivity, whether it supports a critical function, and data location. Control strength (0-100) measures what the vendor proves: certification, breach notice, MFA, encryption, pen testing, and the DORA Art 30 contract terms.

| Vendor | Service | Tier | Inherent | Control strength | Decision | Gaps |
|---|---|---|---|---|---|---|
| AWS | Cloud hosting (production) | Tier 1 (critical) | 70 | 100 | Approve | none |
| Okta | Identity provider | Tier 1 (critical) | 55 | 100 | Approve | none |
| Zendesk | Customer support tickets | Tier 2 | 35 | 85 | Approve with remediation plan | No audit right in contract (DORA Art 30(2)); No exit or transition plan (DORA Art 30(2)) |
| Datadog | Logs and monitoring | Tier 2 | 35 | 90 | Approve with remediation plan | No audit right in contract (DORA Art 30(2)) |
| GitHub | Source code hosting | Tier 2 | 35 | 100 | Approve | none |
| PayFlow HR | Payroll (fictional) | Tier 2 | 25 | 20 | Escalate: restrict data or replace | No SOC 2 or ISO 27001 report; Breach notice not specified (policy requires 72h or less); No sub-processor list; MFA not enforced; No penetration test in 12 months; No exit or transition plan (DORA Art 30(2)) |
| NorthQA Labs | Outsourced QA testing (fictional) | Tier 3 | 20 | 15 | Remediate within 90 days or replace | No SOC 2 or ISO 27001 report; Breach notice 168h (policy requires 72h or less); No sub-processor list; No encryption at rest; No penetration test in 12 months; No audit right in contract (DORA Art 30(2)); No exit or transition plan (DORA Art 30(2)) |
