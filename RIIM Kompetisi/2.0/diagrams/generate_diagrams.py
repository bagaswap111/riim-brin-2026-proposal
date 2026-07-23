#!/usr/bin/env python3
"""Generate SVG diagrams for Proposal RIIM 2026 — Data-Centric AI Pipeline."""

import os
import textwrap

OUTDIR = os.path.dirname(os.path.abspath(__file__))

# ── Colour palette ──────────────────────────────────────────────────
C = {
    "bg":        "#FAFCFF",
    "cloud_bg":  "#E8F0FE",
    "edge_bg":   "#E6F7E6",
    "hw_bg":     "#FFF3E0",
    "cloud":     "#1A73E8",
    "edge":      "#2E7D32",
    "hw":        "#E65100",
    "accent1":   "#7C4DFF",
    "accent2":   "#00897B",
    "pipeline":  "#1565C0",
    "text":      "#1F2937",
    "muted":     "#6B7280",
    "white":     "#FFFFFF",
    "border":    "#CBD5E1",
    "arrow":     "#94A3B8",
    "ok":        "#16A34A",
    "warn":      "#F59E0B",
    "err":       "#DC2626",
}

BLUE  = "#1A73E8"
GREEN = "#2E7D32"
ORG   = "#E65100"
PURP  = "#7C4DFF"
TEAL  = "#00897B"

def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def style_str():
    return textwrap.dedent(f"""\
    <style>
      .title  {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 18px; font-weight: 700; fill: {C['text']}; }}
      .sub    {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: {C['muted']}; }}
      .label  {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: 600; fill: #fff; }}
      .label2 {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: {C['text']}; }}
      .tag    {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 10px; fill: {C['muted']}; }}
      .layer  {{ font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: 700; fill: #fff; }}
      .arrow  {{ stroke: {C['arrow']}; stroke-width: 2; fill: none; marker-end: url(#arrow); }}
      .dash   {{ stroke: {C['border']}; stroke-width: 1.5; fill: none; stroke-dasharray: 6,3; }}
    </style>""")


def arrow_def():
    return '<marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto">' \
           '<path d="M0,0 L10,4 L0,8 Z" fill="' + C['arrow'] + '"/></marker>'


def rounded_rect(x, y, w, h, r=8, fill="#fff", stroke=C['border'], sw=1.5, opacity=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" ' \
           f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>'


def layer_label(x, y, w, h, text, color):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{color}" opacity="0.12"/>' \
           f'<text x="{x+12}" y="{y+22}" class="layer" fill="{color}">{esc(text)}</text>'


def box(x, y, w, h, label, sub="", fill=C['white'], txt=C['text'], r=8, fs="label"):
    cls = fs
    out = rounded_rect(x, y, w, h, r, fill, C['border'])
    out += f'<text x="{x+w/2}" y="{y+h/2-6}" text-anchor="middle" class="{cls}" fill="{txt}">{esc(label)}</text>'
    if sub:
        out += f'<text x="{x+w/2}" y="{y+h/2+12}" text-anchor="middle" class="sub" fill="{C["muted"]}">{esc(sub)}</text>'
    return out


# ═══════════════════════════════════════════════════════════════════════
#  FIG 1 — System Architecture
# ═══════════════════════════════════════════════════════════════════════
def fig_architecture():
    W, H = 900, 620
    ly = 80  # layer height
    gap = 4
    layers = [
        ("CLOUD LAYER",  C['cloud'],  60),
        ("EDGE LAYER",   C['edge'],   60 + ly + gap),
        ("HARDWARE LAYER", C['hw'],   60 + (ly+gap)*2),
    ]
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">'
    svg += style_str() + arrow_def()
    svg += f'<rect width="{W}" height="{H}" fill="{C["bg"]}"/>'

    # Title
    svg += f'<text x="{W/2}" y="32" text-anchor="middle" class="title">Arsitektur Smart Charging Hub — Data-Centric AI</text>'

    # Layer backgrounds
    for name, col, y in layers:
        ly_box = 76
        svg += f'<rect x="20" y="{y}" width="{W-40}" height="{ly_box}" rx="10" fill="{col}" opacity="0.07"/>'
        svg += f'<rect x="20" y="{y}" width="{W-40}" height="28" rx="10" fill="{col}" opacity="0.15"/>'
        svg += f'<text x="36" y="{y+19}" class="layer" fill="{col}" font-size="11">{esc(name)}</text>'

    # ── Hardware Layer ──
    hw_y = 60 + (ly+gap)*2 + 34
    hw_boxes = [
        (50,  hw_y, "PV Array\n5,5 kWp",          f'{C["hw"]}20'),
        (220, hw_y, "BESS LiFePO₄\n10 kWh",      f'{C["hw"]}20'),
        (390, hw_y, "Hybrid Inverter\n5 kW",      f'{C["hw"]}20'),
        (560, hw_y, "SPKLU AC 22 kW\n(Mitra)",    f'{C["accent2"]}20'),
        (730, hw_y, "Grid\n3 Fasa PLN",           f'{C["muted"]}20'),
    ]
    for x, yb, lbl, clr in hw_boxes:
        svg += box(x, yb, 140, 60, lbl, "", clr, C['text'], 8, "label2")
        # icon placeholder
        svg += f'<circle cx="{x+20}" cy="{yb+15}" r="6" fill="{C["white"]}" stroke="{C["border"]}" stroke-width="1"/>'

    # Data flow lines hardware → edge
    edge_in_y = 60 + ly + gap + 110
    for hx in [120, 290, 460]:
        svg += f'<path d="M{hx},{hw_y-8} L{hx},{edge_in_y-4}" class="arrow"/>'

    # ── Edge Layer ──
    edge_y = 60 + ly + gap + 34
    # Edge gateway box
    eg_x, eg_y, eg_w, eg_h = 100, edge_y, 700, 68
    svg += rounded_rect(eg_x, eg_y, eg_w, eg_h, 10, "#fff", C['edge'])
    svg += f'<text x="{eg_x+10}" y="{eg_y+18}" class="label" fill="{C["edge"]}" font-size="11">IoT Gateway — Edge Inference Node</text>'

    edge_boxes = [
        (120,  edge_y+24, "Data Integrity\nLayer",        C['edge'], "DQ, anomaly"),
        (290,  edge_y+24, "Hybrid Ensemble\nForecasting", C['edge'], "LSTM+TCN+LGBM"),
        (460,  edge_y+24, "Drift-Adaptive\nRetraining",   C['edge'], "monitor→trigger"),
        (630,  edge_y+24, "CPTS-aware\nEMS",              C['accent1'], "MPC+trust"),
    ]
    for ex, ey, elbl, ecol, esub in edge_boxes:
        svg += box(ex, ey, 145, 40, elbl, esub, ecol+"15", ecol, 6, "label2")

    # Internal arrows edge
    for ex in [265, 435, 605]:
        svg += f'<line x1="{ex}" y1="{edge_y+44}" x2="{ex+25}" y2="{edge_y+44}" class="arrow"/>'

    # ── Cloud Layer ──
    cloud_y = 60 + 34
    cloud_boxes = [
        (80,   cloud_y, "Backend API",    "FastAPI", C['cloud']+"15", C['cloud']),
        (260,  cloud_y, "Time-Series DB", "TimescaleDB", C['cloud']+"15", C['cloud']),
        (440,  cloud_y, "Dashboard",      "Grafana", C['cloud']+"15", C['cloud']),
        (620,  cloud_y, "MQTT Broker",    "EMQX", C['cloud']+"15", C['cloud']),
    ]
    for cx, cyb, clbl, csub, cbg, ct in cloud_boxes:
        svg += box(cx, cyb, 140, 38, clbl, csub, cbg, ct, 6, "label2")

    # Arrow edge → cloud
    svg += f'<path d="M460,{60+ly+gap+28} L460,{60+ly+gap-8}" class="arrow"/>'

    # ── Protocol labels ──
    protos = [
        (120,  hw_y-16, "Modbus RTU/TCP"),
        (290,  hw_y-16, "Modbus/CAN"),
        (460,  hw_y-16, "Modbus"),
        (770,  hw_y-16, "Grid ->"),
    ]
    for px, py, ptxt in protos:
        svg += f'<text x="{px}" y="{py}" text-anchor="middle" class="tag">{esc(ptxt)}</text>'

    # Legend
    lx, ly = 30, H-50
    svg += f'<rect x="{lx}" y="{ly}" width="12" height="12" rx="2" fill="{C["cloud"]}" opacity="0.5"/>'
    svg += f'<text x="{lx+18}" y="{ly+11}" class="tag">Cloud / Internet</text>'
    svg += f'<rect x="{lx+150}" y="{ly}" width="12" height="12" rx="2" fill="{C["edge"]}" opacity="0.5"/>'
    svg += f'<text x="{lx+168}" y="{ly+11}" class="tag">Edge / On-site</text>'
    svg += f'<rect x="{lx+300}" y="{ly}" width="12" height="12" rx="2" fill="{C["hw"]}" opacity="0.5"/>'
    svg += f'<text x="{lx+318}" y="{ly+11}" class="tag">Hardware / Power</text>'

    svg += '</svg>'
    return svg


# ═══════════════════════════════════════════════════════════════════════
#  FIG 2 — Data-Centric AI Pipeline
# ═══════════════════════════════════════════════════════════════════════
def fig_pipeline():
    W, H = 1100, 480
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">'
    svg += style_str() + arrow_def()
    svg += f'<rect width="{W}" height="{H}" fill="{C["bg"]}"/>'
    svg += f'<text x="{W/2}" y="32" text-anchor="middle" class="title">Data-Centric AI Pipeline — Alur Pemrosesan End-to-End</text>'

    # ── Stage 1: Data Ingestion ──
    stag = [
        (40,  60, "Telemetri\nMulti-Protokol", ["OCPP 1.6", "Modbus RTU", "MQTT", "CAN Bus"], C['muted']),
        (240, 60, "Data Integrity\nLayer", ["Packet loss deteksi", "Sensor drift koreksi",
                                            "Clock sync", "DQ Scoring (0–1)"], C['edge']),
        (470, 60, "Hybrid Ensemble\nForecasting", ["LSTM (time-series)", "TCN (convolution)",
                                                    "LightGBM (tabular)", "Weighted Ensemble"], BLUE),
        (700, 60, "Drift-Adaptive\nRetraining", ["Distribution monitor", "Drift trigger",
                                                   "Auto retrain", "Model versioning"], PURP),
        (920, 60, "CPTS-aware\nEMS", ["CPTS calculation", "MPC optimization",
                                       "Penalty term", "Control signal"], TEAL),
    ]

    for sx, sy, stitle, items, scol in stag:
        sw = 140
        sh = 120
        # Box
        svg += rounded_rect(sx, sy, sw, sh, 8, scol+"12", scol)
        svg += f'<rect x="{sx}" y="{sy}" width="{sw}" height="28" rx="8" fill="{scol}" opacity="0.85"/>'
        # Handle multi-line title
        lines = stitle.split("\n")
        for i, ln in enumerate(lines):
            svg += f'<text x="{sx+sw/2}" y="{sy+18+i*14}" text-anchor="middle" class="label" fill="#fff" font-size="11">{esc(ln)}</text>'
        for j, item in enumerate(items):
            dot = "●" if j == 0 else "○"
            svg += f'<text x="{sx+10}" y="{sy+42+j*20}" class="tag" font-size="9">{esc(dot)} {esc(item)}</text>'

    # Arrows between stages
    for ax in [180, 410, 640, 870]:
        svg += f'<line x1="{ax}" y1="120" x2="{ax+20}" y2="120" class="arrow"/>'

    # ── Bottom: Output ──
    bx, by = 350, 220
    svg += rounded_rect(bx, by, 400, 70, 10, C['accent1']+"15", C['accent1'])
    svg += f'<rect x="{bx}" y="{by}" width="400" height="28" rx="10" fill="{C["accent1"]}" opacity="0.85"/>'
    svg += f'<text x="{bx+200}" y="{by+19}" text-anchor="middle" class="label">Outputs / Luaran</text>'
    outputs = ["Setpoint BMS (charge/discharge)", "PV curtailing decision",
               "Charger scheduling 22 kW", "Grid import limit signal"]
    for k, o in enumerate(outputs):
        svg += f'<text x="{bx+60*k+30}" y="{by+50}" text-anchor="middle" class="tag" font-size="9">{esc(o)}</text>'
    svg += f'<path d="M460,180 L460,210" class="arrow"/>'
    svg += f'<path d="M550,180 L550,210" class="arrow"/>'

    # ── Feedback loop (drift → retrain cycle) ──
    svg += f'<path d="M770,180 Q850,160 850,100 Q850,80 840,80" class="dash"/>'
    svg += f'<text x="855" y="130" class="tag" font-size="9">Feedback loop</text>'

    # ── Data quality indicator ──
    dq_x, dq_y = 40, 280
    svg += f'<text x="{dq_x}" y="{dq_y}" class="sub" font-size="11">Data Quality Pipeline:</text>'
    dq_steps = [
        (40,   300, "Raw\nData",      C['err']+"30", C['err']),
        (160,  300, "Parse &\nValidate", C['warn']+"30", C['warn']),
        (280,  300, "DQ Score\n0–1",  C['warn']+"30", C['warn']),
        (400,  300, "Impute\nFlags",  C['ok']+"30", C['ok']),
        (520,  300, "Trusted\nStream", C['ok']+"30", C['ok']),
    ]
    for dx, dy, dlbl, dbg, dcol in dq_steps:
        svg += box(dx, dy, 100, 36, dlbl, "", dbg, dcol, 6, "label2")
    for dx in [140, 260, 380, 500]:
        svg += f'<line x1="{dx}" y1="318" x2="{dx+20}" y2="318" class="arrow"/>'

    svg += '</svg>'
    return svg


# ═══════════════════════════════════════════════════════════════════════
#  FIG 3 — Research Methodology (WP Timeline)
# ═══════════════════════════════════════════════════════════════════════
def fig_methodology():
    W, H = 1100, 520
    # WP definitions: (name, color, start_month, duration_months, row)
    wp_data = [
        ("WP1: Data Integrity Layer",        C['edge'],   1,  8,  1),
        ("WP2: Digital Twin & Simulasi",     BLUE,        3,  8,  2),
        ("WP3: Hybrid Ensemble Forecasting", C['pipeline'], 5, 8, 1),
        ("WP4: Drift-Adaptive Retraining",   PURP,        5,  8,  2),
        ("WP5: CPTS-aware EMS",              TEAL,        9,  8,  1),
        ("WP6: Integrasi & Validasi Pilot",  ORG,         13, 10, 1),
        ("WP7: Diseminasi & Luaran",         C['accent2'], 18, 6, 2),
    ]

    milestones = [
        (7,  "DQ Layer v1", C['edge']),
        (11, "Forecast v1", C['pipeline']),
        (12, "EMS Prototype", TEAL),
        (16, "Pilot Integration", ORG),
        (22, "Final Report", C['accent2']),
    ]

    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">'
    svg += style_str()
    svg += f'<rect width="{W}" height="{H}" fill="{C["bg"]}"/>'
    svg += f'<text x="{W/2}" y="30" text-anchor="middle" class="title">Metodologi Riset — Alur Kerja 24 Bulan</text>'

    # ── Timeline axis ──
    gx, gy, gw = 160, 80, 880
    svg += f'<line x1="{gx}" y1="{gy}" x2="{gx+gw}" y2="{gy}" stroke="{C["border"]}" stroke-width="2"/>'
    svg += f'<line x1="{gx}" y1="{gy-6}" x2="{gx}" y2="{gy+6}" stroke="{C["border"]}" stroke-width="2"/>'
    svg += f'<line x1="{gx+gw}" y1="{gy-6}" x2="{gx+gw}" y2="{gy+6}" stroke="{C["border"]}" stroke-width="2"/>'

    # Month ticks (0, 3, 6, 9, 12, 15, 18, 21, 24)
    for m in range(0, 25, 3):
        mx = gx + (m / 24) * gw
        svg += f'<line x1="{mx}" y1="{gy-4}" x2="{mx}" y2="{gy+4}" stroke="{C["border"]}" stroke-width="1.5"/>'
        svg += f'<text x="{mx}" y="{gy+18}" text-anchor="middle" class="tag">{esc(f"B{m}")}</text>'

    # Year labels
    y1x = gx + (12/24)*gw
    svg += f'<text x="{gx+180}" y="{gy+36}" class="sub" font-size="11">Tahun I</text>'
    svg += f'<text x="{y1x+180}" y="{gy+36}" class="sub" font-size="11">Tahun II</text>'

    # Separator between years
    sep_x = gx + gw/2
    svg += f'<line x1="{sep_x}" y1="{gy-10}" x2="{sep_x}" y2="{gy+370}" stroke="{C["border"]}" stroke-width="1" stroke-dasharray="4,4"/>'

    # ── WP bars ──
    row_h = 50
    bar_h = 28
    for wp_name, wp_col, sm, dur, row in wp_data:
        y = gy + 50 + row * row_h
        x1 = gx + (sm / 24) * gw
        bw = (dur / 24) * gw
        svg += rounded_rect(x1, y, bw, bar_h, 6, wp_col+"20", wp_col)
        svg += f'<rect x="{x1}" y="{y}" width="{bw}" height="{bar_h}" rx="6" fill="{wp_col}" opacity="0.15"/>'
        svg += f'<text x="{x1+8}" y="{y+18}" class="label2" fill="{wp_col}" font-size="11">{esc(wp_name)}</text>'
        # Duration label
        svg += f'<text x="{x1+bw+5}" y="{y+18}" class="tag" font-size="9">{esc(f"{dur} bln")}</text>'

    # ── Milestones ──
    for mm, mlbl, mcol in milestones:
        mx = gx + (mm / 24) * gw
        y = gy + 48 + 3 * row_h + 40
        svg += f'<circle cx="{mx}" cy="{y}" r="5" fill="{mcol}" stroke="#fff" stroke-width="2"/>'
        svg += f'<text x="{mx}" y="{y+16}" text-anchor="middle" class="tag" fill="{mcol}" font-size="9">{esc(mlbl)}</text>'

    # ── Legend ──
    ly = H - 60
    svg += f'<text x="40" y="{ly}" class="label2">Legend:</text>'
    l_items = [
        ("AI/Software Dev", C['edge']),
        ("Modeling/Simulasi", BLUE),
        ("Integrasi", ORG),
        ("Diseminasi", C['accent2']),
    ]
    for li, (llbl, lcol) in enumerate(l_items):
        lx = 40 + li * 220
        svg += f'<rect x="{lx}" y="{ly+10}" width="14" height="14" rx="3" fill="{lcol}" opacity="0.5"/>'
        svg += f'<text x="{lx+20}" y="{ly+22}" class="tag">{esc(llbl)}</text>'

    # TKT labels
    svg += f'<text x="40" y="90" class="sub" font-size="11">TKT 3</text>'
    svg += f'<text x="40" y="240" class="sub" font-size="11">TKT 4</text>'
    svg += f'<text x="40" y="380" class="sub" font-size="11">TKT 6</text>'
    # TKT arrows
    svg += f'<path d="M{gx+40},{gy+390} L{gx+140},{gy+390}" class="arrow"/>'
    svg += f'<text x="{gx+160}" y="{gy+394}" class="tag" font-size="9">TKT Progression</text>'

    svg += '</svg>'
    return svg


# ═══════════════════════════════════════════════════════════════════════
#  FIG 4 — CPTS Mechanism
# ═══════════════════════════════════════════════════════════════════════
def fig_cpts():
    W, H = 800, 380
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">'
    svg += style_str() + arrow_def()
    svg += f'<rect width="{W}" height="{H}" fill="{C["bg"]}"/>'
    svg += f'<text x="{W/2}" y="30" text-anchor="middle" class="title">Cyber-Physical Trust Score (CPTS) — Mekanisme Integrasi</text>'

    # ── Three input pillars ──
    inputs = [
        (60,  80, "Anomaly\nScore", f"• Autoencoder\n• Isolation Forest\n• Statistical", C['err']),
        (290, 80, "Data Quality\nMetrics", f"• Completeness\n• Accuracy\n• Timeliness", C['warn']),
        (520, 80, "Forecast\nUncertainty", f"• Prediction interval\n• Ensemble variance\n• Past error rate", BLUE),
    ]
    for ix, iy, ititle, ibody, icol in inputs:
        iw, ih = 200, 130
        svg += rounded_rect(ix, iy, iw, ih, 10, icol+"12", icol)
        svg += f'<rect x="{ix}" y="{iy}" width="{iw}" height="28" rx="10" fill="{icol}" opacity="0.85"/>'
        lines = ititle.split("\n")
        for i, ln in enumerate(lines):
            svg += f'<text x="{ix+iw/2}" y="{iy+18+i*14}" text-anchor="middle" class="label" font-size="11">{esc(ln)}</text>'
        # Body items
        for j, bline in enumerate(ibody.split("\n")):
            svg += f'<text x="{ix+15}" y="{iy+46+j*20}" class="tag" font-size="9">{esc(bline)}</text>'

    # ── CPTS calculation ──
    calc_x, calc_y = 280, 240
    cw, ch = 200, 50
    svg += rounded_rect(calc_x, calc_y, cw, ch, 10, C['accent1']+"15", C['accent1'])
    svg += f'<text x="{calc_x+cw/2}" y="{calc_y+20}" text-anchor="middle" class="label" fill="{C["accent1"]}">CPTS = f(α·A + β·DQ + γ·U)</text>'
    svg += f'<text x="{calc_x+cw/2}" y="{calc_y+38}" text-anchor="middle" class="tag" fill="{C["accent1"]}">Bobot adaptif berdasarkan konteks</text>'

    # Arrows inputs → calculation
    for iax, iay in [(160, 210), (390, 210), (620, 210)]:
        svg += f'<line x1="{iax}" y1="{iay}" x2="{iax}" y2="{calc_y}" class="arrow"/>'

    # ── Output: EMS integration ──
    ox, oy = 560, 240
    ow, oh = 170, 50
    svg += rounded_rect(ox, oy, ow, oh, 10, C['accent2']+"15", C['accent2'])
    svg += f'<text x="{ox+ow/2}" y="{oy+20}" text-anchor="middle" class="label" fill="{C["accent2"]}">EMS Objective</text>'
    svg += f'<text x="{ox+ow/2}" y="{oy+38}" text-anchor="middle" class="tag" fill="{C["accent2"]}">min J = J₀ + λ · CPTS</text>'

    svg += f'<line x1="{calc_x+cw}" y1="{calc_y+25}" x2="{ox}" y2="{oy+25}" class="arrow"/>'

    # ── Bottom: Decisions ──
    decs = [
        (60,  320, "Charge/Discharge\nRate Limit", C['edge']),
        (240, 320, "PV Curtailing\nThreshold",     C['hw']),
        (420, 320, "Charger Scheduling\nPriority", BLUE),
        (600, 320, "Grid Import\nLimit",           C['muted']),
    ]
    for dx, dy, dlbl, dcol in decs:
        svg += box(dx, dy, 150, 36, dlbl, "", dcol+"15", dcol, 6, "label2")
    svg += f'<line x1="{380}" y1="{290}" x2="{380}" y2="{316}" class="arrow"/>'
    svg += f'<line x1="480" y1="{290}" x2="480" y2="{316}" class="arrow"/>'

    svg += '</svg>'
    return svg


# ═══════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    figs = [
        ("architecture.svg", fig_architecture()),
        ("pipeline.svg",     fig_pipeline()),
        ("methodology.svg",  fig_methodology()),
        ("cpts.svg",         fig_cpts()),
    ]
    for fname, svg_content in figs:
        fpath = os.path.join(OUTDIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"✅ {fpath}  ({len(svg_content)} bytes)")
    print("Done — 4 diagrams generated.")
