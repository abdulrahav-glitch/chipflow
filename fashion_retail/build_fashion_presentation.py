import sys
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

    # Color Palette: Luxury Fashion Executive Theme
    BG_COLOR = RGBColor(9, 13, 22)         # #090D16 Deep Obsidian Slate
    CARD_BG = RGBColor(22, 32, 54)          # #162036 Card Navy
    CARD_BORDER = RGBColor(51, 65, 85)      # #334155 Slate Border
    ACCENT_GOLD = RGBColor(245, 158, 11)    # #F59E0B Champagne Gold
    ACCENT_ROSE = RGBColor(251, 113, 133)   # #FB7185 Rose Pink
    ACCENT_EMERALD = RGBColor(16, 185, 129) # #10B981 Emerald
    ACCENT_CYAN = RGBColor(56, 189, 248)    # #38BDF8 Cyan
    ACCENT_PURPLE = RGBColor(192, 132, 252) # #C084FC Lilac Purple
    TEXT_WHITE = RGBColor(248, 250, 252)    # #F8FAFC Heading White
    TEXT_MUTED = RGBColor(148, 163, 184)    # #94A3B8 Muted Slate
    TEXT_BODY = RGBColor(226, 232, 240)     # #E2E8F0 Body Text White

    blank_layout = prs.slide_layouts[6]

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = BG_COLOR
        bg.line.fill.background()
        return bg

    def add_header(slide, title_text, category="GLOBAL FASHION RETAIL SALES & OMNICHANNEL STRATEGY"):
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.7), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = category.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = ACCENT_GOLD

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

    def add_card(slide, left, top, width, height, title, items, accent_color=ACCENT_GOLD, title_icon=""):
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

    def add_metric_box(slide, left, top, width, height, val, label, subtext, color=ACCENT_GOLD):
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

    # ==================== SLIDE 1: TITLE SLIDE (WITH RUNWAY IMAGE) ====================
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_background(s1)

    # Embed Runway Hero Image on Right
    img_runway = "fashion_retail/images/fashion_runway.jpg"
    if os.path.exists(img_runway):
        s1.shapes.add_picture(img_runway, Inches(8.2), Inches(0.8), width=Inches(4.5))

    bar = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.8), Inches(0.1), Inches(3.6))
    bar.fill.solid()
    bar.fill.fore_color.rgb = ACCENT_GOLD
    bar.line.fill.background()

    tb = s1.shapes.add_textbox(Inches(1.2), Inches(1.7), Inches(6.8), Inches(4.0))
    tf = tb.text_frame
    tf.word_wrap = True

    p0 = tf.paragraphs[0]
    p0.text = "EXECUTIVE RETAIL STRATEGY & MARKET DYNAMICS"
    p0.font.size = Pt(12)
    p0.font.bold = True
    p0.font.color.rgb = ACCENT_GOLD
    p0.space_after = Pt(10)

    p1 = tf.add_paragraph()
    p1.text = "Fashion Retail Sales Analysis"
    p1.font.size = Pt(36)
    p1.font.bold = True
    p1.font.color.rgb = TEXT_WHITE
    p1.space_after = Pt(8)

    p2 = tf.add_paragraph()
    p2.text = "Omnichannel Economics, Inventory Velocity, Markdown Science & Supply Chain Agility Across Global Apparel Giants"
    p2.font.size = Pt(14)
    p2.font.color.rgb = ACCENT_ROSE
    p2.space_after = Pt(20)

    p3 = tf.add_paragraph()
    p3.text = "Benchmarking Inditex (Zara), Shein, Nike, LVMH & Fast Retailing (Uniqlo)"
    p3.font.size = Pt(12)
    p3.font.color.rgb = TEXT_MUTED

    # Bottom metric badges
    badges = [
        ("Global Market", "$1.7 Trillion+"),
        ("E-Com Penetration", "32% Digital Share"),
        ("Zara Speed", "15-Day Design-Rack"),
        ("Returns Drag", "$800B Reverse Cost")
    ]
    for i, (b_label, b_val) in enumerate(badges):
        add_metric_box(s1, Inches(0.8 + i * 2.98), Inches(5.8), Inches(2.8), Inches(1.15), b_val, b_label, "Industry Benchmark 2026", ACCENT_GOLD if i%2==0 else ACCENT_ROSE)

    # ==================== SLIDE 2: EXECUTIVE SUMMARY ====================
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_background(s2)
    add_header(s2, "Executive Summary: The Modern Fashion Retail Battlefield")

    add_metric_box(s2, Inches(0.8), Inches(1.65), Inches(2.78), Inches(1.2), "$1.73T", "Global Market Value", "Apparel, Footwear & Accessories", ACCENT_GOLD)
    add_metric_box(s2, Inches(3.78), Inches(1.65), Inches(2.78), Inches(1.2), "68%", "Zara Full-Price Sell-Thru", "Vs 45% Industry Average", ACCENT_EMERALD)
    add_metric_box(s2, Inches(6.76), Inches(1.65), Inches(2.78), Inches(1.2), "28.5%", "E-Commerce Return Rate", "Triples Physical Store Returns", ACCENT_ROSE)
    add_metric_box(s2, Inches(9.74), Inches(1.65), Inches(2.78), Inches(1.2), "7-15 Days", "Agile Cycle Time", "Ultra-Fast On-Demand Production", ACCENT_CYAN)

    add_card(s2, Inches(0.8), Inches(3.1), Inches(3.75), Inches(3.8), "The Death of 6-Month Seasons", [
        ("Agile Velocity Over Volume", "Traditional Autumn/Winter & Spring/Summer collections have been dismantled by micro-seasons."),
        ("Small-Batch Testing", "Retail winners test initial runs of 100-500 units before triggering automated reorders, eliminating unsold deadstock."),
        ("Nearshoring Advantage", "Moving production closer to primary consumption hubs (Morocco, Turkey, Mexico) cuts transit from weeks to days.")
    ], ACCENT_GOLD, "⚡")

    add_card(s2, Inches(4.78), Inches(3.1), Inches(3.75), Inches(3.8), "Omnichannel Friction & Returns", [
        ("Digital Channel Saturation", "Customer Acquisition Cost (CAC) via digital ads has surged +65% post-iOS privacy changes."),
        ("The Reverse Logistics Crisis", "Online apparel returns now exceed 25-30%, destroying unit margins and creating massive warehouse costs."),
        ("The Re-Energized Store", "Physical stores have evolved into experiential showrooms and local fulfillment nodes (BOPIS / Ship-from-Store).")
    ], ACCENT_ROSE, "🔄")

    add_card(s2, Inches(8.76), Inches(3.1), Inches(3.75), Inches(3.8), "AI-Driven Hyper-Personalization", [
        ("Predictive Merchandising", "Computer vision scans social media and runway trends to forecast demand before manufacturing commences."),
        ("Dynamic Markdown Algorithms", "AI models price clearance items dynamically by store cluster, saving 4-6% in gross margin."),
        ("Circular Economy Compliance", "EU regulations (CSDDD, Digital Product Passports) force retailers to account for garment lifecycle and recycling.")
    ], ACCENT_EMERALD, "🤖")

    # ==================== SLIDE 3: FASHION RETAIL SEGMENTS ====================
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_background(s3)
    add_header(s3, "Anatomy of Fashion Retail Segments: Business Models & Margins")

    add_card(s3, Inches(0.8), Inches(1.65), Inches(2.78), Inches(5.35), "1. Ultra-Fast Fashion\n(Shein, Temu, Cider)", [
        ("Operating Cycle", "7-10 day design-to-app launch; 6,000+ new SKUs dropped daily."),
        ("Batch Size", "Micro-batches of 50-100 units; automated reorders based on clicks."),
        ("Margin Profile", "Gross margin: 40-48%; Net margin: 5-8% (reliant on cross-border de minimis tax exemptions)."),
        ("Customer Dynamic", "Gen Z mobile shoppers driven by extreme price elasticity and social micro-trends.")
    ], ACCENT_PURPLE, "⚡")

    add_card(s3, Inches(3.78), Inches(1.65), Inches(2.78), Inches(5.35), "2. Agile Fast Fashion\n(Zara / Inditex, H&M)", [
        ("Operating Cycle", "15-30 day turnaround; 50%+ production nearshored (Spain, Portugal, Turkey)."),
        ("Batch Size", "Limited store allocations creating deliberate artificial scarcity."),
        ("Margin Profile", "Gross margin: 56-59%; Net margin: 12-14% with superior full-price sell-through (>65%)."),
        ("Customer Dynamic", "Fashion-conscious mass market seeking runway aesthetics at accessible price points.")
    ], ACCENT_ROSE, "👗")

    add_card(s3, Inches(6.76), Inches(1.65), Inches(2.78), Inches(5.35), "3. Sportswear / Athleisure\n(Nike, Lululemon, Adidas)", [
        ("Operating Cycle", "6-9 month performance R&D cycles; multi-year footwear tooling."),
        ("Batch Size", "Mass industrial production in Southeast Asia (Vietnam, Indonesia)."),
        ("Margin Profile", "Gross margin: 45-58%; Net margin: 10-15% backed by massive sponsorship brand equity."),
        ("Customer Dynamic", "Performance athletes and casual lifestyle consumers; high brand loyalty.")
    ], ACCENT_CYAN, "👟")

    add_card(s3, Inches(9.74), Inches(1.65), Inches(2.78), Inches(5.35), "4. Luxury & Haute Couture\n(LVMH, Kering, Hermès)", [
        ("Operating Cycle", "Handcrafted artisanal heritage; deliberate supply throttling."),
        ("Batch Size", "Limited edition numbered production in France, Italy, Switzerland."),
        ("Margin Profile", "Gross margin: 68-75%; Net margin: 25-32% (Zero markdown policy)."),
        ("Customer Dynamic", "Ultra-High-Net-Worth individuals; purchases driven by status, investment, and exclusivity.")
    ], ACCENT_GOLD, "👑")

    # ==================== SLIDE 4: LUXURY STORE & MERCHANDISING ====================
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_background(s4)
    add_header(s4, "The Modern Store Experience: Flagships as Media & Fulfillment Hubs")

    img_store = "fashion_retail/images/luxury_store.jpg"
    if os.path.exists(img_store):
        s4.shapes.add_picture(img_store, Inches(0.8), Inches(1.65), width=Inches(5.6))

    add_card(s4, Inches(6.7), Inches(1.65), Inches(5.8), Inches(2.6), "Stores as Experiential Showrooms", [
        ("Redefining Physical Retail", "Store floors are no longer warehouse storage; they are high-touch brand engagement theaters."),
        ("RFID Inventory Precision", "Zara and Nike utilize item-level RFID tags to achieve 99.5% real-time inventory visibility across global fleets."),
        ("Clienteling & Digital Styling", "Sales associates equipped with mobile tablets access customer online wishlist data and order history.")
    ], ACCENT_GOLD, "🏛️")

    add_card(s4, Inches(6.7), Inches(4.4), Inches(5.8), Inches(2.6), "Micro-Fulfillment & Ship-from-Store", [
        ("BOPIS Domination", "Buy-Online-Pick-Up-In-Store drives 20-30% higher incremental basket size when shoppers collect items."),
        ("Last-Mile Speed", "Using physical downtown stores to fulfill same-day local online delivery cuts freight costs by 35%."),
        ("Return Drop-Off Nodes", "Encouraging store returns eliminates reverse shipping fees and immediately puts inventory back on sales racks.")
    ], ACCENT_EMERALD, "📦")

    # ==================== SLIDE 5: INDITEX / ZARA DEEP DIVE ====================
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_background(s5)
    add_header(s5, "Company Deep-Dive: Inditex / Zara — The Agile Nearshoring Master")

    add_card(s5, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The 15-Day Agile Supply Chain", [
        ("Headquarters in Arteixo, Spain", "Centralized decision-making hub connecting designers directly with commercial store managers."),
        ("Nearshore Sourcing (50%+)", "Fabricates rapid-response trend items in Portugal, Morocco, Spain, and Turkey; reserves basic staples for Asia."),
        ("Air Freight Delivery", "Twice-weekly deliveries to every Zara store globally by air and truck; stock on racks rotates every 3 weeks."),
        ("Store-Driven Feedback Loop", "Store managers feed POS sales and customer requests daily into design computers to adjust cutting orders in real time.")
    ], ACCENT_ROSE, "🇪🇸")

    add_card(s5, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "Inventory & Markdown Superiority", [
        ("Deliberate Scarcity Principle", "'Buy it now or you'll never see it again' drives full-price purchases without waiting for clearance."),
        ("68% Full-Price Sell-Through", "Dramatically outperforms the fashion industry average (40-45%), shielding gross margins (>57%)."),
        ("Single Integrated Stock Pool", "RFID tags merge online and physical inventory into one unified supply pool, preventing lost sales."),
        ("Flagship Optimization", "Closing smaller stores to open larger, digitally connected flagship mega-stores (average size +20%).")
    ], ACCENT_GOLD, "🏷️")

    add_card(s5, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Financial Scale & Strategic Risks", [
        ("Revenue Scale", "Inditex generated over $38.5B in annual revenue across Zara, Massimo Dutti, Bershka, and Stradivarius."),
        ("Rising Air Freight Costs", "Rapid air-freight logistics face margin pressure as jet fuel prices fluctuate."),
        ("Wage Inflation in Europe", "Nearshoring manufacturing costs in Southern Europe are rising, testing Zara's price ceiling."),
        ("Online Returns Surcharge", "Zara pioneered charging customers a return fee for mail-in online returns, slashing frivolous orders by 22%.")
    ], ACCENT_EMERALD, "📊")

    # ==================== SLIDE 6: SHEIN DEEP DIVE ====================
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_background(s6)
    add_header(s6, "Company Deep-Dive: Shein — The Algorithm-Driven Ultra-Fast Disrupter")

    add_card(s6, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "Real-Time Algorithmic Merchandising", [
        ("Digital Trend Scraping", "Proprietary software crawls TikTok, Instagram, and competitor sites to identify emerging aesthetic trends."),
        ("100-Unit Micro Batches", "Suppliers are given automated orders for just 100 units; if CTR and add-to-cart spike, 5,000 units are ordered within 48 hours."),
        ("Guangzhou Supply Cluster", "Over 5,000 contract garment workshops connected directly via Shein's proprietary digital MES platform."),
        ("Zero Physical Stores", "Eliminates physical real estate CapEx, leasing, and store staff overhead entirely.")
    ], ACCENT_PURPLE, "📱")

    add_card(s6, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "Cross-Border Logistics Advantage", [
        ("De Minimis Customs Loophole", "Ships individual parcels directly from China to consumer doorsteps under the $800 US / €150 EU tariff-free threshold."),
        ("Air-Cargo Capacity Grip", "Consumes an estimated 5,000 tons of air freight daily out of Southern China, chartering entire cargo fleets."),
        ("Negative Cash Conversion Cycle", "Customers pay immediately online, while Shein pays factory suppliers on 30-to-45-day terms."),
        ("Unmatched Catalog Depth", "Maintains an active catalog of over 600,000 SKUs, dwarfing any traditional department store.")
    ], ACCENT_CYAN, "✈️")

    add_card(s6, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Geopolitical & Regulatory Exposure", [
        ("Closing the De Minimis Gap", "US and EU governments are legislating to eliminate tariff exemptions on low-value e-commerce packages."),
        ("IP Infringement Lawsuits", "Fierce litigation from independent designers and brands over algorithmic copyright infringement."),
        ("ESG & Fast Fashion Backlash", "Severe scrutiny over synthetic polyester waste, carbon-heavy air freight, and garment factory labor standards."),
        ("Supply Chain Diversification", "Investing in manufacturing hubs in Brazil, Turkey, and Mexico to establish regional fulfillment.")
    ], ACCENT_ROSE, "⚠️")

    # ==================== SLIDE 7: NIKE INC DEEP DIVE ====================
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_background(s7)
    add_header(s7, "Company Deep-Dive: Nike Inc. — DTC Overreach & Wholesale Realignment")

    add_card(s7, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The Aggressive DTC Pivot", [
        ("Consumer Direct Acceleration", "Aggressively cut ties with wholesale partners (Foot Locker, Macy's, independent retailers) to prioritize Nike.com and Nike Apps."),
        ("Direct Margin Ambition", "Aimed to capture full retail markup rather than selling at 50% wholesale discounts to department stores."),
        ("SNKRS App Cultural Engine", "Gamified limited-edition sneaker drops (Air Jordan, Dunk), driving cult-like digital engagement and zero-CAC hype."),
        ("Digital Share Surge", "Digital DTC revenue rose from 15% to >40% of total Nike revenue between 2018 and 2023.")
    ], ACCENT_CYAN, "👟")

    add_card(s7, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "The Wholesale Backlash & Inventory Glut", [
        ("Loss of Shelf Space", "Cutting wholesale partners opened prime retail shelf space for emerging challenger brands like On Running and Hoka."),
        ("The Post-Pandemic Inventory Bullwhip", "Supply chain delays followed by sudden demand drops left Nike with billions in excess apparel and sneaker stock."),
        ("Aggressive Factory Store Markdowns", "Forced to liquidate millions of sneakers at 30-50% off in Nike Factory Outlets, eroding premium brand equity."),
        ("The Strategic Realignment", "Pivoting back to 'Win with Wholesale' partners to rebuild brand presence in malls and sporting goods stores.")
    ], ACCENT_ROSE, "📉")

    add_card(s7, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Supply Chain & Footwear Engineering", [
        ("Mass Industrial Scale", "Produces over 1.2 billion items annually across contract factories in Vietnam (50%), Indonesia (27%), and China."),
        ("Automated Flyknit Weaving", "Computer-controlled knitting machines reduce upper waste by 60% and shave hours off footwear assembly."),
        ("Long-Cycle Lead Times", "Footwear tooling and mold manufacturing require 6 to 9 months of advance planning."),
        ("Athletic Sponsorship Moat", "Multi-billion dollar athlete endorsements (LeBron, Jordan, Mbappé) maintain unmatched cultural relevance.")
    ], ACCENT_GOLD, "🏅")

    # ==================== SLIDE 8: LVMH & LUXURY RETAIL ====================
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_background(s8)
    add_header(s8, "Company Deep-Dive: LVMH — The Economics of Extreme Scarcity & Luxury")

    add_card(s8, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The Anti-Fast-Fashion Philosophy", [
        ("Deliberate Scarcity & Allocation", "Products (Louis Vuitton, Dior, Celine) are intentionally undersupplied to cultivate aspirational desire."),
        ("Zero Markdown Policy", "Luxury leaders never discount or hold clearance sales; unsold items are stored in archives or repurposed."),
        ("Vertical Integration Control", "Owns tannery operations, leather workshops, and 100% of retail distribution flagships globally."),
        ("The Hermès Model Comparison", "Waitlists for flagship bags (Birkin/Kelly) enforce brand loyalty and eliminate inventory obsolescence risk.")
    ], ACCENT_GOLD, "💎")

    add_card(s8, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "Clienteling & Spatial Experience", [
        ("Private Salons for VICs", "Top 5% of Very Important Clients (VICs) generate over 40% of luxury fashion revenue via private VIP salons."),
        ("Trophy Real Estate Dominance", "Invests billions in flagship properties on Fifth Avenue (NYC), Champs-Élysées (Paris), and Ginza (Tokyo)."),
        ("Hospitality Synergy", "Integrating luxury retail with branded cafés, hotels (Cheval Blanc), and contemporary art foundations."),
        ("High Gross Margins (>70%)", "Exceptional pricing power allows consecutive annual price increases without dampening demand.")
    ], ACCENT_EMERALD, "🍾")

    add_card(s8, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Macro Vulnerabilities & Re-commerce", [
        ("China Consumer Slowdown", "Heavy reliance on Chinese affluent travelers and domestic luxury consumption creates revenue exposure."),
        ("The 'Aspirational' Squeeze", "Middle-class aspirational consumers cut back on $1,500 canvas bags during economic inflationary cycles."),
        ("The Certified Pre-Owned Threat", "Secondary luxury resale platforms (Vestiaire Collective, The RealReal) disrupt pricing control."),
        ("Digital Resistance", "Balancing the need for digital reach with the exclusivity of in-store champagne clienteling.")
    ], ACCENT_ROSE, "⚠️")

    # ==================== SLIDE 9: FAST RETAILING / UNIQLO ====================
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_background(s9)
    add_header(s9, "Company Deep-Dive: Fast Retailing / Uniqlo — The Science of LifeWear")

    add_card(s9, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The 'Made for All' LifeWear Philosophy", [
        ("Anti-Trend Strategy", "Unlike Zara or Shein, Uniqlo designs high-quality functional wardrobe staples that never go out of style."),
        ("Limited SKU Depth", "Maintains ~1,000 highly engineered core SKUs compared to tens of thousands at typical fast fashion retailers."),
        ("Material Science Moats", "Proprietary textile partnerships with Toray Industries: HEATTECH (thermal retention) and AIRism (cooling)."),
        ("Multi-Year Product Cycles", "Refines the exact same down jacket or fleece over 10+ seasons, optimizing manufacturing yields to 99%+.")
    ], ACCENT_EMERALD, "🇯🇵")

    add_card(s9, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "High-Volume Factory Commitments", [
        ("Dedicated Partner Factories", "Contracts with a small network of large factories in China, Vietnam, and Bangladesh with year-round production."),
        ("Immense Scale Discounts", "Orders millions of units per colorway, securing bottom-dollar raw textile and spinning costs."),
        ("High Inventory Predictability", "Low seasonal obsolescence allows Uniqlo to carry basic inventory across quarters without steep markdowns."),
        ("Automated Warehouses", "Pioneered 90% robotic automated fulfillment centers in Ariake, Tokyo, with RFID automated sorting.")
    ], ACCENT_CYAN, "🏭")

    add_card(s9, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Global Expansion & Western Push", [
        ("Asia Dominance", "Stronghold in Japan, Greater China, and Southeast Asia; accelerating store openings in North America and Europe."),
        ("Gross Margin Discipline", "Consistently delivers 52-54% gross margins with exceptionally low markdown write-downs."),
        ("Collaborations as Cultural Hype", "Capsule collections with designers (Jil Sander, JW Anderson, KAWS) drive massive store lines."),
        ("Currency & Sourcing Headwinds", "Weaker Japanese Yen inflates raw cotton and energy import costs for domestic stores.")
    ], ACCENT_GOLD, "🌏")

    # ==================== SLIDE 10: MARKET REVENUES (WITH CHART) ====================
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_background(s10)
    add_header(s10, "Global Market Benchmarks: Annual Fashion Revenues & Leaders")

    chart_market = "fashion_retail/charts/fashion_market_share.png"
    if os.path.exists(chart_market):
        s10.shapes.add_picture(chart_market, Inches(0.8), Inches(1.65), width=Inches(6.6))

    add_card(s10, Inches(7.6), Inches(1.65), Inches(4.9), Inches(2.6), "Scale & Profit Pool Divergence", [
        ("Nike & Inditex Scale Giants", "Nike ($51B+) and Inditex ($38B+) lead the global apparel and footwear space in revenue and supply chain footprint."),
        ("LVMH Luxury Dominance ($46B)", "Fashion & leather goods division captures the highest operating margins in retail (>38% EBIT margin)."),
        ("Shein's Meteoric Rise ($34B)", "Disrupted traditional retail in under a decade to surpass H&M and rival Zara in global sales volume.")
    ], ACCENT_GOLD, "📊")

    add_card(s10, Inches(7.6), Inches(4.4), Inches(4.9), Inches(2.6), "Strategic Market Observations", [
        ("Fast Retailing Global Push", "Uniqlo's parent company is scaling toward $30B+ by dominating Asian markets and expanding in the US."),
        ("H&M's Transition Struggle", "Caught between Shein's unbeatable pricing and Zara's superior aesthetic speed, forcing store rationalization."),
        ("Segment Polarization", "The fashion middle is hollowing out: consumers buy either ultra-cheap basics or premium luxury.")
    ], ACCENT_EMERALD, "💡")

    # ==================== SLIDE 11: 5-TIER FASHION SUPPLY CHAIN ====================
    s11 = prs.slides.add_slide(blank_layout)
    set_slide_background(s11)
    add_header(s11, "The 5-Tier Fashion Supply Chain: Cotton & Polymer to Consumer Wardrobe")

    tiers = [
        ("Tier 4: Raw Agricultural & Petrochemical Fiber Production", "Cotton Cultivation (India, US, Brazil) • Synthetic Polymers & Polyester (China, Taiwan) • Wool, Silk, Viscose\nOver 65% of all global garment fibers are now synthetic polyester derived from petroleum.", ACCENT_ROSE),
        ("Tier 3: Yarn Spinning, Weaving, Knitting & Fabric Finishing", "Textile Mills in China, India, Pakistan, Turkey • Dyeing, Printing, Washing, Water-proofing & Functional Coatings\nHeavy chemical and clean-water consumption; major environmental and wastewater scrutiny.", ACCENT_GOLD),
        ("Tier 2: Garment Manufacturing, Cut-Make-Trim (CMT) & Assembly", "Garment Assembly in Bangladesh, Vietnam, Cambodia, Indonesia, Mexico, Portugal, Morocco\nLabor-intensive sewing lines; transitioning toward automated fabric laser-cutting and digital pattern markers.", ACCENT_CYAN),
        ("Tier 1: Global Freight, Consolidation & Regional Fulfillment Hubs", "Intermodal Ocean Freight (20-30 days) vs Air Express (2-4 days) • Automated Distribution Centers (RFID, AGVs)\nCross-docking facilities sorting inventory into e-commerce parcels vs bulk retail store shipments.", ACCENT_PURPLE),
        ("Tier 0: Retail Floor Merchandising, DTC E-Commerce & Reverse Logistics", "Omnichannel Stores (Visual Merchandising, Clienteling) • E-Commerce Last-Mile Delivery (FedEx, DHL, Local Couriers)\nReverse Logistics Processing Centers inspecting, cleaning, and restocking returned garments.", ACCENT_EMERALD)
    ]

    for i, (t_title, t_desc, col) in enumerate(tiers):
        c = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.65 + i * 1.08), Inches(11.733), Inches(0.98))
        c.fill.solid()
        c.fill.fore_color.rgb = CARD_BG
        c.line.color.rgb = CARD_BORDER
        c.line.width = Pt(1)

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

    # ==================== SLIDE 12: OMNICHANNEL CHANNEL SPLIT (WITH CHART) ====================
    s12 = prs.slides.add_slide(blank_layout)
    set_slide_background(s12)
    add_header(s12, "Omnichannel Channel Evolution: The In-Store vs. Digital Convergence")

    chart_channels = "fashion_retail/charts/omnichannel_sales_split.png"
    if os.path.exists(chart_channels):
        s12.shapes.add_picture(chart_channels, Inches(0.8), Inches(1.65), width=Inches(6.6))

    add_card(s12, Inches(7.6), Inches(1.65), Inches(4.9), Inches(2.6), "The 50/50 Channel Equilibrium", [
        ("Store Share Stabilizes at ~50%", "After pandemic peaks, in-store shopping rebounded strongly; consumers still demand tactile touch, fit, and immediate gratification."),
        ("E-Commerce Stabilizes at ~33%", "Pure-play online growth has normalized as shipping costs and return rates erode pure digital profitability."),
        ("Social & Live Shopping Surges (17%)", "TikTok Shop and live video commerce represent the fastest-growing fashion retail channel globally.")
    ], ACCENT_GOLD, "📱")

    add_card(s12, Inches(7.6), Inches(4.4), Inches(4.9), Inches(2.6), "Strategic Channel Synergy", [
        ("The 'Halo Effect' of Stores", "Opening a new physical flagship store increases local online traffic to that brand by +35% within 90 days."),
        ("Unified Commerce Engines", "Single customer ID profiles merging in-store loyalty cards with online mobile app browsing behavior."),
        ("Endless Aisle Deployment", "Store associates ordering out-of-stock sizes online directly from the register for free home delivery.")
    ], ACCENT_CYAN, "🔗")

    # ==================== SLIDE 13: LEAD TIMES VS TURNS (WITH CHART) ====================
    s13 = prs.slides.add_slide(blank_layout)
    set_slide_background(s13)
    add_header(s13, "Speed-to-Market vs. Inventory Turnover: The Velocity Metric")

    chart_speed = "fashion_retail/charts/inventory_turnover_leadtime.png"
    if os.path.exists(chart_speed):
        s13.shapes.add_picture(chart_speed, Inches(0.8), Inches(1.65), width=Inches(6.6))

    add_card(s13, Inches(7.6), Inches(1.65), Inches(4.9), Inches(2.6), "The Working Capital Multiplier", [
        ("Inventory Velocity Drives Cash", "Shein turns inventory 12.5x per year; Zara turns stock 8.2x. Traditional apparel brands turn stock only 2.8x."),
        ("Minimizing Working Capital Tie-up", "High inventory turns free up cash reserves, allowing retailers to reinvest in immediate trend batches."),
        ("Lead Time Compounding", "Every extra week of design-to-rack lead time increases forecasting error by ~8-12%, compounding markdown risks.")
    ], ACCENT_ROSE, "⏱️")

    add_card(s13, Inches(7.6), Inches(4.4), Inches(4.9), Inches(2.6), "The Nearshoring Advantage", [
        ("Nearshore Flexibility", "Zara accepts a +15% higher labor cost in Portugal/Morocco because it eliminates 30 days of ocean container transit."),
        ("Postponement Strategy", "Holding greige (undyed) fabrics in distribution centers and dyeing them only when seasonal color trends emerge."),
        ("Test & Re-order Discipline", "Only 15-20% of inventory is committed before the season begins, keeping 80% open-to-buy (OTB).")
    ], ACCENT_EMERALD, "🚢")

    # ==================== SLIDE 14: UNIT ECONOMICS (WITH CHART) ====================
    s14 = prs.slides.add_slide(blank_layout)
    set_slide_background(s14)
    add_header(s14, "Unit Economics of a $100 Retail Garment: Cost Breakdown")

    chart_unit = "fashion_retail/charts/retail_cost_breakdown.png"
    if os.path.exists(chart_unit):
        s14.shapes.add_picture(chart_unit, Inches(0.8), Inches(1.65), width=Inches(6.6))

    add_card(s14, Inches(7.6), Inches(1.65), Inches(4.9), Inches(2.6), "Where Does the $100 Go?", [
        ("Raw COGS ($22):", "Fabric, zippers, thread, and garment factory labor represent less than a quarter of the consumer retail tag."),
        ("Retail Store Operations ($24):", "Store rent in premier high-street malls, utilities, and sales associate wages remain a dominant cost driver."),
        ("Digital Marketing & CAC ($14):", "Paid social media ads (Meta, TikTok, Google) consume a growing slice of apparel margins.")
    ], ACCENT_GOLD, "💵")

    add_card(s14, Inches(7.6), Inches(4.4), Inches(4.9), Inches(2.6), "The Silent Profit Killers", [
        ("Reverse Logistics & Returns ($11):", "Inspection, repackaging, and freight on returned items erode more profit than shipping costs."),
        ("Markdowns & Discounts ($13):", "Promotional end-of-season sales reduce the average realized garment selling price to $87."),
        ("Net Operating Profit ($10):", "Leaves the typical fashion retailer with an EBIT operating margin of approximately 8-12%.")
    ], ACCENT_ROSE, "⚠️")

    # ==================== SLIDE 15: REVERSE LOGISTICS CRISIS ====================
    s15 = prs.slides.add_slide(blank_layout)
    set_slide_background(s15)
    add_header(s15, "The Reverse Logistics Nightmare: E-Commerce Returns Management")

    add_card(s15, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The Return Rate Gap", [
        ("Physical Store Returns (8-10%)", "Customers try items in fitting rooms before purchase, resulting in low return rates."),
        ("E-Commerce Returns (25-35%)", "Online apparel suffers from 'bracketing'—shoppers buy 3 sizes or colors with the intention of returning 2."),
        ("Holiday Spike (40%+)", "Post-holiday January return waves overwhelm logistics hubs and flood warehouses with seasonal items."),
        ("The $800B Global Cost", "Handling reverse logistics costs the global retail industry over $800 billion annually in freight and value loss.")
    ], ACCENT_ROSE, "📦")

    add_card(s15, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "The Reverse Supply Chain Pipeline", [
        ("Transportation Freight Squeeze", "Customer return shipping costs $10-$15 per package, often wiping out the entire product margin."),
        ("Manual Labor Inspection", "Every returned garment must be individually inspected for wear, stains, tags, and damage."),
        ("Restocking Depreciation", "Takes an average of 14-21 days for a returned item to get back onto active inventory racks, missing full-price selling windows."),
        ("The Landfill Scandal", "Historically, cheap fast fashion items were trashed rather than restocked due to inspection labor costs exceeding garment value.")
    ], ACCENT_GOLD, "🔄")

    add_card(s15, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Retail Mitigation Strategies", [
        ("Return Surcharges", "Zara, H&M, and ASOS now charge $2.50 to $4.00 for mail-in returns, encouraging in-store returns for free."),
        ("3D Virtual Fitting & AI Sizing", "Using 3D computer vision body scanners and precise garment measurement guides reduces fit-related returns by 18%."),
        ("Final Sale / Non-Returnable", "Designating steep clearance items as final sale to prevent dead-stock loops."),
        ("In-Store Exchange Incentives", "Offering 110% store credit bonuses if customers choose to exchange in-store rather than request cash refunds.")
    ], ACCENT_EMERALD, "🛡️")

    # ==================== SLIDE 16: MARKDOWN OPTIMIZATION ====================
    s16 = prs.slides.add_slide(blank_layout)
    set_slide_background(s16)
    add_header(s16, "Markdown Optimization & Dynamic Pricing: Protecting Gross Margins")

    add_card(s16, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The Promotional Margin Trap", [
        ("The Discount Addiction", "Department stores that rely on perpetual 30-50% off sales train consumers never to buy at full price."),
        ("Erosion of Brand Prestige", "Excessive discounting dilutes brand perception, shifting brands from aspirational to commodity status."),
        ("Gross Margin Return on Investment", "GMROI measures gross profit dollars earned for every dollar of inventory investment (Target: >3.0x)."),
        ("Deadstock Liquidation", "Off-price retail channels (TJ Maxx, Ross, outlet malls) purchase secondary inventory at 80-90% below wholesale.")
    ], ACCENT_ROSE, "🏷️")

    add_card(s16, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "AI-Powered Dynamic Markdowns", [
        ("Localized Store Elasticity", "A coat might sell out at full price in Chicago while needing a 20% discount in Atlanta; AI sets localized prices."),
        ("Optimal Markdown Timing", "Algorithmic models predict the exact date and discount percentage needed to clear inventory before season end."),
        ("Personalized Dynamic Offers", "Targeting discounts only to at-risk or price-sensitive app users while maintaining full price for loyalists."),
        ("Margin Recovery Impact", "Sophisticated markdown optimization saves retailers 350 to 500 basis points of gross margin annually.")
    ], ACCENT_GOLD, "🤖")

    add_card(s16, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Full-Price Sell-Through Levers", [
        ("Limited Production Runs", "Creating artificial scarcity by deliberately producing 10% less than projected demand (Zara playbook)."),
        ("Rapid Mid-Season Reorders", "Only reordering proven winners rather than committing budget to unproven seasonal items."),
        ("Cross-Merchandising Styling", "Merchandising complete outfits rather than standalone garments increases multi-item basket conversion."),
        ("VIP Early Access Drops", "Rewarding top-tier loyalty members with exclusive 48-hour access to full-price seasonal collections.")
    ], ACCENT_EMERALD, "💎")

    # ==================== SLIDE 17: RETAIL TECHNOLOGY & AI ====================
    s17 = prs.slides.add_slide(blank_layout)
    set_slide_background(s17)
    add_header(s17, "Fashion Retail Tech Stack: Computer Vision, RFID & Automated Logistics")

    add_card(s17, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "Trend Forecasting Algorithms", [
        ("Social Scraping & Sentiment", "Algorithms ingest billions of images across TikTok, Pinterest, and runway shows to detect emerging fabrics, colors, and cuts."),
        ("Lead Time Compression", "Reduces trend-to-design cycle from 8 weeks to 48 hours for fast fashion design studios."),
        ("Generative AI CAD Prototyping", "Generating 3D virtual garment prototypes (CLO3D) eliminates physical sample shipping and cutting waste.")
    ], ACCENT_PURPLE, "🔮")

    add_card(s17, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "RFID & Smart In-Store Tech", [
        ("Item-Level RFID Tracking", "Every garment carries a passive RFID tag scanned at checkout, inventory intake, and fitting rooms."),
        ("Smart Fitting Room Mirrors", "Touchscreen mirrors detect garment RFID tags, allowing shoppers to request different sizes from store staff."),
        ("Frictionless Self-Checkout", "Shoppers drop their entire basket into an RFID scanner bucket; all items are rung up simultaneously in 3 seconds.")
    ], ACCENT_CYAN, "📡")

    add_card(s17, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "Automated Robotics & Logistics", [
        ("AutoStore & Pocket Sorters", "High-density automated warehouse cubes with autonomous robots fetching inventory totes 24/7."),
        ("Automated Hanging Garment Sorters", "Suspended ceiling track systems sorting hundreds of thousands of dresses and coats directly onto delivery pallets."),
        ("Real-Time Delivery Routing", "Dynamic parcel optimization reducing last-mile e-commerce fulfillment costs by 15-20%.")
    ], ACCENT_EMERALD, "🤖")

    # ==================== SLIDE 18: STRATEGIC RADAR (WITH CHART) ====================
    s18 = prs.slides.add_slide(blank_layout)
    set_slide_background(s18)
    add_header(s18, "Competitive Agility Benchmark: The Retail Capabilities Matrix")

    chart_radar = "fashion_retail/charts/brand_resilience_radar.png"
    if os.path.exists(chart_radar):
        s18.shapes.add_picture(chart_radar, Inches(0.8), Inches(1.65), width=Inches(6.6))

    add_card(s18, Inches(7.6), Inches(1.65), Inches(4.9), Inches(2.6), "Strategic Capabilities Comparison", [
        ("Zara Leads Balanced Agility", "Scores exceptionally high in speed-to-market and full-price sell-through with robust gross margins."),
        ("Shein Unmatched in Digital Speed", "Dominates speed and digital e-commerce penetration, but lags severely in sustainability and return rates."),
        ("Nike Strong in Brand Equity", "Massive global sponsorship moat and DTC penetration, balancing wholesale realignments.")
    ], ACCENT_ROSE, "⚡")

    add_card(s18, Inches(7.6), Inches(4.4), Inches(4.9), Inches(2.6), "LVMH's Pricing Sanctuary", [
        ("Absolute Margin Hegemony", "LVMH operates in an entirely different margin universe (>75% gross margin) immune to promotional discounting."),
        ("The Luxury Moat", "Heritage, scarcity, and in-store clienteling create an enduring economic moat that fast fashion cannot replicate."),
        ("Key Strategic Takeaway", "To survive, retailers must either own extreme speed (Shein/Zara) or extreme brand equity and scarcity (LVMH/Hermès).")
    ], ACCENT_GOLD, "👑")

    # ==================== SLIDE 19: SUSTAINABILITY & CIRCULAR FASHION ====================
    s19 = prs.slides.add_slide(blank_layout)
    set_slide_background(s19)
    add_header(s19, "Sustainability, ESG & Circular Fashion: The Regulatory Reckoning")

    add_card(s19, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "The Overproduction Crisis", [
        ("100 Billion Garments Annually", "The fashion industry manufactures over 100 billion garments each year for 8 billion people."),
        ("30% Never Sold at Full Price", "An estimated 20-30% of manufactured clothing is liquidated through off-price channels, incinerated, or sent to landfills."),
        ("Textile Waste in the Global South", "Atacama Desert (Chile) and Kantamanto Market (Ghana) overwhelmed by discarded fast-fashion clothing mountains."),
        ("Microplastic Water Pollution", "Washing synthetic polyester and nylon garments releases 500,000 tons of microfibers into oceans annually.")
    ], ACCENT_ROSE, "🌍")

    add_card(s19, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "The Regulatory Hammer", [
        ("EU Corporate Sustainability Directive", "Mandates strict due diligence on child labor, living wages, and environmental damage across supply chains."),
        ("Digital Product Passports (DPP)", "EU requirement by 2027: garments must carry scannable QR tags detailing material composition, carbon footprint, and recyclability."),
        ("Ban on Destruction of Unsold Goods", "New European legislation officially outlawing the destruction of unsold textile inventory."),
        ("Extended Producer Responsibility (EPR)", "Brands taxed based on the volume and recyclability of garments they introduce into the market.")
    ], ACCENT_GOLD, "⚖️")

    add_card(s19, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "The Re-Commerce & Circular Frontier", [
        ("The Resale Boom ($350B by 2028)", "Secondhand luxury and vintage resale growing 3x faster than traditional apparel retail."),
        ("Brand-Owned Resale Portals", "Zara Pre-Owned and Lululemon Like New allowing customers to trade in used garments for store vouchers."),
        ("Fiber-to-Fiber Recycling", "Infinited Fiber, Renewcell, and textile recycling transforming post-consumer cotton scraps into fresh virgin-quality yarn."),
        ("Rental & Subscription Models", "Rent the Runway and luxury rental services providing access over ownership for occasion-wear.")
    ], ACCENT_EMERALD, "♻️")

    # ==================== SLIDE 20: STRATEGIC PLAYBOOK & CONCLUSION ====================
    s20 = prs.slides.add_slide(blank_layout)
    set_slide_background(s20)
    add_header(s20, "Strategic Playbook for Fashion Retail Executives & Conclusion")

    add_card(s20, Inches(0.8), Inches(1.65), Inches(3.75), Inches(5.35), "1. Agility & Supply Chain", [
        ("Nearshore 30-40% of Volume", "Establish rapid-response nearshoring hubs to reorder seasonal bestsellers within 15 days."),
        ("Small-Batch Test & Re-Order", "Limit initial SKU production runs to small trial batches; never commit >30% of inventory upfront."),
        ("Item-Level RFID Everywhere", "Deploy RFID across every garment to achieve >99% inventory accuracy and enable ship-from-store."),
        ("Diversify Freight Dependency", "Balance high-cost air freight with rail and intermodal transport to insulate against fuel spikes.")
    ], ACCENT_GOLD, "🏭")

    add_card(s20, Inches(4.78), Inches(1.65), Inches(3.75), Inches(5.35), "2. Omnichannel & Margins", [
        ("Curb Free Mail-in Returns", "Charge nominal fees for online mail returns while keeping in-store drop-offs free to drive foot traffic."),
        ("Dynamic Localized Markdowns", "Replace blanket 40% store sales with AI algorithms that discount items based on local store velocity."),
        ("Elevate In-Store Experiences", "Treat physical stores as media flagships, community event hubs, and rapid micro-fulfillment centers."),
        ("Unified Loyalty & Data Profiles", "Merge online browsing data with in-store clienteling tablets to maximize Lifetime Value (LTV).")
    ], ACCENT_ROSE, "💎")

    add_card(s20, Inches(8.76), Inches(1.65), Inches(3.75), Inches(5.35), "3. Circularity & Future", [
        ("Prepare for Digital Passports", "Audit fiber traceability and supply tier transparency ahead of EU 2027 DPP mandates."),
        ("Capture Secondhand Resale", "Launch proprietary brand-owned pre-owned trade-in programs to recapture secondary market value."),
        ("The Winning Formula", "Success in 2026+ demands mastering the intersection of runway design, algorithmic velocity, and circular sustainability."),
        ("Executive Verdict", "Agile speed protects margins from markdowns; strong brand equity protects margins from commoditization.")
    ], ACCENT_EMERALD, "🎯")

    out_path = "fashion_retail/fashion_retail_sales_presentation.pptx"
    prs.save(out_path)
    print(f"Fashion presentation saved successfully to {out_path}")

if __name__ == '__main__':
    build_presentation()
