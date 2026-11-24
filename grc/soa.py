"""Statement of Applicability (ISO/IEC 27001:2022 clause 6.1.3 d) plus SOC 2 and DORA coverage views."""

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

STATUSES = ["Implemented", "Partial", "Planned", "Not applicable"]


def load(path: Path) -> list[dict]:
    return list(csv.DictReader(open(path, newline="")))


def readiness(controls) -> dict:
    applicable = [c for c in controls if c["applicable"] == "Yes"]
    by_status = Counter(c["status"] for c in controls)
    by_theme = defaultdict(Counter)
    for c in applicable:
        by_theme[c["theme"]][c["status"]] += 1
    # Score: Implemented = 1, Partial = 0.5, Planned = 0
    score = sum({"Implemented": 1, "Partial": 0.5}.get(c["status"], 0) for c in applicable) / len(applicable)
    return {"total": len(controls), "applicable": len(applicable), "by_status": by_status,
            "by_theme": by_theme, "score": round(100 * score, 1),
            "gaps": [c for c in applicable if c["status"] != "Implemented"]}


def coverage(controls, field: str) -> dict:
    """Map each SOC 2 criterion / DORA article to the Annex A controls that support it."""
    cov = defaultdict(list)
    for c in controls:
        if c["applicable"] != "Yes":
            continue
        for ref in re.split(r"[;,]", c[field]):
            ref = ref.strip()
            if ref and not ref.startswith("n/a"):
                cov[ref].append(c)
    return dict(sorted(cov.items(), key=lambda kv: _natural(kv[0])))


def _natural(s):
    import re
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def soa_md(controls, stats) -> str:
    lines = ["# Statement of Applicability: Ledgerly ISMS", "",
             "Standard: ISO/IEC 27001:2022, Annex A (93 controls). Scope: the Ledgerly reconciliation platform, its AWS "
             "production environment, corporate IT and the Luxembourg office.", "",
             f"- Applicable: **{stats['applicable']} of {stats['total']}**. Excluded: "
             + "; ".join(f"{c['control_id']} {c['title']} ({c['justification']})" for c in controls if c["applicable"] == "No"),
             "- Status: " + ", ".join(f"{s} {stats['by_status'][s]}" for s in STATUSES),
             f"- Readiness score: **{stats['score']}%** (Implemented = 1, Partial = 0.5, Planned = 0)", "",
             "| Control | Title | Applicable | Status | Owner | Justification | Evidence | SOC 2 | DORA |",
             "|---|---|---|---|---|---|---|---|---|"]
    for c in controls:
        lines.append(f"| {c['control_id']} | {c['title']} | {c['applicable']} | {c['status']} | {c['owner']} | "
                     f"{c['justification']} | {c['evidence']} | {c['soc2_tsc']} | {c['dora']} |")
    return "\n".join(lines) + "\n"


def gaps_md(stats) -> str:
    lines = ["# Gap Remediation Plan", "", "| Control | Title | Status | Owner | What is missing |", "|---|---|---|---|---|"]
    order = {"Planned": 0, "Partial": 1}
    for c in sorted(stats["gaps"], key=lambda c: (order[c["status"]], _natural(c["control_id"]))):
        lines.append(f"| {c['control_id']} | {c['title']} | {c['status']} | {c['owner']} | {c['justification']} |")
    return "\n".join(lines) + "\n"


def mapping_md(title, intro, cov) -> str:
    lines = [f"# {title}", "", intro, "", "| Requirement | Supported by Annex A controls | Weakest status |", "|---|---|---|"]
    rank = {"Implemented": 0, "Partial": 1, "Planned": 2}
    for ref, cs in cov.items():
        weakest = max((c["status"] for c in cs), key=lambda s: rank[s])
        lines.append(f"| {ref} | {', '.join(c['control_id'] for c in cs)} | {weakest} |")
    return "\n".join(lines) + "\n"
