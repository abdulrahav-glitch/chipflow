/**
 * ATELIER RETAIL: Fashion Retail Sales Analysis & Slide Deck
 * Interactive 20-Slide Presentation Engine & Simulation Suite
 */

// ==========================================================================
// 1. SLIDE DATA REPOSITORY (20 COMPREHENSIVE FASHION SLIDES)
// ==========================================================================
const slidesData = [
  {
    id: 1,
    category: "EXECUTIVE TITLE",
    title: "Global Fashion Retail Sales Strategy",
    subtitle: "Omnichannel Economics, Inventory Velocity, Markdown Science & Supply Chain Agility Across Global Apparel Giants",
    type: "hero_fashion",
    img: "images/fashion_runway.jpg",
    notes: "Welcome everyone. Today we are presenting an executive-level analysis of Global Fashion Retail Sales. We examine the entire retail value chain—from agile nearshoring at Zara and algorithmic micro-batching at Shein to omnichannel returns, markdown optimization algorithms, and luxury brand equity at LVMH."
  },
  {
    id: 2,
    category: "EXECUTIVE SUMMARY",
    title: "Executive Summary: The Modern Fashion Retail Battlefield",
    type: "metrics_and_cards",
    metrics: [
      { val: "$1.73T", label: "Global Market Value", sub: "Apparel & Footwear Retail", color: "" },
      { val: "68%", label: "Zara Full-Price Sell-Thru", sub: "Vs 45% Industry Average", color: "val-emerald" },
      { val: "28.5%", label: "E-Commerce Return Rate", sub: "Triples in-store return rate", color: "val-rose" },
      { val: "7-15 Days", label: "Agile Cycle Time", sub: "Design to consumer rack", color: "val-cyan" }
    ],
    cards: [
      {
        title: "The Death of 6-Month Seasons",
        icon: "⚡",
        trim: "trim-gold",
        items: [
          { label: "Agile Velocity Over Volume", desc: "Traditional Autumn/Winter & Spring/Summer collections dismantled by continuous micro-seasons." },
          { label: "Small-Batch Testing", desc: "Testing trial runs of 100-500 units before triggering automated reorders eliminates deadstock." },
          { label: "Nearshoring Advantage", desc: "Sourcing in Portugal, Morocco, Turkey, and Mexico cuts transit times from weeks to days." }
        ]
      },
      {
        title: "Omnichannel Friction & Returns",
        icon: "🔄",
        trim: "trim-rose",
        items: [
          { label: "Digital Channel Saturation", desc: "Customer Acquisition Cost (CAC) via digital ads has surged +65% post-iOS privacy changes." },
          { label: "The Reverse Logistics Crisis", desc: "Online apparel returns now exceed 25-30%, destroying unit margins and creating massive costs." },
          { label: "The Re-Energized Store", desc: "Physical stores have evolved into experiential showrooms and local fulfillment nodes." }
        ]
      },
      {
        title: "AI & Circular Compliance",
        icon: "🤖",
        trim: "trim-emerald",
        items: [
          { label: "Predictive Merchandising", desc: "Computer vision scans social media and runway trends to forecast demand before manufacturing." },
          { label: "Dynamic Markdown Science", desc: "Algorithmic models price clearance items dynamically by store cluster, saving 4-6% in margin." },
          { label: "Circular Regulatory Hammer", desc: "EU directives (CSDDD, Digital Product Passports) mandate fiber traceability and outlaw waste." }
        ]
      }
    ],
    notes: "Set the strategic context: Fashion retail is no longer about predicting trends 6 months ahead. It is about agile supply chains that test in small batches and reorder winners within 15 days."
  },
  {
    id: 3,
    category: "RETAIL ARCHETYPES",
    title: "Anatomy of Fashion Retail Segments: Business Models & Margins",
    type: "cards_grid",
    layout: "grid-4-col",
    cards: [
      {
        title: "1. Ultra-Fast\n(Shein, Temu)",
        icon: "⚡",
        trim: "trim-purple",
        items: [
          { label: "Operating Cycle", desc: "7-10 day turnaround; 6,000+ new SKUs dropped daily." },
          { label: "Batch Size", desc: "50-100 unit test batches; automated factory reorders." },
          { label: "Margin Profile", desc: "Gross margin: 40-48%; Net margin: 5-8% (de minimis reliant)." },
          { label: "Audience", desc: "Gen Z mobile shoppers driven by extreme price elasticity." }
        ]
      },
      {
        title: "2. Agile Fast Fashion\n(Zara, H&M)",
        icon: "👗",
        trim: "trim-rose",
        items: [
          { label: "Operating Cycle", desc: "15-30 day turnaround; 50%+ nearshore sourcing." },
          { label: "Batch Size", desc: "Limited allocations creating deliberate store scarcity." },
          { label: "Margin Profile", desc: "Gross margin: 56-59%; Net margin: 12-14% with high sell-through." },
          { label: "Audience", desc: "Fashion-conscious shoppers wanting runway looks at retail." }
        ]
      },
      {
        title: "3. Sportswear\n(Nike, Lululemon)",
        icon: "👟",
        trim: "trim-cyan",
        items: [
          { label: "Operating Cycle", desc: "6-9 month performance R&D; complex footwear molds." },
          { label: "Batch Size", desc: "Mass scale in Vietnam, Indonesia, and Cambodia." },
          { label: "Margin Profile", desc: "Gross margin: 45-58%; Net margin: 10-15% (brand equity)." },
          { label: "Audience", desc: "Athletes and lifestyle consumers with high brand loyalty." }
        ]
      },
      {
        title: "4. Artisanal Luxury\n(LVMH, Hermès)",
        icon: "👑",
        trim: "trim-gold",
        items: [
          { label: "Operating Cycle", desc: "Artisanal handcrafting; deliberate supply throttling." },
          { label: "Batch Size", desc: "Limited edition numbered runs in France & Italy." },
          { label: "Margin Profile", desc: "Gross margin: 68-75%; Net: 25-32% (Zero markdown policy)." },
          { label: "Audience", desc: "UHNW clients seeking status, investment, and exclusivity." }
        ]
      }
    ],
    notes: "Contrast the 4 operating archetypes. Emphasize how luxury commands over 70% gross margin with zero discounting, while ultra-fast fashion relies on high-velocity micro-batches."
  },
  {
    id: 4,
    category: "STORE EXPERIENCE",
    title: "The Modern Store Experience: Flagships as Media & Fulfillment Hubs",
    type: "photo_and_cards",
    img: "images/luxury_store.jpg",
    cards: [
      {
        title: "Stores as Experiential Showrooms",
        icon: "🏛️",
        trim: "trim-gold",
        items: [
          { label: "Redefining Physical Retail", desc: "Store floors are no longer warehouse storage; they are high-touch brand engagement theaters." },
          { label: "RFID Inventory Precision", desc: "Zara and Nike utilize item-level RFID tags to achieve 99.5% real-time inventory visibility." },
          { label: "Clienteling & Digital Styling", desc: "Sales associates equipped with tablets access customer online wishlist data and order history." }
        ]
      },
      {
        title: "Micro-Fulfillment & Ship-from-Store",
        icon: "📦",
        trim: "trim-emerald",
        items: [
          { label: "BOPIS Domination", desc: "Buy-Online-Pick-Up-In-Store drives 20-30% higher incremental basket size when shoppers collect items." },
          { label: "Last-Mile Speed", desc: "Using physical downtown stores to fulfill same-day local online delivery cuts freight costs by 35%." },
          { label: "Return Drop-Off Nodes", desc: "Encouraging store returns eliminates reverse shipping fees and immediately restocks sales racks." }
        ]
      }
    ],
    notes: "Physical retail is not dead—it has been reinvented. Physical stores act as local fulfillment nodes, return processing hubs, and high-margin customer acquisition venues."
  },
  {
    id: 5,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: Inditex / Zara — The Agile Nearshoring Master",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "The 15-Day Agile Supply Chain",
        icon: "🇪🇸",
        trim: "trim-rose",
        items: [
          { label: "Headquarters in Arteixo, Spain", desc: "Centralized hub connecting designers directly with commercial store managers." },
          { label: "Nearshore Sourcing (50%+)", desc: "Fabricates trend items in Portugal, Morocco, Spain, and Turkey; basics in Asia." },
          { label: "Air Freight Delivery", desc: "Twice-weekly deliveries to every Zara store globally by air and truck." },
          { label: "Store Feedback Loop", desc: "Store managers feed POS sales daily into design systems to adjust cutting orders." }
        ]
      },
      {
        title: "Inventory & Markdown Superiority",
        icon: "🏷️",
        trim: "trim-gold",
        items: [
          { label: "Deliberate Scarcity Principle", desc: "'Buy it now or you'll never see it again' drives full-price purchases without waiting." },
          { label: "68% Full-Price Sell-Through", desc: "Dramatically outperforms the fashion industry average (40-45%), protecting margins." },
          { label: "Single Integrated Stock Pool", desc: "RFID tags merge online and physical inventory into one unified supply pool." },
          { label: "Flagship Mega-Stores", desc: "Closing smaller stores to open larger, digitally connected flagship spaces." }
        ]
      },
      {
        title: "Financial Scale & Strategic Risks",
        icon: "📊",
        trim: "trim-emerald",
        items: [
          { label: "Revenue Scale", desc: "Generated over $38.5B in annual revenue across Zara, Massimo Dutti, and Bershka." },
          { label: "Rising Air Freight Costs", desc: "Rapid air-freight logistics face margin pressure as jet fuel prices fluctuate." },
          { label: "European Wage Inflation", desc: "Nearshoring costs in Southern Europe are rising, testing Zara's pricing ceiling." },
          { label: "Online Returns Surcharge", desc: "Pioneered charging fees for mail-in returns, slashing frivolous orders by 22%." }
        ]
      }
    ],
    notes: "Zara is the gold standard of agile supply chains. Nearshoring in Portugal and Morocco enables 15-day turnaround, achieving an industry-leading 68% full-price sell-through."
  },
  {
    id: 6,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: Shein — The Algorithm-Driven Ultra-Fast Disrupter",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "Real-Time Algorithmic Merchandising",
        icon: "📱",
        trim: "trim-purple",
        items: [
          { label: "Digital Trend Scraping", desc: "Software crawls TikTok, Instagram, and competitor sites to detect micro-trends." },
          { label: "100-Unit Micro Batches", desc: "Automated orders for just 100 units; if clicks surge, 5,000 units are ordered in 48h." },
          { label: "Guangzhou Supply Cluster", desc: "Over 5,000 contract sewing workshops connected via Shein's digital MES platform." },
          { label: "Zero Physical Stores", desc: "Eliminates physical store leasing, staff wages, and mall overhead entirely." }
        ]
      },
      {
        title: "Cross-Border Logistics Advantage",
        icon: "✈️",
        trim: "trim-cyan",
        items: [
          { label: "De Minimis Customs Loophole", desc: "Ships parcels directly from China under the $800 US / €150 EU tariff-free threshold." },
          { label: "Air-Cargo Grip", desc: "Consumes an estimated 5,000 tons of air freight daily, chartering entire Boeing 777 fleets." },
          { label: "Negative Cash Conversion", desc: "Customers pay immediately online, while Shein pays factory suppliers on 45-day terms." },
          { label: "600,000+ SKU Catalog", desc: "Dwarfs traditional retailers, offering unmatched variety with minimal inventory risk." }
        ]
      },
      {
        title: "Geopolitical & Regulatory Exposure",
        icon: "⚠️",
        trim: "trim-rose",
        items: [
          { label: "Closing De Minimis Loophole", desc: "US and EU governments are legislating to eliminate tariff exemptions on low-value parcels." },
          { label: "IP Litigation", desc: "Fierce lawsuits from independent designers over algorithmic design copying." },
          { label: "ESG Backlash", desc: "Intense scrutiny over polyester microfiber waste and garment factory labor standards." },
          { label: "Global Fabs Diversification", desc: "Investing in manufacturing hubs in Brazil, Turkey, and Mexico to diversify supply." }
        ]
      }
    ],
    notes: "Shein represents the algorithmization of fashion. Rather than hiring trend forecasters, computer algorithms monitor add-to-carts and social media clicks to drive production."
  },
  {
    id: 7,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: Nike Inc. — DTC Overreach & Wholesale Realignment",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "The Aggressive DTC Pivot",
        icon: "👟",
        trim: "trim-cyan",
        items: [
          { label: "Consumer Direct Acceleration", desc: "Cut wholesale partners (Foot Locker, Macy's) to prioritize Nike.com and Nike Apps." },
          { label: "Direct Margin Ambition", desc: "Aimed to capture full retail markup rather than selling at 50% wholesale discounts." },
          { label: "SNKRS App Hype Engine", desc: "Gamified sneaker drops (Air Jordan, Dunk) driving cult-like digital engagement." },
          { label: "Digital Share Surge", desc: "Digital revenue rose from 15% to >40% of total Nike revenue between 2018 and 2023." }
        ]
      },
      {
        title: "Wholesale Backlash & Inventory Glut",
        icon: "📉",
        trim: "trim-rose",
        items: [
          { label: "Loss of Shelf Space", desc: "Cutting wholesale opened shelf space for challenger brands like On Running and Hoka." },
          { label: "Inventory Bullwhip", desc: "Supply delays followed by demand drops left Nike with billions in excess sneakers." },
          { label: "Factory Store Markdowns", desc: "Forced to liquidate sneakers at 30-50% off in outlet stores, eroding brand equity." },
          { label: "Wholesale Return", desc: "Pivoting back to 'Win with Wholesale' partners to restore mall presence." }
        ]
      },
      {
        title: "Supply Chain & Footwear Engineering",
        icon: "🏅",
        trim: "trim-gold",
        items: [
          { label: "Mass Industrial Scale", desc: "Produces over 1.2 billion items annually in Vietnam (50%), Indonesia, and China." },
          { label: "Automated Flyknit Weaving", desc: "Computerized knitting machines reduce upper waste by 60% and speed assembly." },
          { label: "Long Lead Times", desc: "Footwear tooling and mold engineering require 6 to 9 months of advance planning." },
          { label: "Sponsorship Moat", desc: "Multi-billion dollar athlete endorsements (Jordan, LeBron, Mbappé) maintain cultural moat." }
        ]
      }
    ],
    notes: "Nike provides a cautionary tale on DTC overreach: cutting wholesale accounts too quickly left shelf space open to competitors and caused a multi-billion dollar inventory glut."
  },
  {
    id: 8,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: LVMH — The Economics of Extreme Scarcity & Luxury",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "The Anti-Fast-Fashion Philosophy",
        icon: "💎",
        trim: "trim-gold",
        items: [
          { label: "Deliberate Scarcity & Allocation", desc: "Products (Louis Vuitton, Dior, Celine) are undersupplied to cultivate aspirational desire." },
          { label: "Zero Markdown Policy", desc: "Luxury leaders never discount or hold clearance sales; unsold items are archived." },
          { label: "Vertical Integration Control", desc: "Owns tannery operations, leather workshops, and 100% of retail distribution flagships." },
          { label: "Waitlist Power", desc: "Waitlists enforce brand loyalty and eliminate inventory obsolescence risk." }
        ]
      },
      {
        title: "Clienteling & Spatial Experience",
        icon: "🍾",
        trim: "trim-emerald",
        items: [
          { label: "Private Salons for VICs", desc: "Top 5% of Very Important Clients (VICs) generate over 40% of luxury fashion revenue." },
          { label: "Trophy Real Estate Dominance", desc: "Invests billions in flagship properties on Fifth Avenue, Champs-Élysées, and Ginza." },
          { label: "Hospitality Synergy", desc: "Integrating luxury retail with branded cafés, hotels, and contemporary art foundations." },
          { label: "High Gross Margins (>70%)", desc: "Exceptional pricing power allows consecutive annual price hikes without volume drops." }
        ]
      },
      {
        title: "Macro Vulnerabilities & Re-commerce",
        icon: "⚠️",
        trim: "trim-rose",
        items: [
          { label: "China Consumer Slowdown", desc: "Heavy reliance on Chinese affluent travelers creates regional revenue exposure." },
          { label: "Aspirational Squeeze", desc: "Middle-class aspirational shoppers cut back on $1,500 canvas bags during inflation." },
          { label: "Certified Pre-Owned Threat", desc: "Secondary resale platforms (Vestiaire Collective) challenge primary brand pricing." },
          { label: "Digital Balance", desc: "Balancing digital reach with the exclusivity of in-store champagne clienteling." }
        ]
      }
    ],
    notes: "LVMH operates on the inverted rules of luxury: rather than meeting demand, luxury throttles supply to increase pricing power and achieve >72% gross margins."
  },
  {
    id: 9,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: Fast Retailing / Uniqlo — The Science of LifeWear",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "The 'LifeWear' Philosophy",
        icon: "🇯🇵",
        trim: "trim-emerald",
        items: [
          { label: "Anti-Trend Strategy", desc: "Unlike Zara or Shein, Uniqlo designs high-quality functional basics that never go out of style." },
          { label: "Limited SKU Depth", desc: "Maintains ~1,000 highly engineered core SKUs compared to tens of thousands at fast fashion peers." },
          { label: "Material Science Moats", desc: "Partnerships with Toray Industries: HEATTECH (thermal retention) and AIRism (cooling)." },
          { label: "Multi-Year Product Cycles", desc: "Refines the exact same down jacket over 10+ seasons, optimizing factory yields to 99%+." }
        ]
      },
      {
        title: "High-Volume Factory Commitments",
        icon: "🏭",
        trim: "trim-cyan",
        items: [
          { label: "Dedicated Partner Factories", desc: "Contracts with a small network of large factories in China, Vietnam, and Bangladesh." },
          { label: "Immense Scale Discounts", desc: "Orders millions of units per colorway, securing bottom-dollar raw textile prices." },
          { label: "High Inventory Predictability", desc: "Low seasonal obsolescence allows carrying basic inventory across quarters without write-downs." },
          { label: "Automated Warehouses", desc: "Pioneered 90% robotic automated fulfillment centers in Ariake, Tokyo, with RFID sorting." }
        ]
      },
      {
        title: "Global Expansion & Western Push",
        icon: "🌏",
        trim: "trim-gold",
        items: [
          { label: "Asia Dominance", desc: "Stronghold in Japan, Greater China, and SE Asia; accelerating store rollouts in the US and Europe." },
          { label: "Gross Margin Discipline", desc: "Delivers 52-54% gross margins with exceptionally low promotional markdown write-downs." },
          { label: "Designer Collaborations", desc: "Capsule collections with designers (Jil Sander, JW Anderson, KAWS) drive massive store queues." },
          { label: "Currency Headwinds", desc: "Weaker Japanese Yen inflates raw cotton and energy import costs for domestic stores." }
        ]
      }
    ],
    notes: "Uniqlo's genius is manufacturing basic functional apparel with material science (HEATTECH) that has no expiration date, avoiding seasonal fashion obsolescence."
  },
  {
    id: 10,
    category: "MARKET DYNAMICS",
    title: "Global Market Benchmarks: Annual Fashion Revenues & Leaders",
    type: "chart_and_cards",
    chart: "charts/fashion_market_share.png",
    cards: [
      {
        title: "Scale & Profit Pool Divergence",
        icon: "📊",
        trim: "trim-gold",
        items: [
          { label: "Nike & Inditex Scale Giants", desc: "Nike ($51B+) and Inditex ($38B+) lead global apparel in revenue, store footprint, and logistics." },
          { label: "LVMH Luxury Dominance ($46B)", desc: "Captures the highest operating margins in retail (>38% EBIT margin) with zero discounts." },
          { label: "Shein's Meteoric Rise ($34B)", desc: "Disrupted traditional retail in under a decade to rival Zara in global sales volume." }
        ]
      },
      {
        title: "Strategic Market Observations",
        icon: "💡",
        trim: "trim-emerald",
        items: [
          { label: "Fast Retailing Scaling Up", desc: "Uniqlo's parent company is expanding past $20B+ by winning market share in the US and Europe." },
          { label: "H&M's Transition Squeeze", desc: "Caught between Shein's low prices and Zara's superior aesthetics, forcing store closures." },
          { label: "Middle Tier Hollows Out", desc: "Consumers bifurcate into ultra-cheap basics or aspirational luxury, squeezing mid-tier department stores." }
        ]
      }
    ],
    notes: "Review the bar chart showing global fashion revenues: Nike, LVMH, Inditex, and Shein represent the four dominant pillars of global fashion retail."
  },
  {
    id: 11,
    category: "SUPPLY CHAIN TIERS",
    title: "The 5-Tier Fashion Supply Chain: Cotton & Polymer to Consumer",
    type: "tier_stack",
    tiers: [
      { tag: "TIER 4", title: "Raw Agricultural & Petrochemical Fiber Production", desc: "Cotton Cultivation (India, US, Brazil) • Synthetic Polymers & Polyester (China, Taiwan) • 65%+ of fibers are petroleum synthetics", cls: "tb-rose" },
      { tag: "TIER 3", title: "Yarn Spinning, Weaving, Knitting & Fabric Finishing", desc: "Textile Mills in China, India, Pakistan, Turkey • Dyeing, Printing, Washing & Chemical Coatings • Water & chemical intensive", cls: "tb-gold" },
      { tag: "TIER 2", title: "Garment Manufacturing (Cut-Make-Trim / CMT)", desc: "Assembly sewing lines in Bangladesh, Vietnam, Cambodia, Indonesia, Mexico, Morocco • Transitioning to automated laser cutting", cls: "tb-cyan" },
      { tag: "TIER 1", title: "Global Freight, Consolidation & Regional Warehousing", desc: "Intermodal Ocean Freight (20-30 days) vs Air Express (2-4 days) • Automated Fulfillment Centers (AutoStore, Pocket Sorters, RFID)", cls: "tb-purple" },
      { tag: "TIER 0", title: "Omnichannel Retail, DTC E-Commerce & Reverse Logistics", desc: "Experiential Flagship Stores, BOPIS, Ship-from-Store • Reverse Logistics Centers inspecting, cleaning, and restocking returns", cls: "tb-emerald" }
    ],
    notes: "Walk through the 5 tiers of apparel manufacturing. Emphasize that Tier 4 is increasingly petrochemical-based, while Tier 0 now bears the immense burden of reverse logistics."
  },
  {
    id: 12,
    category: "OMNICHANNEL DYNAMICS",
    title: "Omnichannel Channel Evolution: The In-Store vs. Digital Convergence",
    type: "chart_and_cards",
    chart: "charts/omnichannel_sales_split.png",
    cards: [
      {
        title: "The 50/50 Channel Equilibrium",
        icon: "📱",
        trim: "trim-gold",
        items: [
          { label: "Store Share Stabilizes at ~50%", desc: "Physical stores rebounded; consumers still demand tactile touch, fit check, and instant gratification." },
          { label: "E-Commerce Stabilizes at ~33%", desc: "Pure digital growth normalized as freight costs and 30% return rates cap profitability." },
          { label: "Social & Live Shopping Surges (17%)", desc: "TikTok Shop and live video commerce represent the fastest-growing sales channel globally." }
        ]
      },
      {
        title: "Strategic Channel Synergy",
        icon: "🔗",
        trim: "trim-cyan",
        items: [
          { label: "The Store Halo Effect", desc: "Opening a new physical flagship increases local online traffic to that brand by +35% within 90 days." },
          { label: "Unified Commerce Profiles", desc: "Single customer loyalty ID merging in-store purchases with mobile app browsing history." },
          { label: "Endless Aisle Deployment", desc: "Store associates ordering out-of-stock sizes online directly from the register for free delivery." }
        ]
      }
    ],
    notes: "Notice how physical in-store shopping has stabilized at 50% of total revenue. Stores are essential showrooms and return drop-off hubs that make e-commerce economically viable."
  },
  {
    id: 13,
    category: "SPEED VS TURNS",
    title: "Speed-to-Market vs. Inventory Turnover: The Velocity Metric",
    type: "chart_and_cards",
    chart: "charts/inventory_turnover_leadtime.png",
    cards: [
      {
        title: "Working Capital Multiplier",
        icon: "⏱️",
        trim: "trim-rose",
        items: [
          { label: "Inventory Velocity Drives Cash", desc: "Shein turns inventory 12.5x; Zara turns stock 8.2x; traditional brands turn stock only 2.8x." },
          { label: "Minimizing Tied-Up Capital", desc: "High inventory turns free up working capital, allowing immediate reinvestment in trend batches." },
          { label: "Lead Time Compounding", desc: "Every extra week of lead time increases forecasting error by ~8-12%, compounding markdown risks." }
        ]
      },
      {
        title: "The Nearshoring Advantage",
        icon: "🚢",
        trim: "trim-emerald",
        items: [
          { label: "Nearshore Flexibility", desc: "Zara accepts +15% higher labor in Portugal because it cuts 30 days of ocean shipping transit." },
          { label: "Postponement Strategy", desc: "Holding undyed fabric in warehouses and dyeing it only when seasonal color trends emerge." },
          { label: "Test & Re-order Discipline", desc: "Committing only 15-20% of inventory upfront keeps 80% open-to-buy budget flexible." }
        ]
      }
    ],
    notes: "Direct attention to the dual-axis chart: Short lead times (pink bars) directly drive high annual inventory turns (green bars), resulting in superior cash generation."
  },
  {
    id: 14,
    category: "UNIT ECONOMICS",
    title: "Unit Economics of a $100 Retail Garment: Cost Breakdown",
    type: "chart_and_cards",
    chart: "charts/retail_cost_breakdown.png",
    cards: [
      {
        title: "Where Does the $100 Go?",
        icon: "💵",
        trim: "trim-gold",
        items: [
          { label: "Raw COGS ($22)", desc: "Fabric, zippers, thread, and garment factory labor represent less than 1/4 of the consumer price." },
          { label: "Store Operations ($24)", desc: "Mall leases in prime locations, utilities, and retail staff wages remain the largest cost." },
          { label: "Marketing & CAC ($14)", desc: "Paid social media ads (Meta, TikTok, Google) consume an expanding slice of revenue." }
        ]
      },
      {
        title: "The Silent Profit Killers",
        icon: "⚠️",
        trim: "trim-rose",
        items: [
          { label: "Reverse Logistics ($11)", desc: "Inspection, cleaning, and repackaging on returned items erode more profit than outbound shipping." },
          { label: "Markdowns & Clearance ($13)", desc: "Promotional sales reduce the average realized garment selling price from $100 to $87." },
          { label: "Net Operating Profit ($10)", desc: "Leaves the typical fashion retailer with an EBIT operating margin of approximately 8-12%." }
        ]
      }
    ],
    notes: "Break down the $100 garment: Notice that markdown losses ($13) and returns ($11) combined cost more than the entire manufacturing and fabric production ($22)!"
  },
  {
    id: 15,
    category: "REVERSE LOGISTICS",
    title: "The Reverse Logistics Nightmare: E-Commerce Returns Management",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "The Return Rate Gap",
        icon: "📦",
        trim: "trim-rose",
        items: [
          { label: "Physical Store Returns (8-10%)", desc: "Customers try items in fitting rooms before purchase, keeping return rates minimal." },
          { label: "E-Commerce Returns (25-35%)", desc: "Online apparel suffers from 'bracketing'—shoppers buy 3 sizes with the intention of returning 2." },
          { label: "Holiday Spike (40%+)", desc: "Post-holiday return waves flood warehouses with winter seasonal items." },
          { label: "The $800B Global Cost", desc: "Handling reverse logistics costs the global retail sector over $800 billion annually in freight." }
        ]
      },
      {
        title: "The Reverse Supply Chain Pipeline",
        icon: "🔄",
        trim: "trim-gold",
        items: [
          { label: "Transportation Freight Squeeze", desc: "Customer return parcel shipping costs $10-$15, wiping out garment margins." },
          { label: "Manual Labor Inspection", desc: "Every returned garment must be hand-inspected for stains, tags, and damage." },
          { label: "Restocking Latency (14-21 Days)", desc: "Takes 3 weeks to get returned stock back onto active sales racks, missing full-price windows." },
          { label: "Landfill Scandal", desc: "Cheap fast fashion was historically trashed because return inspection cost more than the garment." }
        ]
      },
      {
        title: "Retail Mitigation Strategies",
        icon: "🛡️",
        trim: "trim-emerald",
        items: [
          { label: "Return Surcharges", desc: "Zara, H&M, and ASOS now charge $2.50 to $4.00 for mail-in returns, keeping store returns free." },
          { label: "3D Virtual Fitting & AI", desc: "3D computer vision body sizing tools reduce fit-related returns by 18-25%." },
          { label: "Final Sale Policies", desc: "Designating deep clearance items as final sale to prevent perpetual return loops." },
          { label: "In-Store Credit Bonuses", desc: "Offering 110% store credit bonuses if customers choose in-store exchange over cash refund." }
        ]
      }
    ],
    notes: "E-commerce return rates of 25-35% are destroying online apparel margins. Charging nominal fees for mail returns while keeping in-store drop-offs free is saving retailers millions."
  },
  {
    id: 16,
    category: "MARKDOWN SCIENCE",
    title: "Markdown Optimization & Dynamic Pricing: Protecting Gross Margins",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "The Promotional Margin Trap",
        icon: "🏷️",
        trim: "trim-rose",
        items: [
          { label: "The Discount Addiction", desc: "Department stores offering permanent 40% sales train consumers never to buy at full price." },
          { label: "Erosion of Brand Prestige", desc: "Excessive discounting dilutes brand perception, shifting brands from aspirational to commodity." },
          { label: "GMROI Benchmark", desc: "Gross Margin Return on Investment measures gross profit dollars per dollar of inventory (Target: >3.0x)." },
          { label: "Deadstock Liquidation", desc: "Off-price outlets (TJ Maxx, Ross) buy secondary stock at 85% below wholesale." }
        ]
      },
      {
        title: "AI-Powered Dynamic Markdowns",
        icon: "🤖",
        trim: "trim-gold",
        items: [
          { label: "Store-Cluster Elasticity", desc: "A coat selling out in NYC might need a 20% discount in Miami; AI localizes prices." },
          { label: "Optimal Markdown Timing", desc: "Algorithmic models predict the exact date and discount needed to clear stock before season end." },
          { label: "Personalized Dynamic Offers", desc: "Targeting promotions to at-risk app users while keeping full price for loyal brand fans." },
          { label: "Margin Recovery Impact", desc: "Markdown optimization algorithms save retailers 350 to 500 basis points of gross margin." }
        ]
      },
      {
        title: "Full-Price Sell-Through Levers",
        icon: "💎",
        trim: "trim-emerald",
        items: [
          { label: "Limited Production Runs", desc: "Deliberately producing 10% less than projected demand (Zara playbook) avoids markdowns." },
          { label: "Mid-Season Reorder Agility", desc: "Only reordering proven bestsellers rather than committing upfront budget to unproven items." },
          { label: "Outfit Cross-Merchandising", desc: "Styling complete coordinated looks on mannequins increases multi-item basket conversion." },
          { label: "VIP Early Access Drops", desc: "Rewarding loyalty members with exclusive 48-hour access to full-price drops." }
        ]
      }
    ],
    notes: "Markdown optimization is the secret weapon of modern retail profitability. Instead of blanket 40% clearance sales, AI algorithms discount items on a localized store-by-store basis."
  },
  {
    id: 17,
    category: "RETAIL TECH",
    title: "Fashion Retail Tech Stack: Computer Vision, RFID & Automated Logistics",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "Trend Forecasting Algorithms",
        icon: "🔮",
        trim: "trim-purple",
        items: [
          { label: "Social Scraping & Sentiment", desc: "Algorithms ingest billions of images on TikTok and Instagram to detect silhouettes and colors." },
          { label: "Lead Time Compression", desc: "Reduces trend-to-design cycle from 8 weeks to 48 hours for fast fashion design studios." },
          { label: "Generative AI CAD Prototyping", desc: "3D virtual garment modeling (CLO3D) eliminates physical sample shipping and cutting waste." }
        ]
      },
      {
        title: "RFID & Smart In-Store Tech",
        icon: "📡",
        trim: "trim-cyan",
        items: [
          { label: "Item-Level RFID Tracking", desc: "Every garment carries a passive RFID tag scanned at checkout, inventory intake, and racks." },
          { label: "Smart Fitting Room Mirrors", desc: "Touchscreen mirrors detect garment RFID tags, allowing shoppers to request alternate sizes." },
          { label: "Frictionless Self-Checkout", desc: "Shoppers drop baskets into an RFID bucket; all items are rung up simultaneously in 3 seconds." }
        ]
      },
      {
        title: "Automated Robotics & Logistics",
        icon: "🤖",
        trim: "trim-emerald",
        items: [
          { label: "AutoStore & Pocket Sorters", desc: "High-density automated warehouse cubes with autonomous robots fetching inventory totes 24/7." },
          { label: "Automated Hanging Garments", desc: "Suspended ceiling track systems sorting hundreds of thousands of coats directly onto pallets." },
          { label: "Dynamic Delivery Routing", desc: "Last-mile route optimization reducing e-commerce fulfillment costs by 15-20%." }
        ]
      }
    ],
    notes: "Technology is modernizing fashion: item-level RFID tags allow instant 3-second self-checkout and 99.5% inventory visibility, while automated warehouses sort online orders 24/7."
  },
  {
    id: 18,
    category: "COMPETITIVE RADAR",
    title: "Competitive Agility Benchmark: The Retail Capabilities Matrix",
    type: "chart_and_cards",
    chart: "charts/brand_resilience_radar.png",
    cards: [
      {
        title: "Strategic Capabilities Comparison",
        icon: "⚡",
        trim: "trim-rose",
        items: [
          { label: "Zara Leads Balanced Agility", desc: "Scores high in speed-to-market (9/10) and full-price sell-through (8/10) with robust gross margins." },
          { label: "Shein Unmatched in Digital Speed", desc: "Dominates speed (10/10) and digital reach, but scores low in sustainability and return rates." },
          { label: "Nike Strong in Brand Equity", desc: "Massive sponsorship moat and DTC penetration, balancing wholesale channel realignments." }
        ]
      },
      {
        title: "LVMH's Pricing Sanctuary",
        icon: "👑",
        trim: "trim-gold",
        items: [
          { label: "Absolute Margin Hegemony", desc: "LVMH operates in a different universe (>75% gross margin) immune to promotional discounting." },
          { label: "The Luxury Moat", desc: "Artisanal heritage, scarcity, and spatial clienteling create an enduring economic moat." },
          { label: "Key Strategic Takeaway", desc: "To thrive, retailers must either master extreme speed (Zara/Shein) or extreme brand exclusivity (LVMH)." }
        ]
      }
    ],
    notes: "Examine the radar chart: LVMH dominates gross margin power and sell-through, Zara excels in balanced operational agility, and Shein leads in raw digital speed."
  },
  {
    id: 19,
    category: "ESG & CIRCULARITY",
    title: "Sustainability, ESG & Circular Fashion: The Regulatory Reckoning",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "The Overproduction Crisis",
        icon: "🌍",
        trim: "trim-rose",
        items: [
          { label: "100 Billion Garments Annually", desc: "Manufactures 100 billion garments each year for a global population of 8 billion people." },
          { label: "30% Never Sold at Full Price", desc: "20-30% of clothing is liquidated through off-price channels, incinerated, or landfilled." },
          { label: "Textile Waste Mountains", desc: "Atacama Desert (Chile) and Ghana markets overwhelmed by discarded clothing heaps." },
          { label: "Microfiber Ocean Pollution", desc: "Washing polyester garments sheds 500,000 tons of plastic microfibers into oceans annually." }
        ]
      },
      {
        title: "The Regulatory Hammer",
        icon: "⚖️",
        trim: "trim-gold",
        items: [
          { label: "EU Corporate Sustainability Directive", desc: "Mandates due diligence on child labor, living wages, and environmental damage across tiers." },
          { label: "Digital Product Passports (2027)", desc: "Garments must carry scannable QR tags detailing fiber origin, carbon footprint, and recyclability." },
          { label: "Ban on Destroying Unsold Goods", desc: "European legislation outlawing the shredding or incineration of unsold textile inventory." },
          { label: "Extended Producer Responsibility", desc: "Eco-taxes on brands proportional to the volume and recyclability of garments produced." }
        ]
      },
      {
        title: "The Re-Commerce & Circular Frontier",
        icon: "♻️",
        trim: "trim-emerald",
        items: [
          { label: "The Resale Boom ($350B by 2028)", desc: "Secondhand vintage and resale growing 3x faster than overall retail apparel." },
          { label: "Brand-Owned Resale Portals", desc: "Zara Pre-Owned and Lululemon Like New allowing trade-ins of used garments for store credit." },
          { label: "Fiber-to-Fiber Recycling", desc: "Chemical recycling technologies transforming post-consumer poly-cotton into virgin-grade yarn." },
          { label: "Rental Subscriptions", desc: "Rent the Runway and luxury rental services providing access over ownership for occasion-wear." }
        ]
      }
    ],
    notes: "The regulatory hammer is falling on fashion: EU Digital Product Passports by 2027 and bans on destroying unsold goods will force retailers to eliminate overproduction."
  },
  {
    id: 20,
    category: "CONCLUSION",
    title: "Strategic Playbook for Fashion Retail Executives & Conclusion",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "1. Agility & Supply Chain",
        icon: "🏭",
        trim: "trim-gold",
        items: [
          { label: "Nearshore 30-40% of Volume", desc: "Establish rapid-response hubs (Portugal, Morocco, Mexico) to reorder bestsellers in 15 days." },
          { label: "Small-Batch Test & Re-Order", desc: "Limit initial runs to small trial batches; never commit >30% of inventory upfront." },
          { label: "Item-Level RFID Everywhere", desc: "Deploy RFID across every garment to achieve >99% inventory accuracy and enable ship-from-store." },
          { label: "Diversify Logistics", desc: "Balance high-cost air freight with rail and intermodal transport to insulate against fuel spikes." }
        ]
      },
      {
        title: "2. Omnichannel & Margins",
        icon: "💎",
        trim: "trim-rose",
        items: [
          { label: "Curb Free Mail-in Returns", desc: "Charge nominal fees for online mail returns while keeping in-store drop-offs free." },
          { label: "Dynamic Localized Markdowns", desc: "Replace blanket 40% store sales with AI algorithms that discount items based on local store velocity." },
          { label: "Elevate In-Store Experiences", desc: "Treat physical stores as media flagships, community hubs, and micro-fulfillment centers." },
          { label: "Unified Loyalty Profiles", desc: "Merge online browsing data with in-store clienteling tablets to maximize Lifetime Value (LTV)." }
        ]
      },
      {
        title: "3. Circularity & Future",
        icon: "🎯",
        trim: "trim-emerald",
        items: [
          { label: "Prepare for Digital Passports", desc: "Audit fiber traceability and supply tier transparency ahead of EU 2027 DPP mandates." },
          { label: "Capture Secondhand Resale", desc: "Launch brand-owned pre-owned trade-in programs to recapture secondary market profit pools." },
          { label: "The Winning Formula", desc: "Success in 2026 demands mastering the intersection of runway design, algorithmic velocity, and circularity." },
          { label: "Executive Verdict", desc: "Agile speed protects margins from markdowns; strong brand equity protects margins from commoditization." }
        ]
      }
    ],
    notes: "Conclude with the executive formula: Nearshore agility protects margins from markdowns, while strong brand equity and experiential stores protect retailers from price commoditization."
  }
];

// ==========================================================================
// 2. BRAND DATA REPOSITORY (FOR COMPARATOR TOOL)
// ==========================================================================
const brandsData = {
  zara: {
    name: "Inditex / Zara",
    tagline: "Agile Nearshore Pioneer",
    model: "Agile Nearshore Fast Fashion",
    revenue: 38.5,
    leadTime: 15,
    turns: 8.2,
    fullPrice: 68,
    grossMargin: 57.8,
    sourcing: "Spain, Portugal, Morocco, Turkey (50%+ Nearshore)",
    ecomShare: 25,
    highlight: "15-day design-to-rack speed and deliberate store scarcity drive an industry-leading 68% full-price sell-through rate."
  },
  shein: {
    name: "Shein",
    tagline: "Ultra-Fast Algorithmic Disrupter",
    model: "Ultra-Fast Digital On-Demand",
    revenue: 34.0,
    leadTime: 7,
    turns: 12.5,
    fullPrice: 50,
    grossMargin: 44.0,
    sourcing: "Guangzhou, China (5,000+ Contract Workshops)",
    ecomShare: 100,
    highlight: "Uses social trend scraping and 100-unit test batches; turns inventory 12.5x per year with zero physical store overhead."
  },
  nike: {
    name: "Nike Inc.",
    tagline: "Sportswear & Footwear Colossus",
    model: "Performance Athletic Brand",
    revenue: 51.4,
    leadTime: 180,
    turns: 3.8,
    fullPrice: 58,
    grossMargin: 44.6,
    sourcing: "Vietnam (50%), Indonesia (27%), Cambodia",
    ecomShare: 42,
    highlight: "Unmatched cultural brand equity and footwear engineering; balancing direct digital DTC apps with wholesale partner networks."
  },
  lvmh: {
    name: "LVMH Fashion & Leather",
    tagline: "The Pinnacle of Luxury & Scarcity",
    model: "Artisanal Luxury & Haute Couture",
    revenue: 46.2,
    leadTime: 240,
    turns: 2.1,
    fullPrice: 98,
    grossMargin: 72.5,
    sourcing: "France, Italy, Switzerland (Artisanal Workshops)",
    ecomShare: 12,
    highlight: "Commands astronomical gross margins (>72%) with a strict zero-markdown policy and in-store high-touch VIP clienteling."
  },
  uniqlo: {
    name: "Fast Retailing (Uniqlo)",
    tagline: "Material Science & Functional Basics",
    model: "LifeWear Functional Apparel",
    revenue: 20.8,
    leadTime: 90,
    turns: 5.5,
    fullPrice: 74,
    grossMargin: 52.4,
    sourcing: "China, Vietnam, Bangladesh (Partner Mills)",
    ecomShare: 18,
    highlight: "Anti-trend basics with proprietary fabrics (HEATTECH, AIRism) that never expire, avoiding seasonal fashion write-downs."
  },
  hm: {
    name: "H&M Group",
    tagline: "Mass Fast Fashion Pioneer",
    model: "Traditional Fast Fashion",
    revenue: 22.3,
    leadTime: 60,
    turns: 4.2,
    fullPrice: 48,
    grossMargin: 51.2,
    sourcing: "Bangladesh, India, China, Cambodia",
    ecomShare: 30,
    highlight: "Transitioning retail fleet toward higher-end concepts (COS, Arket) to escape price pressure from ultra-fast competitors."
  }
};

// ==========================================================================
// 3. APP STATE & ELEMENT REFERENCES
// ==========================================================================
let currentSlideIndex = 0;
const totalSlides = slidesData.length;

let autoplayTimer = null;
let isAutoplayActive = false;
const AUTOPLAY_DURATION = 6500;

let isLaserActive = false;

// DOM Elements
const currentSlideNumEl = document.getElementById("currentSlideNum");
const totalSlidesNumEl = document.getElementById("totalSlidesNum");
const slideCategoryBadgeEl = document.getElementById("slideCategoryBadge");
const progressBarEl = document.getElementById("presentationProgressBar");
const autoplayTimerBarEl = document.getElementById("autoplayTimerBar");
const slideStageEl = document.getElementById("slideStage");
const slideViewportWrapperEl = document.getElementById("slideViewportWrapper");
const speakerNotesTextEl = document.getElementById("speakerNotesText");
const speakerNotesPanelEl = document.getElementById("speakerNotesPanel");
const laserPointerEl = document.getElementById("laserPointer");

// Modals
const slideDrawerOverlayEl = document.getElementById("slideDrawerOverlay");
const drawerGridEl = document.getElementById("drawerGrid");
const slideSearchInputEl = document.getElementById("slideSearchInput");

const shortcutsModalOverlayEl = document.getElementById("shortcutsModalOverlay");
const comparatorModalOverlayEl = document.getElementById("comparatorModalOverlay");
const simulatorModalOverlayEl = document.getElementById("simulatorModalOverlay");

// View Tabs
const navTabs = document.querySelectorAll(".nav-tab");
const viewSections = {
  presentation: document.getElementById("viewPresentation"),
  report: document.getElementById("viewReport"),
  charts: document.getElementById("viewCharts")
};

// ==========================================================================
// 4. SLIDE RENDERING ENGINE
// ==========================================================================
function renderSlide(index) {
  if (index < 0 || index >= totalSlides) return;
  currentSlideIndex = index;
  const slide = slidesData[index];

  currentSlideNumEl.textContent = String(slide.id).padStart(2, '0');
  totalSlidesNumEl.textContent = String(totalSlides).padStart(2, '0');
  slideCategoryBadgeEl.textContent = slide.category;
  progressBarEl.style.width = `${((index + 1) / totalSlides) * 100}%`;

  if (isAutoplayActive) {
    resetAutoplayTimer();
  }

  speakerNotesTextEl.innerHTML = `<strong>Slide ${slide.id}: ${slide.title}</strong><br><br>${slide.notes}`;

  let contentHtml = "";

  if (slide.type === "hero_fashion") {
    contentHtml = `
      <div class="slide-content-root">
        <div class="slide-body grid-chart-and-cards" style="align-items: center;">
          <div class="slide-hero">
            <div class="hero-tag">✨ ${slide.category}</div>
            <h1 class="hero-title">${slide.title}</h1>
            <p class="hero-subtitle">${slide.subtitle}</p>
            <div class="hero-meta">Executive Retail Strategy & Academic Report 2026 | Atelier Retail Analytics</div>
            <div class="metrics-row" style="grid-template-columns: repeat(2, 1fr);">
              <div class="metric-card">
                <div class="metric-val">$1.73T</div>
                <div class="metric-lbl">Global Market Value</div>
                <div class="metric-sub">Apparel & Footwear Retail</div>
              </div>
              <div class="metric-card">
                <div class="metric-val val-rose">68% Full-Price</div>
                <div class="metric-lbl">Zara Sell-Through</div>
                <div class="metric-sub">Vs 45% Industry Average</div>
              </div>
            </div>
          </div>
          <div class="slide-chart-container" style="max-height: 440px;">
            <img src="${slide.img}" alt="Fashion Runway" class="slide-chart-img" style="border-radius: var(--radius-md);">
          </div>
        </div>
      </div>
    `;
  } else if (slide.type === "photo_and_cards") {
    let cardsHtml = `<div style="display: flex; flex-direction: column; gap: 1rem; height: 100%; justify-content: center;">`;
    slide.cards.forEach(c => {
      cardsHtml += `
        <div class="slide-card" style="flex: 1;">
          <div class="slide-card-trim ${c.trim}"></div>
          <div class="card-title"><span>${c.icon}</span> ${c.title}</div>
          <ul class="card-list">
            ${c.items.map(it => `<li><strong>${it.label}:</strong> ${it.desc}</li>`).join('')}
          </ul>
        </div>
      `;
    });
    cardsHtml += `</div>`;

    contentHtml = `
      <div class="slide-content-root">
        <div class="slide-header">
          <div class="slide-tag">${slide.category}</div>
          <div class="slide-title">${slide.title}</div>
        </div>
        <div class="slide-body grid-chart-and-cards">
          <div class="slide-chart-container">
            <img src="${slide.img}" alt="${slide.title}" class="slide-chart-img">
          </div>
          ${cardsHtml}
        </div>
      </div>
    `;
  } else if (slide.type === "metrics_and_cards") {
    let metricsHtml = `<div class="metrics-row">`;
    slide.metrics.forEach(m => {
      metricsHtml += `
        <div class="metric-card">
          <div class="metric-val ${m.color}">${m.val}</div>
          <div class="metric-lbl">${m.label}</div>
          <div class="metric-sub">${m.sub}</div>
        </div>
      `;
    });
    metricsHtml += `</div>`;

    let cardsHtml = `<div class="grid-3-col">`;
    slide.cards.forEach(c => {
      cardsHtml += `
        <div class="slide-card">
          <div class="slide-card-trim ${c.trim}"></div>
          <div class="card-title"><span>${c.icon}</span> ${c.title}</div>
          <ul class="card-list">
            ${c.items.map(it => `<li><strong>${it.label}:</strong> ${it.desc}</li>`).join('')}
          </ul>
        </div>
      `;
    });
    cardsHtml += `</div>`;

    contentHtml = `
      <div class="slide-content-root">
        <div class="slide-header">
          <div class="slide-tag">${slide.category}</div>
          <div class="slide-title">${slide.title}</div>
        </div>
        <div class="slide-body" style="flex-direction: column;">
          ${metricsHtml}
          ${cardsHtml}
        </div>
      </div>
    `;
  } else if (slide.type === "cards_grid") {
    let cardsHtml = `<div class="${slide.layout || 'grid-3-col'}">`;
    slide.cards.forEach(c => {
      cardsHtml += `
        <div class="slide-card">
          <div class="slide-card-trim ${c.trim}"></div>
          <div class="card-title"><span>${c.icon}</span> ${c.title.replace('\n', '<br>')}</div>
          <ul class="card-list">
            ${c.items.map(it => `<li><strong>${it.label}:</strong> ${it.desc}</li>`).join('')}
          </ul>
        </div>
      `;
    });
    cardsHtml += `</div>`;

    contentHtml = `
      <div class="slide-content-root">
        <div class="slide-header">
          <div class="slide-tag">${slide.category}</div>
          <div class="slide-title">${slide.title}</div>
        </div>
        <div class="slide-body">
          ${cardsHtml}
        </div>
      </div>
    `;
  } else if (slide.type === "chart_and_cards") {
    let cardsHtml = `<div style="display: flex; flex-direction: column; gap: 1rem; height: 100%; justify-content: center;">`;
    slide.cards.forEach(c => {
      cardsHtml += `
        <div class="slide-card" style="flex: 1;">
          <div class="slide-card-trim ${c.trim}"></div>
          <div class="card-title"><span>${c.icon}</span> ${c.title}</div>
          <ul class="card-list">
            ${c.items.map(it => `<li><strong>${it.label}:</strong> ${it.desc}</li>`).join('')}
          </ul>
        </div>
      `;
    });
    cardsHtml += `</div>`;

    contentHtml = `
      <div class="slide-content-root">
        <div class="slide-header">
          <div class="slide-tag">${slide.category}</div>
          <div class="slide-title">${slide.title}</div>
        </div>
        <div class="slide-body grid-chart-and-cards">
          <div class="slide-chart-container">
            <img src="${slide.chart}" alt="${slide.title}" class="slide-chart-img">
          </div>
          ${cardsHtml}
        </div>
      </div>
    `;
  } else if (slide.type === "tier_stack") {
    let stackHtml = `<div class="tier-stack">`;
    slide.tiers.forEach(t => {
      stackHtml += `
        <div class="tier-bar ${t.cls}">
          <div class="tier-bar-title">
            <span class="slide-tag" style="margin-bottom:0;">${t.tag}</span>
            <span>${t.title}</span>
          </div>
          <div class="tier-bar-desc">${t.desc}</div>
        </div>
      `;
    });
    stackHtml += `</div>`;

    contentHtml = `
      <div class="slide-content-root">
        <div class="slide-header">
          <div class="slide-tag">${slide.category}</div>
          <div class="slide-title">${slide.title}</div>
        </div>
        <div class="slide-body">
          ${stackHtml}
        </div>
      </div>
    `;
  }

  slideStageEl.innerHTML = contentHtml;
  updateDrawerCurrent();
}

function nextSlide() {
  if (currentSlideIndex < totalSlides - 1) {
    renderSlide(currentSlideIndex + 1);
  } else if (isAutoplayActive) {
    renderSlide(0);
  }
}

function prevSlide() {
  if (currentSlideIndex > 0) {
    renderSlide(currentSlideIndex - 1);
  }
}

// ==========================================================================
// 5. AUTOPLAY & LASER POINTER
// ==========================================================================
function toggleAutoplay() {
  isAutoplayActive = !isAutoplayActive;
  const btn = document.getElementById("btnToggleAutoplay");
  const icon = document.getElementById("autoplayIcon");
  const label = document.getElementById("autoplayLabel");

  if (isAutoplayActive) {
    btn.classList.add("active");
    icon.textContent = "⏸";
    label.textContent = "Pause";
    startAutoplayTimer();
  } else {
    btn.classList.remove("active");
    icon.textContent = "▶";
    label.textContent = "Auto";
    stopAutoplayTimer();
  }
}

function startAutoplayTimer() {
  stopAutoplayTimer();
  resetAutoplayTimer();
  autoplayTimer = setInterval(() => {
    nextSlide();
  }, AUTOPLAY_DURATION);
}

function resetAutoplayTimer() {
  autoplayTimerBarEl.style.transition = 'none';
  autoplayTimerBarEl.style.width = '0%';
  setTimeout(() => {
    autoplayTimerBarEl.style.transition = `width ${AUTOPLAY_DURATION}ms linear`;
    autoplayTimerBarEl.style.width = '100%';
  }, 30);
}

function stopAutoplayTimer() {
  if (autoplayTimer) clearInterval(autoplayTimer);
  autoplayTimer = null;
  autoplayTimerBarEl.style.transition = 'none';
  autoplayTimerBarEl.style.width = '0%';
}

function toggleLaserPointer() {
  isLaserActive = !isLaserActive;
  const btn = document.getElementById("btnToggleLaser");
  if (isLaserActive) {
    btn.classList.add("active");
    laserPointerEl.classList.add("active");
    slideViewportWrapperEl.style.cursor = "none";
  } else {
    btn.classList.remove("active");
    laserPointerEl.classList.remove("active");
    slideViewportWrapperEl.style.cursor = "default";
  }
}

slideViewportWrapperEl.addEventListener("mousemove", (e) => {
  if (!isLaserActive) return;
  const rect = slideViewportWrapperEl.getBoundingClientRect();
  laserPointerEl.style.left = `${e.clientX - rect.left}px`;
  laserPointerEl.style.top = `${e.clientY - rect.top}px`;
});

// ==========================================================================
// 6. AMBIENT GOLD SPARKLE CANVAS
// ==========================================================================
function initAmbientSparkles() {
  const canvas = document.getElementById("ambientCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  let width = (canvas.width = slideViewportWrapperEl.clientWidth);
  let height = (canvas.height = slideViewportWrapperEl.clientHeight);

  window.addEventListener("resize", () => {
    width = canvas.width = slideViewportWrapperEl.clientWidth;
    height = canvas.height = slideViewportWrapperEl.clientHeight;
  });

  const sparkles = [];
  const sparkleCount = 45;

  for (let i = 0; i < sparkleCount; i++) {
    sparkles.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.35,
      vy: (Math.random() - 0.5) * 0.35,
      size: Math.random() * 2.2 + 0.8,
      alpha: Math.random() * 0.6 + 0.2,
      color: Math.random() > 0.4 ? "245, 158, 11" : "251, 113, 133"
    });
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);

    for (let i = 0; i < sparkles.length; i++) {
      const s = sparkles[i];
      s.x += s.vx;
      s.y += s.vy;

      if (s.x < 0) s.x = width;
      if (s.x > width) s.x = 0;
      if (s.y < 0) s.y = height;
      if (s.y > height) s.y = 0;

      ctx.beginPath();
      ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(${s.color}, ${s.alpha})`;
      ctx.shadowBlur = 8;
      ctx.shadowColor = `rgba(${s.color}, 0.5)`;
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  draw();
}

// ==========================================================================
// 7. BRAND COMPARATOR TOOL
// ==========================================================================
function renderComparison() {
  const brandAKey = document.getElementById("selectCompA").value;
  const brandBKey = document.getElementById("selectCompB").value;

  const a = brandsData[brandAKey];
  const b = brandsData[brandBKey];
  const container = document.getElementById("comparisonResults");

  function buildColumn(data, otherData) {
    const isHigherRev = data.revenue > otherData.revenue;
    const isFasterLead = data.leadTime < otherData.leadTime;
    const isHigherTurns = data.turns > otherData.turns;
    const isHigherSell = data.fullPrice > otherData.fullPrice;

    return `
      <div class="comp-column">
        <div class="comp-col-header">
          <div class="comp-chip-badge">${data.tagline}</div>
          <h4>${data.name}</h4>
          <p style="font-size: 0.8rem; color: var(--text-muted);">${data.model}</p>
        </div>

        <div class="comp-stat-row">
          <div class="comp-stat-header">
            <span>Annual Revenue (USD):</span>
            <span class="comp-stat-val" style="color: ${isHigherRev ? 'var(--accent-gold)' : 'var(--text-white)'}">$${data.revenue} Billion</span>
          </div>
          <div class="comp-bar-bg">
            <div class="comp-bar-fill" style="width: ${(data.revenue / 55) * 100}%; background: ${isHigherRev ? 'var(--accent-gold)' : 'var(--accent-cyan)'}"></div>
          </div>
        </div>

        <div class="comp-stat-row">
          <div class="comp-stat-header">
            <span>Design-to-Rack Lead Time:</span>
            <span class="comp-stat-val" style="color: ${isFasterLead ? 'var(--accent-emerald)' : 'var(--text-white)'}">${data.leadTime} Days</span>
          </div>
          <div class="comp-bar-bg">
            <div class="comp-bar-fill" style="width: ${Math.min(100, (data.leadTime / 180) * 100)}%; background: ${isFasterLead ? 'var(--accent-emerald)' : 'var(--accent-rose)'}"></div>
          </div>
        </div>

        <div class="comp-stat-row">
          <div class="comp-stat-header">
            <span>Annual Inventory Turns:</span>
            <span class="comp-stat-val" style="color: ${isHigherTurns ? 'var(--accent-emerald)' : 'var(--text-white)'}">${data.turns}x / year</span>
          </div>
          <div class="comp-bar-bg">
            <div class="comp-bar-fill" style="width: ${(data.turns / 13) * 100}%; background: var(--accent-purple)"></div>
          </div>
        </div>

        <div class="comp-stat-row">
          <div class="comp-stat-header">
            <span>Full-Price Sell-Through:</span>
            <span class="comp-stat-val" style="color: ${isHigherSell ? 'var(--accent-gold)' : 'var(--text-white)'}">${data.fullPrice}%</span>
          </div>
          <div class="comp-bar-bg">
            <div class="comp-bar-fill" style="width: ${data.fullPrice}%; background: var(--accent-gold)"></div>
          </div>
        </div>

        <div style="font-size: 0.82rem; background: var(--bg-surface); padding: 0.8rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 0.4rem;">
          <div><strong>Gross Margin:</strong> ${data.grossMargin}%</div>
          <div><strong>Primary Sourcing Hubs:</strong> ${data.sourcing}</div>
          <div><strong>E-Commerce Penetration:</strong> ${data.ecomShare}%</div>
        </div>

        <div style="font-size: 0.8rem; color: var(--accent-gold); line-height: 1.4; border-top: 1px solid var(--border-subtle); padding-top: 0.6rem;">
          <strong>Strategic Takeaway:</strong> ${data.highlight}
        </div>
      </div>
    `;
  }

  container.innerHTML = buildColumn(a, b) + buildColumn(b, a);
}

// ==========================================================================
// 8. FASHION MARKDOWN & MARGIN SIMULATOR
// ==========================================================================
const garmentPresets = {
  luxury_coat: { msrp: 950, cogs: 180, sellThrough: 95, discount: 0.20, returns: 12 },
  tailored_blazer: { msrp: 120, cogs: 26, sellThrough: 68, discount: 0.40, returns: 25 },
  athleisure_hoodie: { msrp: 95, cogs: 22, sellThrough: 58, discount: 0.30, returns: 22 },
  fast_dress: { msrp: 22, cogs: 5.5, sellThrough: 50, discount: 0.50, returns: 32 }
};

function calculateMarkdownBOM() {
  const msrp = parseFloat(document.getElementById("simMSRP").value);
  const cogs = parseFloat(document.getElementById("simCOGS").value);
  const sellThrough = parseFloat(document.getElementById("simFullPriceSellThrough").value) / 100;
  const discountRate = parseFloat(document.getElementById("simMarkdownDiscount").value);
  const returnRate = parseFloat(document.getElementById("simReturnRate").value) / 100;

  // Realized Selling Price (Blended between full price & discounted items)
  const fullPriceUnitsShare = sellThrough;
  const discountedUnitsShare = 1 - sellThrough;
  const discountedPrice = msrp * (1 - discountRate);

  const realizedPrice = (msrp * fullPriceUnitsShare) + (discountedPrice * discountedUnitsShare);

  // Operational Cost Allocations (per unit realized)
  const storeAndLease = realizedPrice * 0.24;
  const marketingAndCAC = realizedPrice * 0.14;
  const returnCost = (realizedPrice * returnRate * 0.35); // Logistics, sanitizing & re-packaging
  const markdownLoss = msrp - realizedPrice;

  const totalOperatingCosts = cogs + storeAndLease + marketingAndCAC + returnCost;
  const netOperatingProfit = realizedPrice - totalOperatingCosts;
  const netMarginPct = ((netOperatingProfit / realizedPrice) * 100).toFixed(1);
  const grossMarginDollar = realizedPrice - cogs;
  const grossMarginPct = ((grossMarginDollar / realizedPrice) * 100).toFixed(1);

  // Update UI Elements
  document.getElementById("simMSRPVal").textContent = `$${msrp.toLocaleString()}`;
  document.getElementById("simCOGSVal").textContent = `$${cogs.toLocaleString()}`;
  document.getElementById("simFullPriceVal").textContent = `${(sellThrough * 100).toFixed(0)}%`;
  document.getElementById("simReturnVal").textContent = `${(returnRate * 100).toFixed(0)}%`;

  document.getElementById("simRealizedPrice").textContent = `$${realizedPrice.toFixed(2)}`;
  document.getElementById("simGrossMarginPct").textContent = `${grossMarginPct}%`;
  document.getElementById("simGrossMarginDollar").textContent = `$${grossMarginDollar.toFixed(2)} / unit`;

  const netEl = document.getElementById("simNetMarginDollar");
  const healthEl = document.getElementById("simMarginHealth");

  netEl.textContent = `$${netOperatingProfit.toFixed(2)} (${netMarginPct}%)`;

  if (parseFloat(netMarginPct) >= 15) {
    netEl.className = "out-value accent-emerald";
    healthEl.textContent = "Health: Strong Profitability (Zara/Luxury Model)";
  } else if (parseFloat(netMarginPct) >= 8) {
    netEl.className = "out-value accent-cyan";
    healthEl.textContent = "Health: Healthy Commercial Margin (Standard Retail)";
  } else if (parseFloat(netMarginPct) > 0) {
    netEl.className = "out-value accent-gold";
    healthEl.textContent = "Health: Thin Margins (Heavy Markdown / High Returns)";
  } else {
    netEl.className = "out-value accent-rose";
    healthEl.textContent = "Health: Operating Loss (Clearance Trap)";
  }

  // Update Stacked Bar
  const totalBase = realizedPrice;
  document.getElementById("segCOGS").style.width = `${Math.max(5, (cogs / totalBase) * 100)}%`;
  document.getElementById("segStore").style.width = `${Math.max(5, (storeAndLease / totalBase) * 100)}%`;
  document.getElementById("segMarketing").style.width = `${Math.max(5, (marketingAndCAC / totalBase) * 100)}%`;
  document.getElementById("segReturns").style.width = `${Math.max(5, (returnCost / totalBase) * 100)}%`;
  document.getElementById("segMarkdown").style.width = `${Math.max(5, (markdownLoss / totalBase) * 100)}%`;
  document.getElementById("segProfit").style.width = `${Math.max(0, (Math.max(0, netOperatingProfit) / totalBase) * 100)}%`;

  // Dynamic Insight Text
  const insightBox = document.getElementById("simInsightBox");
  if (sellThrough >= 0.85) {
    insightBox.innerHTML = `<strong>Executive Reviewer Takeaway:</strong> With an exceptional <strong>${(sellThrough * 100).toFixed(0)}% full-price sell-through</strong>, this garment achieves luxury-tier profitability ($${netOperatingProfit.toFixed(2)} EBIT / unit). Zero inventory write-downs protect gross margins from markdown destruction.`;
  } else if (returnRate >= 0.30) {
    insightBox.innerHTML = `<strong>Executive Reviewer Takeaway:</strong> High return rate (<strong>${(returnRate * 100).toFixed(0)}%</strong>) is the primary margin killer, costing <strong>$${returnCost.toFixed(2)} per unit</strong> in reverse logistics. Introducing a nominal mail-return fee or AI sizing tool will directly restore profitability.`;
  } else {
    insightBox.innerHTML = `<strong>Executive Reviewer Takeaway:</strong> At a <strong>${(sellThrough * 100).toFixed(0)}% full-price sell-through</strong>, markdown discounts erode <strong>$${markdownLoss.toFixed(2)}</strong> from initial MSRP. Nearshoring smaller initial production batches (100-300 units) will lift full-price sell-through to Zara levels (>68%), expanding net margins by +400 bps.`;
  }
}

function applyGarmentPreset(key) {
  const p = garmentPresets[key];
  if (!p) return;

  document.getElementById("simMSRP").value = p.msrp;
  document.getElementById("simCOGS").value = p.cogs;
  document.getElementById("simFullPriceSellThrough").value = p.sellThrough;
  document.getElementById("simMarkdownDiscount").value = p.discount;
  document.getElementById("simReturnRate").value = p.returns;

  document.querySelectorAll(".btn-preset").forEach(btn => {
    if (btn.getAttribute("data-preset") === key) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });

  calculateMarkdownBOM();
}

// ==========================================================================
// 9. SLIDE DRAWER & MODALS
// ==========================================================================
function buildSlideDrawer(filterQuery = "") {
  drawerGridEl.innerHTML = "";
  const query = filterQuery.toLowerCase().trim();

  slidesData.forEach((s, idx) => {
    if (query && !s.title.toLowerCase().includes(query) && !s.category.toLowerCase().includes(query)) {
      return;
    }

    const thumb = document.createElement("div");
    thumb.className = `drawer-thumb ${idx === currentSlideIndex ? 'current' : ''}`;
    thumb.innerHTML = `
      <div class="thumb-num">SLIDE ${String(s.id).padStart(2, '0')} • ${s.category}</div>
      <div class="thumb-title">${s.title}</div>
    `;
    thumb.addEventListener("click", () => {
      renderSlide(idx);
      closeSlideDrawer();
    });
    drawerGridEl.appendChild(thumb);
  });
}

function updateDrawerCurrent() {
  const thumbs = drawerGridEl.querySelectorAll(".drawer-thumb");
  thumbs.forEach((th, i) => {
    if (i === currentSlideIndex) {
      th.classList.add("current");
    } else {
      th.classList.remove("current");
    }
  });
}

function openSlideDrawer() {
  buildSlideDrawer(slideSearchInputEl.value);
  slideDrawerOverlayEl.classList.add("active");
  setTimeout(() => slideSearchInputEl.focus(), 50);
}

function closeSlideDrawer() {
  slideDrawerOverlayEl.classList.remove("active");
}

slideSearchInputEl.addEventListener("input", (e) => {
  buildSlideDrawer(e.target.value);
});

function toggleSpeakerNotes() {
  speakerNotesPanelEl.classList.toggle("open");
}

function openModal(modalEl) { modalEl.classList.add("active"); }
function closeModal(modalEl) { modalEl.classList.remove("active"); }
function closeAllModals() {
  closeSlideDrawer();
  closeModal(shortcutsModalOverlayEl);
  closeModal(comparatorModalOverlayEl);
  closeModal(simulatorModalOverlayEl);
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(err => {
      console.warn(`Fullscreen error: ${err.message}`);
    });
  } else {
    document.exitFullscreen();
  }
}

// ==========================================================================
// 10. EVENT LISTENERS
// ==========================================================================
document.getElementById("btnNextSlide").addEventListener("click", nextSlide);
document.getElementById("btnPrevSlide").addEventListener("click", prevSlide);
document.getElementById("arrowNext").addEventListener("click", nextSlide);
document.getElementById("arrowPrev").addEventListener("click", prevSlide);

document.getElementById("btnToggleAutoplay").addEventListener("click", toggleAutoplay);
document.getElementById("btnToggleLaser").addEventListener("click", toggleLaserPointer);
document.getElementById("btnSlideDrawer").addEventListener("click", openSlideDrawer);
document.getElementById("btnCloseDrawer").addEventListener("click", closeSlideDrawer);
document.getElementById("btnToggleNotes").addEventListener("click", toggleSpeakerNotes);
document.getElementById("btnCloseNotes").addEventListener("click", toggleSpeakerNotes);
document.getElementById("btnToggleFullscreen").addEventListener("click", toggleFullscreen);

document.getElementById("btnOpenShortcuts").addEventListener("click", () => openModal(shortcutsModalOverlayEl));
document.getElementById("btnCloseShortcuts").addEventListener("click", () => closeModal(shortcutsModalOverlayEl));

document.getElementById("btnOpenComparator").addEventListener("click", () => {
  renderComparison();
  openModal(comparatorModalOverlayEl);
});
document.getElementById("btnCloseComparator").addEventListener("click", () => closeModal(comparatorModalOverlayEl));

document.getElementById("btnOpenSimulator").addEventListener("click", () => {
  calculateMarkdownBOM();
  openModal(simulatorModalOverlayEl);
});
document.getElementById("btnCloseSimulator").addEventListener("click", () => closeModal(simulatorModalOverlayEl));

document.getElementById("selectCompA").addEventListener("change", renderComparison);
document.getElementById("selectCompB").addEventListener("change", renderComparison);

["simMSRP", "simCOGS", "simFullPriceSellThrough", "simMarkdownDiscount", "simReturnRate"].forEach(id => {
  document.getElementById(id).addEventListener("input", calculateMarkdownBOM);
  document.getElementById(id).addEventListener("change", calculateMarkdownBOM);
});

document.querySelectorAll(".btn-preset").forEach(btn => {
  btn.addEventListener("click", () => {
    applyGarmentPreset(btn.getAttribute("data-preset"));
  });
});

[slideDrawerOverlayEl, shortcutsModalOverlayEl, comparatorModalOverlayEl, simulatorModalOverlayEl].forEach(overlay => {
  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) closeAllModals();
  });
});

// Keyboard Navigation
document.addEventListener("keydown", (e) => {
  if (["input", "textarea", "select"].includes(document.activeElement.tagName.toLowerCase())) {
    if (e.key === "Escape") closeAllModals();
    return;
  }

  const key = e.key.toLowerCase();

  if (e.key === "ArrowRight" || e.key === " " || e.key === "PageDown") {
    e.preventDefault();
    nextSlide();
  } else if (e.key === "ArrowLeft" || e.key === "PageUp") {
    e.preventDefault();
    prevSlide();
  } else if (e.key === "Home") {
    e.preventDefault();
    renderSlide(0);
  } else if (e.key === "End") {
    e.preventDefault();
    renderSlide(totalSlides - 1);
  } else if (key === "p") {
    e.preventDefault();
    toggleAutoplay();
  } else if (key === "l") {
    e.preventDefault();
    toggleLaserPointer();
  } else if (key === "c") {
    e.preventDefault();
    renderComparison();
    openModal(comparatorModalOverlayEl);
  } else if (key === "b") {
    e.preventDefault();
    calculateMarkdownBOM();
    openModal(simulatorModalOverlayEl);
  } else if (key === "g") {
    e.preventDefault();
    openSlideDrawer();
  } else if (key === "n") {
    e.preventDefault();
    toggleSpeakerNotes();
  } else if (key === "f") {
    e.preventDefault();
    toggleFullscreen();
  } else if (e.key === "?") {
    e.preventDefault();
    openModal(shortcutsModalOverlayEl);
  } else if (e.key === "Escape") {
    closeAllModals();
    if (isLaserActive) toggleLaserPointer();
  }
});

// View Tabs
navTabs.forEach(tab => {
  tab.addEventListener("click", () => {
    const targetView = tab.getAttribute("data-view");
    navTabs.forEach(t => t.classList.remove("active"));
    tab.classList.add("active");

    Object.keys(viewSections).forEach(vKey => {
      if (vKey === targetView) {
        viewSections[vKey].classList.add("active");
      } else {
        viewSections[vKey].classList.remove("active");
      }
    });

    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
});

// Init on DOM Ready
document.addEventListener("DOMContentLoaded", () => {
  renderSlide(0);
  buildSlideDrawer();
  initAmbientSparkles();
  renderComparison();
  calculateMarkdownBOM();
  console.log("Atelier Retail Presentation Engine Initialized (20 Slides Active).");
});
