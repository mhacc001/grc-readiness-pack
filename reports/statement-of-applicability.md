# Statement of Applicability: Ledgerly ISMS

Standard: ISO/IEC 27001:2022, Annex A (93 controls). Scope: the Ledgerly reconciliation platform, its AWS production environment, corporate IT and the Luxembourg office.

- Applicable: **91 of 93**. Excluded: 7.6 Working in secure areas (No secure areas: production runs only in AWS and no restricted rooms exist on site); 7.12 Cabling security (Building cabling is owned and secured by the landlord; Ledgerly runs no cabling of its own)
- Status: Implemented 75, Partial 14, Planned 2, Not applicable 2
- Readiness score: **90.1%** (Implemented = 1, Partial = 0.5, Planned = 0)

| Control | Title | Applicable | Status | Owner | Justification | Evidence | SOC 2 | DORA |
|---|---|---|---|---|---|---|---|---|
| 5.1 | Policies for information security | Yes | Implemented | CISO | Information Security Policy approved by the CEO, reviewed annually | POL-01 | CC5.3; CC1.1 | Art 5, Art 6(2) |
| 5.2 | Information security roles and responsibilities | Yes | Implemented | CISO | RACI in the ISMS manual; CISO reports to the CEO | ISMS-RACI | CC1.3 | Art 5(2) |
| 5.3 | Segregation of duties | Yes | Partial | CISO | Production deploy and approval are split in CI; finance SoD review not yet formalised | EV-CI-APPROVALS | CC5.1 | Art 9(4)(c) |
| 5.4 | Management responsibilities | Yes | Implemented | CEO | Leadership signs the policy and attends the quarterly security review | EV-MGMT-REVIEW | CC1.1; CC1.2 | Art 5(2) |
| 5.5 | Contact with authorities | Yes | Implemented | Legal & Compliance | Contacts listed for CNPD (GDPR), CSSF and CIRCL for incident escalation | IRP-01 | CC2.3 | Art 14, Art 19 |
| 5.6 | Contact with special interest groups | Yes | Implemented | CISO | Member of a national security information-sharing community; follows ENISA and CIRCL advisories | EV-ISAC | CC2.3 | Art 45 |
| 5.7 | Threat intelligence | Yes | Partial | CISO | Advisory feeds reviewed weekly; no formal threat-intel reporting yet | EV-TI-LOG | CC3.2; CC7.1 | Art 13(1) |
| 5.8 | Information security in project management | Yes | Implemented | CTO | Security review gate in the product delivery checklist | EV-PDLC | CC3.4 | Art 8(3) |
| 5.9 | Inventory of information and other associated assets | Yes | Implemented | IT Operations | Asset inventory generated from AWS Config and the MDM tool, owners assigned | EV-ASSET-INV | CC6.1 | Art 8(1), Art 8(4) |
| 5.10 | Acceptable use of information and other associated assets | Yes | Implemented | People Lead | Acceptable use policy signed at onboarding | POL-01 | CC1.4; CC2.2 | Art 9(4) |
| 5.11 | Return of assets | Yes | Implemented | People Lead | Offboarding checklist includes laptop return and MDM wipe | EV-OFFBOARD | CC6.5 | Art 9(4) |
| 5.12 | Classification of information | Yes | Implemented | CISO | Four levels: Public, Internal, Confidential, Restricted (customer financial data) | POL-01 | CC6.1; C1.1 | Art 8(1) |
| 5.13 | Labelling of information | Yes | Partial | CISO | Labels applied to documents in the drive; database fields not yet tagged | EV-LABELS | C1.1 | Art 8(1) |
| 5.14 | Information transfer | Yes | Implemented | CISO | TLS 1.2+ for all transfers; SFTP with key auth for bank file exchange | EV-TLS-SCAN | CC6.7 | Art 9(4)(a) |
| 5.15 | Access control | Yes | Implemented | CISO | Access Control Policy: least privilege, role-based, deny by default | POL-02 | CC6.1; CC6.3 | Art 9(4)(c) |
| 5.16 | Identity management | Yes | Implemented | IT Operations | Okta is the single identity source; HR-driven joiner-mover-leaver | EV-JML | CC6.2 | Art 9(4)(c) |
| 5.17 | Authentication information | Yes | Implemented | IT Operations | Passwordless or 14+ character passwords, phishing-resistant MFA for admins | POL-02 | CC6.1 | Art 9(4)(d) |
| 5.18 | Access rights | Yes | Partial | CISO | Quarterly access reviews run; Q3 review found 1 late removal (see control test CT-01) | CT-01 | CC6.2; CC6.3 | Art 9(4)(c) |
| 5.19 | Information security in supplier relationships | Yes | Implemented | Legal & Compliance | Supplier Security Policy with risk tiers | POL-03 | CC9.2 | Art 28(1) |
| 5.20 | Addressing information security within supplier agreements | Yes | Partial | Legal & Compliance | Standard security addendum exists; 4 supplier contracts lack DORA Art 30 audit or exit clauses (see vendor scorecard) | EV-VENDOR-REVIEW | CC9.2 | Art 30(2) |
| 5.21 | Managing information security in the ICT supply chain | Yes | Partial | CTO | Dependency scanning in CI; no SBOM shared with customers yet | EV-SCA | CC9.2; CC8.1 | Art 28(3) |
| 5.22 | Monitoring, review and change management of supplier services | Yes | Implemented | Legal & Compliance | Annual vendor reassessment, tiered by risk score | EV-VENDOR-REVIEW | CC9.2 | Art 28(6) |
| 5.23 | Information security for use of cloud services | Yes | Implemented | CTO | AWS shared-responsibility matrix documented; AWS SOC 2 report reviewed yearly | EV-AWS-SOC2 | CC9.2; CC6.6 | Art 28(2) |
| 5.24 | Information security incident management planning and preparation | Yes | Implemented | CISO | Incident Response Plan with roles, severities and contact tree | IRP-01 | CC7.3 | Art 17(1) |
| 5.25 | Assessment and decision on information security events | Yes | Implemented | CISO | Severity matrix aligned to DORA major-incident criteria | IRP-01 | CC7.3; CC7.4 | Art 18 |
| 5.26 | Response to information security incidents | Yes | Implemented | CISO | Runbooks for account takeover, data exposure and ransomware | IRP-01 | CC7.4 | Art 17(3), Art 11 |
| 5.27 | Learning from information security incidents | Yes | Implemented | CISO | Blameless post-incident review within 10 business days | IRP-01 | CC7.5 | Art 13 |
| 5.28 | Collection of evidence | Yes | Partial | CISO | Log retention covers evidence; formal chain-of-custody form not yet adopted | IRP-01 | CC7.4 | Art 17(3) |
| 5.29 | Information security during disruption | Yes | Implemented | IT Operations | Security controls stay active in the disaster recovery region | EV-DR-TEST | A1.2 | Art 11(1) |
| 5.30 | ICT readiness for business continuity | Yes | Partial | IT Operations | Multi-AZ production and a tested restore; full region failover not yet exercised | CT-02 | A1.2; A1.3 | Art 11(2), Art 12 |
| 5.31 | Legal, statutory, regulatory and contractual requirements | Yes | Implemented | Legal & Compliance | Register of obligations: GDPR, DORA flow-down from bank clients, contracts | EV-OBLIGATIONS | CC2.3; P1.1 | Art 30 |
| 5.32 | Intellectual property rights | Yes | Implemented | Legal & Compliance | Open-source licence scan in CI; licensed software tracked | EV-SCA | CC1.4 | n/a |
| 5.33 | Protection of records | Yes | Implemented | Legal & Compliance | Retention schedule; audit logs immutable for 12 months | EV-RETENTION | CC7.2; C1.2 | Art 12 |
| 5.34 | Privacy and protection of PII | Yes | Implemented | Legal & Compliance | GDPR record of processing, DPIA for the reconciliation engine, DPO appointed | EV-ROPA | P1.1; C1.1 | n/a (GDPR) |
| 5.35 | Independent review of information security | Yes | Planned | CISO | First external ISO 27001 readiness audit booked for Q2 2027 | EV-AUDIT-PLAN | CC4.1 | Art 6(6) |
| 5.36 | Compliance with policies, rules and standards for information security | Yes | Implemented | CISO | Quarterly internal control testing (see control tests) | CT-01..CT-04 | CC4.1; CC4.2 | Art 6(6) |
| 5.37 | Documented operating procedures | Yes | Implemented | IT Operations | Runbooks in the engineering wiki, reviewed with each change | EV-RUNBOOKS | CC5.3 | Art 9(4) |
| 6.1 | Screening | Yes | Implemented | People Lead | Background and reference checks for all hires, criminal record extract for production access | EV-HR-SCREEN | CC1.4 | Art 9(4) |
| 6.2 | Terms and conditions of employment | Yes | Implemented | People Lead | Security obligations in employment contracts | EV-HR-CONTRACT | CC1.4 | Art 9(4) |
| 6.3 | Information security awareness, education and training | Yes | Partial | People Lead | Annual training 94% complete; phishing simulations quarterly | EV-TRAINING | CC1.4; CC2.2 | Art 13(6) |
| 6.4 | Disciplinary process | Yes | Implemented | People Lead | Disciplinary process references security policy breaches | EV-HR-HANDBOOK | CC1.5 | n/a |
| 6.5 | Responsibilities after termination or change of employment | Yes | Implemented | People Lead | Confidentiality survives termination; access removed same day | EV-OFFBOARD | CC6.2 | Art 9(4)(c) |
| 6.6 | Confidentiality or non-disclosure agreements | Yes | Implemented | Legal & Compliance | NDA for staff, contractors and suppliers | EV-NDA | C1.1 | Art 30(2) |
| 6.7 | Remote working | Yes | Implemented | CISO | Remote-first: managed laptops, disk encryption, MFA, no split tunnelling to admin tools | POL-01 | CC6.1; CC6.7 | Art 9(4) |
| 6.8 | Information security event reporting | Yes | Implemented | CISO | One-click report button and a #security-report channel | IRP-01 | CC2.2; CC7.3 | Art 17(2) |
| 7.1 | Physical security perimeters | Yes | Implemented | IT Operations | Luxembourg office in a badge-controlled building; data centres inherited from AWS | EV-AWS-SOC2 | CC6.4 | Art 9 |
| 7.2 | Physical entry | Yes | Implemented | IT Operations | Badge entry and visitor log at the office | EV-OFFICE | CC6.4 | Art 9 |
| 7.3 | Securing offices, rooms and facilities | Yes | Implemented | IT Operations | No servers on premises; network cabinet locked | EV-OFFICE | CC6.4 | Art 9 |
| 7.4 | Physical security monitoring | Yes | Implemented | IT Operations | Building CCTV run by the landlord; AWS facilities inherited | EV-AWS-SOC2 | CC6.4 | Art 9 |
| 7.5 | Protecting against physical and environmental threats | Yes | Implemented | IT Operations | Inherited from AWS for production; office covered by building systems | EV-AWS-SOC2 | A1.2 | Art 11 |
| 7.6 | Working in secure areas | No | Not applicable | IT Operations | No secure areas: production runs only in AWS and no restricted rooms exist on site | n/a | n/a | n/a |
| 7.7 | Clear desk and clear screen | Yes | Implemented | People Lead | Auto screen lock at 5 minutes enforced by MDM | EV-MDM | CC6.1 | Art 9 |
| 7.8 | Equipment siting and protection | Yes | Implemented | IT Operations | Office network gear in a locked cabinet | EV-OFFICE | CC6.4 | Art 9 |
| 7.9 | Security of assets off-premises | Yes | Implemented | IT Operations | Laptops encrypted and remotely wipeable | EV-MDM | CC6.4; CC6.7 | Art 9 |
| 7.10 | Storage media | Yes | Implemented | IT Operations | USB storage blocked by MDM; no removable media in use | EV-MDM | CC6.7 | Art 9 |
| 7.11 | Supporting utilities | Yes | Implemented | IT Operations | Inherited from AWS for production | EV-AWS-SOC2 | A1.2 | Art 11 |
| 7.12 | Cabling security | No | Not applicable | IT Operations | Building cabling is owned and secured by the landlord; Ledgerly runs no cabling of its own | n/a | n/a | n/a |
| 7.13 | Equipment maintenance | Yes | Implemented | IT Operations | Laptops under vendor warranty; OS updates enforced by MDM | EV-MDM | A1.2 | Art 9 |
| 7.14 | Secure disposal or re-use of equipment | Yes | Implemented | IT Operations | Certified wipe before re-use or disposal, certificate kept | EV-DISPOSAL | CC6.5 | Art 9 |
| 8.1 | User endpoint devices | Yes | Implemented | IT Operations | All laptops enrolled in MDM with encryption, firewall and EDR | EV-MDM | CC6.8 | Art 9(2) |
| 8.2 | Privileged access rights | Yes | Partial | CISO | Just-in-time AWS admin via SSO; 2 standing admin accounts still being removed | CT-01 | CC6.1; CC6.3 | Art 9(4)(c) |
| 8.3 | Information access restriction | Yes | Implemented | CTO | Tenant isolation enforced in the application and database row-level security | EV-PENTEST | CC6.1 | Art 9(4)(c) |
| 8.4 | Access to source code | Yes | Implemented | CTO | GitHub with SSO, branch protection and required reviews | EV-CI-APPROVALS | CC6.1; CC8.1 | Art 9(4)(c) |
| 8.5 | Secure authentication | Yes | Implemented | IT Operations | Okta MFA for all users; WebAuthn required for administrators | CT-03 | CC6.1 | Art 9(4)(d) |
| 8.6 | Capacity management | Yes | Implemented | IT Operations | Autoscaling with capacity alerts | EV-MONITORING | A1.1 | Art 9(1) |
| 8.7 | Protection against malware | Yes | Implemented | IT Operations | EDR on every endpoint, malware scanning of uploaded files | EV-MDM | CC6.8 | Art 9(2) |
| 8.8 | Management of technical vulnerabilities | Yes | Partial | CISO | Weekly scanning with SLAs; 2 high findings past SLA (see control test CT-04) | CT-04 | CC7.1 | Art 9(4)(f), Art 10 |
| 8.9 | Configuration management | Yes | Implemented | IT Operations | Infrastructure as code (Terraform) with drift detection | EV-IAC | CC7.1; CC8.1 | Art 9(4)(e) |
| 8.10 | Information deletion | Yes | Implemented | Legal & Compliance | Customer data deleted 90 days after contract end, with certificate | EV-RETENTION | C1.2; CC6.5 | Art 12 |
| 8.11 | Data masking | Yes | Partial | CTO | Masked datasets in staging; one analytics export still unmasked | EV-MASKING | C1.1 | Art 9(4) |
| 8.12 | Data leakage prevention | Yes | Planned | CISO | DLP for email and drive planned for Q1 2027 | EV-ROADMAP | CC6.7 | Art 9(4) |
| 8.13 | Information backup | Yes | Implemented | IT Operations | Encrypted daily backups, cross-region copy, quarterly restore test | CT-02 | A1.2 | Art 12 |
| 8.14 | Redundancy of information processing facilities | Yes | Implemented | IT Operations | Multi-AZ databases and load-balanced services | EV-ARCH | A1.2 | Art 11, Art 12 |
| 8.15 | Logging | Yes | Implemented | IT Operations | Central logging with 12-month retention, immutable audit trail | EV-LOGGING | CC7.2 | Art 10 |
| 8.16 | Monitoring activities | Yes | Implemented | CISO | SIEM alerts triaged 24/7 by an MDR provider | EV-MONITORING | CC7.2; CC7.3 | Art 10 |
| 8.17 | Clock synchronization | Yes | Implemented | IT Operations | AWS time sync on all hosts | EV-IAC | CC7.2 | Art 10 |
| 8.18 | Use of privileged utility programs | Yes | Implemented | IT Operations | No SSH to production; break-glass access logged and reviewed | EV-BREAKGLASS | CC6.1 | Art 9(4)(c) |
| 8.19 | Installation of software on operational systems | Yes | Implemented | IT Operations | Immutable container images built in CI only | EV-IAC | CC8.1 | Art 9(4)(e) |
| 8.20 | Networks security | Yes | Implemented | IT Operations | Private subnets, security groups as code, WAF in front of the app | EV-IAC | CC6.6 | Art 9(4)(a) |
| 8.21 | Security of network services | Yes | Implemented | IT Operations | Managed AWS network services with TLS everywhere | EV-TLS-SCAN | CC6.6 | Art 9(4)(a) |
| 8.22 | Segregation of networks | Yes | Implemented | IT Operations | Separate VPCs and accounts for production, staging and corporate | EV-ARCH | CC6.6 | Art 9(4)(a) |
| 8.23 | Web filtering | Yes | Implemented | IT Operations | DNS filtering on managed laptops | EV-MDM | CC6.8 | Art 9(2) |
| 8.24 | Use of cryptography | Yes | Implemented | CTO | AES-256 at rest with KMS, TLS 1.2+ in transit, key rotation yearly | EV-KMS | CC6.1; CC6.7 | Art 9(4)(d) |
| 8.25 | Secure development life cycle | Yes | Implemented | CTO | Threat modelling for new features, security review gate | EV-PDLC | CC8.1 | Art 9(4)(e) |
| 8.26 | Application security requirements | Yes | Implemented | CTO | OWASP ASVS level 2 used as the requirement baseline | EV-PDLC | CC8.1 | Art 9(4)(e) |
| 8.27 | Secure system architecture and engineering principles | Yes | Implemented | CTO | Architecture principles documented and reviewed yearly | EV-ARCH | CC8.1 | Art 9(4)(e) |
| 8.28 | Secure coding | Yes | Implemented | CTO | SAST, secret scanning and dependency scanning block merges | EV-SCA | CC8.1 | Art 9(4)(e) |
| 8.29 | Security testing in development and acceptance | Yes | Implemented | CTO | Annual external penetration test plus DAST in staging | EV-PENTEST | CC8.1; CC4.1 | Art 24, Art 25 |
| 8.30 | Outsourced development | Yes | Partial | CTO | Offshore QA contractor under NDA; secure-coding clause missing from contract | EV-VENDOR-REVIEW | CC9.2; CC8.1 | Art 30(2) |
| 8.31 | Separation of development, test and production environments | Yes | Implemented | CTO | Separate AWS accounts; no production data in development | EV-ARCH | CC8.1 | Art 9(4)(e) |
| 8.32 | Change management | Yes | Implemented | CTO | Pull request review, CI checks and approval before production deploy | EV-CI-APPROVALS | CC8.1 | Art 9(4)(e) |
| 8.33 | Test information | Yes | Partial | CTO | Synthetic data for tests; one analytics export still contains real data | EV-MASKING | C1.1 | Art 9(4) |
| 8.34 | Protection of information systems during audit testing | Yes | Implemented | CISO | Audit and pen-test activity scheduled, scoped and approved in writing | EV-PENTEST | CC4.1 | Art 24 |
