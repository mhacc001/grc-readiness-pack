"""Build every GRC artifact from the data files.

  python -m grc build [--as-of YYYY-MM-DD]

Writes reports/: statement-of-applicability.md/.csv, gap-remediation-plan.md, risk-register.md,
risk-heatmap-*.svg, vendor-scorecard.md, control-testing.md, soc2-mapping.md, dora-mapping.md, dashboard.html
"""

import argparse
import csv
from datetime import date
from pathlib import Path

from . import dashboard, risk, soa, testing, vendors

ROOT = Path(__file__).resolve().parent.parent
DATA, REPORTS = ROOT / "data", ROOT / "reports"


def build(as_of: date) -> dict:
    REPORTS.mkdir(exist_ok=True)
    controls = soa.load(DATA / "controls.csv")
    stats = soa.readiness(controls)
    risks = risk.load(DATA / "risk_register.csv")
    vend = vendors.assess(DATA / "vendors.csv")
    tests = testing.run_all(DATA / "evidence", as_of)
    soc2_cov = soa.coverage(controls, "soc2_tsc")
    dora_cov = soa.coverage(controls, "dora")

    known = {c["control_id"] for c in controls}
    for r in risks:
        missing = [c for c in r["control_list"] if c not in known]
        if missing:
            raise ValueError(f"{r['risk_id']} references unknown controls {missing}")

    (REPORTS / "statement-of-applicability.md").write_text(soa.soa_md(controls, stats))
    with open(REPORTS / "statement-of-applicability.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(controls[0].keys()))
        w.writeheader()
        w.writerows(controls)
    (REPORTS / "gap-remediation-plan.md").write_text(soa.gaps_md(stats))
    (REPORTS / "risk-register.md").write_text(risk.register_md(risks))
    (REPORTS / "risk-heatmap-inherent.svg").write_text(risk.heatmap_svg(risks, "inherent", "Inherent risk"))
    (REPORTS / "risk-heatmap-residual.svg").write_text(risk.heatmap_svg(risks, "residual", "Residual risk"))
    (REPORTS / "vendor-scorecard.md").write_text(vendors.report_md(vend))
    (REPORTS / "control-testing.md").write_text(testing.report_md(tests, as_of))
    (REPORTS / "soc2-mapping.md").write_text(soa.mapping_md(
        "SOC 2 Trust Services Criteria to ISO 27001 Annex A", "One control set, two frameworks: each SOC 2 criterion "
        "is evidenced by the Annex A controls below.", soc2_cov))
    (REPORTS / "dora-mapping.md").write_text(soa.mapping_md(
        "DORA (EU 2022/2554) to ISO 27001 Annex A", "Ledgerly is an ICT third-party service provider to EU banks. "
        "DORA binds the banks, and the banks flow its requirements down to Ledgerly by contract (Art 28-30). "
        "This table shows which controls let Ledgerly meet those requirements.", dora_cov))
    (REPORTS / "dashboard.html").write_text(dashboard.build(stats, risks, vend, tests, soc2_cov, dora_cov, as_of))
    return {"stats": stats, "risks": risks, "vendors": vend, "tests": tests, "soc2": soc2_cov, "dora": dora_cov}


def main():
    p = argparse.ArgumentParser(prog="grc", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("cmd", choices=["build"])
    p.add_argument("--as-of", default=None)
    a = p.parse_args()
    as_of = date.fromisoformat(a.as_of) if a.as_of else date.today()
    r = build(as_of)
    s = r["stats"]
    print(f"Annex A: {s['applicable']}/{s['total']} applicable, readiness {s['score']}%, "
          f"{len(s['gaps'])} gaps ({s['by_status']['Partial']} partial, {s['by_status']['Planned']} planned)")
    print(f"Risks: {len(r['risks'])}, above appetite after treatment: "
          f"{[x['risk_id'] for x in r['risks'] if x['residual_band'] != 'Low']}")
    for v in r["vendors"]:
        print(f"Vendor {v['vendor']:<13} {v['tier']:<18} inherent {v['inherent']:>2}  controls {v['strength']:>3}  {v['decision']}")
    for t in r["tests"]:
        print(f"{t['id']} {t['result']:<26} {len(t['exceptions'])} exception(s)")
    print(f"SOC 2 criteria mapped: {len(r['soc2'])}, DORA references mapped: {len(r['dora'])}")
    print("Reports written to reports/ (open reports/dashboard.html)")


if __name__ == "__main__":
    main()
