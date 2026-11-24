# POL-02 Access Control Policy

| Owner | Approved by | Version | Effective | Next review |
|---|---|---|---|---|
| CISO | CEO | 1.0 | 2026-11-01 | 2027-11-01 |

Annex A: 5.15, 5.16, 5.17, 5.18, 8.2, 8.3, 8.5. SOC 2: CC6.1, CC6.2, CC6.3. DORA: Art 9(4)(c) and (d).

## Rules

1. **Single identity.** Okta is the only identity source. Every application uses SSO where it supports it.
2. **HR drives the lifecycle.**
   - **Joiners** get birthright and role access from their HR record.
   - **Movers** lose old role access when their role changes.
   - **Leavers** lose all access by the **next business day** after termination.
3. **Least privilege.** Access is granted to roles (groups), not to individuals. Deny by default.
4. **Privileged access.**
   - Production and cloud admin rights are **just-in-time**, approved per request and time-limited.
   - There are no standing admin accounts except two sealed break-glass accounts.
   - Every use of a break-glass account is reviewed.
5. **Authentication.**
   - MFA for every user.
   - **Phishing-resistant MFA (WebAuthn security key or platform authenticator) for every administrator.**
   - Passwords are at least 14 characters where passwordless is not available.
6. **Separation of duties.** Nobody can both write and approve the same production change, or both create a vendor and approve payment to it.
7. **Access reviews.**
   - Managers certify their team's access every quarter.
   - Privileged access is reviewed every month.
   - The IAM team removes rejected access within 5 business days.
   - The review is kept as audit evidence.

## Monitoring

Control test **CT-01** checks leaver timing and **CT-03** checks MFA (see `reports/control-testing.md`). The Q4 2026 tests found:
- one AWS removal 3 business days late, because that user still had access outside SSO
- one administrator without a phishing-resistant factor

Both are tracked to closure in the gap plan.
