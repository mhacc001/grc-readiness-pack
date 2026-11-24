# POL-03 Supplier Security Policy

| Owner | Approved by | Version | Effective | Next review |
|---|---|---|---|---|
| Legal & Compliance | CEO | 1.0 | 2026-11-01 | 2027-11-01 |

Annex A: 5.19 to 5.23, 8.30. SOC 2: CC9.2. DORA: Art 28 to 30.

## Why this matters for Ledgerly

Our customers are EU banks. Under DORA, every bank keeps a register of its ICT third-party providers. Each bank must have specific contract terms with them (Art 30), including:
- audit and access rights
- incident assistance
- exit strategies
- location of data and services

Ledgerly is one of those providers. We flow the same expectations down to the suppliers that support our service. Otherwise we cannot honour our own contracts.

## Tiering

Each supplier gets an **inherent risk score (0-80)**:
- data sensitivity: Restricted 40, Confidential 25, Internal 10
- whether it supports a critical function: +30
- data outside the EU: +10, because a GDPR transfer mechanism is needed

| Tier | Inherent score | Review cycle |
|---|---|---|
| Tier 1 (critical) | 55 or more | Annual reassessment plus continuous monitoring |
| Tier 2 | 25 to 54 | Annual reassessment |
| Tier 3 | below 25 | Every two years |

## Required evidence and contract terms

Each supplier also gets a **control strength score (0-100)**. Points come from:
- an independent report (SOC 2 Type II or ISO 27001 certificate)
- breach notification within 72 hours
- a sub-processor list
- enforced MFA
- encryption at rest
- a penetration test in the last 12 months
- an **audit right** and an **exit plan** in the contract (DORA Art 30(2))

## Decisions

- **No gaps:** approve.
- **Gaps but control strength of 60 or more:** approve with a dated remediation plan.
- **Control strength below 60:**
  - Tier 1 and Tier 2 suppliers are escalated to the CISO, who restricts data or replaces the supplier.
  - Tier 3 suppliers must remediate within 90 days or be replaced.

The current scorecard is in `reports/vendor-scorecard.md`.
