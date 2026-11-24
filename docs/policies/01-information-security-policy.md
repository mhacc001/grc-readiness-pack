# POL-01 Information Security Policy

| Owner | Approved by | Version | Effective | Next review |
|---|---|---|---|---|
| CISO | CEO | 1.0 | 2026-11-01 | 2027-11-01 |

## 1. Purpose

Ledgerly processes bank reconciliation data for financial institutions in the EU. This policy sets out how we protect the confidentiality, integrity and availability of that data and of the systems that process it. It meets ISO/IEC 27001:2022 clause 5.2 and Annex A 5.1.

## 2. Scope

All employees, contractors and suppliers with access to Ledgerly information. All systems in the ISMS scope: the reconciliation platform, the AWS production environment, corporate SaaS tools, managed laptops and the Luxembourg office.

## 3. Commitments

1. We protect customer financial data as **Restricted**, our highest classification.
2. We manage information security risk with a documented method (likelihood x impact, 5x5) and an approved risk appetite.
3. We give access on a least-privilege, role basis, and we review it every quarter (POL-02).
4. We assess every supplier before onboarding and review them by risk tier (POL-03).
5. We detect, report and learn from incidents, and we notify customers within the timelines our contracts and DORA require (IRP-01).
6. We meet our legal, regulatory and contractual obligations, including GDPR and the DORA requirements our bank clients flow down to us.
7. We continually improve the ISMS through internal control testing, management review and an independent audit.

## 4. Information classification

| Level | Examples | Handling |
|---|---|---|
| Restricted | Customer transaction data, bank files | Encrypted at rest and in transit, production access only through SSO and just-in-time approval |
| Confidential | Contracts, employee data, source code | Need-to-know access, no external sharing without approval |
| Internal | Policies, runbooks | Employees and contractors under NDA |
| Public | Marketing site | No restriction |

## 5. Acceptable use and remote working

Ledgerly is remote-first. Work happens on managed laptops only, with disk encryption, EDR, a screen lock and MFA. Personal devices may not access Restricted or Confidential data. Report lost devices and suspected incidents immediately in #security-report.

## 6. Roles

- **CEO:** approves this policy and the risk appetite, and chairs the quarterly security review.
- **CISO:** owns the ISMS, the risk register and control testing.
- **Control owners:** run their controls and keep the evidence current (see the Statement of Applicability).
- **Everyone:** completes annual training and reports security events.

## 7. Compliance

Breaches of this policy are handled through the disciplinary process. Exceptions need a documented risk acceptance signed by the CISO, with an expiry date.
