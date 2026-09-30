import os

def create_svg_template(view_box="0 0 800 370"):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{view_box}" width="100%" height="auto" style="max-width: 800px; background: #FFFFFF; border-radius: 12px; border: 1px solid #CBD5E1; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <marker id="arrow-blue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0284C7"/>
    </marker>
    <marker id="arrow-orange" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#EA580C"/>
    </marker>
    <marker id="arrow-first" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0369A1"/>
    </marker>
    <marker id="arrow-last" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#C2410C"/>
    </marker>
    <marker id="arrow-p" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#7C3AED"/>
    </marker>
    <marker id="arrow-q" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#0891B2"/>
    </marker>
    <filter id="shadow" x="-5%" y="-10%" width="110%" height="130%">
      <feDropShadow dx="0" dy="2" stdDeviation="2.5" flood-color="#0F172A" flood-opacity="0.08"/>
    </filter>
  </defs>
"""

def render_node(x, y, data_text, prev_null=False, next_null=False, variant="normal", width=110, height=52):
    styles = {
        "normal": {
            "outer_fill": "#F8FAFC", "outer_stroke": "#0284C7",
            "data_fill": "#E0F2FE", "text_color": "#0369A1", "subtext": "#64748B", "dot": "#0284C7"
        },
        "new": {
            "outer_fill": "#F0FDF4", "outer_stroke": "#16A34A",
            "data_fill": "#DCFCE7", "text_color": "#15803D", "subtext": "#16A34A", "dot": "#16A34A"
        },
        "target": {
            "outer_fill": "#FEFCE8", "outer_stroke": "#CA8A04",
            "data_fill": "#FEF08A", "text_color": "#A16207", "subtext": "#854D0E", "dot": "#CA8A04"
        },
        "delete": {
            "outer_fill": "#FEF2F2", "outer_stroke": "#DC2626",
            "data_fill": "#FEE2E2", "text_color": "#B91C1C", "subtext": "#DC2626", "dot": "#DC2626"
        },
        "helper": {
            "outer_fill": "#F5F3FF", "outer_stroke": "#7C3AED",
            "data_fill": "#EDE9FE", "text_color": "#6D28D9", "subtext": "#7C3AED", "dot": "#7C3AED"
        }
    }
    s = styles.get(variant, styles["normal"])
    
    comp_prev = 28
    comp_data = width - (comp_prev * 2)
    comp_next = 28
    
    svg = f"""  <!-- Node {data_text} -->
  <g transform="translate({x}, {y})" filter="url(#shadow)">
    <rect x="0" y="0" width="{width}" height="{height}" rx="7" fill="{s['outer_fill']}" stroke="{s['outer_stroke']}" stroke-width="1.8"/>
    <rect x="{comp_prev}" y="0" width="{comp_data}" height="{height}" fill="{s['data_fill']}" stroke="{s['outer_stroke']}" stroke-width="1.2"/>
    <line x1="{comp_prev}" y1="0" x2="{comp_prev}" y2="{height}" stroke="{s['outer_stroke']}" stroke-width="1.2"/>
    <line x1="{comp_prev + comp_data}" y1="0" x2="{comp_prev + comp_data}" y2="{height}" stroke="{s['outer_stroke']}" stroke-width="1.2"/>
    <text x="{comp_prev/2}" y="12" font-size="7.5" fill="{s['subtext']}" text-anchor="middle" font-weight="600">prev</text>
    <text x="{comp_prev + comp_data/2}" y="33" font-size="18" font-weight="bold" fill="{s['text_color']}" text-anchor="middle">{data_text}</text>
    <text x="{width - comp_next/2}" y="12" font-size="7.5" fill="{s['subtext']}" text-anchor="middle" font-weight="600">next</text>
"""
    if prev_null:
        svg += f"""    <line x1="6" y1="{height-10}" x2="{comp_prev-6}" y2="16" stroke="#DC2626" stroke-width="2.2" stroke-linecap="round"/>
"""
    else:
        svg += f"""    <circle cx="{comp_prev/2}" cy="{height/2 + 7}" r="3" fill="{s['dot']}"/>
"""

    if next_null:
        svg += f"""    <line x1="{width - comp_next + 6}" y1="{height-10}" x2="{width - 6}" y2="16" stroke="#DC2626" stroke-width="2.2" stroke-linecap="round"/>
"""
    else:
        svg += f"""    <circle cx="{width - comp_next/2}" cy="{height/2 + 7}" r="3" fill="{s['dot']}"/>
"""
    svg += "  </g>\n"
    return svg

def render_pointer(x_center, y_top, label="First(L)", p_type="first", width=None):
    colors = {
        "first": ("#0369A1", "url(#arrow-first)"),
        "last": ("#C2410C", "url(#arrow-last)"),
        "p": ("#7C3AED", "url(#arrow-p)"),
        "q": ("#0891B2", "url(#arrow-q)"),
        "target": ("#CA8A04", "url(#arrow-first)"),
        "blue": ("#2563EB", "url(#arrow-blue)")
    }
    color, marker = colors.get(p_type, ("#0369A1", "url(#arrow-first)"))
    badge_w = width if width else (max(52, len(label) * 7.5 + 14))
    badge_h = 20
    bx = x_center - (badge_w / 2)
    return f"""  <!-- Pointer Badge {label} -->
  <g transform="translate({bx}, {y_top})">
    <rect x="0" y="0" width="{badge_w}" height="{badge_h}" rx="4" fill="{color}"/>
    <text x="{badge_w/2}" y="14" font-size="9.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle" letter-spacing="0.5">{label}</text>
  </g>
  <line x1="{x_center}" y1="{y_top + badge_h}" x2="{x_center}" y2="{y_top + badge_h + 12}" stroke="{color}" stroke-width="1.8" marker-end="{marker}"/>
"""

def render_link(x1, x2, y_fwd=104, y_bwd=120):
    return f"""  <!-- Links -->
  <line x1="{x1}" y1="{y_fwd}" x2="{x2}" y2="{y_fwd}" stroke="#0284C7" stroke-width="1.8" marker-end="url(#arrow-blue)"/>
  <line x1="{x2}" y1="{y_bwd}" x2="{x1}" y2="{y_bwd}" stroke="#EA580C" stroke-width="1.8" marker-end="url(#arrow-orange)"/>
"""

def render_bottom_tag(x_center, y_top, text, variant="info"):
    colors = {
        "info": {"bg": "#F1F5F9", "border": "#CBD5E1", "text": "#475569"},
        "new": {"bg": "#DCFCE7", "border": "#86EFAC", "text": "#15803D"},
        "target": {"bg": "#FEF9C3", "border": "#FDE047", "text": "#854D0E"},
        "delete": {"bg": "#FEE2E2", "border": "#FCA5A5", "text": "#991B1B"},
        "p": {"bg": "#F5F3FF", "border": "#DDD6FE", "text": "#6D28D9"},
        "q": {"bg": "#ECFEFF", "border": "#A5F3FC", "text": "#0E7490"},
    }
    c = colors.get(variant, colors["info"])
    tw = len(text) * 6.5 + 16
    bx = x_center - (tw / 2)
    return f"""  <g transform="translate({bx}, {y_top})">
    <rect x="0" y="0" width="{tw}" height="{19}" rx="4" fill="{c['bg']}" stroke="{c['border']}" stroke-width="1"/>
    <text x="{tw/2}" y="13.5" font-size="10" font-weight="600" fill="{c['text']}" text-anchor="middle">{text}</text>
  </g>
"""

# -------------------------------------------------------------
# SOAL 01: Insert Empty
# -------------------------------------------------------------
def gen_soal_01():
    out = create_svg_template("0 0 800 370")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">1. Kondisi Awal (List L masih kosong, Node baru P dialokasikan):</text>\n'
    out += render_pointer(220, 50, "First(L) = NULL", "first", width=95)
    out += render_pointer(360, 50, "Last(L) = NULL", "last", width=95)
    out += render_pointer(580, 50, "P (Node Baru)", "p", width=95)
    
    out += """  <g transform="translate(170, 86)">
    <rect x="0" y="0" width="100" height="48" rx="6" fill="#F8FAFC" stroke="#94A3B8" stroke-dasharray="4 4" stroke-width="1.5"/>
    <text x="50" y="29" font-size="12" font-weight="bold" fill="#94A3B8" text-anchor="middle">NULL</text>
  </g>
  <g transform="translate(310, 86)">
    <rect x="0" y="0" width="100" height="48" rx="6" fill="#F8FAFC" stroke="#94A3B8" stroke-dasharray="4 4" stroke-width="1.5"/>
    <text x="50" y="29" font-size="12" font-weight="bold" fill="#94A3B8" text-anchor="middle">NULL</text>
  </g>
"""
    out += render_node(525, 86, "D", prev_null=True, next_null=True, variant="new")
    out += render_bottom_tag(580, 145, "P = BIKIN_NODE(&quot;D&quot;)", "p")

    out += '  <line x1="30" y1="175" x2="770" y2="175" stroke="#E2E8F0" stroke-width="1"/>\n'
    out += '  <text x="30" y="205" font-size="13" font-weight="bold" fill="#0F172A">2. Hasil Akhir (First(L) &lt;- P, Last(L) &lt;- P):</text>\n'
    out += render_pointer(315, 222, "First(L)", "first")
    out += render_pointer(485, 222, "Last(L)", "last")
    out += render_node(345, 260, "D", prev_null=True, next_null=True, variant="new")
    out += render_bottom_tag(400, 322, "First(L) = Last(L) = P", "new")
    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 02: Insert First
# -------------------------------------------------------------
def gen_soal_02():
    out = create_svg_template("0 0 800 370")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">1. Kondisi Awal (Node Baru P di depan + List &quot;A&quot; &lt;-&gt; &quot;B&quot; &lt;-&gt; &quot;C&quot;):</text>\n'
    out += render_pointer(115, 48, "P (Node Baru)", "p", width=95)
    out += render_pointer(275, 48, "First(L)", "first")
    out += render_pointer(595, 48, "Last(L)", "last")
    
    out += render_node(60, 86, "E", prev_null=True, next_null=True, variant="new")
    out += render_bottom_tag(115, 145, "P = BIKIN_NODE(&quot;E&quot;)", "p")
    
    out += render_node(220, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(330, 380, 104, 120)
    out += render_node(380, 86, "B", prev_null=False, next_null=False, variant="normal")
    out += render_link(490, 540, 104, 120)
    out += render_node(540, 86, "C", prev_null=False, next_null=True, variant="normal")

    out += '  <line x1="30" y1="175" x2="770" y2="175" stroke="#E2E8F0" stroke-width="1"/>\n'
    out += '  <text x="30" y="205" font-size="13" font-weight="bold" fill="#0F172A">2. Hasil Akhir (P tersambung di depan &quot;A&quot;, First(L) &lt;- P):</text>\n'
    out += render_pointer(115, 222, "First(L) (P)", "first", width=80)
    out += render_pointer(595, 222, "Last(L)", "last")
    out += render_node(60, 260, "E", prev_null=True, next_null=False, variant="new")
    out += render_link(170, 220, 278, 294)
    out += render_node(220, 260, "A", prev_null=False, next_null=False, variant="normal")
    out += render_link(330, 380, 278, 294)
    out += render_node(380, 260, "B", prev_null=False, next_null=False, variant="normal")
    out += render_link(490, 540, 278, 294)
    out += render_node(540, 260, "C", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(115, 322, "First(L) Baru (P)", "new")
    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 03: Insert Last
# -------------------------------------------------------------
def gen_soal_03():
    out = create_svg_template("0 0 800 370")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">1. Kondisi Awal (List &quot;A&quot; &lt;-&gt; &quot;B&quot; &lt;-&gt; &quot;C&quot; + Node Baru P di belakang):</text>\n'
    out += render_pointer(115, 48, "First(L)", "first")
    out += render_pointer(435, 48, "Last(L)", "last")
    out += render_pointer(595, 48, "P (Node Baru)", "p", width=95)
    
    out += render_node(60, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(170, 220, 104, 120)
    out += render_node(220, 86, "B", prev_null=False, next_null=False, variant="normal")
    out += render_link(330, 380, 104, 120)
    out += render_node(380, 86, "C", prev_null=False, next_null=True, variant="normal")
    out += render_node(540, 86, "F", prev_null=True, next_null=True, variant="new")
    out += render_bottom_tag(595, 145, "P = BIKIN_NODE(&quot;F&quot;)", "p")

    out += '  <line x1="30" y1="175" x2="770" y2="175" stroke="#E2E8F0" stroke-width="1"/>\n'
    out += '  <text x="30" y="205" font-size="13" font-weight="bold" fill="#0F172A">2. Hasil Akhir (P tersambung di belakang &quot;C&quot;, Last(L) &lt;- P):</text>\n'
    out += render_pointer(115, 222, "First(L)", "first")
    out += render_pointer(595, 222, "Last(L) (P)", "last", width=80)
    out += render_node(60, 260, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(170, 220, 278, 294)
    out += render_node(220, 260, "B", prev_null=False, next_null=False, variant="normal")
    out += render_link(330, 380, 278, 294)
    out += render_node(380, 260, "C", prev_null=False, next_null=False, variant="normal")
    out += render_link(490, 540, 278, 294)
    out += render_node(540, 260, "F", prev_null=False, next_null=True, variant="new")
    out += render_bottom_tag(595, 322, "Last(L) Baru (P)", "new")
    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 04: Insert After
# -------------------------------------------------------------
def gen_soal_04():
    out = create_svg_template("0 0 800 370")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">1. Kondisi Awal (List 3 Node: target = &quot;B&quot;, Q = next(target) = &quot;C&quot; + Node Baru P):</text>\n'
    out += render_pointer(125, 48, "First(L)", "first")
    out += render_pointer(285, 48, "target", "target", width=60)
    out += render_pointer(445, 48, "Q (next(target))", "q", width=110)
    out += render_pointer(625, 48, "P (Node Baru)", "p", width=95)
    
    out += render_node(70, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(180, 230, 104, 120)
    out += render_node(230, 86, "B", prev_null=False, next_null=False, variant="target")
    out += render_link(340, 390, 104, 120)
    out += render_node(390, 86, "C", prev_null=False, next_null=True, variant="normal")
    out += render_node(570, 86, "G", prev_null=True, next_null=True, variant="new")
    out += render_bottom_tag(285, 145, "target (&quot;B&quot;)", "target")
    out += render_bottom_tag(625, 145, "P = BIKIN_NODE(&quot;G&quot;)", "p")

    out += '  <line x1="30" y1="175" x2="770" y2="175" stroke="#E2E8F0" stroke-width="1"/>\n'
    out += '  <text x="30" y="205" font-size="13" font-weight="bold" fill="#0F172A">2. Hasil Akhir (P disisipkan SETELAH target &quot;B&quot;, List menjadi 4 Node):</text>\n'
    out += render_pointer(115, 222, "First(L)", "first")
    out += render_pointer(275, 222, "target", "target", width=55)
    out += render_pointer(435, 222, "P (Baru)", "p", width=65)
    out += render_pointer(595, 222, "Last(L) (Q)", "last", width=80)
    out += render_node(60, 260, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(170, 220, 278, 294)
    out += render_node(220, 260, "B", prev_null=False, next_null=False, variant="target")
    out += render_link(330, 380, 278, 294)
    out += render_node(380, 260, "G", prev_null=False, next_null=False, variant="new")
    out += render_link(490, 540, 278, 294)
    out += render_node(540, 260, "C", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(435, 322, "P tersambung di antara target &amp; Q", "new")
    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 05: Insert Before
# -------------------------------------------------------------
def gen_soal_05():
    out = create_svg_template("0 0 800 370")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">1. Kondisi Awal (List 3 Node: Q = prev(target) = &quot;A&quot;, target = &quot;B&quot; + Node Baru P):</text>\n'
    out += render_pointer(125, 48, "First(L) (Q)", "first", width=85)
    out += render_pointer(285, 48, "target", "target", width=60)
    out += render_pointer(445, 48, "Last(L)", "last")
    out += render_pointer(625, 48, "P (Node Baru)", "p", width=95)
    
    out += render_node(70, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(180, 230, 104, 120)
    out += render_node(230, 86, "B", prev_null=False, next_null=False, variant="target")
    out += render_link(340, 390, 104, 120)
    out += render_node(390, 86, "C", prev_null=False, next_null=True, variant="normal")
    out += render_node(570, 86, "H", prev_null=True, next_null=True, variant="new")
    out += render_bottom_tag(285, 145, "target (&quot;B&quot;)", "target")
    out += render_bottom_tag(625, 145, "P = BIKIN_NODE(&quot;H&quot;)", "p")

    out += '  <line x1="30" y1="175" x2="770" y2="175" stroke="#E2E8F0" stroke-width="1"/>\n'
    out += '  <text x="30" y="205" font-size="13" font-weight="bold" fill="#0F172A">2. Hasil Akhir (P disisipkan SEBELUM target &quot;B&quot;, List menjadi 4 Node):</text>\n'
    out += render_pointer(115, 222, "First(L) (Q)", "first", width=85)
    out += render_pointer(275, 222, "P (Baru)", "p", width=65)
    out += render_pointer(435, 222, "target", "target", width=55)
    out += render_pointer(595, 222, "Last(L)", "last")
    out += render_node(60, 260, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(170, 220, 278, 294)
    out += render_node(220, 260, "H", prev_null=False, next_null=False, variant="new")
    out += render_link(330, 380, 278, 294)
    out += render_node(380, 260, "B", prev_null=False, next_null=False, variant="target")
    out += render_link(490, 540, 278, 294)
    out += render_node(540, 260, "C", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(275, 322, "P tersambung di antara Q &amp; target", "new")
    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 06: Traversal Maju
# -------------------------------------------------------------
def gen_soal_06():
    out = create_svg_template("0 0 800 270")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">Penelusuran Maju (P &lt;- First(L), lalu berulang P &lt;- next(P)):</text>\n'
    out += render_pointer(230, 48, "P (Mulai = First(L))", "p", width=130)
    out += render_pointer(570, 48, "Last(L) (Berhenti)", "last", width=120)
    out += render_node(175, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += '  <line x1="285" y1="112" x2="345" y2="112" stroke="#7C3AED" stroke-width="2.8" marker-end="url(#arrow-p)"/>\n'
    out += render_node(345, 86, "B", prev_null=False, next_null=False, variant="normal")
    out += '  <line x1="455" y1="112" x2="515" y2="112" stroke="#7C3AED" stroke-width="2.8" marker-end="url(#arrow-p)"/>\n'
    out += render_node(515, 86, "C", prev_null=False, next_null=True, variant="normal")
    
    out += """  <g transform="translate(180, 185)">
    <rect x="0" y="0" width="440" height="46" rx="8" fill="#F5F3FF" stroke="#DDD6FE" stroke-width="1.2"/>
    <text x="220" y="28" font-size="14" font-weight="bold" fill="#6D28D9" text-anchor="middle">Hasil Return String:  &quot;A &lt;-&gt; B &lt;-&gt; C&quot;</text>
  </g>
</svg>"""
    return out

# -------------------------------------------------------------
# SOAL 07: Traversal Mundur
# -------------------------------------------------------------
def gen_soal_07():
    out = create_svg_template("0 0 800 270")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">Penelusuran Mundur (P &lt;- Last(L), lalu berulang P &lt;- prev(P)):</text>\n'
    out += render_pointer(230, 48, "First(L) (Berhenti)", "first", width=120)
    out += render_pointer(570, 48, "P (Mulai = Last(L))", "p", width=130)
    out += render_node(175, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += '  <line x1="345" y1="112" x2="285" y2="112" stroke="#EA580C" stroke-width="2.8" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(345, 86, "B", prev_null=False, next_null=False, variant="normal")
    out += '  <line x1="515" y1="112" x2="455" y2="112" stroke="#EA580C" stroke-width="2.8" marker-end="url(#arrow-orange)"/>\n'
    out += render_node(515, 86, "C", prev_null=False, next_null=True, variant="normal")
    
    out += """  <g transform="translate(180, 185)">
    <rect x="0" y="0" width="440" height="46" rx="8" fill="#FFF7ED" stroke="#FED7AA" stroke-width="1.2"/>
    <text x="220" y="28" font-size="14" font-weight="bold" fill="#C2410C" text-anchor="middle">Hasil Return String:  &quot;C &lt;-&gt; B &lt;-&gt; A&quot;</text>
  </g>
</svg>"""
    return out

# -------------------------------------------------------------
# SOAL 08: Search Node
# -------------------------------------------------------------
def gen_soal_08():
    out = create_svg_template("0 0 800 270")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">Mencari Nilai &quot;B&quot; (P berjalan dari First(L) sampai info(P) == &quot;B&quot;):</text>\n'
    out += render_pointer(230, 48, "First(L)", "first")
    out += render_pointer(400, 48, "P (Ditemukan!)", "p", width=105)
    out += render_pointer(570, 48, "Last(L)", "last")
    out += render_node(175, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(285, 345, 104, 120)
    out += render_node(345, 86, "B", prev_null=False, next_null=False, variant="target")
    out += render_link(455, 515, 104, 120)
    out += render_node(515, 86, "C", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(400, 145, "info(P) == target", "target")
    
    out += """  <g transform="translate(180, 185)">
    <rect x="0" y="0" width="440" height="46" rx="8" fill="#FEFCE8" stroke="#FEF08A" stroke-width="1.2"/>
    <text x="220" y="28" font-size="14" font-weight="bold" fill="#854D0E" text-anchor="middle">Hasil Return: Objek Node P (&quot;B&quot;)</text>
  </g>
</svg>"""
    return out

# -------------------------------------------------------------
# SOAL 09: Delete First
# -------------------------------------------------------------
def gen_soal_09():
    out = create_svg_template("0 0 800 370")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">1. Kondisi Awal (List 3 Node, node pertama &quot;A&quot; ditunjuk P untuk dihapus):</text>\n'
    out += render_pointer(230, 48, "First(L) (P)", "first", width=85)
    out += render_pointer(400, 48, "First(L) Baru", "blue", width=90)
    out += render_pointer(570, 48, "Last(L)", "last")
    out += render_node(175, 86, "A", prev_null=True, next_null=False, variant="delete")
    out += render_link(285, 345, 104, 120)
    out += render_node(345, 86, "B", prev_null=False, next_null=False, variant="normal")
    out += render_link(455, 515, 104, 120)
    out += render_node(515, 86, "C", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(230, 145, "P akan dihapus", "delete")
    
    out += '  <line x1="30" y1="175" x2="770" y2="175" stroke="#E2E8F0" stroke-width="1"/>\n'
    out += '  <text x="30" y="205" font-size="13" font-weight="bold" fill="#0F172A">2. Hasil Akhir (List berkurang menjadi 2 Node &quot;B&quot; &lt;-&gt; &quot;C&quot;):</text>\n'
    out += render_pointer(315, 222, "First(L)", "first")
    out += render_pointer(485, 222, "Last(L)", "last")
    out += render_node(260, 260, "B", prev_null=True, next_null=False, variant="normal")
    out += render_link(370, 430, 278, 294)
    out += render_node(430, 260, "C", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(315, 322, "First(L) Baru (prev = NULL)", "info")
    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 10: Delete Last
# -------------------------------------------------------------
def gen_soal_10():
    out = create_svg_template("0 0 800 370")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">1. Kondisi Awal (List 3 Node, node terakhir &quot;C&quot; ditunjuk P untuk dihapus):</text>\n'
    out += render_pointer(230, 48, "First(L)", "first")
    out += render_pointer(400, 48, "Last(L) Baru", "blue", width=85)
    out += render_pointer(570, 48, "Last(L) (P)", "last", width=85)
    out += render_node(175, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(285, 345, 104, 120)
    out += render_node(345, 86, "B", prev_null=False, next_null=False, variant="normal")
    out += render_link(455, 515, 104, 120)
    out += render_node(515, 86, "C", prev_null=False, next_null=True, variant="delete")
    out += render_bottom_tag(570, 145, "P akan dihapus", "delete")
    
    out += '  <line x1="30" y1="175" x2="770" y2="175" stroke="#E2E8F0" stroke-width="1"/>\n'
    out += '  <text x="30" y="205" font-size="13" font-weight="bold" fill="#0F172A">2. Hasil Akhir (List berkurang menjadi 2 Node &quot;A&quot; &lt;-&gt; &quot;B&quot;):</text>\n'
    out += render_pointer(315, 222, "First(L)", "first")
    out += render_pointer(485, 222, "Last(L)", "last")
    out += render_node(260, 260, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(370, 430, 278, 294)
    out += render_node(430, 260, "B", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(485, 322, "Last(L) Baru (next = NULL)", "info")
    out += "</svg>"
    return out

# -------------------------------------------------------------
# SOAL 11: Delete Node
# -------------------------------------------------------------
def gen_soal_11():
    out = create_svg_template("0 0 800 370")
    out += '  <text x="30" y="28" font-size="13" font-weight="bold" fill="#0F172A">1. Kondisi Awal (List 3 Node: P = prev(target), Q = next(target), target &quot;B&quot; dihapus):</text>\n'
    out += render_pointer(230, 48, "P (prev(target))", "p", width=110)
    out += render_pointer(400, 48, "target", "target", width=60)
    out += render_pointer(570, 48, "Q (next(target))", "q", width=110)
    
    out += render_node(175, 86, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(285, 345, 104, 120)
    out += render_node(345, 86, "B", prev_null=False, next_null=False, variant="delete")
    out += render_link(455, 515, 104, 120)
    out += render_node(515, 86, "C", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(400, 145, "target akan dihapus", "delete")
    
    out += '  <line x1="30" y1="175" x2="770" y2="175" stroke="#E2E8F0" stroke-width="1"/>\n'
    out += '  <text x="30" y="205" font-size="13" font-weight="bold" fill="#0F172A">2. Hasil Akhir (P dan Q disambungkan langsung, List menjadi 2 Node):</text>\n'
    out += render_pointer(315, 222, "First(L) (P)", "first", width=85)
    out += render_pointer(485, 222, "Last(L) (Q)", "last", width=85)
    out += render_node(260, 260, "A", prev_null=True, next_null=False, variant="normal")
    out += render_link(370, 430, 278, 294)
    out += render_node(430, 260, "C", prev_null=False, next_null=True, variant="normal")
    out += render_bottom_tag(375, 322, "next(P) &lt;- Q  &amp;  prev(Q) &lt;- P", "info")
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
