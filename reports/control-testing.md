# Control Testing Results: Ledgerly (2026-11-24)

Each test re-performs the control from the raw evidence in `data/evidence/`.

| Test | Control(s) | SOC 2 | Population | Exceptions | Result |
|---|---|---|---|---|---|
| CT-01 Leaver access removed by the next business day | 5.18, 6.5, 5.16 | CC6.2 | 6 Q3 leavers x 3 systems | 1 | **Effective with exceptions** |
| CT-02 Quarterly database restore within the 4-hour RTO, with integrity checks | 8.13, 5.30 | A1.2, A1.3 | 4 quarterly restore tests (2026) | 0 | **Effective** |
| CT-03 MFA for all users and phishing-resistant MFA (WebAuthn) for administrators | 8.5, 5.17 | CC6.1 | 61 users, 5 admins | 1 | **Effective with exceptions** |
| CT-04 Vulnerabilities remediated within SLA (Critical 7d, High 30d, Medium 90d, Low 180d) | 8.8 | CC7.1 | 10 findings (Sept to Nov 2026) | 2 | **Effective with exceptions** |

## CT-01: Leaver access removed by the next business day

- Exception: r.diallo: aws access removed on 2026-09-03 (3 business days after the 2026-08-31 deadline)

Conclusion: Okta and GitHub removals were on time. One AWS removal was late because AWS access was still granted outside SSO. Remediation: move the last AWS users to SSO-only access (R04).

## CT-02: Quarterly database restore within the 4-hour RTO, with integrity checks

- No exceptions.

Conclusion: All restores finished inside the RTO (slowest 131 min of 240) with matching row counts and checksums. Scope gap: a full region failover has not been exercised, so 5.30 stays Partial.

## CT-03: MFA for all users and phishing-resistant MFA (WebAuthn) for administrators

- Exception: s.ahmed (Org Admin) has no phishing-resistant factor (only okta_verify)

Conclusion: Every user has MFA. One administrator relies on push MFA only, which phishing kits can bypass. Remediation: enrol a security key and block admin sign-in without WebAuthn (R02).

## CT-04: Vulnerabilities remediated within SLA (Critical 7d, High 30d, Medium 90d, Low 180d)

- Exception: V-205 High on reporting-svc: open and overdue, 54 days vs 30-day SLA
- Exception: V-206 High on bastion-ami: open and overdue, 48 days vs 30-day SLA

Conclusion: 8 of 10 findings met the SLA, including both criticals. Two high findings on internal services are overdue. Remediation: patch by 2026-12-05, add an SLA breach alert (R07).
