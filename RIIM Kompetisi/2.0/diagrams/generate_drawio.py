#!/usr/bin/env python3
"""Generate .drawio (mxGraph XML) files for Proposal RIIM 2026 diagrams."""

import os
import hashlib
import xml.sax.saxutils as saxutils

OUTDIR = os.path.dirname(os.path.abspath(__file__))

def esc(s):
    return saxutils.escape(str(s))

def uid(seed):
    return abs(hash(seed)) % (10**8)

# ── Colours (hex without # for styles) ──
C = {
    "bg":        "#FAFCFF",
    "cloud":     "#1A73E8",
    "edge":      "#2E7D32",
    "hw":        "#E65100",
    "accent1":   "#7C4DFF",
    "accent2":   "#00897B",
    "pipeline":  "#1565C0",
    "text":      "#1F2937",
    "muted":     "#6B7280",
    "border":    "#CBD5E1",
    "arrow":     "#94A3B8",
    "ok":        "#16A34A",
    "warn":      "#F59E0B",
    "err":       "#DC2626",
    "white":     "#FFFFFF",
}


class Diagram:
    """Helper to build a draw.io diagram."""

    def __init__(self, name, w, h):
        self.name = name
        self.w = w
        self.h = h
        self._cells = []
        self._id_counter = 1
        # Cell 0 (root) and 1 (default parent)
        self.c0 = self._next_id()
        self.c1 = self._next_id()
        self._root_cells = [
            '<mxCell id="0" />',
            f'<mxCell id="{self.c1}" parent="0" />',
        ]

    def _next_id(self):
        i = self._id_counter
        self._id_counter += 1
        return i

    def add_box(self, x, y, w, h, label, fill="#fff", stroke=C["border"], font=C["text"],
                fs=11, bold=False, radius=8, parent=None, layer_label=False):
        cid = self._next_id()
        p = parent or self.c1
        fw = "font-weight=bold;" if bold else ""
        style = (f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};"
                 f"strokeColor={stroke};fontColor={font};fontSize={fs};"
                 f"arcSize={radius};{fw}"
                 f"verticalAlign=middle;align=center;")
        if layer_label:
            style += "textOpacity=100;"
        lines = esc(label).split("\n")
        # Multi-line: insert <br> for line breaks
        if len(lines) > 1:
            html_content = "<br>".join(f"<span>{esc(l)}</span>" for l in lines)
            val = esc(html_content)
        else:
            val = esc(label)
        xml = f'<mxCell id="{cid}" value="{val}" style="{style}" vertex="1" parent="{p}">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        xml += '</mxCell>'
        self._root_cells.append(xml)
        return cid

    def add_rect(self, x, y, w, h, fill, stroke=C["border"], opacity=100, radius=8, label=""):
        cid = self._next_id()
        style = (f"rounded=1;whiteSpace=wrap;html=1;fillColor={fill};"
                 f"strokeColor={stroke};fontSize=10;arcSize={radius};")
        if opacity < 100:
            style += f"opacity={opacity / 100};"
        val = esc(label)
        xml = f'<mxCell id="{cid}" value="{val}" style="{style}" vertex="1" parent="{self.c1}">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry"/>'
        xml += '</mxCell>'
        self._root_cells.append(xml)
        return cid

    def add_arrow(self, x1, y1, x2, y2, style="edgeStyle=orthogonalEdgeStyle;", label="",
                  src_id=None, dst_id=None, dash=False):
        cid = self._next_id()
        base = (f"rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
                f"strokeColor={C['arrow']};strokeWidth=2;endArrow=classic;endFill=1;")
        if dash:
            base += "dashed=1;dashPattern=6 3;"
        style_attr = style + base
        src = src_id if src_id else self.c1
        dst = dst_id if dst_id else self.c1
        val = esc(label)
        xml = f'<mxCell id="{cid}" value="{val}" style="{style_attr}" edge="1" parent="{self.c1}" source="{src}" target="{dst}">'
        xml += '<mxGeometry relative="1" as="geometry">'
        # If no explicit source/target, use absolute coordinates
        if not src_id or not dst_id:
            xml += f'<mxPoint x="{x1}" y="{y1}" as="sourcePoint"/>'
            xml += f'<mxPoint x="{x2}" y="{y2}" as="targetPoint"/>'
        xml += '</mxGeometry>'
        xml += '</mxCell>'
        self._root_cells.append(xml)
        return cid

    def add_line(self, x1, y1, x2, y2, color=C["border"], width=1.5, dash=False):
        cid = self._next_id()
        style = (f"rounded=0;html=1;strokeColor={color};strokeWidth={width};")
        if dash:
            style += "dashed=1;dashPattern=4 4;"
        val = ""
        xml = f'<mxCell id="{cid}" value="{val}" style="{style}" edge="1" parent="{self.c1}">'
        xml += '<mxGeometry relative="1" as="geometry">'
        xml += f'<mxPoint x="{x1}" y="{y1}" as="sourcePoint"/>'
        xml += f'<mxPoint x="{x2}" y="{y2}" as="targetPoint"/>'
        xml += '</mxGeometry>'
        xml += '</mxCell>'
        self._root_cells.append(xml)
        return cid

    def add_circle(self, x, y, r, fill, stroke=C["border"], label=""):
        cid = self._next_id()
        style = (f"ellipse;whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};"
                 f"fontSize=10;fontColor={C['text']};")
        xml = f'<mxCell id="{cid}" value="{esc(label)}" style="{style}" vertex="1" parent="{self.c1}">'
        xml += f'<mxGeometry x="{x}" y="{y}" width="{r*2}" height="{r*2}" as="geometry"/>'
        xml += '</mxCell>'
        self._root_cells.append(xml)
        return cid

    def render(self):
        cells_xml = "\n".join(self._root_cells)
        digest = hashlib.md5(self.name.encode()).hexdigest()[:16]
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="opencode" modified="2026-07-22T00:00:00.000Z">
  <diagram name="{esc(self.name)}" id="{digest}">
    <mxGraphModel dx="0" dy="0" grid="1" gridSize="10" guides="1" tooltips="1"
                  connect="1" arrows="1" fold="1" page="1" pageScale="1"
                  pageWidth="{self.w}" pageHeight="{self.h}" math="0" shadow="0">
      <root>
{cells_xml}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''


# ═══════════════════════════════════════════════════════════════════════
# FIG 1 — Architecture
# ═══════════════════════════════════════════════════════════════════════
def draw_architecture():
    d = Diagram("Architecture", 900, 620)
    bg = d.add_rect(0, 0, 900, 620, C["bg"], C["bg"], 0, 0)

    # Title
    d.add_box(0, 10, 900, 30, "Arsitektur Smart Charging Hub \u2014 Data-Centric AI",
              fill="transparent", stroke="none", font=C["text"], fs=16, bold=True)

    # Layer backgrounds
    ly_y = [60, 140, 220]
    ly_h = 76
    for i, (lbl, col, y) in enumerate([("CLOUD LAYER", C["cloud"], 60),
                                        ("EDGE LAYER", C["edge"], 140),
                                        ("HARDWARE LAYER", C["hw"], 220)]):
        d.add_rect(20, y, 860, ly_h, col, col, 8, 8)
        d.add_rect(20, y, 860, 28, col, col, 20, 8)
        d.add_box(32, y + 3, 200, 22, lbl, "transparent", "none", "#fff", 11, True)

    # ── Hardware layer ──
    hw_y = ly_y[2] + 34
    hw_boxes = [
        (50,  hw_y, "PV Array 5,5 kWp",          C["hw"]),
        (220, hw_y, "BESS LiFePO\u2084 10 kWh",   C["hw"]),
        (390, hw_y, "Hybrid Inverter 5 kW",      C["hw"]),
        (560, hw_y, "SPKLU AC 22 kW (Mitra)",    C["accent2"]),
        (730, hw_y, "Grid 3 Fasa PLN",           C["muted"]),
    ]
    for hx, hy, hlbl, hcol in hw_boxes:
        d.add_box(hx, hy, 140, 60, hlbl, hcol + "20", hcol, hcol, 10, False)
        # Small circle as icon
        d.add_circle(hx + 12, hy + 8, 6, "#fff", hcol)

    # Data flow arrows hardware → edge
    edge_in_y = ly_y[1] + 110
    for hx in [120, 290, 460]:
        d.add_arrow(hx, hw_y - 8, hx, edge_in_y - 4)

    # ── Edge layer ──
    edge_y = ly_y[1] + 34
    eg = d.add_box(100, edge_y, 700, 68, "IoT Gateway \u2014 Edge Inference Node",
                   C["white"], C["edge"], C["edge"], 11, True, 10)
    edge_boxes = [
        (120,  edge_y + 24, "Data Integrity Layer",   C["edge"], "DQ, anomaly"),
        (290,  edge_y + 24, "Hybrid Ensemble\nForecasting", C["edge"], "LSTM+TCN+LGBM"),
        (460,  edge_y + 24, "Drift-Adaptive\nRetraining",   C["edge"], "monitor\u2192trigger"),
        (630,  edge_y + 24, "CPTS-aware EMS",         C["accent1"], "MPC+trust"),
    ]
    for ex, ey, elbl, ecol, esub in edge_boxes:
            d.add_box(ex, ey, 145, 40, elbl, ecol + "15", ecol, ecol, 10)

    # Internal arrows edge
    for ax in [265, 435, 605]:
        d.add_line(ax, edge_y + 44, ax + 25, edge_y + 44, C["arrow"], 2)

    # ── Cloud layer ──
    cloud_y = ly_y[0] + 34
    cloud_boxes = [
        (80,   cloud_y, "Backend API\n(FastAPI)",   C["cloud"]),
        (260,  cloud_y, "Time-Series DB\n(TimescaleDB)", C["cloud"]),
        (440,  cloud_y, "Dashboard\n(Grafana)",     C["cloud"]),
        (620,  cloud_y, "MQTT Broker\n(EMQX)",      C["cloud"]),
    ]
    for cx, cy, clbl, ccol in cloud_boxes:
        d.add_box(cx, cy, 140, 38, clbl, ccol + "15", ccol, ccol, 10)

    # Edge → cloud arrow
    d.add_arrow(460, ly_y[1] + 28, 460, ly_y[1] - 8)

    # Protocol labels on lines
    protos = [
        (120,  hw_y - 16, "Modbus RTU/TCP"),
        (290,  hw_y - 16, "Modbus/CAN"),
        (460,  hw_y - 16, "Modbus"),
    ]
    for px, py, ptxt in protos:
        d.add_box(px - 40, py - 10, 80, 18, ptxt, "transparent", "none", C["muted"], 9)

    # Legend
    lx, ly = 30, 550
    items = [
        (lx,      ly, C["cloud"], "Cloud / Internet"),
        (lx + 150, ly, C["edge"],  "Edge / On-site"),
        (lx + 300, ly, C["hw"],    "Hardware / Power"),
    ]
    for ix, iy, icol, ilbl in items:
        d.add_rect(ix, iy, 12, 12, icol, icol, 50, 2)
        d.add_box(ix + 18, iy - 3, 120, 18, ilbl, "transparent", "none", C["muted"], 10)

    return d.render()


# ═══════════════════════════════════════════════════════════════════════
# FIG 2 — Pipeline
# ═══════════════════════════════════════════════════════════════════════
def draw_pipeline():
    d = Diagram("Pipeline", 1100, 480)
    d.add_rect(0, 0, 1100, 480, C["bg"], C["bg"], 0, 0)

    d.add_box(0, 10, 1100, 30, "Data-Centric AI Pipeline \u2014 Alur Pemrosesan End-to-End",
              "transparent", "none", C["text"], 16, True)

    # Stages
    stag = [
        (40,  60, "Telemetri\nMulti-Protokol", ["OCPP 1.6", "Modbus RTU", "MQTT", "CAN Bus"], C["muted"]),
        (240, 60, "Data Integrity\nLayer", ["Packet loss", "Sensor drift", "Clock sync", "DQ Score"], C["edge"]),
        (470, 60, "Hybrid Ensemble\nForecasting", ["LSTM", "TCN", "LightGBM", "Weighted"], C["cloud"]),
        (700, 60, "Drift-Adaptive\nRetraining", ["PSI monitor", "Drift trigger", "Auto retrain", "Versioning"], C["accent1"]),
        (920, 60, "CPTS-aware\nEMS", ["CPTS calc", "MPC optim.", "Penalty", "Control"], C["accent2"]),
    ]
    for sx, sy, stitle, items, scol in stag:
        d.add_rect(sx, sy, 140, 120, scol + "12", scol, 100, 8)
        d.add_rect(sx, sy, 140, 28, scol, scol, 90, 8)
        lines = stitle.split("\n")
        label = "<br>".join(lines)
        d.add_box(sx, sy + 2, 140, 24, label, "transparent", "none", "#fff", 11, True)
        item_text = "<br>".join(f"\u2022 {x}" for x in items)
        d.add_box(sx + 5, sy + 34, 130, 80, item_text, "transparent", "none", C["text"], 9)

    # Arrows between stages
    for ax in [180, 410, 640, 870]:
        d.add_line(ax, 120, ax + 20, 120, C["arrow"], 2)

    # Outputs
    bx, by = 350, 220
    d.add_rect(bx, by, 400, 70, C["accent1"] + "15", C["accent1"], 100, 10)
    d.add_rect(bx, by, 400, 28, C["accent1"], C["accent1"], 90, 10)
    d.add_box(bx, by + 2, 400, 24, "Outputs / Luaran", "transparent", "none", "#fff", 11, True)
    outputs = ["Setpoint BMS", "PV curtailing", "Charger sched.", "Grid limit"]
    for k, o in enumerate(outputs):
        d.add_box(bx + 60 * k + 10, by + 38, 60, 24, o, "transparent", "none", C["text"], 9)
    d.add_arrow(460, 180, 460, 216)
    d.add_arrow(550, 180, 550, 216)

    # Feedback loop
    d.add_line(770, 180, 850, 160, C["arrow"], 2, True)
    d.add_line(850, 160, 850, 100, C["arrow"], 2, True)
    d.add_line(850, 100, 840, 88, C["arrow"], 2, True)
    d.add_box(855, 125, 80, 18, "Feedback loop", "transparent", "none", C["muted"], 9)

    # Data quality pipeline (bottom)
    d.add_box(40, 270, 120, 16, "Data Quality Pipeline:", "transparent", "none", C["text"], 11, True)
    dq_steps = [
        (40,   295, "Raw Data",          C["err"]),
        (160,  295, "Parse & Validate",  C["warn"]),
        (280,  295, "DQ Score 0\u20131", C["warn"]),
        (400,  295, "Impute Flags",      C["ok"]),
        (520,  295, "Trusted Stream",    C["ok"]),
    ]
    for dx, dy, dlbl, dcol in dq_steps:
        d.add_box(dx, dy, 100, 36, dlbl, dcol + "30", dcol, dcol, 10)
    for dx in [140, 260, 380, 500]:
        d.add_line(dx, 313, dx + 20, 313, C["arrow"], 2)

    return d.render()


# ═══════════════════════════════════════════════════════════════════════
# FIG 3 — Methodology
# ═══════════════════════════════════════════════════════════════════════
def draw_methodology():
    d = Diagram("Methodology", 1100, 520)
    d.add_rect(0, 0, 1100, 520, C["bg"], C["bg"], 0, 0)
    d.add_box(0, 10, 1100, 30, "Metodologi Riset \u2014 Alur Kerja 24 Bulan",
              "transparent", "none", C["text"], 16, True)

    gx, gy, gw = 160, 80, 880

    # Timeline axis
    d.add_line(gx, gy, gx + gw, gy, C["border"], 2)
    d.add_line(gx, gy - 6, gx, gy + 6, C["border"], 2)
    d.add_line(gx + gw, gy - 6, gx + gw, gy + 6, C["border"], 2)

    # Month ticks (0, 3, 6, 9, 12, 15, 18, 21, 24)
    for m in range(0, 25, 3):
        mx = gx + (m / 24) * gw
        d.add_line(mx, gy - 4, mx, gy + 4, C["border"], 1.5)
        d.add_box(mx - 12, gy + 8, 24, 16, f"B{m}", "transparent", "none", C["muted"], 9)

    # Year labels
    y1x = gx + (12 / 24) * gw
    d.add_box(gx + 140, gy + 30, 100, 18, "Tahun I", "transparent", "none", C["text"], 11, True)
    d.add_box(y1x + 140, gy + 30, 100, 18, "Tahun II", "transparent", "none", C["text"], 11, True)

    # Year separator
    sep_x = gx + gw / 2
    d.add_line(sep_x, gy - 10, sep_x, gy + 370, C["border"], 1, True)

    # WP bars
    wp_data = [
        ("WP1: Data Integrity Layer",        C["edge"],   1,  8,  1),
        ("WP2: Digital Twin & Simulasi",     C["cloud"],  3,  8,  2),
        ("WP3: Hybrid Ensemble Forecasting", C["pipeline"], 5, 8, 1),
        ("WP4: Drift-Adaptive Retraining",   C["accent1"], 5, 8, 2),
        ("WP5: CPTS-aware EMS",              C["accent2"], 9, 8, 1),
        ("WP6: Integrasi & Validasi Pilot",  C["hw"],      13, 10, 1),
        ("WP7: Diseminasi & Luaran",         C["accent2"], 18, 6, 2),
    ]

    row_h = 50
    for wp_name, wp_col, sm, dur, row in wp_data:
        y = gy + 50 + row * row_h
        x1 = gx + (sm / 24) * gw
        bw = (dur / 24) * gw
        d.add_rect(x1, y, bw, 28, wp_col + "20", wp_col, 100, 6)
        d.add_box(x1 + 8, y + 2, bw - 16, 24, wp_name, "transparent", "none", wp_col, 11, True)
        d.add_box(x1 + bw + 5, y + 4, 50, 20, f"{dur} bln", "transparent", "none", C["muted"], 9)

    # Milestones
    milestones = [
        (7,  "DQ Layer v1", C["edge"]),
        (11, "Forecast v1", C["pipeline"]),
        (12, "EMS Prototype", C["accent2"]),
        (16, "Pilot Integration", C["hw"]),
        (22, "Final Report", C["accent2"]),
    ]
    for mm, mlbl, mcol in milestones:
        mx = gx + (mm / 24) * gw
        my = gy + 48 + 3 * row_h + 40
        d.add_circle(mx - 5, my - 5, 5, mcol, "#fff")
        d.add_box(mx - 30, my + 10, 60, 16, mlbl, "transparent", "none", mcol, 9)

    # TKT labels
    d.add_box(40, 90, 80, 18, "TKT 3", "transparent", "none", C["muted"], 11, True)
    d.add_box(40, 240, 80, 18, "TKT 4", "transparent", "none", C["muted"], 11, True)
    d.add_box(40, 380, 80, 18, "TKT 6", "transparent", "none", C["muted"], 11, True)

    # TKT progression arrow
    tkt_y = 420
    d.add_line(gx + 40, tkt_y, gx + 140, tkt_y, C["arrow"], 2)
    d.add_box(gx + 145, tkt_y - 8, 120, 18, "TKT Progression", "transparent", "none", C["muted"], 9)

    # Legend
    ly = 460
    d.add_box(40, ly, 100, 18, "Legend:", "transparent", "none", C["text"], 11, True)
    l_items = [
        ("AI/Software Dev", C["edge"]),
        ("Modeling/Simulasi", C["cloud"]),
        ("Integrasi", C["hw"]),
        ("Diseminasi", C["accent2"]),
    ]
    for li, (llbl, lcol) in enumerate(l_items):
        lx = 40 + li * 220
        d.add_rect(lx, ly + 10, 14, 14, lcol, lcol, 50, 3)
        d.add_box(lx + 20, ly + 8, 150, 18, llbl, "transparent", "none", C["muted"], 10)

    return d.render()


# ═══════════════════════════════════════════════════════════════════════
# FIG 4 — CPTS Mechanism
# ═══════════════════════════════════════════════════════════════════════
def draw_cpts():
    d = Diagram("CPTS", 800, 380)
    d.add_rect(0, 0, 800, 380, C["bg"], C["bg"], 0, 0)
    d.add_box(0, 8, 800, 30, "Cyber-Physical Trust Score (CPTS) \u2014 Mekanisme Integrasi",
              "transparent", "none", C["text"], 14, True)

    # Three input pillars
    inputs = [
        (60,  80, "Anomaly\nScore",     "\u2022 Autoencoder\n\u2022 Isolation Forest\n\u2022 Statistical", C["err"]),
        (290, 80, "Data Quality\nMetrics", "\u2022 Completeness\n\u2022 Accuracy\n\u2022 Timeliness", C["warn"]),
        (520, 80, "Forecast\nUncertainty", "\u2022 Prediction interval\n\u2022 Ensemble variance\n\u2022 Past error rate", C["cloud"]),
    ]
    for ix, iy, ititle, ibody, icol in inputs:
        d.add_rect(ix, iy, 200, 130, icol + "12", icol, 100, 10)
        d.add_rect(ix, iy, 200, 28, icol, icol, 90, 10)
        lines = ititle.split("\n")
        d.add_box(ix, iy + 2, 200, 24, "<br>".join(lines), "transparent", "none", "#fff", 11, True)
        d.add_box(ix + 10, iy + 36, 180, 84, ibody, "transparent", "none", C["text"], 10)

    # CPTS calculation box
    calc_x, calc_y = 280, 240
    d.add_rect(calc_x, calc_y, 200, 50, C["accent1"] + "15", C["accent1"], 100, 10)
    d.add_box(calc_x + 5, calc_y + 2, 190, 22,
              "CPTS = f(\u03b1\u00b7A + \u03b2\u00b7DQ + \u03b3\u00b7U)",
              "transparent", "none", C["accent1"], 12, True)
    d.add_box(calc_x + 5, calc_y + 26, 190, 20,
              "Bobot adaptif berdasarkan konteks",
              "transparent", "none", C["accent1"], 9)

    # Arrows inputs → calc
    for ax in [160, 390, 620]:
        d.add_line(ax, 210, ax, 238, C["arrow"], 2)

    # EMS objective box
    ox, oy = 560, 240
    d.add_rect(ox, oy, 170, 50, C["accent2"] + "15", C["accent2"], 100, 10)
    d.add_box(ox + 5, oy + 2, 160, 22, "EMS Objective",
              "transparent", "none", C["accent2"], 12, True)
    d.add_box(ox + 5, oy + 26, 160, 20, "min J = J\u2080 + \u03bb\u00b7CPTS",
              "transparent", "none", C["accent2"], 10)

    d.add_line(480, 265, 558, 265, C["arrow"], 2)

    # Decisions at bottom
    decs = [
        (60,  320, "Charge/Discharge\nRate Limit", C["edge"]),
        (240, 320, "PV Curtailing\nThreshold",     C["hw"]),
        (420, 320, "Charger Scheduling\nPriority", C["cloud"]),
        (600, 320, "Grid Import\nLimit",           C["muted"]),
    ]
    for dx, dy, dlbl, dcol in decs:
        d.add_box(dx, dy, 150, 36, dlbl, dcol + "15", dcol, dcol, 10)

    d.add_line(380, 290, 380, 316, C["arrow"], 2)
    d.add_line(480, 290, 480, 316, C["arrow"], 2)

    return d.render()


# ═══════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    figs = [
        ("architecture.drawio", draw_architecture()),
        ("pipeline.drawio",     draw_pipeline()),
        ("methodology.drawio",  draw_methodology()),
        ("cpts.drawio",         draw_cpts()),
    ]
    for fname, content in figs:
        fpath = os.path.join(OUTDIR, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ {fpath}  ({len(content)} bytes)")
    print("Done \u2014 4 draw.io files generated.")
