import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    BG_COLOR = RGBColor(11, 17, 32)       # #0B1120
    CARD_BG = RGBColor(22, 32, 54)        # #162036
    CARD_BORDER = RGBColor(51, 65, 85)    # #334155
    ACCENT_BLUE = RGBColor(56, 189, 248)  # #38BDF8
    ACCENT_ORANGE = RGBColor(251, 146, 60)# #FB923C
    ACCENT_GREEN = RGBColor(52, 211, 153) # #34D399
    ACCENT_PURPLE = RGBColor(167, 139, 250)# #A78BFA
    ACCENT_ROSE = RGBColor(244, 63, 94)   # #F43F5E
    ACCENT_AMBER = RGBColor(251, 191, 36) # #FBBF24
    TEXT_WHITE = RGBColor(248, 250, 252)  # #F8FAFC
    TEXT_MUTED = RGBColor(148, 163, 184)  # #94A3B8
    TEXT_BODY = RGBColor(226, 232, 240)   # #E2E8F0

    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="GLOBAL MOBILE PROCESSOR SUPPLY CHAIN ANALYSIS"):
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_BLUE

        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.7), Inches(0.65))
        tf = title_box.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = TEXT_WHITE

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.42), Inches(11.733), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = CARD_BORDER
        line.line.fill.background()

    def add_card(slide, left, top, width, height, title, items, accent_color=ACCENT_BLUE, title_icon=""):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = CARD_BG
        card.line.color.rgb = CARD_BORDER
        card.line.width = Pt(1)

        trim = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + Inches(0.15), top, width - Inches(0.3), Inches(0.04))
        trim.fill.solid()
        trim.fill.fore_color.rgb = accent_color
        trim.line.fill.background()

        tb = slide.shapes.add_textbox(left + Inches(0.22), top + Inches(0.18), width - Inches(0.44), height - Inches(0.28))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p_title = tf.paragraphs[0]
        p_title.text = f"{title_icon} {title}".strip()
        p_title.font.size = Pt(14)
        p_title.font.bold = True
        p_title.font.color.rgb = accent_color
        p_title.space_after = Pt(8)

        for item in items:
            p = tf.add_paragraph()
            p.space_after = Pt(5)
            if isinstance(item, tuple):
                label, desc = item
                run_lbl = p.add_run()
                run_lbl.text = f"• {label}: "
                run_lbl.font.bold = True
                run_lbl.font.size = Pt(10.5)
                run_lbl.font.color.rgb = TEXT_WHITE
                run_desc = p.add_run()
                run_desc.text = desc
                run_desc.font.size = Pt(10)
                run_desc.font.color.rgb = TEXT_MUTED
            else:
                run = p.add_run()
                run.text = f"• {item}"
                run.font.size = Pt(10.5)
                run.font.color.rgb = TEXT_BODY

    def add_metric_box(slide, left, top, width, height, val, label, subtext, color=ACCENT_BLUE):
        box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
        box.fill.solid()
        box.fill.fore_color.rgb = CARD_BG
        box.line.color.rgb = CARD_BORDER
        box.line.width = Pt(1)

        tb = slide.shapes.add_textbox(left + Inches(0.1), top + Inches(0.12), width - Inches(0.2), height - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = val
        p1.font.size = Pt(22)
        p1.font.bold = True
        p1.font.color.rgb = color
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = label
        p2.font.size = Pt(10.5)
        p2.font.bold = True
        p2.font.color.rgb = TEXT_WHITE
        p2.alignment = PP_ALIGN.CENTER
        p2.space_before = Pt(2)

        p3 = tf.add_paragraph()
        p3.text = subtext
        p3.font.size = Pt(9)
        p3.font.color.rgb = TEXT_MUTED
        p3.alignment = PP_ALIGN.CENTER

    # ==================== SLIDE 1: TITLE SLIDE ====================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Accent decorative bar
    bar = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(0.1), Inches(3.8))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_BLUE
    bar.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.7), Inches(11.2), Inches(4.2))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "SUPPLY CHAIN & STRATEGIC ECOSYSTEM ANALYSIS"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_BLUE
    p0.space_after = Pt(12)

    p1 = tf.add_paragraph()
    p1.text = "Global Mobile Phone Processors"
    p1.font.size = Pt(38)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "End-to-End Comparative Analysis: Apple, Qualcomm, MediaTek, Samsung & HiSilicon Across Wafer Fabs, Advanced Packaging & Geopolitics"
    p2.font.size = Pt(15)
    p2.font.color.rgb = ACCENT_ORANGE
    p2.space_after = Pt(24)

    p3 = tf.add_paragraph()
    p3.text = "Comprehensive Industry Research Project | Academic & Executive Strategy Report"
    p3.font.size = Pt(12)
    p3.font.color.rgb = TEXT_MUTED

    # Bottom metric highlight badges
    badges = [
        ("Market Size", "$45B+ SoC Sector"),
        ("Annual Volume", "1.2 Billion Units"),
        ("Foundry Choke", ">87% Sub-5nm TSMC"),
        ("Silicon Lead Time", "16-22 Wks Wafer Fab")
    ]
    for i, (b_label, b_val) in enumerate(badges):
        add_metric_box(s1, Inches(0.8 + i * 2.98), Inches(5.8), Inches(2.8), Inches(1.15), b_val, b_label, "Global Semiconductor Benchmark", ACCENT_BLUE if i%2==0 else ACCENT_ORANGE)

    # ==================== SLIDE 2: EXECUTIVE SUMMARY ====================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Executive Summary: The Geopolitics & Economics of Mobile Silicon")

    # Top metrics
    add_metric_box(s2, Inches(0.8), Inches(1.65), Inches(2.78), Inches(1.2), "$180+", "Flagship SoC Cost", "Up from $70 in 2019 (+157%)", ACCENT_ROSE)
    add_metric_box(s2, Inches(3.78), Inches(1.65), Inches(2.78), Inches(1.2), "3nm / 2nm", "Cutting-Edge Nodes", "TSMC N3B, N3E & N2 GAA", ACCENT_BLUE)
    add_metric_box(s2, Inches(6.76), Inches(1.65), Inches(2.78), Inches(1.2), "72%+", "Revenue Duopoly", "Apple & Qualcomm Value Capture", ACCENT_GREEN)
    add_metric_box(s2, Inches(9.74), Inches(1.65), Inches(2.78), Inches(1.2), "50+ TOPS", "On-Device NPU Era", "Hardware AI Accelerators", ACCENT_PURPLE)

    # 3 Summary Cards
    add_card(s2, Inches(0.8), Inches(3.1), Inches(3.75), Inches(3.8), "Extreme Foundry Concentration", [
        ("The TSMC Chokepoint", "Over 87% of sub-5nm advanced mobile wafer fabrication occurs exclusively in Taiwan."),
        ("Bespoke Access", "Apple leverages cash reserves to buy 100% of initial cutting-edge capacity (e.g. TSMC N3B), leaving Android rivals to wait."),
        ("Geopolitical Vulnerability", "Cross-strait tensions make mobile hardware the world's most geographically vulnerable consumer supply chain.")
    ], ACCENT_BLUE, "🏭")

    add_card(s2, Inches(4.78), Inches(3.1), Inches(3.75), Inches(3.8), "Soaring Wafer & R&D Costs", [
        ("Moore's Law Inflation", "Advanced 3nm wafers exceed $20,000 each, while next-gen 2nm GAA wafers approach $28,000-$30,000."),
        ("Tape-Out Escalation", "Mask sets and physical chip verification for a 3nm flagship processor cost upwards of $300M-$500M."),
        ("BOM Squeeze", "SoC now represents 20-25% of total smartphone hardware BOM, forcing OEMs to raise prices or cut display/camera specs.")
    ], ACCENT_ORANGE, "📈")

    add_card(s2, Inches(8.76), Inches(3.1), Inches(3.75), Inches(3.8), "Strategic Architectural Divergence", [
        ("Captive vs Merchant", "Apple & Google design silicon solely for their own hardware; Qualcomm & MediaTek sell to external OEMs."),
        ("ISA Friction", "Arm's revised licensing fees and lawsuits have triggered Qualcomm's custom Oryon cores and industry RISC-V exploration."),
        ("Packaging is the New Node", "Monolithic scaling limits are making 3D stacking and InFO advanced packaging the true battleground.")
    ], ACCENT_GREEN, "⚙️")

    # ==================== SLIDE 3: ANATOMY OF A MOBILE SOC ====================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Anatomy of a Mobile SoC: The Monolithic Silicon Engine")

    add_card(s3, Inches(0.8), Inches(1.65), Inches(3.75), Inches(2.6), "Central Processing Unit (CPU)", [
        ("Heterogeneous Clustering", "Big.LITTLE architectures combining high-performance cores with high-efficiency cores."),
        ("Core Architectures", "Custom microarchitectures (Apple Firestorm/Everest, Qualcomm Oryon) vs standard ARM Cortex-X4/A720."),
        ("Thermal Throttling", "Severe thermal envelopes (5W-10W) dictate burst vs sustained clock performance.")
    ], ACCENT_BLUE, "🧠")

    add_card(s3, Inches(4.78), Inches(1.65), Inches(3.75), Inches(2.6), "Graphics Processing Unit (GPU)", [
        ("Hardware Ray Tracing", "Desktop-class rendering with hardware-accelerated BVH traversal on mobile dies."),
        ("Key Architectures", "Qualcomm Adreno, ARM Immortalis (MediaTek), Apple Custom GPU, and Samsung Xclipse (AMD RDNA3)."),
        ("Compute Overhead", "Consumes up to 30-35% of total silicon die area in modern flagship processors.")
    ], ACCENT_ORANGE, "🎮")

    add_card(s3, Inches(8.76), Inches(1.65), Inches(3.75), Inches(2.6), "Neural Processing Unit (NPU / TPU)", [
        ("The AI Pivot", "Dedicated tensor accelerators delivering 45-50+ TOPS for on-device LLMs and generative image diffusion."),
        ("Specialized Memory Paths", "High-bandwidth direct memory channels bypassing CPU to avoid bottlenecks."),
        ("Architectural Leaders", "Apple Neural Engine, Qualcomm Hexagon NPU, Google Tensor TPU, MediaTek APU.")
    ], ACCENT_PURPLE, "⚡")

    add_card(s3, Inches(0.8), Inches(4.5), Inches(3.75), Inches(2.55), "Image Signal Processor (ISP)", [
        ("Computational Photography", "Multi-exposure HDR blending, zero shutter lag, zero-noise night mode processing."),
        ("Data Throughput", "Capable of processing 2-3 gigapixels/sec in real-time across 200MP camera sensors."),
        ("Key Implementations", "Qualcomm Spectra, Apple Photonic Engine, Google Ultra HDR Pipeline.")
    ], ACCENT_GREEN, "📷")

    add_card(s3, Inches(4.78), Inches(4.5), Inches(3.75), Inches(2.55), "5G Baseband Modem & RF", [
        ("High Barrier to Entry", "Decades of patent portfolios covering Sub-6GHz and mmWave carrier aggregation."),
        ("Qualcomm Dominance", "Snapdragon X75/X80 modems; Apple still reliant on Qualcomm modems despite in-house silicon."),
        ("Monolithic vs Discrete", "Flagship chips integrate modem on-die to save motherboard space and optimize battery.")
    ], ACCENT_ROSE, "📡")

    add_card(s3, Inches(8.76), Inches(4.5), Inches(3.75), Inches(2.55), "Packaging & Memory Subsystem", [
        ("PoP (Package-on-Package)", "LPDDR5X DRAM (8GB-24GB) soldered directly on top of the SoC via micro-bumps."),
        ("Unified Memory Architecture", "Zero-copy data sharing between CPU, GPU, and NPU for extreme memory bandwidth (>136 GB/s)."),
        ("System-Level Cache (SLC)", "16MB-32MB on-die caches buffering traffic to power-hungry external DRAM.")
    ], ACCENT_AMBER, "📦")

    # ==================== SLIDE 4: BUSINESS MODELS ====================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "Semiconductor Business Models: Fabless vs. Captive vs. IDM")

    add_card(s4, Inches(0.8), Inches(1.65), Inches(2.78), Inches(5.35), "1. Captive Fabless\n(Apple, Google)", [
        ("Core Philosophy", "Design chips exclusively for proprietary hardware devices."),
        ("No Merchant Sales", "Zero exposure to external OEM contract volatility."),
        ("Margin Synergy", "Chip cost is absorbed into finished device margin; can spend $150+ per chip because iPhone sells at $1,000+."),
        ("Foundry Stance", "100% outsourced fabrication to TSMC; buys first-wave node exclusivity through massive cash prepayments."),
        ("Strategic Strength", "Deepest hardware-software co-design; vertical lock-in.")
    ], ACCENT_BLUE, "🛡️")

    add_card(s4, Inches(3.78), Inches(1.65), Inches(2.78), Inches(5.35), "2. Merchant Fabless\n(Qualcomm, MediaTek)", [
        ("Core Philosophy", "Design silicon to sell to third-party smartphone OEMs globally."),
        ("Customer Dependence", "Exposed to OEM inventory cycles (Samsung, Xiaomi, Oppo, Vivo)."),
        ("Pricing Pressure", "Must maintain OEM profitability; face strict margin ceilings on chip pricing."),
        ("Foundry Stance", "Outsource to TSMC / Samsung; must negotiate wafer allocation against Apple."),
        ("Strategic Strength", "Massive global volume economies of scale across high, mid, and low tiers.")
    ], ACCENT_ORANGE, "🌐")

    add_card(s4, Inches(6.76), Inches(1.65), Inches(2.78), Inches(5.35), "3. Integrated IDM\n(Samsung Electronics)", [
        ("Core Philosophy", "System LSI designs chips; Samsung Foundry fabricates; Samsung MX buys."),
        ("Internal Conflict", "Captive customer (Galaxy phones) frequently rejects internal Exynos chips for Qualcomm."),
        ("Foundry Stance", "Uses internal fabs; struggles with sub-5nm yields compared to pure-play TSMC."),
        ("Capital Burden", "Must fund multi-billion dollar fab CapEx while competing with dedicated design houses."),
        ("Strategic Vulnerability", "Trailing TSMC node efficiency creates structural headwinds.")
    ], ACCENT_PURPLE, "🔄")

    add_card(s4, Inches(9.74), Inches(1.65), Inches(2.78), Inches(5.35), "4. Pure-Play Foundry\n(TSMC)", [
        ("Core Philosophy", "Fabricate wafers for external designers; never compete with customers."),
        ("Monopolistic Pricing", "Dictates wafer pricing due to lack of competitive alternatives at <3nm."),
        ("CapEx Scale", "Invests $30B-$40B annually in advanced fab tools (ASML EUV machines)."),
        ("Customer Dynamic", "Balances mega-client Apple (~25% of TSMC revenue) with Qualcomm, AMD, Nvidia."),
        ("Geopolitical Risk", "Fabs concentrated in Hsinchu/Tainan; expanding to US/Japan.")
    ], ACCENT_GREEN, "🏗️")

    # ==================== SLIDE 5: APPLE SILICON ====================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Company Deep-Dive: Apple Silicon (A-Series & M-Series)")

    add_card(s5, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "Supply Chain Power & Sourcing", [
        ("TSMC Alpha Customer", "Apple accounts for ~23-25% of TSMC's total corporate revenue, giving it supreme bargaining power."),
        ("Node Monopolization", "Apple pre-reserved 100% of TSMC's initial 3nm (N3B) capacity in 2023-2024 for A17 Pro and M3."),
        ("Yield Risk Absorption", "Negotiated historic agreement where TSMC absorbed defective die costs during initial 3nm ramp-up."),
        ("Advanced Packaging", "Pioneered TSMC's InFO (Integrated Fan-Out) wafer-level packaging, eliminating substrate height."),
        ("Cash Reserves Advantage", "Can commit $10B+ in multi-year capital prepayments to secure next-generation nodes (N2).")
    ], ACCENT_BLUE, "🍏")

    add_card(s5, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "Architectural & Value Strategy", [
        ("Proprietary Microarchitecture", "Fully custom ARM-based microarchitectures (wide-decode pipelines, massive L2 caches)."),
        ("Captive Margin Flywheel", "Estimated manufacturing cost of $110-$135 per A18 Pro; integrated into $1,199 iPhone 16 Pro (super-premium margins)."),
        ("Apple Intelligence Engine", "Re-engineered 16-core Neural Engine and memory bandwidth (>136 GB/s) for on-device privacy-first models."),
        ("Silicon Commonality", "Shared architectural IP across iPhone (A-series), iPad/Mac (M-series), and Vision Pro."),
        ("Modem Chokepoint", "Sole remaining external dependency: Qualcomm 5G modems, despite Apple's $1B Intel modem acquisition.")
    ], ACCENT_ORANGE, "💎")

    add_card(s5, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Vulnerabilities & Supply Risks", [
        ("Single-Source Foundry Risk", "Zero secondary foundry backup; 100% of cutting-edge Apple chips are fabricated in Taiwan."),
        ("Taiwan Strait Exposure", "Any disruption to TSMC's Fab 18 in Tainan would halt global iPhone production within 60 days."),
        ("Fab 21 Arizona Reality", "TSMC's Arizona fab will produce 4nm/3nm wafers, but advanced packaging (InFO) still ships back to Taiwan."),
        ("Rising Wafer Premiums", "TSMC raising wafer prices 5-10% as node complexity increases, slightly eroding gross margins."),
        ("Qualcomm Baseband Lock", "Internal 5G modem project delayed multiple years due to engineering & global patent minefields.")
    ], ACCENT_ROSE, "⚠️")

    # ==================== SLIDE 6: QUALCOMM SNAPDRAGON ====================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Company Deep-Dive: Qualcomm Snapdragon")

    add_card(s6, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "Merchant Leadership & Architecture", [
        ("Merchant Standard", "The benchmark processor for the global Android flagship ecosystem (Samsung Galaxy, Xiaomi, OnePlus, Vivo)."),
        ("The 'Oryon' Revolution", "Acquired Nuvia for $1.4B; transitioned away from standard ARM Cortex cores to custom Oryon CPU microarchitecture."),
        ("5G Modem Monopoly", "Industry-leading Snapdragon X-series RF systems; bundles AP + modem + RF front-end into lucrative OEM packages."),
        ("Snapdragon Elite Series", "Desktop-grade performance ported to mobile, directly challenging Apple's single-core CPU supremacy."),
        ("High Dollar Share", "Captures ~34% of global smartphone SoC revenues despite having lower unit volume than MediaTek.")
    ], ACCENT_ORANGE, "⚡")

    add_card(s6, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "Foundry Dual-Sourcing Odyssey", [
        ("The Samsung 4nm Fiasco", "Snapdragon 8 Gen 1 was fabricated on Samsung Foundry 4nm; suffered severe thermal throttling and poor yields (~35%)."),
        ("Mid-Cycle Pivot to TSMC", "Qualcomm scrambled to re-tape Snapdragon 8+ Gen 1 to TSMC 4nm, gaining +30% power efficiency immediately."),
        ("TSMC Lock-in", "Snapdragon 8 Gen 2, 3, and 8 Elite fully committed to TSMC N4P and N3E nodes, abandoning Samsung flagship foundry."),
        ("Wafer Cost Penalty", "Must pay premium spot prices to TSMC after Apple consumes primary volume, resulting in $180-$200 chip prices."),
        ("Dual-Sourcing Ambition", "Keeps dialogue with Samsung Foundry for future 2nm GAA to regain pricing leverage against TSMC.")
    ], ACCENT_BLUE, "🔄")

    add_card(s6, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Customer & Legal Pressures", [
        ("Samsung MX Concentration", "Samsung Mobile is both Qualcomm's biggest customer and an unpredictable partner (flirting with Exynos)."),
        ("Arm Litigation Threat", "Arm sued Qualcomm over Nuvia architectural licenses, threatening royalty structures and core IP access."),
        ("OEM Price Resistance", "Chinese OEMs (Xiaomi, Vivo) push back on $180+ SoC costs, looking to MediaTek for cost-competitive flagships."),
        ("Automotive & PC Hedge", "Diversifying supply chain exposure into Snapdragon Ride (autos) and Snapdragon X Elite (Windows Copilot+ PCs)."),
        ("OSAT Diversification", "Uses multiple packaging houses including Amkor, ASE, and stats chipPAC to balance test throughput.")
    ], ACCENT_AMBER, "⚖️")

    # ==================== SLIDE 7: MEDIATEK DIMENSITY ====================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Company Deep-Dive: MediaTek Dimensity")

    add_card(s7, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "Volume King to Flagship Disruptor", [
        ("Global Unit Leader", "Accounts for ~37-38% of all smartphone processors shipped worldwide, powering 450M+ phones annually."),
        ("Budget & Mid-Tier Stronghold", "Dominates Helio and Dimensity 6000/7000 lines across emerging markets (India, Southeast Asia, LatAm, Africa)."),
        ("The 'All-Big-Core' Gamble", "Dimensity 9300 & 9400 eliminated small efficiency cores entirely, utilizing 4x Cortex-X + 4x Cortex-A720 cores."),
        ("Flagship Benchmark Parity", "Dimensity 9400 achieved multi-core and GPU performance rivaling Snapdragon 8 Elite and Apple A18 Pro."),
        ("Lower Cost-per-Die", "Leverages standard ARM Cortex IP to minimize R&D tape-out overhead compared to Qualcomm's custom Oryon cores.")
    ], ACCENT_GREEN, "🏆")

    add_card(s7, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "Symbiotic TSMC Alignment", [
        ("Hsinchu Proximity", "Headquartered in Hsinchu Science Park, Taiwan, walking distance from TSMC headquarters and R&D fabs."),
        ("Pacesetter on Second Wave", "Consistently the primary fast-follower on TSMC's enhanced nodes (e.g. N3E for Dimensity 9400)."),
        ("Wafer Allocation Efficiency", "Packages wafer orders across automotive, smart TV, Wi-Fi router, and mobile lines to secure volume discounts."),
        ("Yield Optimization", "Works closely with TSMC on Design-Technology Co-Optimization (DTCO) to extract maximum frequency per watt."),
        ("Zero Advanced Foundry Alternatives", "Entirely dependent on TSMC; does not evaluate Samsung Foundry for high-end Dimensity silicon.")
    ], ACCENT_BLUE, "🤝")

    add_card(s7, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Strategic Headwinds & Opportunities", [
        ("Brand Perception Ceiling", "Struggles to command equal prestige to Snapdragon in western premium carrier channels."),
        ("Chinese OEM Concentration", "Over 70% of Dimensity revenue is tied to Chinese OEMs (Vivo, Oppo, Xiaomi, Transsion)."),
        ("Margin Expansion Push", "Successfully increasing blended ASP from $25 in 2020 to >$42 in 2025 by winning flagship tier contracts."),
        ("Nvidia Partnership Synergy", "Partnering with Nvidia for automotive cockpit processors and custom AI PC silicon."),
        ("ARM Royalty Exposure", "Most vulnerable to Arm's proposed device-level royalty model due to 100% adherence to standard ARM cores.")
    ], ACCENT_PURPLE, "📊")

    # ==================== SLIDE 8: SAMSUNG EXYNOS ====================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Company Deep-Dive: Samsung System LSI & Foundry")

    add_card(s8, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The IDM Dilemma", [
        ("Divided House", "Samsung System LSI designs the chip, while Samsung Foundry manufactures it; both are distinct business units."),
        ("Internal Customer Rebellion", "Samsung Mobile (MX Division) is fiercely pragmatic; if Exynos falls behind Snapdragon, MX uses Qualcomm."),
        ("Regional Bifurcation", "Galaxy S flagship line frequently split: Snapdragon in US/Korea/China, Exynos in Europe/Latin America."),
        ("Full Desertion (Galaxy S23)", "Samsung MX completely dropped Exynos 2300 due to Samsung Foundry 4nm thermal/yield issues, going 100% Snapdragon."),
        ("Partial Comeback (S24/S25)", "Exynos 2400 restored competitiveness on 4nm FOWLP; Exynos 2500 faced severe 3nm GAA yield hurdles.")
    ], ACCENT_PURPLE, "🔄")

    add_card(s8, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "3nm GAA Yield Challenges", [
        ("The First to GAA", "Pioneered Gate-All-Around (MBCFET) nanosheet architecture ahead of TSMC at the 3nm node."),
        ("Yield Disasters", "Industry reports indicated initial 3nm GAA yields struggled below 20-30%, causing massive financial bleed."),
        ("Customer Defections", "Qualcomm and Nvidia abandoned Samsung Foundry, consolidating advanced node orders onto TSMC."),
        ("Massive CapEx Drag", "Samsung invested $35B+ annually in semiconductor equipment, but Foundry struggles to achieve positive operating margin."),
        ("2nm Make-or-Break", "Pouring immense resources into 2nm GAA (SF2) to attempt a leapfrog over TSMC's 2nm ramp.")
    ], ACCENT_ROSE, "⚠️")

    add_card(s8, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Packaging & In-House Advantages", [
        ("FOWLP Packaging Pioneer", "First to commercialize Fan-Out Wafer-Level Packaging on Exynos 2400, eliminating PCB interposer to reduce heat."),
        ("Memory Synergy", "Samsung is the world's #1 DRAM & NAND maker; can bundle LPDDR5X and UFS 4.0 storage packages internally."),
        ("AMD GPU Collaboration", "Licensed AMD RDNA architecture for Xclipse GPU, bringing desktop ray tracing to mobile Exynos."),
        ("Geopolitical Sanctuary", "Headquartered in South Korea with fabs in Pyeongtaek and Taylor, Texas; insulated from direct Taiwan cross-strait risk."),
        ("System LSI Crisis", "Without internal foundry parity, System LSI may eventually be forced to fabricate Exynos at TSMC.")
    ], ACCENT_BLUE, "🛡️")

    # ==================== SLIDE 9: GOOGLE TENSOR & HISILICON ====================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Special Cases: Google Tensor & HiSilicon (Huawei)")

    add_card(s9, Inches(0.8), Inches(1.65), Inches(5.7), Inches(5.35), "Google Tensor: Custom TPU Focus to TSMC", [
        ("Silicon Thesis", "Google abandoned Qualcomm Snapdragon off-the-shelf chips in 2021 to build Tensor, prioritizing AI/ML over synthetic benchmarks."),
        ("Samsung Co-Design Era (G1-G4)", "Tensor G1 through G4 were co-developed with Samsung System LSI and fabricated on Samsung 5nm/4nm nodes."),
        ("Thermal & Efficiency Penalties", "Suffered from Samsung Foundry's higher power leakage and lower modem efficiency compared to TSMC equivalents."),
        ("The Big Pivot: Tensor G5 on TSMC 3nm", "Google took design 100% in-house with full custom RTL and taped out Tensor G5 on TSMC's 3nm (N3E) node."),
        ("Advanced Packaging Evolution", "Adopting TSMC InFO-PoP packaging to solve thermal dissipation in Pixel 10 devices."),
        ("Captive Integration Strategy", "Designed exclusively to power Gemini Nano, on-device multimodal models, and computational photography.")
    ], ACCENT_BLUE, "🔍")

    add_card(s9, Inches(6.8), Inches(1.65), Inches(5.7), Inches(5.35), "HiSilicon (Huawei): Sanctions & Autarky", [
        ("The Pre-Sanctions Giant", "In 2020, HiSilicon Kirin 9000 was the world's first 5nm SoC, beating Apple to TSMC's cutting-edge fab line."),
        ("US Entity List Impact", "US export controls banned TSMC, ASML, and US EDA tools from supplying HiSilicon, halting production overnight."),
        ("The Kirin 9000s Miracle", "Huawei shocked the world in late 2023 by releasing the Mate 60 Pro powered by a 7nm Kirin 9000s fabricated by SMIC."),
        ("DUV Multi-Patterning", "Lacking ASML EUV scanners, SMIC utilized immersion DUV multi-patterning (SAQP), resulting in low yields (~40%) and high costs."),
        ("Domestic Substitution Ecosystem", "Replacing Synopsys/Cadence with Chinese EDA (Empyrean) and domestic packaging (JCET, Tongfu Micro)."),
        ("Strategic Implications", "Demonstrates that geopolitical sanctions can slow advanced node access but accelerate domestic autarky.")
    ], ACCENT_ROSE, "🛡️")

    # ==================== SLIDE 10: MARKET SHARE (WITH CHART) ====================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Market Share Dynamics: Unit Volume vs. Revenue Value Capture")

    # Embed Chart on Left
    if os.path.exists("charts/market_share_soc.png"):
        s10.shapes.add_picture("charts/market_share_soc.png", Inches(0.8), Inches(1.65), width=Inches(6.8))

    # Analytical Cards on Right
    add_card(s10, Inches(7.8), Inches(1.65), Inches(4.7), Inches(2.6), "The Volume vs. Value Paradox", [
        ("MediaTek Leads Volume (37%)", "Dominates mass-market shipments across Asia, Africa, and Latin America through price-competitive Helio & Dimensity SoCs."),
        ("Apple & Qualcomm Capture Value (72%)", "Together control almost three-quarters of total dollar revenues in the global smartphone processor industry."),
        ("Flagship Premiumization", "Consumers holding phones longer (3.5+ years) drives demand for $800+ devices, shifting profit pools to high-end silicon.")
    ], ACCENT_ORANGE, "📊")

    add_card(s10, Inches(7.8), Inches(4.4), Inches(4.7), Inches(2.6), "Strategic Key Takeaways", [
        ("Margin Asymmetry", "Apple captures ~38% revenue share with only 18% unit volume by internalizing chip profits inside the iPhone ecosystem."),
        ("Unisoc in the Entry Tier", "Chinese designer Unisoc captures 9% unit share in ultra-budget 4G/entry 5G phones (<$150 retail)."),
        ("HiSilicon's Comeback", "Capturing 3% global unit volume entirely within mainland China, taking share away from Qualcomm in the high end.")
    ], ACCENT_GREEN, "💡")

    # ==================== SLIDE 11: MULTI-TIER SUPPLY CHAIN ARCHITECTURE ====================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "The Multi-Tier Mobile Silicon Supply Chain: Quartz to Device")

    tiers = [
        ("Tier 4: Raw Materials & Specialty Chemicals", "Quartz & Electronic-Grade Polysilicon (Shin-Etsu, SUMCO, Siltronic)\nHigh-purity Photoresists, Ultra-pure HF, Neon gas, Gallium, Palladium, Copper", ACCENT_ROSE),
        ("Tier 3: Semiconductor Equipment & EDA / IP", "Lithography Monopoly: ASML (Netherlands - sole supplier of EUV scanners)\nDeposition & Etch: Applied Materials, Lam Research, Tokyo Electron, KLA\nEDA Software: Synopsys, Cadence | Core Architecture: ARM Holdings (UK)", ACCENT_ORANGE),
        ("Tier 2: Wafer Fabrication (Foundries)", "Advanced Node Foundry: TSMC (Taiwan - >87% of sub-5nm mobile fabrication)\nSecondary Foundries: Samsung Foundry (S. Korea), SMIC (China)\nFab cycle time: 16-22 weeks through 1,500+ individual precision chemical/laser steps", ACCENT_BLUE),
        ("Tier 1: Advanced Packaging & Testing (OSAT)", "Wafer-Level Fan-Out (TSMC InFO-PoP), 2.5D/3D Stacking, Substrates (Unimicron, Ibiden)\nOSAT Leaders: ASE Group (Taiwan), Amkor Technology (US/Korea), JCET (China)\nAutomated Test Equipment (ATE): Advantest, Teradyne", ACCENT_PURPLE),
        ("Tier 0: OEM Integration & Final Distribution", "Surface Mount Technology (SMT) Motherboard Integration (Foxconn, Pegatron, Luxshare)\nSmartphone Assembly: Apple, Samsung, Xiaomi, Oppo, Vivo, Google\nGlobal Air-Freight Logistics: High-value, low-weight air shipping to global retail hubs", ACCENT_GREEN)
    ]

    for i, (t_title, t_desc, col) in enumerate(tiers):
        c = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65 + i * 1.08), Inches(11.733), Inches(0.98))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = CARD_BORDER
        c.line.width = Pt(1)

        # Accent left border strip
        strip = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(1.65 + i * 1.08), Inches(0.08), Inches(0.98))
        strip.fill.solid()
        strip.fill.fore_color.rgb = col
        strip.line.fill.background()

        tb = s11.shapes.add_textbox(Inches(1.05), Inches(1.7 + i * 1.08), Inches(11.3), Inches(0.88))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = t_title
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = col

        p2 = tf.add_paragraph()
        p2.text = t_desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = TEXT_BODY
        p2.space_before = Pt(2)

    # ==================== SLIDE 12: TIER 4 DEEP DIVE (ASML & UPSTREAM) ====================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Tier 4 Deep Dive: ASML Lithography & Upstream Monopolies")

    add_card(s12, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "ASML: The Ultimate Chokepoint", [
        ("The EUV Monopoly", "100% global market share in Extreme Ultraviolet (EUV) lithography scanners (13.5nm light wavelength)."),
        ("Engineering Complexity", "Uses high-powered lasers pulsing tin droplets 50,000 times/sec inside a high-vacuum chamber with Zeiss mirrors."),
        ("High-NA EUV Rollout", "Next-gen Twinscan EXE:5000 scanners cost ~$350M+ each; essential for sub-2nm mass production."),
        ("Lead Times", "Order-to-delivery lead time of 18-24 months; production capacity capped at ~50-60 EUV machines per year."),
        ("Export Control Lever", "The Dutch government, under US pressure, bans ASML from shipping advanced EUV/DUV tools to China.")
    ], ACCENT_ROSE, "🔬")

    add_card(s12, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "Raw Silicon Wafers & Substrates", [
        ("300mm Ingot Duopoly", "Shin-Etsu Chemical (Japan) and SUMCO (Japan) control >55% of global electronic-grade silicon wafer manufacturing."),
        ("Extreme Purity Standards", "Requires Eleven-Nines (99.999999999%) purity monocrystalline silicon grown via the Czochralski process."),
        ("Pricing Power", "Wafer manufacturers lock foundries into 3-5 year Long-Term Agreements (LTAs) with take-or-pay clauses."),
        ("Substrate Scarcity", "Ajinomoto Build-up Film (ABF) and BT resin substrates periodically bottleneck advanced packaging lines.")
    ], ACCENT_BLUE, "⚪")

    add_card(s12, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Critical Gases & Specialty Chemicals", [
        ("Japanese Chemical Grip", "JSR, Tokyo Ohka Kogyo (TOK), and Shin-Etsu control >80% of cutting-edge fluorinated polyimides and EUV photoresists."),
        ("Rare Gases Vulnerability", "Ukraine historically produced ~50% of semiconductor-grade purified Neon gas used in DUV excimer lasers."),
        ("Ultra-Pure Acids & Water", "Fabs require billions of gallons of ultra-pure water (UPW) and electronic-grade Hydrogen Fluoride (HF)."),
        ("Single Point of Failure", "A major fire or chemical plant shutdown in Japan or Germany can halt wafer fabrication worldwide within weeks.")
    ], ACCENT_AMBER, "🧪")

    # ==================== SLIDE 13: TIER 3 DEEP DIVE (ARM & EDA) ====================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)
    add_header(s13, "Tier 3 Deep Dive: ARM Holdings & The EDA Software Duopoly")

    add_card(s13, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "ARM Holdings: The Architectural Hegemony", [
        ("Universal Mobile ISA", "Over 99% of all mobile phone processors globally utilize the ARM architecture (ARMv8 / ARMv9)."),
        ("Licensing Models", "Two distinct access paths: Architectural License (allows custom cores e.g. Apple, Qualcomm Oryon) vs Core License (off-the-shelf Cortex cores e.g. MediaTek)."),
        ("ARMv9 Feature Matrix", "Introduced Scalable Vector Extensions 2 (SVE2), Memory Tagging Extension (MTE), and Confidential Compute Architecture."),
        ("The Business Model Conflict", "Arm has attempted to shift from chip-level royalty (~1-2% of SoC price) to finished device-level royalty (~1-2% of smartphone MSRP), triggering fierce industry resistance."),
        ("Qualcomm vs. Arm Lawsuit", "Legal battle over whether Nuvia's custom server IP licenses transferred to Qualcomm; threatens Qualcomm's Oryon CPU roadmap.")
    ], ACCENT_BLUE, "📐")

    add_card(s13, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "The EDA Tooling Duopoly (Synopsys & Cadence)", [
        ("The Software Gatekeepers", "Synopsys and Cadence Design Systems control ~70-75% of the Electronic Design Automation (EDA) market."),
        ("Billion-Transistor Simulation", "Designing a 15-billion transistor mobile SoC is physically impossible without advanced EDA logic synthesis, place-and-route, and timing closure."),
        ("PDK Integration", "Foundries (TSMC, Samsung) release Process Design Kits (PDKs) exclusively formatted for Synopsys and Cadence tools."),
        ("Pricing Power", "Multi-year software subscription licenses run into tens of millions of dollars per design team."),
        ("Sanctions Weapon", "US banned export of GAA-capable EDA software to China, severely limiting domestic 3nm/2nm design efforts.")
    ], ACCENT_ORANGE, "💻")

    add_card(s13, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "The Open-Source Hedge: RISC-V", [
        ("Architectural Independence", "Open-standard instruction set architecture with zero royalty fees and no single corporate owner."),
        ("Microcontroller Beachhead", "Already pervasive in low-level smartphone subsystems (power management, security enclaves, touch controllers)."),
        ("The RISC-V Mobile Consortium", "Qualcomm, Google, MediaTek, and NXP formed Quintauris in Germany to accelerate RISC-V software ecosystem."),
        ("Android Compatibility", "Google officially declared Android's commitment to treat RISC-V as a tier-1 architecture alongside ARM."),
        ("Timeline to Flagship", "5-7 years away from matching ARM's single-core IPC and vector math in premium mobile application processors.")
    ], ACCENT_GREEN, "⚡")

    # ==================== SLIDE 14: TIER 2 DEEP DIVE (TSMC MONOPOLY - WITH CHART) ====================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14)
    add_header(s14, "Tier 2 Deep Dive: TSMC's Advanced Node Fabrication Hegemony")

    if os.path.exists("charts/foundry_advanced_nodes.png"):
        s14.shapes.add_picture("charts/foundry_advanced_nodes.png", Inches(0.8), Inches(1.65), width=Inches(6.4))

    add_card(s14, Inches(7.4), Inches(1.65), Inches(5.1), Inches(2.6), "TSMC: The Linchpin of the Digital Age", [
        ("87% Dominance at <5nm", "TSMC manufactures virtually every cutting-edge mobile processor for Apple, Qualcomm, and MediaTek."),
        ("GigaFab Economies of Scale", "Fab 18 in Tainan produces >100,000 advanced 300mm wafers per month, creating unbeatable yield learning curves."),
        ("The 'Pure-Play' Trust Advantage", "TSMC does not sell consumer hardware, guaranteeing clients that their proprietary RTL designs will never be copied.")
    ], ACCENT_BLUE, "🏭")

    add_card(s14, Inches(7.4), Inches(4.4), Inches(5.1), Inches(2.6), "Capacity Allocation & The Apple Tax", [
        ("Apple Pre-Emption", "Apple consistently secures entire initial production runs of new nodes (N5 in 2020, N3B in 2023, N2 in 2025/2026)."),
        ("Android's 1-Year Lag", "Qualcomm and MediaTek must wait 9-12 months for secondary node iterations (N3E/N3P) to ramp in volume."),
        ("Extreme Price Inelasticity", "TSMC announced consecutive 5-8% wafer price increases, which chip designers are forced to absorb or pass to OEMs.")
    ], ACCENT_ROSE, "⚠️")

    # ==================== SLIDE 15: WAFER ECONOMICS (WITH CHART) ====================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15)
    add_header(s15, "Wafer Economics: The Exponential Cost of Moore's Law")

    if os.path.exists("charts/wafer_cost_escalation.png"):
        s15.shapes.add_picture("charts/wafer_cost_escalation.png", Inches(0.8), Inches(1.65), width=Inches(6.5))

    add_card(s15, Inches(7.5), Inches(1.65), Inches(5.0), Inches(2.6), "The Death of Dennard Scaling & Cost/Transistor", [
        ("Wafer Price Doubling", "Processed 300mm wafer costs jumped from $3,000 at 28nm to $20,500 at 3nm, heading toward $28,000+ at 2nm GAA."),
        ("Mask Set Inflation", "Full optical mask set for a 3nm tape-out costs upwards of $50M-$80M alone, limiting node access to mega-corps."),
        ("Defect Density vs. Die Size", "Larger dies (>120mm²) suffer severe yield penalties; driving designers toward aggressive chiplet partitioning.")
    ], ACCENT_ORANGE, "📈")

    add_card(s15, Inches(7.5), Inches(4.4), Inches(5.0), Inches(2.6), "Impact on Consumer Smartphone Prices", [
        ("ASP Inflation", "Flagship processor prices rose from ~$70 in 2019 (Snapdragon 855) to ~$180-$200 in 2025 (Snapdragon 8 Elite)."),
        ("Margin Compression", "Android OEMs unable to pass $50+ chip cost increases to consumers are forced to downgrade peripheral specs (RAM, lenses)."),
        ("Premium Tier Polarization", "Only smartphones retailing at $900+ can absorb the margin requirements of cutting-edge 3nm/2nm silicon.")
    ], ACCENT_GREEN, "🏷️")

    # ==================== SLIDE 16: BOM BREAKDOWN (WITH CHART) ====================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16)
    add_header(s16, "Smartphone Bill of Materials (BOM): The SoC as Value Epicenter")

    if os.path.exists("charts/bom_cost_breakdown.png"):
        s16.shapes.add_picture("charts/bom_cost_breakdown.png", Inches(0.8), Inches(1.65), width=Inches(6.6))

    add_card(s16, Inches(7.6), Inches(1.65), Inches(4.9), Inches(2.6), "SoC Represents 25-30% of Total BOM", [
        ("The Single Costliest Component", "At ~$165, the Application Processor + RF subsystem surpasses the LTPO OLED display ($95) and camera module ($88)."),
        ("Bundled RF Complexity", "Modem integration requires companion RF Transceivers, Power Amplifiers (Skyworks, Qorvo), and mmWave antennas."),
        ("DRAM Packaging Squeeze", "Stacking 16GB-24GB of high-speed LPDDR5X directly on the SoC adds another $45-$65 to the processor subsystem.")
    ], ACCENT_PURPLE, "💰")

    add_card(s16, Inches(7.6), Inches(4.4), Inches(4.9), Inches(2.6), "Tiered Smartphone BOM Comparison", [
        ("Flagship Tier ($1,000+ MSRP)", "BOM: ~$560 | SoC Cost: $160-$190 (TSMC 3nm / N3E) | Represents 28-32% of total hardware cost."),
        ("Mid-Tier ($400-$600 MSRP)", "BOM: ~$240 | SoC Cost: $50-$75 (TSMC 4nm / MediaTek Dimensity 8300) | Represents ~22% of BOM."),
        ("Budget Tier (<$200 MSRP)", "BOM: ~$95 | SoC Cost: $18-$25 (TSMC 6nm / Unisoc T616) | Highly commoditized silicon margins.")
    ], ACCENT_BLUE, "📱")

    # ==================== SLIDE 17: TIER 1 ADVANCED PACKAGING ====================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17)
    add_header(s17, "Tier 1 Deep Dive: Advanced Packaging (OSAT) & InFO-PoP")

    add_card(s17, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "TSMC InFO-PoP Technology", [
        ("Integrated Fan-Out Package-on-Package", "Eliminates the traditional organic substrate, utilizing high-density redistribution layers (RDL)."),
        ("Apple Exclusivity Engine", "Apple switched from standard substrate packaging to InFO with the A10 Fusion, shaving 30% off package height and boosting thermal conductivity."),
        ("DRAM Direct Stacking", "LPDDR5X DRAM dies are soldered directly on top of the SoC silicon using copper pillars, enabling 100+ GB/s memory bandwidth."),
        ("Thermal Dissipation", "Thin profile allows smartphone chassis to act as an effective heat sink without bulky vapor chambers in compact devices.")
    ], ACCENT_BLUE, "📦")

    add_card(s17, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "The OSAT Merchant Ecosystem", [
        ("Outsourced Assembly & Test (OSAT)", "Independent packaging specialists handle mid-to-high volume merchant processors (Qualcomm, MediaTek, Unisoc)."),
        ("ASE Technology Holding (Taiwan)", "The world's largest OSAT provider (~30% market share); operates massive packaging facilities in Kaohsiung and Shanghai."),
        ("Amkor Technology (USA/Korea)", "Strategic partner to Qualcomm and Apple; pioneering advanced substrate and System-in-Package (SiP) modules."),
        ("JCET & Tongfu Microelectronics (China)", "Dominant packaging houses for domestic Chinese processors and mid-tier smartphone silicon.")
    ], ACCENT_ORANGE, "🏭")

    add_card(s17, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "The Mobile Chiplet Horizon", [
        ("Breaking the Monolithic Die", "As wafer costs explode, separating compute (CPU/GPU) from I/O and analog modems onto cheaper legacy nodes is the next frontier."),
        ("Interconnect Latency Challenges", "Mobile power budgets (3-5W) make high-speed inter-die interconnects (UCIe) difficult to implement without battery drain."),
        ("3D Hybrid Bonding", "Direct copper-to-copper wafer stacking (TSMC SoIC) will allow SRAM caches to be stacked directly under CPU cores by 2027."),
        ("Substrate Warping & Yields", "Advanced multi-die packaging introduces compound yield risks where one bad die scraps the entire package.")
    ], ACCENT_GREEN, "🧩")

    # ==================== SLIDE 18: RISKS & BULLWHIP EFFECT (WITH CHART) ====================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18)
    add_header(s18, "Supply Chain Resilience, Bottlenecks & The Bullwhip Effect")

    if os.path.exists("charts/company_resilience_radar.png"):
        s18.shapes.add_picture("charts/company_resilience_radar.png", Inches(0.8), Inches(1.65), width=Inches(5.7))

    add_card(s18, Inches(6.7), Inches(1.65), Inches(5.8), Inches(2.6), "The Semiconductor Bullwhip Effect", [
        ("Long Inelastic Lead Times", "From silicon wafer start to finished smartphone in consumer hands takes 20 to 26 weeks; fab capacity cannot flex overnight."),
        ("The 2021 Shortage vs. 2023 Glut", "OEM double-ordering during COVID created phantom demand; when consumer demand dipped in 2023, chip inventories took 18 months to clear."),
        ("Buffer Stock Shift", "Transition from lean 'Just-in-Time' (JIT) to strategic 'Just-in-Case' (JIC) inventory with 90-120 days of component buffers.")
    ], ACCENT_ORANGE, "⚠️")

    add_card(s18, Inches(6.7), Inches(4.4), Inches(5.8), Inches(2.6), "Geopolitical Chokepoint Vulnerability", [
        ("Taiwan Strait Concentration", "A hypothetical naval blockade or earthquake in Taiwan would halt >85% of global advanced mobile processor supply."),
        ("US Export Controls & Entity List", "Export bans on <14nm equipment and advanced EDA tools divide the global supply chain into Western and Chinese blocs."),
        ("Raw Material Sanctions", "China's export restrictions on Gallium, Germanium, and Antimony threaten compound semiconductor and wafer manufacturing.")
    ], ACCENT_ROSE, "🌐")

    # ==================== SLIDE 19: FUTURE OUTLOOK (2NM GAA & AI) ====================
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_background(s19)
    add_header(s19, "Future Horizons: 2nm GAA, On-Device AI & Geopolitical Diversification")

    add_card(s19, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The 2nm GAA & Backside Power Leap", [
        ("Nanosheet Transistors", "Transitioning from FinFET to Gate-All-Around (GAA) nanosheets to minimize sub-threshold leakage at 2nm."),
        ("Backside Power Delivery (BSPDN)", "Routing power rails on the backside of the wafer (TSMC A16 / Intel PowerVia) frees top interconnect layers for signals, boosting speed +10% and density +15%."),
        ("Staggering Tool CapEx", "2nm fabs require High-NA EUV scanners ($350M each), driving fab construction costs past $20B per module."),
        ("Initial Allocation", "Apple has already locked up TSMC's 2nm pilot and early mass production capacity in Hsinchu Fab 20.")
    ], ACCENT_BLUE, "🔬")

    add_card(s19, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "The On-Device Generative AI Super-Cycle", [
        ("Silicon Real Estate Reallocation", "NPU/TPU die area expanding from <8% to >20% of total SoC footprint to run 10B+ parameter LLMs locally."),
        ("LPDDR5T & LPDDR6 Memory Rush", "On-device AI requires memory bandwidth exceeding 150 GB/s, driving rapid adoption of next-gen LPDDR6 standards."),
        ("Context Window Cache Demands", "System-level on-die cache expanding to 32MB-48MB to prevent DRAM round-trips that drain mobile batteries."),
        ("AI Agent Workloads", "Mobile silicon optimized for autonomous multi-modal agents processing voice, screen pixels, and sensors simultaneously.")
    ], ACCENT_PURPLE, "🤖")

    add_card(s19, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Geographic De-Risking (CHIPS Acts)", [
        ("TSMC Fab 21 (Arizona, USA)", "$65B investment in three fab modules; Phase 1 producing 4nm wafers, Phase 2 targeting 3nm/2nm."),
        ("The Packaging Blindspot", "Arizona-produced wafers still require air-freight back to Taiwan for InFO packaging, leaving supply chains partially exposed."),
        ("TSMC JASM (Kumamoto, Japan)", "Specialty logic and image sensor fab operating with Japanese government subsidies (Sony/Denso partner)."),
        ("Samsung Taylor Fab (Texas)", "Expanding US advanced foundry footprint with $6.4B US CHIPS Act grants to rival TSMC in North America.")
    ], ACCENT_GREEN, "🌍")

    # ==================== SLIDE 20: STRATEGIC RECOMMENDATIONS ====================
    s20 = prs.slides.add_slide(blank_layout)
    set_slide_background(s20)
    add_header(s20, "Strategic Recommendations for Industry Leaders & Conclusion")

    add_card(s20, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "For Smartphone OEMs (Device Makers)", [
        ("Dual-Sourcing Silicon Roads", "Avoid 100% single-merchant dependency; balance Qualcomm and MediaTek portfolios to protect gross margins."),
        ("Strategic Buffer Contracts", "Lock in 12-to-18 month component allocations with take-or-pay flexibility to withstand cyclical supply shocks."),
        ("Software-Silicon Co-Design", "Optimize proprietary neural runtimes (e.g. Gemini, Apple CoreML) to squeeze max performance out of existing nodes."),
        ("Tiered Model Strategy", "Reserve expensive sub-3nm processors exclusively for flagship Pro tiers; utilize mature 4nm/6nm for mass market.")
    ], ACCENT_BLUE, "📱")

    add_card(s20, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "For Chip Designers (Qualcomm, MediaTek)", [
        ("Dual-Foundry PDK Portability", "Maintain dual-compatible physical design rules to allow tape-out migration between TSMC and Samsung Foundry if yields shift."),
        ("Accelerate Chiplet Architectures", "Disaggregate I/O and analog modem circuitry onto mature nodes, reserving costly 2nm GAA wafers solely for CPU/GPU dies."),
        ("Architectural Royalty Hedging", "Invest aggressively in RISC-V compute engines and custom microarchitectures to reduce exposure to ARM licensing fees."),
        ("Automotive & Edge Expansion", "Repurpose high-performance smartphone SoC platforms for automotive cockpits and AI PC markets.")
    ], ACCENT_ORANGE, "⚙️")

    add_card(s20, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Conclusion & Final Outlook", [
        ("The Sovereign Silicon Era", "Mobile processors are no longer mere consumer electronics parts; they are strategic national assets shaping geopolitical power."),
        ("High Barriers to Entry", "With $300M+ tape-outs and $20B+ fab costs, the barrier to entering the cutting-edge mobile SoC race is practically insurmountable."),
        ("TSMC Remains Indispensable", "Despite US/EU CHIPS Acts, Taiwan's integrated semiconductor cluster will remain the world's primary silicon foundry through 2030."),
        ("The AI Paradigm Shift", "The next decade will be defined not by raw CPU gigahertz, but by TOPS/watt efficiency and memory bandwidth.")
    ], ACCENT_GREEN, "🎯")

    output_path = "mobile_processor_supply_chain_presentation.pptx"
    prs.save(output_path)
    print(f"Presentation saved successfully to {output_path}")

if __name__ == '__main__':
    build_presentation()
