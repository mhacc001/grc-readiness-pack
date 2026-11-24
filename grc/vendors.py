"""Third-party risk scorecard: inherent risk (what the vendor touches) vs control strength (what it proves).

Tiering follows the Supplier Security Policy (docs/policies/03-supplier-security-policy.md).
DORA Art. 30 lists contract terms that bank clients must have with ICT providers, and Ledgerly flows
the same terms down to its own critical suppliers. Missing audit rights or exit plans become findings.
"""

import csv
from pathlib import Path

DATA_WEIGHT = {"Restricted": 40, "Confidential": 25, "Internal": 10, "Public": 0}


def inherent_risk(v) -> int:
    score = DATA_WEIGHT[v["data_access"]]
    score += 30 if v["supports_critical_function"] == "Yes" else 0
    score += 10 if v["data_location"] not in ("EU",) else 0  # GDPR transfer mechanism needed
    return score  # 0-80


def control_strength(v) -> tuple[int, list[str]]:
    pts, gaps = 0, []

    def check(ok, points, gap):
        nonlocal pts
        if ok:
            pts += points
        else:
            gaps.append(gap)

    certs = v["certification"]
    check(certs != "None", 25, "No SOC 2 or ISO 27001 report")
    hours = v["breach_notice_hours"]
    check(hours.isdigit() and int(hours) <= 72, 15,
          f"Breach notice {'not specified' if not hours.isdigit() else hours + 'h'} (policy requires 72h or less)")
    check(v["subprocessor_list"] == "Yes", 10, "No sub-processor list")
    check(v["mfa_enforced"] == "Yes", 15, "MFA not enforced")
    check(v["encryption_at_rest"] == "Yes", 10, "No encryption at rest")
    check(v["pentest_last_12m"] == "Yes", 10, "No penetration test in 12 months")
    check(v["contract_audit_right"] == "Yes", 10, "No audit right in contract (DORA Art 30(2))")
    check(v["contract_exit_plan"] == "Yes", 5, "No exit or transition plan (DORA Art 30(2))")
    return pts, gaps  # 0-100


def assess(path: Path) -> list[dict]:
    out = []
    for v in csv.DictReader(open(path, newline="")):
        inh = inherent_risk(v)
        strength, gaps = control_strength(v)
        tier = "Tier 1 (critical)" if inh >= 55 else "Tier 2" if inh >= 25 else "Tier 3"
        if not gaps:
            decision = "Approve"
        elif strength >= 60:
            decision = "Approve with remediation plan"
        elif inh >= 25:
            decision = "Escalate: restrict data or replace"
        else:
            decision = "Remediate within 90 days or replace"
        out.append({**v, "inherent": inh, "strength": strength, "gaps": gaps, "tier": tier, "decision": decision,
                    "review_cycle": "Annual + continuous monitoring" if tier.startswith("Tier 1") else
                    "Annual" if tier == "Tier 2" else "Every 2 years"})
    return sorted(out, key=lambda x: (-x["inherent"], x["strength"]))


def report_md(rows) -> str:
    lines = ["# Third-Party Risk Scorecard: Ledgerly", "",
             "Inherent risk (0-80) measures what the vendor touches: data sensitivity, whether it supports a critical "
             "function, and data location. Control strength (0-100) measures what the vendor proves: certification, "
             "breach notice, MFA, encryption, pen testing, and the DORA Art 30 contract terms.", "",
             "| Vendor | Service | Tier | Inherent | Control strength | Decision | Gaps |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        gaps = "; ".join(r["gaps"]) or "none"
        lines.append(f"| {r['vendor']} | {r['service']} | {r['tier']} | {r['inherent']} | {r['strength']} | {r['decision']} | {gaps} |")
    return "\n".join(lines) + "\n"
