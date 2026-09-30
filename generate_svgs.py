import os

def create_svg_template(view_box="0 0 820 400"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" width="100%" height="auto" style="max-width: 820px; background: #FFFFFF; border-radius: 12px; border: 1px solid #CBD5E1; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284C7"/>
    </marker>
    <marker id="arrow-orange" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#EA580C"/>
    </marker>
    <marker id="arrow-red" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#DC2626"/>
    </marker>
    <marker id="arrow-first" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0369A1"/>
    </marker>
    <marker id="arrow-last" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#EA580C"/>
    </marker>
    <marker id="arrow-p" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284C7"/>
    </marker>
    <filter id="shadow" x="-4%" y="-8%" width="108%" height="124%">
      <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#0F172A" flood-opacity="0.06"/>
    </filter>
  </defs>
"""

def render_node(x, y, info_text, prev_slash=False, next_slash=False, variant="normal", width=105, height=48):
    styles = {
        "normal": {"bg": "#FFFFFF", "stroke": "#334155", "info_bg": "#F8FAFC", "text": "#0F172A", "slash": "#64748B"},
        "new": {"bg": "#F0FDF4", "stroke": "#16A34A", "info_bg": "#DCFCE7", "text": "#15803D", "slash": "#16A34A"},
        "target": {"bg": "#FEFCE8", "stroke": "#CA8A04", "info_bg": "#FEF08A", "text": "#854D0E", "slash": "#CA8A04"},
        "delete": {"bg": "#FEF2F2", "stroke": "#DC2626", "info_bg": "#FEE2E2", "text": "#B91C1C", "slash": "#DC2626"}
    }
    s = styles.get(variant, styles["normal"])
    comp_prev = 24
    comp_info = width - (comp_prev * 2)
    comp_next = 24
    
    svg = f"""  <!-- Node {info_text} at ({x}, {y}) -->
  <g transform="translate({x}, {y})" filter="url(#shadow)">
    <rect x="0" y="0" width="{width}" height="{height}" fill="{s['bg']}" stroke="{s['stroke']}" stroke-width="1.6"/>
    <rect x="{comp_prev}" y="0" width="{comp_info}" height="{height}" fill="{s['info_bg']}" stroke="{s['stroke']}" stroke-width="1.2"/>
    <line x1="{comp_prev}" y1="0" x2="{comp_prev}" y2="{height}" stroke="{s['stroke']}" stroke-width="1.2"/>
    <line x1="{comp_prev + comp_info}" y1="0" x2="{comp_prev + comp_info}" y2="{height}" stroke="{s['stroke']}" stroke-width="1.2"/>
    <text x="{comp_prev + comp_info/2}" y="{height/2 + 6}" font-size="16" font-weight="bold" fill="{s['text']}" text-anchor="middle">{info_text}</text>
"""
    if prev_slash:
        svg += f"""    <line x1="6" y1="{height-8}" x2="{comp_prev-6}" y2="8" stroke="{s['slash']}" stroke-width="2" stroke-linecap="round"/>\n"""
    if next_slash:
        svg += f"""    <line x1="{width - comp_next + 6}" y1="{height-8}" x2="{width-6}" y2="8" stroke="{s['slash']}" stroke-width="2" stroke-linecap="round"/>\n"""
    svg += "  </g>\n"
    return svg

def render_box(x, y, text, w=48, h=26, stroke="#334155", fill="#FFFFFF", text_color="#0F172A", font_size=11):
    return f"""  <g transform="translate({x}, {y})">
    <rect x="0" y="0" width="{w}" height="{h}" fill="{fill}" stroke="{stroke}" stroke-width="1.4"/>
    <text x="{w/2}" y="{h/2 + 4.5}" font-size="{font_size}" font-weight="600" fill="{text_color}" text-anchor="middle">{text}</text>
  </g>
"""

def render_list_label(x, y):
    return f"""  <text x="{x}" y="{y}" font-size="17" font-weight="bold" fill="#0F172A" font-style="italic">L</text>\n"""

def render_down_arrow(x, y):
    return f"""  <!-- Transition arrow -->
  <g transform="translate({x}, {y})">
    <polygon points="0,0 24,0 24,20 34,20 12,38 -10,20 0,20" fill="#0D9488" stroke="#0F766E" stroke-width="1"/>
  </g>
"""

# -------------------------------------------------------------
# SOAL 01: Insert Empty
# -------------------------------------------------------------
def gen_soal_01():
    out = create_svg_template("0 0 820 400")
    # Title
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">INSERT PADA LIST KOSONG</text>\n'
    
    # 1. INITIAL STATE (Top)
    out += '  <text x="30" y="65" font-size="12" font-weight="bold" fill="#64748B">INITIAL STATE (First(L) &amp; Last(L) masih NULL / nil):</text>\n'
    out += render_list_label(70, 118)
    out += render_box(95, 100, "First", 52, 28, stroke="#0369A1", text_color="#0369A1")
    # arrow from First to [/]
    out += '  <path d="M 147 114 H 195 V 135 H 220" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    # Null Box
    out += render_box(220, 122, "/", 32, 28, stroke="#64748B", fill="#F8FAFC", text_color="#DC2626", font_size=15)
    
    # arrow from Last to [/]
    out += '  <path d="M 330 114 H 285 V 135 H 255" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_box(330, 100, "Last", 52, 28, stroke="#EA580C", text_color="#EA580C")
    
    # Node p at top right
    out += render_box(500, 60, "p", 36, 24, stroke="#0284C7", text_color="#0284C7")
    out += '  <path d="M 536 72 H 580 V 96" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(527, 98, "D", prev_slash=True, next_slash=True, variant="new")

    # Algorithm box at top
    out += """  <g transform="translate(660, 50)">
    <rect x="0" y="0" width="130" height="75" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2"/>
    <text x="12" y="20" font-size="11" font-weight="bold" fill="#15803D">Algoritma:</text>
    <text x="12" y="42" font-size="11" font-weight="bold" fill="#166534">First(L) &lt;- p</text>
    <text x="12" y="62" font-size="11" font-weight="bold" fill="#166534">Last(L) &lt;- p</text>
  </g>
"""

    out += render_down_arrow(398, 175)

    # 2. FINAL STATE (Bottom)
    out += '  <text x="30" y="235" font-size="12" font-weight="bold" fill="#64748B">HASIL AKHIR (First(L) &lt;- p, Last(L) &lt;- p):</text>\n'
    out += render_list_label(70, 310)
    out += render_box(95, 292, "First", 52, 28, stroke="#0369A1", text_color="#0369A1")
    # arrow First to p
    out += '  <path d="M 147 306 H 240 V 315 H 270" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    # Node p
    out += render_box(240, 245, "p", 36, 24, stroke="#0284C7", text_color="#0284C7")
    out += '  <path d="M 276 257 H 322 V 288" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(270, 290, "D", prev_slash=True, next_slash=True, variant="new")
    
    # arrow Last to p
    out += render_box(460, 292, "Last", 52, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 460 306 H 405 V 315 H 378" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 02: Insert First
# -------------------------------------------------------------
def gen_soal_02():
    out = create_svg_template("0 0 820 400")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">INSERT FIRST</text>\n'
    
    # Algoritma box
    out += """  <g transform="translate(615, 25)">
    <rect x="0" y="0" width="175" height="85" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2"/>
    <text x="12" y="18" font-size="11" font-weight="bold" fill="#15803D">Algoritma:</text>
    <text x="12" y="37" font-size="11" font-weight="bold" fill="#166534">next(p) &lt;- First(L)</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#166534">prev(First(L)) &lt;- p</text>
    <text x="12" y="73" font-size="11" font-weight="bold" fill="#166534">First(L) &lt;- p</text>
  </g>
"""
    # 1. INITIAL STATE (Top)
    # Node p above
    out += render_box(160, 40, "p", 36, 24, stroke="#0284C7", text_color="#0284C7")
    out += '  <path d="M 196 52 H 235 V 70" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(185, 72, "E", prev_slash=True, next_slash=True, variant="new")
    
    # List L below
    out += render_list_label(45, 138)
    out += render_box(65, 120, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 148 V 162 H 270" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    # 3 Nodes (A, B, C)
    out += render_node(270, 140, "A", prev_slash=True, next_slash=False, variant="normal")
    # links A <-> B
    out += '  <path d="M 363 154 H 410" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 422 172 H 378" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(410, 140, "B", prev_slash=False, next_slash=False, variant="normal")
    # links B <-> C
    out += '  <path d="M 503 154 H 550" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 562 172 H 518" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(550, 140, "C", prev_slash=False, next_slash=True, variant="normal")
    
    out += render_box(670, 120, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 695 148 V 162 H 658" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_down_arrow(398, 195)

    # 2. FINAL STATE (Bottom)
    out += render_box(160, 245, "p", 36, 24, stroke="#0284C7", text_color="#0284C7")
    out += '  <path d="M 196 257 H 235 V 275" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(185, 277, "E", prev_slash=True, next_slash=False, variant="new")
    
    out += render_list_label(45, 343)
    out += render_box(65, 325, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    # First points to node E (p)
    out += '  <path d="M 115 339 H 155 V 295 H 182" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    # next(p) points down-right to A
    out += '  <path d="M 278 290 H 295 V 355 H 322" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    # prev(A) points up-left to E
    out += '  <path d="M 334 373 H 250 V 315 H 250 V 305 H 243 V 305" fill="none" stroke="#EA580C" stroke-width="0"/>\n'
    out += '  <path d="M 334 373 H 245 V 305 H 245" fill="none" stroke="#EA580C" stroke-width="2"/>\n'
    out += '  <path d="M 245 305 V 295 H 245" fill="none" stroke="#EA580C" stroke-width="2"/>\n'
    out += '  <line x1="245" y1="315" x2="245" y2="295" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    # Nodes A, B, C below
    out += render_node(325, 345, "A", prev_slash=False, next_slash=False, variant="normal")
    out += '  <path d="M 418 359 H 465" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 477 377 H 433" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(465, 345, "B", prev_slash=False, next_slash=False, variant="normal")
    out += '  <path d="M 558 359 H 605" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 617 377 H 573" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(605, 345, "C", prev_slash=False, next_slash=True, variant="normal")

    out += render_box(725, 325, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 750 353 V 367 H 713" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 03: Insert Last
# -------------------------------------------------------------
def gen_soal_03():
    out = create_svg_template("0 0 820 400")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">INSERT LAST</text>\n'
    
    out += """  <g transform="translate(615, 25)">
    <rect x="0" y="0" width="175" height="85" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2"/>
    <text x="12" y="18" font-size="11" font-weight="bold" fill="#15803D">Algoritma:</text>
    <text x="12" y="37" font-size="11" font-weight="bold" fill="#166534">prev(p) &lt;- Last(L)</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#166534">next(Last(L)) &lt;- p</text>
    <text x="12" y="73" font-size="11" font-weight="bold" fill="#166534">Last(L) &lt;- p</text>
  </g>
"""
    # 1. INITIAL STATE
    out += render_list_label(45, 138)
    out += render_box(65, 120, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 148 V 162 H 145" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    out += render_node(145, 140, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 238 154 H 285" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 297 172 H 253" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(285, 140, "B", prev_slash=False, next_slash=False, variant="normal")
    out += '  <path d="M 378 154 H 425" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 437 172 H 393" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(425, 140, "C", prev_slash=False, next_slash=True, variant="normal")

    out += render_box(545, 120, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 570 148 V 162 H 533" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    # Node p above-right
    out += render_box(460, 40, "p", 36, 24, stroke="#0284C7", text_color="#0284C7")
    out += '  <path d="M 496 52 H 535 V 70" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(490, 72, "F", prev_slash=True, next_slash=True, variant="new")

    out += render_down_arrow(398, 195)

    # 2. FINAL STATE (Bottom)
    out += render_list_label(45, 343)
    out += render_box(65, 325, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 353 V 367 H 145" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    out += render_node(145, 345, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 238 359 H 285" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 297 377 H 253" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(285, 345, "B", prev_slash=False, next_slash=False, variant="normal")
    out += '  <path d="M 378 359 H 425" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 437 377 H 393" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(425, 345, "C", prev_slash=False, next_slash=False, variant="normal")

    # Node p at right
    out += render_box(535, 245, "p", 36, 24, stroke="#0284C7", text_color="#0284C7")
    out += '  <path d="M 571 257 H 605 V 275" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(565, 277, "F", prev_slash=False, next_slash=True, variant="new")

    # next(C) points up-right to F
    out += '  <path d="M 518 360 H 545 V 300 H 562" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    # prev(F) points down-left to C
    out += '  <path d="M 577 280 H 530 V 375 H 533" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    # Last points to F (p)
    out += render_box(720, 325, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 745 325 V 295 H 673" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 04: Insert After
# -------------------------------------------------------------
def gen_soal_04():
    out = create_svg_template("0 0 820 400")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">INSERT AFTER (Sisip Setelah Target)</text>\n'
    
    out += """  <g transform="translate(605, 20)">
    <rect x="0" y="0" width="185" height="100" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2"/>
    <text x="12" y="16" font-size="11" font-weight="bold" fill="#15803D">Algoritma:</text>
    <text x="12" y="33" font-size="10.5" font-weight="bold" fill="#166534">Q &lt;- next(target)</text>
    <text x="12" y="49" font-size="10.5" font-weight="bold" fill="#166534">prev(P) &lt;- target</text>
    <text x="12" y="65" font-size="10.5" font-weight="bold" fill="#166534">next(P) &lt;- Q</text>
    <text x="12" y="81" font-size="10.5" font-weight="bold" fill="#166534">next(target) &lt;- P</text>
    <text x="12" y="95" font-size="10.5" font-weight="bold" fill="#166534">prev(Q) &lt;- P</text>
  </g>
"""
    # 1. INITIAL STATE
    out += render_list_label(45, 138)
    out += render_box(65, 120, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 148 V 162 H 145" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    out += render_node(145, 140, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 238 154 H 285" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 297 172 H 253" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    
    # Target "B"
    out += render_box(315, 95, "target", 48, 22, stroke="#CA8A04", text_color="#854D0E", font_size=10)
    out += '  <line x1="339" y1="117" x2="339" y2="138" stroke="#CA8A04" stroke-width="1.8" marker-end="url(#arrow-last)"/>\n'
    out += render_node(285, 140, "B", prev_slash=False, next_slash=False, variant="target")
    
    out += '  <path d="M 378 154 H 425" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 437 172 H 393" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    
    # Q "C"
    out += render_box(455, 95, "Q", 42, 22, stroke="#0891B2", text_color="#0891B2", font_size=10)
    out += '  <line x1="476" y1="117" x2="476" y2="138" stroke="#0891B2" stroke-width="1.8" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(425, 140, "C", prev_slash=False, next_slash=True, variant="normal")

    out += render_box(545, 120, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 570 148 V 162 H 533" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    # Node P above
    out += render_box(330, 35, "P", 36, 24, stroke="#0284C7", text_color="#0284C7")
    out += '  <path d="M 366 47 H 400 V 65" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(355, 67, "G", prev_slash=True, next_slash=True, variant="new")

    out += render_down_arrow(398, 205)

    # 2. FINAL STATE
    out += render_list_label(45, 343)
    out += render_box(65, 325, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 353 V 367 H 135" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    out += render_node(135, 345, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 228 359 H 265" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 277 377 H 243" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    
    out += render_node(265, 345, "B", prev_slash=False, next_slash=False, variant="target")
    out += '  <path d="M 358 359 H 395" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 407 377 H 373" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(395, 345, "G", prev_slash=False, next_slash=False, variant="new")
    out += '  <path d="M 488 359 H 525" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 537 377 H 503" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(525, 345, "C", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(645, 325, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 670 353 V 367 H 633" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 05: Insert Before
# -------------------------------------------------------------
def gen_soal_05():
    out = create_svg_template("0 0 820 400")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">INSERT BEFORE (Sisip Sebelum Target)</text>\n'
    
    out += """  <g transform="translate(605, 20)">
    <rect x="0" y="0" width="185" height="100" rx="6" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2"/>
    <text x="12" y="16" font-size="11" font-weight="bold" fill="#15803D">Algoritma:</text>
    <text x="12" y="33" font-size="10.5" font-weight="bold" fill="#166534">Q &lt;- prev(target)</text>
    <text x="12" y="49" font-size="10.5" font-weight="bold" fill="#166534">next(P) &lt;- target</text>
    <text x="12" y="65" font-size="10.5" font-weight="bold" fill="#166534">prev(P) &lt;- Q</text>
    <text x="12" y="81" font-size="10.5" font-weight="bold" fill="#166534">prev(target) &lt;- P</text>
    <text x="12" y="95" font-size="10.5" font-weight="bold" fill="#166534">next(Q) &lt;- P</text>
  </g>
"""
    # 1. INITIAL STATE
    out += render_list_label(45, 138)
    out += render_box(65, 120, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 148 V 162 H 145" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    # Q "A"
    out += render_box(175, 95, "Q", 42, 22, stroke="#0891B2", text_color="#0891B2", font_size=10)
    out += '  <line x1="196" y1="117" x2="196" y2="138" stroke="#0891B2" stroke-width="1.8" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(145, 140, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 238 154 H 285" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 297 172 H 253" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    
    # Target "B"
    out += render_box(315, 95, "target", 48, 22, stroke="#CA8A04", text_color="#854D0E", font_size=10)
    out += '  <line x1="339" y1="117" x2="339" y2="138" stroke="#CA8A04" stroke-width="1.8" marker-end="url(#arrow-last)"/>\n'
    out += render_node(285, 140, "B", prev_slash=False, next_slash=False, variant="target")
    
    out += '  <path d="M 378 154 H 425" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 437 172 H 393" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(425, 140, "C", prev_slash=False, next_slash=True, variant="normal")

    out += render_box(545, 120, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 570 148 V 162 H 533" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    # Node P above
    out += render_box(215, 35, "P", 36, 24, stroke="#0284C7", text_color="#0284C7")
    out += '  <path d="M 251 47 H 285 V 65" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(240, 67, "H", prev_slash=True, next_slash=True, variant="new")

    out += render_down_arrow(398, 205)

    # 2. FINAL STATE
    out += render_list_label(45, 343)
    out += render_box(65, 325, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 353 V 367 H 135" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    out += render_node(135, 345, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 228 359 H 265" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 277 377 H 243" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(265, 345, "H", prev_slash=False, next_slash=False, variant="new")
    out += '  <path d="M 358 359 H 395" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 407 377 H 373" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(395, 345, "B", prev_slash=False, next_slash=False, variant="target")
    out += '  <path d="M 488 359 H 525" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 537 377 H 503" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(525, 345, "C", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(645, 325, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 670 353 V 367 H 633" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 06: Traversal Maju
# -------------------------------------------------------------
def gen_soal_06():
    out = create_svg_template("0 0 820 280")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">TRAVERSE MAJU (First(L) -&gt; Last(L))</text>\n'
    
    out += render_list_label(50, 118)
    out += render_box(75, 100, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 100 128 V 142 H 170" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'

    out += render_box(195, 60, "P (Mulai)", 65, 24, stroke="#0284C7", fill="#E0F2FE", text_color="#0369A1", font_size=10)
    out += '  <line x1="227" y1="84" x2="227" y2="118" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'

    out += render_node(170, 120, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 263 134 H 330" fill="none" stroke="#0284C7" stroke-width="2.5" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 342 152 H 278" fill="none" stroke="#EA580C" stroke-width="1.5" marker-end="url(#arrow-orange)"/>\n'
    
    out += render_node(330, 120, "B", prev_slash=False, next_slash=False, variant="normal")
    out += '  <path d="M 423 134 H 490" fill="none" stroke="#0284C7" stroke-width="2.5" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 502 152 H 438" fill="none" stroke="#EA580C" stroke-width="1.5" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(490, 120, "C", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(610, 100, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 635 128 V 142 H 598" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += """  <g transform="translate(170, 205)">
    <rect x="0" y="0" width="450" height="46" rx="8" fill="#F0FDF4" stroke="#86EFAC" stroke-width="1.2"/>
    <text x="225" y="28" font-size="14" font-weight="bold" fill="#15803D" text-anchor="middle">Hasil Return String:  &quot;A &lt;-&gt; B &lt;-&gt; C&quot;</text>
  </g>
</svg>"""
    return out

# -------------------------------------------------------------
# SOAL 07: Traversal Mundur
# -------------------------------------------------------------
def gen_soal_07():
    out = create_svg_template("0 0 820 280")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">TRAVERSE MUNDUR (Last(L) -&gt; First(L))</text>\n'
    
    out += render_list_label(50, 118)
    out += render_box(75, 100, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 100 128 V 142 H 170" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'

    out += render_node(170, 120, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 263 134 H 330" fill="none" stroke="#0284C7" stroke-width="1.5" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 342 152 H 278" fill="none" stroke="#EA580C" stroke-width="2.5" marker-end="url(#arrow-orange)"/>\n'
    
    out += render_node(330, 120, "B", prev_slash=False, next_slash=False, variant="normal")
    out += '  <path d="M 423 134 H 490" fill="none" stroke="#0284C7" stroke-width="1.5" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 502 152 H 438" fill="none" stroke="#EA580C" stroke-width="2.5" marker-end="url(#arrow-orange)"/>\n'

    out += render_box(515, 60, "P (Mulai)", 65, 24, stroke="#EA580C", fill="#FFF7ED", text_color="#C2410C", font_size=10)
    out += '  <line x1="547" y1="84" x2="547" y2="118" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(490, 120, "C", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(610, 100, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 635 128 V 142 H 598" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += """  <g transform="translate(170, 205)">
    <rect x="0" y="0" width="450" height="46" rx="8" fill="#FFF7ED" stroke="#FED7AA" stroke-width="1.2"/>
    <text x="225" y="28" font-size="14" font-weight="bold" fill="#C2410C" text-anchor="middle">Hasil Return String:  &quot;C &lt;-&gt; B &lt;-&gt; A&quot;</text>
  </g>
</svg>"""
    return out

# -------------------------------------------------------------
# SOAL 08: Search Node
# -------------------------------------------------------------
def gen_soal_08():
    out = create_svg_template("0 0 820 280")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">SEARCH NODE (Mencari info(P) == target)</text>\n'
    
    out += render_list_label(50, 118)
    out += render_box(75, 100, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 100 128 V 142 H 170" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'

    out += render_node(170, 120, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 263 134 H 330" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 342 152 H 278" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    
    out += render_box(345, 60, "P (Ditemukan!)", 85, 24, stroke="#CA8A04", fill="#FEF08A", text_color="#854D0E", font_size=10)
    out += '  <line x1="387" y1="84" x2="387" y2="118" stroke="#CA8A04" stroke-width="2" marker-end="url(#arrow-last)"/>\n'

    out += render_node(330, 120, "B", prev_slash=False, next_slash=False, variant="target")
    out += '  <path d="M 423 134 H 490" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 502 152 H 438" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(490, 120, "C", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(610, 100, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 635 128 V 142 H 598" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += """  <g transform="translate(170, 205)">
    <rect x="0" y="0" width="450" height="46" rx="8" fill="#FEFCE8" stroke="#FEF08A" stroke-width="1.2"/>
    <text x="225" y="28" font-size="14" font-weight="bold" fill="#854D0E" text-anchor="middle">Hasil Return: Objek Node P (&quot;B&quot;)</text>
  </g>
</svg>"""
    return out

# -------------------------------------------------------------
# SOAL 09: Delete First
# -------------------------------------------------------------
def gen_soal_09():
    out = create_svg_template("0 0 820 400")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">DELETE FIRST</text>\n'
    
    out += """  <g transform="translate(615, 25)">
    <rect x="0" y="0" width="175" height="85" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.2"/>
    <text x="12" y="18" font-size="11" font-weight="bold" fill="#991B1B">Algoritma:</text>
    <text x="12" y="37" font-size="11" font-weight="bold" fill="#B91C1C">P &lt;- First(L)</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#B91C1C">First(L) &lt;- next(First(L))</text>
    <text x="12" y="73" font-size="11" font-weight="bold" fill="#B91C1C">prev(First(L)) &lt;- NULL</text>
  </g>
"""
    # 1. INITIAL STATE
    out += render_list_label(45, 138)
    out += render_box(65, 120, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 148 V 162 H 170" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    out += render_box(195, 75, "P (dihapus)", 70, 22, stroke="#DC2626", fill="#FEE2E2", text_color="#B91C1C", font_size=10)
    out += '  <line x1="230" y1="97" x2="230" y2="118" stroke="#DC2626" stroke-width="1.8" marker-end="url(#arrow-red)"/>\n'

    out += render_node(170, 120, "A", prev_slash=True, next_slash=False, variant="delete")
    out += '  <path d="M 263 134 H 330" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 342 152 H 278" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    
    out += render_node(330, 120, "B", prev_slash=False, next_slash=False, variant="normal")
    out += '  <path d="M 423 134 H 490" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 502 152 H 438" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(490, 120, "C", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(610, 120, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 635 148 V 162 H 598" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_down_arrow(398, 195)

    # 2. FINAL STATE
    out += render_list_label(45, 318)
    out += render_box(165, 300, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 190 328 V 342 H 260" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'

    out += render_node(260, 300, "B", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 353 314 H 420" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 432 332 H 368" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(420, 300, "C", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(540, 300, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 565 328 V 342 H 528" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 10: Delete Last
# -------------------------------------------------------------
def gen_soal_10():
    out = create_svg_template("0 0 820 400")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">DELETE LAST</text>\n'
    
    out += """  <g transform="translate(615, 25)">
    <rect x="0" y="0" width="175" height="85" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.2"/>
    <text x="12" y="18" font-size="11" font-weight="bold" fill="#991B1B">Algoritma:</text>
    <text x="12" y="37" font-size="11" font-weight="bold" fill="#B91C1C">P &lt;- Last(L)</text>
    <text x="12" y="55" font-size="11" font-weight="bold" fill="#B91C1C">Last(L) &lt;- prev(Last(L))</text>
    <text x="12" y="73" font-size="11" font-weight="bold" fill="#B91C1C">next(Last(L)) &lt;- NULL</text>
  </g>
"""
    # 1. INITIAL STATE
    out += render_list_label(45, 138)
    out += render_box(65, 120, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 148 V 162 H 170" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    out += render_node(170, 120, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 263 134 H 330" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 342 152 H 278" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    
    out += render_node(330, 120, "B", prev_slash=False, next_slash=False, variant="normal")
    out += '  <path d="M 423 134 H 490" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 502 152 H 438" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_box(515, 75, "P (dihapus)", 70, 22, stroke="#DC2626", fill="#FEE2E2", text_color="#B91C1C", font_size=10)
    out += '  <line x1="550" y1="97" x2="550" y2="118" stroke="#DC2626" stroke-width="1.8" marker-end="url(#arrow-red)"/>\n'

    out += render_node(490, 120, "C", prev_slash=False, next_slash=True, variant="delete")
    out += render_box(610, 120, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 635 148 V 162 H 598" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_down_arrow(398, 195)

    # 2. FINAL STATE
    out += render_list_label(45, 318)
    out += render_box(165, 300, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 190 328 V 342 H 260" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'

    out += render_node(260, 300, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 353 314 H 420" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 432 332 H 368" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(420, 300, "B", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(540, 300, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 565 328 V 342 H 528" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 11: Delete Node
# -------------------------------------------------------------
def gen_soal_11():
    out = create_svg_template("0 0 820 400")
    out += '  <text x="30" y="32" font-size="16" font-weight="bold" fill="#1E293B">DELETE TARGET NODE</text>\n'
    
    out += """  <g transform="translate(615, 25)">
    <rect x="0" y="0" width="175" height="85" rx="6" fill="#FEF2F2" stroke="#FCA5A5" stroke-width="1.2"/>
    <text x="12" y="18" font-size="11" font-weight="bold" fill="#991B1B">Algoritma:</text>
    <text x="12" y="37" font-size="10.5" font-weight="bold" fill="#B91C1C">P &lt;- prev(target)</text>
    <text x="12" y="53" font-size="10.5" font-weight="bold" fill="#B91C1C">Q &lt;- next(target)</text>
    <text x="12" y="69" font-size="10.5" font-weight="bold" fill="#B91C1C">next(P) &lt;- Q</text>
    <text x="12" y="83" font-size="10.5" font-weight="bold" fill="#B91C1C">prev(Q) &lt;- P</text>
  </g>
"""
    # 1. INITIAL STATE
    out += render_list_label(45, 138)
    out += render_box(65, 120, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 90 148 V 162 H 170" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    
    # P "A"
    out += render_box(195, 75, "P", 42, 22, stroke="#0891B2", text_color="#0891B2", font_size=10)
    out += '  <line x1="216" y1="97" x2="216" y2="118" stroke="#0891B2" stroke-width="1.8" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(170, 120, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 263 134 H 330" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 342 152 H 278" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'
    
    # Target "B"
    out += render_box(345, 75, "target", 50, 22, stroke="#DC2626", fill="#FEE2E2", text_color="#B91C1C", font_size=10)
    out += '  <line x1="370" y1="97" x2="370" y2="118" stroke="#DC2626" stroke-width="1.8" marker-end="url(#arrow-red)"/>\n'
    out += render_node(330, 120, "B", prev_slash=False, next_slash=False, variant="delete")
    out += '  <path d="M 423 134 H 490" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 502 152 H 438" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    # Q "C"
    out += render_box(515, 75, "Q", 42, 22, stroke="#0891B2", text_color="#0891B2", font_size=10)
    out += '  <line x1="536" y1="97" x2="536" y2="118" stroke="#0891B2" stroke-width="1.8" marker-end="url(#arrow-blue)"/>\n'
    out += render_node(490, 120, "C", prev_slash=False, next_slash=True, variant="normal")

    out += render_box(610, 120, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 635 148 V 162 H 598" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_down_arrow(398, 195)

    # 2. FINAL STATE
    out += render_list_label(45, 318)
    out += render_box(165, 300, "First", 50, 28, stroke="#0369A1", text_color="#0369A1")
    out += '  <path d="M 190 328 V 342 H 260" fill="none" stroke="#0369A1" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'

    out += render_node(260, 300, "A", prev_slash=True, next_slash=False, variant="normal")
    out += '  <path d="M 353 314 H 420" fill="none" stroke="#0284C7" stroke-width="2" marker-end="url(#arrow-blue)"/>\n'
    out += '  <path d="M 432 332 H 368" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += render_node(420, 300, "C", prev_slash=False, next_slash=True, variant="normal")
    out += render_box(540, 300, "Last", 50, 28, stroke="#EA580C", text_color="#EA580C")
    out += '  <path d="M 565 328 V 342 H 528" fill="none" stroke="#EA580C" stroke-width="2" marker-end="url(#arrow-orange)"/>\n'

    out += "</svg>"
    return out

generators = {
    "soal_01.svg": gen_soal_01,
    "soal_02.svg": gen_soal_02,
    "soal_03.svg": gen_soal_03,
    "soal_04.svg": gen_soal_04,
    "soal_05.svg": gen_soal_05,
    "soal_06.svg": gen_soal_06,
    "soal_07.svg": gen_soal_07,
    "soal_08.svg": gen_soal_08,
    "soal_09.svg": gen_soal_09,
    "soal_10.svg": gen_soal_10,
    "soal_11.svg": gen_soal_11,
}

if __name__ == "__main__":
    os.makedirs("/Users/fandisyarahman/Documents/soalstrukdat/gambar", exist_ok=True)
    for filename, fn in generators.items():
        filepath = os.path.join("/Users/fandisyarahman/Documents/soalstrukdat/gambar", filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fn())
        print(f"Generated {filename}")
