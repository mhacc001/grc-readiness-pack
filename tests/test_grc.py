from collections import Counter
from datetime import date
from pathlib import Path

from grc import risk, soa, testing, vendors
from grc.__main__ import build

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
AS_OF = date(2026, 11, 24)


def test_annex_a_is_complete_and_correctly_themed():
    controls = soa.load(DATA / "controls.csv")
    assert len(controls) == 93
    assert len({c["control_id"] for c in controls}) == 93
    assert Counter(c["theme"] for c in controls) == {"Organizational": 37, "People": 8, "Physical": 14, "Technological": 34}


def test_every_exclusion_and_gap_is_justified():
    for c in soa.load(DATA / "controls.csv"):
        assert c["justification"].strip(), c["control_id"]
        if c["applicable"] == "No":
            assert c["status"] == "Not applicable"
        else:
            assert c["evidence"] and c["owner"], c["control_id"]


def test_risk_scoring_and_appetite_bands():
    assert [risk.band(s) for s in (1, 6, 7, 12, 13, 25)] == ["Low", "Low", "Medium", "Medium", "High", "High"]
    risks = risk.load(DATA / "risk_register.csv")
    for r in risks:
        assert r["residual"] <= r["inherent"], f"{r['risk_id']} residual should not exceed inherent"


def test_risks_only_reference_real_controls():
    ids = {c["control_id"] for c in soa.load(DATA / "controls.csv")}
    for r in risk.load(DATA / "risk_register.csv"):
        assert set(r["control_list"]) <= ids, r["risk_id"]


def test_vendor_tiering_and_decisions():
    v = {x["vendor"]: x for x in vendors.assess(DATA / "vendors.csv")}
    assert v["AWS"]["tier"].startswith("Tier 1") and v["AWS"]["decision"] == "Approve"
    assert v["PayFlow HR"]["decision"].startswith("Escalate")
    assert any("DORA Art 30(2)" in g for g in v["Zendesk"]["gaps"])
    assert v["Zendesk"]["decision"] == "Approve with remediation plan"


def test_leaver_test_uses_business_days():
    t = testing.ct01_leaver_access(DATA / "evidence")
    # m.costa left on a Saturday and was removed on Monday: on time.
    assert len(t["exceptions"]) == 1 and t["exceptions"][0].startswith("r.diallo")


def test_vulnerability_sla_flags_only_overdue_highs():
    t = testing.ct04_vuln_sla(DATA / "evidence", AS_OF)
    assert [e.split()[0] for e in t["exceptions"]] == ["V-205", "V-206"]


def test_full_build_writes_every_report():
    build(AS_OF)
    for name in ["statement-of-applicability.md", "statement-of-applicability.csv", "gap-remediation-plan.md",
                 "risk-register.md", "risk-heatmap-inherent.svg", "vendor-scorecard.md", "control-testing.md",
                 "soc2-mapping.md", "dora-mapping.md", "dashboard.html"]:
        assert (ROOT / "reports" / name).stat().st_size > 200, name
