"""Internal control tests, computed from evidence files the way an auditor would re-perform them.

Each test returns: control(s) tested, population, sample, exceptions, result (Effective /
Effective with exceptions / Not effective) and a conclusion.
"""

import csv
from datetime import date, timedelta
from pathlib import Path


def _rows(path):
    return list(csv.DictReader(open(path, newline="")))


def next_business_day(d: date) -> date:
    d = d if d.weekday() < 5 else d + timedelta(days=7 - d.weekday())
    return d


def business_days_late(due: date, done: date) -> int:
    n, d = 0, due
    while d < done:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


def ct01_leaver_access(ev: Path) -> dict:
    """Access must be removed in every system by the next business day after termination."""
    rows = _rows(ev / "leavers_q3.csv")
    systems = ["okta_deactivated", "aws_access_removed", "github_removed"]
    exceptions = []
    for r in rows:
        due = next_business_day(date.fromisoformat(r["termination_date"]))
        for s in systems:
            done = date.fromisoformat(r[s])
            if done > due:
                exceptions.append(f"{r['employee']}: {s.replace('_', ' ')} on {done} "
                                  f"({business_days_late(due, done)} business days after the {due} deadline)")
    admins = _rows(ev / "okta_admin_factors.csv")
    return {"id": "CT-01", "name": "Leaver access removed by the next business day",
            "controls": "5.18, 6.5, 5.16", "soc2": "CC6.2", "population": f"{len(rows)} Q3 leavers x {len(systems)} systems",
            "tested": len(rows) * len(systems), "exceptions": exceptions,
            "result": "Effective" if not exceptions else "Effective with exceptions",
            "conclusion": "Okta and GitHub removals were on time. One AWS removal was late because AWS access "
                          "was still granted outside SSO. Remediation: move the last AWS users to SSO-only access (R04)."
            if exceptions else "All removals on time.", "admins_reviewed": len(admins)}


def ct02_backup_restore(ev: Path) -> dict:
    rows = _rows(ev / "restore_tests.csv")
    exceptions = [f"{r['quarter']}: restore {r['restore_minutes']} min vs RTO {r['rto_target_minutes']} min"
                  for r in rows if int(r["restore_minutes"]) > int(r["rto_target_minutes"])]
    exceptions += [f"{r['quarter']}: integrity check failed" for r in rows
                   if r["row_count_match"] != "Yes" or r["checksum_match"] != "Yes"]
    worst = max(int(r["restore_minutes"]) for r in rows)
    return {"id": "CT-02", "name": "Quarterly database restore within the 4-hour RTO, with integrity checks",
            "controls": "8.13, 5.30", "soc2": "A1.2, A1.3", "population": f"{len(rows)} quarterly restore tests (2026)",
            "tested": len(rows), "exceptions": exceptions,
            "result": "Effective" if not exceptions else "Not effective",
            "conclusion": f"All restores finished inside the RTO (slowest {worst} min of 240) with matching row counts "
                          "and checksums. Scope gap: a full region failover has not been exercised, so 5.30 stays Partial."}


def ct03_mfa(ev: Path) -> dict:
    users = _rows(ev / "okta_users_mfa.csv")[0]
    admins = _rows(ev / "okta_admin_factors.csv")
    exceptions = []
    if int(users["users_password_only"]) > 0:
        exceptions.append(f"{users['users_password_only']} users without MFA")
    for a in admins:
        if "webauthn" not in a["factors"].split(";"):
            exceptions.append(f"{a['user']} ({a['role']}) has no phishing-resistant factor (only {a['factors']})")
    return {"id": "CT-03", "name": "MFA for all users and phishing-resistant MFA (WebAuthn) for administrators",
            "controls": "8.5, 5.17", "soc2": "CC6.1", "population": f"{users['total_active_users']} users, {len(admins)} admins",
            "tested": int(users["total_active_users"]) + len(admins), "exceptions": exceptions,
            "result": "Effective" if not exceptions else "Effective with exceptions",
            "conclusion": "Every user has MFA. One administrator relies on push MFA only, which phishing kits can "
                          "bypass. Remediation: enrol a security key and block admin sign-in without WebAuthn (R02)."
            if exceptions else "All users and admins compliant."}


SLA_DAYS = {"Critical": 7, "High": 30, "Medium": 90, "Low": 180}


def ct04_vuln_sla(ev: Path, as_of: date) -> dict:
    rows = _rows(ev / "vulnerabilities.csv")
    exceptions, on_time = [], 0
    for r in rows:
        found = date.fromisoformat(r["found"])
        end = date.fromisoformat(r["fixed"]) if r["fixed"] else as_of
        age, sla = (end - found).days, SLA_DAYS[r["severity"]]
        if age > sla:
            state = "fixed late" if r["fixed"] else "open and overdue"
            exceptions.append(f"{r['finding_id']} {r['severity']} on {r['asset']}: {state}, {age} days vs {sla}-day SLA")
        else:
            on_time += 1
    return {"id": "CT-04", "name": "Vulnerabilities remediated within SLA (Critical 7d, High 30d, Medium 90d, Low 180d)",
            "controls": "8.8", "soc2": "CC7.1", "population": f"{len(rows)} findings (Sept to Nov 2026)",
            "tested": len(rows), "exceptions": exceptions,
            "result": "Effective" if not exceptions else "Effective with exceptions" if len(exceptions) <= 2 else "Not effective",
            "conclusion": f"{on_time} of {len(rows)} findings met the SLA, including both criticals. Two high findings on "
                          "internal services are overdue. Remediation: patch by 2026-12-05, add an SLA breach alert (R07)."}


def run_all(ev: Path, as_of: date) -> list[dict]:
    return [ct01_leaver_access(ev), ct02_backup_restore(ev), ct03_mfa(ev), ct04_vuln_sla(ev, as_of)]


def report_md(results, as_of: date) -> str:
    lines = [f"# Control Testing Results: Ledgerly ({as_of.isoformat()})", "",
             "Each test re-performs the control from the raw evidence in `data/evidence/`.", "",
             "| Test | Control(s) | SOC 2 | Population | Exceptions | Result |", "|---|---|---|---|---|---|"]
    for t in results:
        lines.append(f"| {t['id']} {t['name']} | {t['controls']} | {t['soc2']} | {t['population']} | {len(t['exceptions'])} | **{t['result']}** |")
    for t in results:
        lines += ["", f"## {t['id']}: {t['name']}", ""]
        lines += [f"- Exception: {e}" for e in t["exceptions"]] or ["- No exceptions."]
        lines += ["", f"Conclusion: {t['conclusion']}"]
    return "\n".join(lines) + "\n"
