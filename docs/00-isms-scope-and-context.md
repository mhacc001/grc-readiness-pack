# ISMS Scope and Context (ISO/IEC 27001:2022 clauses 4.1 to 4.3)

## The organisation (fictional)

**Ledgerly S.A.** is a 60-person software company in Luxembourg. Its SaaS platform matches bank transaction files against corporate invoices. Customers are EU banks and their corporate clients. Production runs on AWS (eu-central-1 and eu-west-1). The company is remote-first, with a small office in Luxembourg City.

## Internal and external issues (4.1)

| Issue | Effect on the ISMS |
|---|---|
| Customers are banks subject to **DORA** (applies from 17 January 2025) | Banks must manage ICT third-party risk. They will audit Ledgerly, require DORA Art 30 contract terms, and need fast incident notice. |
| Customer data is financial and personal | GDPR applies. Restricted classification. |
| Remote-first workforce | Controls must be identity- and device-based, not office-based. |
| Small team, cloud-only | Physical data-centre controls are inherited from AWS and evidenced by its SOC 2 report. |
| Sales cycle requires SOC 2 Type II and ISO 27001 | One control set, mapped to both frameworks. |

## Interested parties (4.2)

| Party | Requirement |
|---|---|
| Bank customers | DORA contract terms, audit rights, 4-hour incident notice, SOC 2 or ISO 27001 report |
| Corporate end users | Availability, data confidentiality |
| CNPD (data protection authority) | GDPR compliance, breach notification within 72 hours |
| Employees | Clear policies, privacy at work |
| Investors | No breach-driven loss of customers |

## Scope statement (4.3)

> The ISMS covers the design, development, operation and support of the Ledgerly reconciliation platform. That includes its AWS production and staging environments, the corporate SaaS tools and managed endpoints used to run it, and the Luxembourg office. AWS data-centre physical controls are out of scope and inherited from AWS, which is reviewed annually as a Tier 1 supplier.

Applicable controls and the reasons for the two exclusions are in the Statement of Applicability (`reports/statement-of-applicability.md`).
