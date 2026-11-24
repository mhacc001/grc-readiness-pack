"""Risk register: 5x5 likelihood x impact scoring, appetite bands, heat maps."""

import csv
from pathlib import Path

LIKELIHOOD = {1: "Rare", 2: "Unlikely", 3: "Possible", 4: "Likely", 5: "Almost certain"}
IMPACT = {1: "Negligible", 2: "Minor", 3: "Moderate", 4: "Major", 5: "Severe"}
# Appetite: Low 1-6 accept, Medium 7-12 treat within 90 days, High 13-25 treat now
BANDS = [(6, "Low"), (12, "Medium"), (25, "High")]
BAND_COLOR = {"Low": "#d9f2d9", "Medium": "#ffe8a3", "High": "#f7b3b3"}


def band(score: int) -> str:
    return next(name for limit, name in BANDS if score <= limit)


def load(path: Path) -> list[dict]:
    rows = list(csv.DictReader(open(path, newline="")))
    for r in rows:
        r["inherent"] = int(r["inherent_likelihood"]) * int(r["inherent_impact"])
        r["residual"] = int(r["residual_likelihood"]) * int(r["residual_impact"])
        r["inherent_band"], r["residual_band"] = band(r["inherent"]), band(r["residual"])
        r["control_list"] = [c.strip() for c in r["controls"].split(";") if c.strip()]
    return rows


def heatmap_svg(risks, which: str, title: str) -> str:
    """5x5 grid, impact on x, likelihood on y, risk IDs in each cell."""
    cell, pad_l, pad_t = 64, 110, 40
    w, h = pad_l + 5 * cell + 10, pad_t + 5 * cell + 50
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="system-ui,sans-serif" font-size="12">',
           f'<text x="{pad_l}" y="22" font-size="14" font-weight="600">{title}</text>']
    for li in range(5, 0, -1):
        y = pad_t + (5 - li) * cell
        out.append(f'<text x="{pad_l - 8}" y="{y + cell / 2 + 4}" text-anchor="end" fill="#444">{li} {LIKELIHOOD[li]}</text>')
        for im in range(1, 6):
            x = pad_l + (im - 1) * cell
            ids = [r["risk_id"] for r in risks if int(r[f"{which}_likelihood"]) == li and int(r[f"{which}_impact"]) == im]
            out.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{BAND_COLOR[band(li * im)]}" stroke="#fff" stroke-width="2"/>')
            for k, rid in enumerate(ids):
                out.append(f'<text x="{x + cell / 2}" y="{y + 18 + k * 14}" text-anchor="middle" font-weight="600">{rid}</text>')
    for im in range(1, 6):
        x = pad_l + (im - 1) * cell + cell / 2
        out.append(f'<text x="{x}" y="{pad_t + 5 * cell + 16}" text-anchor="middle" fill="#444">{im}</text>')
        out.append(f'<text x="{x}" y="{pad_t + 5 * cell + 30}" text-anchor="middle" fill="#666" font-size="10">{IMPACT[im]}</text>')
    out.append(f'<text x="{pad_l + 2.5 * cell}" y="{h - 4}" text-anchor="middle" fill="#444">Impact</text></svg>')
    return "".join(out)


def register_md(risks) -> str:
    lines = ["# Risk Register: Ledgerly", "",
             "Method: likelihood (1-5) x impact (1-5). Appetite: **Low 1-6** accept, **Medium 7-12** treat within 90 days, "
             "**High 13-25** treat immediately.", "",
             "| ID | Risk | Inherent | Controls (Annex A) | Residual | Owner | Status |", "|---|---|---|---|---|---|---|"]
    for r in risks:
        lines.append(f"| {r['risk_id']} | {r['risk']} | {r['inherent']} {r['inherent_band']} | {', '.join(r['control_list'])} | "
                     f"{r['residual']} {r['residual_band']} | {r['owner']} | {r['status']} |")
    over = [r["risk_id"] for r in risks if r["residual_band"] != "Low"]
    lines += ["", f"Residual risks still above appetite: **{', '.join(over) if over else 'none'}**."]
    return "\n".join(lines) + "\n"
