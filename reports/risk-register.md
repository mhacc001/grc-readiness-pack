# Risk Register: Ledgerly

Method: likelihood (1-5) x impact (1-5). Appetite: **Low 1-6** accept, **Medium 7-12** treat within 90 days, **High 13-25** treat immediately.

| ID | Risk | Inherent | Controls (Annex A) | Residual | Owner | Status |
|---|---|---|---|---|---|---|
| R01 | Customer financial data exposed through a tenant isolation flaw | 15 High | 8.3, 8.25, 8.29, 8.26 | 10 Medium | CTO | Open: pen test retest due Q1 2027 |
| R02 | Admin account takeover through phishing | 20 High | 5.17, 8.5, 8.2, 6.3 | 8 Medium | CISO | Open: 2 standing admin accounts to remove |
| R03 | Ransomware on employee laptops spreads to shared drives | 12 Medium | 8.1, 8.7, 8.23, 8.13 | 6 Low | IT Operations | Accepted at residual |
| R04 | Leaver keeps access after departure | 12 Medium | 5.16, 5.18, 6.5 | 6 Low | IT Operations | Open: CT-01 found one late removal |
| R05 | Critical vendor outage stops the service | 10 Medium | 5.23, 5.30, 8.14, 5.22 | 8 Medium | CTO | Open: region failover not yet tested |
| R06 | Vendor breach exposes Ledgerly data | 12 Medium | 5.19, 5.20, 5.22, 8.11 | 8 Medium | Legal & Compliance | Open: 2 contracts lack audit clauses |
| R07 | High-severity vulnerability exploited before patching | 16 High | 8.8, 8.9, 8.20 | 9 Medium | CISO | Open: CT-04 found 2 overdue highs |
| R08 | Production data copied into test or analytics | 12 Medium | 8.11, 8.33, 8.31 | 6 Low | CTO | Open: one export still unmasked |
| R09 | Major incident not reported to bank clients in time | 10 Medium | 5.24, 5.25, 5.26, 8.16 | 4 Low | CISO | Accepted at residual |
| R10 | Backups cannot be restored when needed | 10 Medium | 8.13, 5.30 | 4 Low | IT Operations | Accepted at residual |
| R11 | Data sent outside the EU without a valid transfer basis | 9 Medium | 5.34, 5.19, 5.31 | 4 Low | Legal & Compliance | Accepted at residual |
| R12 | Insecure code from the outsourced QA contractor | 6 Low | 8.30, 8.28, 8.4 | 4 Low | CTO | Open: secure-coding clause to add |

Residual risks still above appetite: **R01, R02, R05, R06, R07**.
