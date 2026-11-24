"""Single-page HTML readiness dashboard (no external assets) for leadership and auditors."""

import html

from .risk import heatmap_svg

STATUS_COLOR = {"Implemented": "#2e7d32", "Partial": "#f9a825", "Planned": "#c62828", "Not applicable": "#9e9e9e"}
RESULT_COLOR = {"Effective": "#2e7d32", "Effective with exceptions": "#f9a825", "Not effective": "#c62828"}


def _bar(counter, statuses):
    total = sum(counter[s] for s in statuses) or 1
    parts = "".join(f'<div style="width:{100 * counter[s] / total:.1f}%;background:{STATUS_COLOR[s]}" '
                    f'title="{s}: {counter[s]}"></div>' for s in statuses if counter[s])
    return f'<div class="bar">{parts}</div>'


def build(stats, risks, vendors, tests, soc2_cov, dora_cov, as_of) -> str:
    e = html.escape
    statuses = ["Implemented", "Partial", "Planned"]
    themes = "".join(f"<tr><td>{t}</td><td>{_bar(c, statuses)}</td><td>{c['Implemented']}/{sum(c.values())}</td></tr>"
                     for t, c in sorted(stats["by_theme"].items()))
    high_res = sum(r["residual_band"] != "Low" for r in risks)
    test_rows = "".join(
        f"<tr><td><b>{t['id']}</b> {e(t['name'])}</td><td>{t['controls']}</td><td>{len(t['exceptions'])}</td>"
        f"<td><span class='pill' style='background:{RESULT_COLOR[t['result']]}'>{t['result']}</span></td></tr>" for t in tests)
    vend_rows = "".join(
        f"<tr><td><b>{e(v['vendor'])}</b><br><small>{e(v['service'])}</small></td><td>{v['tier']}</td>"
        f"<td>{v['inherent']}</td><td>{v['strength']}</td><td>{e(v['decision'])}</td></tr>" for v in vendors)
    gap_rows = "".join(f"<tr><td>{c['control_id']}</td><td>{e(c['title'])}</td>"
                       f"<td><span class='pill' style='background:{STATUS_COLOR[c['status']]}'>{c['status']}</span></td>"
                       f"<td>{e(c['owner'])}</td></tr>" for c in stats["gaps"])
    dora_weak = [ref for ref, cs in dora_cov.items() if any(c["status"] != "Implemented" for c in cs)]
    return f"""<!doctype html><html><head><meta charset="utf-8"><title>Ledgerly ISMS readiness</title><style>
body{{font:14px/1.45 -apple-system,system-ui,sans-serif;margin:0;background:#f4f6f8;color:#1f2328}}
header{{background:#1d3557;color:#fff;padding:18px 28px}}header h1{{margin:0;font-size:20px}}header p{{margin:4px 0 0;opacity:.85}}
.grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;padding:18px 28px}}
.card{{background:#fff;border-radius:10px;padding:14px 16px;box-shadow:0 1px 2px rgba(0,0,0,.08)}}
.kpi{{font-size:30px;font-weight:700}}.lbl{{color:#57606a;font-size:12px;text-transform:uppercase;letter-spacing:.04em}}
.wide{{grid-column:span 2}}.full{{grid-column:span 4}}h2{{font-size:15px;margin:0 0 10px}}
table{{border-collapse:collapse;width:100%;font-size:13px}}td,th{{padding:6px 6px;border-bottom:1px solid #eaeef2;text-align:left;vertical-align:top}}
.bar{{display:flex;height:14px;border-radius:7px;overflow:hidden;background:#eee;min-width:160px}}.bar div{{height:100%}}
.hm{{display:flex;gap:8px}}.hm>div{{flex:1;min-width:0}}.hm svg{{width:100%;height:auto}}
.pill{{color:#fff;border-radius:10px;padding:1px 8px;font-size:12px;white-space:nowrap}}.legend span{{margin-right:12px;font-size:12px}}
</style></head><body>
<header><h1>Ledgerly: ISO 27001 / SOC 2 / DORA readiness</h1><p>Fictional company. Status as of {as_of.isoformat()}. Built from data/ by python -m grc build</p></header>
<div class="grid">
<div class="card"><div class="lbl">Readiness score</div><div class="kpi">{stats['score']}%</div><div>Annex A, applicable controls</div></div>
<div class="card"><div class="lbl">Controls applicable</div><div class="kpi">{stats['applicable']} / {stats['total']}</div><div>{stats['by_status']['Implemented']} implemented, {stats['by_status']['Partial']} partial, {stats['by_status']['Planned']} planned</div></div>
<div class="card"><div class="lbl">Risks above appetite</div><div class="kpi">{high_res} / {len(risks)}</div><div>after treatment (residual)</div></div>
<div class="card"><div class="lbl">Control tests</div><div class="kpi">{sum(t['result'] == 'Effective' for t in tests)} / {len(tests)} clean</div><div>{sum(len(t['exceptions']) for t in tests)} exceptions found</div></div>
<div class="card wide"><h2>Annex A status by theme</h2><table>{themes}</table>
<div class="legend">{''.join(f"<span style='color:{STATUS_COLOR[s]}'>&#9632; {s}</span>" for s in statuses)}</div></div>
<div class="card wide"><h2>Control tests (re-performed from evidence)</h2><table><tr><th>Test</th><th>Annex A</th><th>Exceptions</th><th>Result</th></tr>{test_rows}</table></div>
<div class="card wide"><h2>Risk heat map</h2><div class="hm"><div>{heatmap_svg(risks, 'inherent', 'Inherent')}</div><div>{heatmap_svg(risks, 'residual', 'Residual')}</div></div></div>
<div class="card wide"><h2>Third-party risk</h2><table><tr><th>Vendor</th><th>Tier</th><th>Inherent</th><th>Controls</th><th>Decision</th></tr>{vend_rows}</table></div>
<div class="card wide"><h2>Open gaps ({len(stats['gaps'])})</h2><table>{gap_rows}</table></div>
<div class="card wide"><h2>Framework coverage</h2>
<p><b>SOC 2</b>: {len(soc2_cov)} Trust Services Criteria mapped to Annex A controls.</p>
<p><b>DORA</b>: {len(dora_cov)} article references mapped. As an ICT provider to EU banks, Ledgerly must support its clients'
DORA duties: ICT risk management (Art 5-16), incident reporting (Art 17-23), resilience testing (Art 24-27) and the contract terms in Art 30.</p>
<p>DORA references with a gap behind them: <b>{', '.join(dora_weak) or 'none'}</b></p></div>
</div></body></html>"""
