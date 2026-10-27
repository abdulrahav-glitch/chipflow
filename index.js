/**
 * SILICON CHAIN: Mobile Processor Supply Chain Analysis
 * Enhanced Interactive Presentation Engine & Simulation Suite
 * Features:
 * - 20-Slide Presentation Engine with Card Stagger Animations
 * - Ambient Silicon Circuit Particle Background (HTML5 Canvas)
 * - Interactive Presenter Laser Pointer Mode (Hotkey 'L')
 * - Autoplay Slides with Progress Timer (Hotkey 'P')
 * - Head-to-Head Chipmaker Comparator (Hotkey 'C')
 * - Interactive Smartphone BOM & Hardware Margin Simulator (Hotkey 'B')
 * - Keyboard Shortcuts HUD (Hotkey '?')
 * - Slide Drawer with Real-Time Search & Filtering (Hotkey 'G')
 * - Collapsible Speaker Notes (Hotkey 'N')
 */

// ==========================================================================
// 1. SLIDE DATA REPOSITORY (20 COMPREHENSIVE SLIDES)
// ==========================================================================
const slidesData = [
  {
    id: 1,
    category: "EXECUTIVE TITLE",
    title: "Global Mobile Phone Processors",
    subtitle: "End-to-End Comparative Analysis: Apple, Qualcomm, MediaTek, Samsung & HiSilicon Across Wafer Fabs, Advanced Packaging & Geopolitics",
    type: "hero",
    notes: "Welcome everyone. Today we are presenting a comprehensive supply chain analysis of mobile phone processors. We examine the complete multi-tier ecosystem, from raw silicon ingots and ASML lithography to wafer fabrication at TSMC, advanced InFO packaging, and device integration across global tech giants."
  },
  {
    id: 2,
    category: "EXECUTIVE SUMMARY",
    title: "Executive Summary: The Geopolitics & Economics of Mobile Silicon",
    type: "metrics_and_cards",
    metrics: [
      { val: "$180+", label: "Flagship SoC Cost", sub: "+157% vs 2019 baseline", color: "val-rose" },
      { val: "3nm / 2nm", label: "Cutting-Edge Nodes", sub: "TSMC N3B, N3E & N2 GAA", color: "" },
      { val: "72%+", label: "Revenue Duopoly", sub: "Apple & Qualcomm Value Capture", color: "val-green" },
      { val: "50+ TOPS", label: "On-Device NPU Era", sub: "Hardware AI Accelerators", color: "val-purple" }
    ],
    cards: [
      {
        title: "Extreme Foundry Concentration",
        icon: "🏭",
        trim: "trim-blue",
        items: [
          { label: "The TSMC Chokepoint", desc: "Over 87% of sub-5nm advanced mobile wafer fabrication occurs exclusively in Taiwan." },
          { label: "Bespoke Access", desc: "Apple leverages cash reserves to buy 100% of initial cutting-edge capacity (e.g. TSMC N3B)." },
          { label: "Geopolitical Vulnerability", desc: "Cross-strait tensions make mobile hardware the world's most vulnerable supply chain." }
        ]
      },
      {
        title: "Soaring Wafer & R&D Costs",
        icon: "📈",
        trim: "trim-orange",
        items: [
          { label: "Moore's Law Inflation", desc: "Advanced 3nm wafers exceed $20,000 each; next-gen 2nm GAA wafers approach $28,000-$30,000." },
          { label: "Tape-Out Escalation", desc: "Mask sets and physical chip verification for a 3nm flagship processor cost upwards of $300M-$500M." },
          { label: "BOM Squeeze", desc: "SoC now represents 25-30% of total smartphone hardware BOM, forcing OEMs to raise prices." }
        ]
      },
      {
        title: "Strategic Architectural Divergence",
        icon: "⚙️",
        trim: "trim-green",
        items: [
          { label: "Captive vs Merchant", desc: "Apple & Google design silicon solely for their own hardware; Qualcomm & MediaTek sell to external OEMs." },
          { label: "ISA Friction", desc: "Arm's revised licensing fees and lawsuits have triggered Qualcomm's custom Oryon cores and RISC-V exploration." },
          { label: "Packaging is the New Node", desc: "Monolithic scaling limits are making 3D stacking and InFO advanced packaging the true battleground." }
        ]
      }
    ],
    notes: "Highlight the four massive macro trends: soaring wafer prices ($20K+ per wafer), extreme concentration in Taiwan (>87% of sub-5nm), the rise of hardware on-device generative AI NPUs, and the shift from pure fabless to captive silicon."
  },
  {
    id: 3,
    category: "CHIP ARCHITECTURE",
    title: "Anatomy of a Mobile SoC: The Monolithic Silicon Engine",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "Central Processing Unit (CPU)",
        icon: "🧠",
        trim: "trim-blue",
        items: [
          { label: "Heterogeneous Clustering", desc: "Big.LITTLE architectures combining high-performance cores with high-efficiency cores." },
          { label: "Core Architectures", desc: "Custom microarchitectures (Apple Firestorm, Qualcomm Oryon) vs stock ARM Cortex-X4/A720." },
          { label: "Thermal Throttling", desc: "Severe mobile thermal envelopes (5W-10W) dictate burst vs sustained clock performance." }
        ]
      },
      {
        title: "Graphics Processing Unit (GPU)",
        icon: "🎮",
        trim: "trim-orange",
        items: [
          { label: "Hardware Ray Tracing", desc: "Desktop-class rendering with hardware-accelerated BVH traversal on mobile dies." },
          { label: "Key Architectures", desc: "Qualcomm Adreno, ARM Immortalis (MediaTek), Apple Custom GPU, Samsung Xclipse (AMD RDNA3)." },
          { label: "Compute Overhead", desc: "Consumes up to 30-35% of total silicon die area in modern flagship processors." }
        ]
      },
      {
        title: "Neural Processing Unit (NPU / TPU)",
        icon: "⚡",
        trim: "trim-purple",
        items: [
          { label: "The AI Pivot", desc: "Dedicated tensor accelerators delivering 45-50+ TOPS for on-device LLMs and generative image diffusion." },
          { label: "Specialized Memory Paths", desc: "High-bandwidth direct memory channels bypassing CPU to avoid bottlenecks." },
          { label: "Architectural Leaders", desc: "Apple Neural Engine, Qualcomm Hexagon NPU, Google Tensor TPU, MediaTek APU." }
        ]
      },
      {
        title: "Image Signal Processor (ISP)",
        icon: "📷",
        trim: "trim-green",
        items: [
          { label: "Computational Photography", desc: "Multi-exposure HDR blending, zero shutter lag, zero-noise night mode processing." },
          { label: "Data Throughput", desc: "Capable of processing 2-3 gigapixels/sec in real-time across 200MP camera sensors." },
          { label: "Key Implementations", desc: "Qualcomm Spectra, Apple Photonic Engine, Google Ultra HDR Pipeline." }
        ]
      },
      {
        title: "5G Baseband Modem & RF",
        icon: "📡",
        trim: "trim-rose",
        items: [
          { label: "High Barrier to Entry", desc: "Decades of patent portfolios covering Sub-6GHz and mmWave carrier aggregation." },
          { label: "Qualcomm Dominance", desc: "Snapdragon X75/X80 modems; Apple still reliant on Qualcomm modems despite in-house silicon." },
          { label: "Monolithic vs Discrete", desc: "Flagship chips integrate modem on-die to save motherboard space and optimize battery." }
        ]
      },
      {
        title: "Packaging & Memory Subsystem",
        icon: "📦",
        trim: "trim-amber",
        items: [
          { label: "PoP (Package-on-Package)", desc: "LPDDR5X DRAM (8GB-24GB) soldered directly on top of the SoC via micro-bumps." },
          { label: "Unified Memory", desc: "Zero-copy data sharing between CPU, GPU, and NPU for extreme memory bandwidth (>136 GB/s)." },
          { label: "System-Level Cache (SLC)", desc: "16MB-32MB on-die caches buffering traffic to power-hungry external DRAM." }
        ]
      }
    ],
    notes: "Explain to the audience that a mobile processor is not just a CPU. It is a complete computing system integrating graphics, tensor accelerators, camera ISP pipelines, and 5G cellular modems on a single die."
  },
  {
    id: 4,
    category: "BUSINESS MODELS",
    title: "Semiconductor Business Models: Fabless vs. Captive vs. IDM",
    type: "cards_grid",
    layout: "grid-4-col",
    cards: [
      {
        title: "1. Captive Fabless\n(Apple, Google)",
        icon: "🛡️",
        trim: "trim-blue",
        items: [
          { label: "Core Philosophy", desc: "Design chips exclusively for proprietary hardware devices." },
          { label: "No Merchant Sales", desc: "Zero exposure to external OEM contract volatility." },
          { label: "Margin Synergy", desc: "Absorbed into $1,000+ retail device; can spend $150+ per chip." },
          { label: "Foundry Stance", desc: "100% outsourced to TSMC; buys first-wave node exclusivity." }
        ]
      },
      {
        title: "2. Merchant Fabless\n(Qualcomm, MediaTek)",
        icon: "🌐",
        trim: "trim-orange",
        items: [
          { label: "Core Philosophy", desc: "Design silicon to sell to third-party smartphone OEMs globally." },
          { label: "Customer Dependence", desc: "Exposed to OEM inventory cycles (Samsung, Xiaomi, Oppo)." },
          { label: "Pricing Pressure", desc: "Must maintain OEM profitability; strict margin ceilings." },
          { label: "Foundry Stance", desc: "Outsource to TSMC / Samsung; negotiate against Apple." }
        ]
      },
      {
        title: "3. Integrated IDM\n(Samsung Electronics)",
        icon: "🔄",
        trim: "trim-purple",
        items: [
          { label: "Core Philosophy", desc: "System LSI designs; Samsung Foundry fabs; Galaxy MX buys." },
          { label: "Internal Conflict", desc: "Captive Galaxy phones reject internal Exynos for Qualcomm." },
          { label: "Foundry Stance", desc: "Uses internal fabs; struggles with sub-5nm yields." },
          { label: "Capital Burden", desc: "Must fund multi-billion fab CapEx while designing." }
        ]
      },
      {
        title: "4. Pure-Play Foundry\n(TSMC)",
        icon: "🏗️",
        trim: "trim-green",
        items: [
          { label: "Core Philosophy", desc: "Fabricate wafers for external designers; never compete." },
          { label: "Monopolistic Pricing", desc: "Dictates wafer pricing due to lack of sub-3nm rivals." },
          { label: "CapEx Scale", desc: "Invests $30B-$40B annually in advanced fab tools." },
          { label: "Geopolitical Risk", desc: "Fabs concentrated in Taiwan; expanding to US/Japan." }
        ]
      }
    ],
    notes: "Contrast the four models. Emphasize why Apple's captive model is so financially dominant: Apple doesn't need to sell chips at a profit on the open market, allowing it to pay astronomical prices for the newest TSMC nodes."
  },
  {
    id: 5,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: Apple Silicon (A-Series & M-Series)",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "Supply Chain Power & Sourcing",
        icon: "🍏",
        trim: "trim-blue",
        items: [
          { label: "TSMC Alpha Customer", desc: "Apple accounts for ~23-25% of TSMC's corporate revenue, giving it unmatched priority." },
          { label: "Node Monopolization", desc: "Pre-reserved 100% of TSMC's initial 3nm (N3B) capacity in 2023-2024 for A17 Pro." },
          { label: "Yield Risk Absorption", desc: "Negotiated terms where TSMC absorbed defective die costs during initial 3nm ramp-up." },
          { label: "Advanced Packaging", desc: "Pioneered TSMC's InFO (Integrated Fan-Out) wafer-level packaging." }
        ]
      },
      {
        title: "Architectural & Value Strategy",
        icon: "💎",
        trim: "trim-orange",
        items: [
          { label: "Proprietary Microarchitecture", desc: "Fully custom ARM-based microarchitectures with massive L2 caches." },
          { label: "Captive Margin Flywheel", desc: "Estimated cost of $110-$135 per A18 Pro; integrated into $1,199 iPhone 16 Pro." },
          { label: "Apple Intelligence Engine", desc: "Re-engineered 16-core Neural Engine and memory bandwidth (>136 GB/s)." },
          { label: "Silicon Commonality", desc: "Shared architectural IP across iPhone, iPad, Mac, and Vision Pro." }
        ]
      },
      {
        title: "Vulnerabilities & Supply Risks",
        icon: "⚠️",
        trim: "trim-rose",
        items: [
          { label: "Single-Source Foundry Risk", desc: "Zero secondary foundry backup; 100% of advanced Apple chips are made in Taiwan." },
          { label: "Taiwan Strait Exposure", desc: "Any disruption to Fab 18 in Tainan would halt global iPhone output within 60 days." },
          { label: "Fab 21 Arizona Reality", desc: "US Arizona fab produces wafers, but InFO packaging still ships back to Taiwan." },
          { label: "Qualcomm Baseband Lock", desc: "Internal 5G modem project delayed multiple years due to cellular patent minefields." }
        ]
      }
    ],
    notes: "Apple is the golden standard of captive silicon integration. Point out the modem chokepoint: despite purchasing Intel's 5G division for $1B, Apple still pays Qualcomm for cellular modems."
  },
  {
    id: 6,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: Qualcomm Snapdragon",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "Merchant Leadership & Architecture",
        icon: "⚡",
        trim: "trim-orange",
        items: [
          { label: "Merchant Standard", desc: "The benchmark processor for Android flagships (Samsung Galaxy, Xiaomi, OnePlus, Vivo)." },
          { label: "The 'Oryon' Revolution", desc: "Acquired Nuvia for $1.4B; transitioned to custom Oryon CPU microarchitecture." },
          { label: "5G Modem Monopoly", desc: "Industry-leading Snapdragon X-series RF systems; bundles AP + modem + RF front-end." },
          { label: "High Dollar Share", desc: "Captures ~34% of global smartphone SoC revenues despite having lower unit volume than MediaTek." }
        ]
      },
      {
        title: "Foundry Dual-Sourcing Odyssey",
        icon: "🔄",
        trim: "trim-blue",
        items: [
          { label: "The Samsung 4nm Fiasco", desc: "Snapdragon 8 Gen 1 was fabricated on Samsung 4nm; suffered thermal throttling and low yields." },
          { label: "Mid-Cycle Pivot to TSMC", desc: "Qualcomm re-taped Snapdragon 8+ Gen 1 to TSMC 4nm, gaining +30% power efficiency." },
          { label: "TSMC Lock-in", desc: "Snapdragon 8 Gen 2, 3, and 8 Elite fully committed to TSMC N4P and N3E nodes." },
          { label: "Wafer Cost Penalty", desc: "Must pay premium spot prices to TSMC after Apple consumes primary volume ($180-$200 chip prices)." }
        ]
      },
      {
        title: "Customer & Legal Pressures",
        icon: "⚖️",
        trim: "trim-amber",
        items: [
          { label: "Samsung MX Concentration", desc: "Samsung Mobile is Qualcomm's biggest customer and an unpredictable partner." },
          { label: "Arm Litigation Threat", desc: "Arm sued Qualcomm over Nuvia architectural licenses, threatening royalty structures." },
          { label: "OEM Price Resistance", desc: "Chinese OEMs push back on $180+ SoC costs, looking to MediaTek for flagships." },
          { label: "Automotive & PC Hedge", desc: "Diversifying into Snapdragon Ride (autos) and Snapdragon X Elite (Copilot+ PCs)." }
        ]
      }
    ],
    notes: "Qualcomm's story illustrates the extreme importance of foundry node selection: when Samsung 4nm lagged TSMC, Qualcomm had to scramble to switch foundries mid-product cycle."
  },
  {
    id: 7,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: MediaTek Dimensity",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "Volume King to Flagship Disruptor",
        icon: "🏆",
        trim: "trim-green",
        items: [
          { label: "Global Unit Leader", desc: "Accounts for ~37-38% of all smartphone processors shipped worldwide (450M+ phones)." },
          { label: "Budget & Mid-Tier Stronghold", desc: "Dominates Helio and Dimensity 6000/7000 across Asia, Africa, and Latin America." },
          { label: "The 'All-Big-Core' Gamble", desc: "Dimensity 9300 & 9400 eliminated small efficiency cores entirely (4x Cortex-X + 4x Cortex-A720)." },
          { label: "Flagship Benchmark Parity", desc: "Dimensity 9400 achieved multi-core and GPU performance rivaling Snapdragon 8 Elite." }
        ]
      },
      {
        title: "Symbiotic TSMC Alignment",
        icon: "🤝",
        trim: "trim-blue",
        items: [
          { label: "Hsinchu Proximity", desc: "Headquartered walking distance from TSMC headquarters and R&D fabs in Taiwan." },
          { label: "Pacesetter on Second Wave", desc: "Consistently the primary fast-follower on TSMC's enhanced nodes (e.g. N3E for Dimensity 9400)." },
          { label: "Wafer Allocation Efficiency", desc: "Packages wafer orders across automotive, smart TV, and mobile lines for volume discounts." },
          { label: "Zero Advanced Alternatives", desc: "Entirely dependent on TSMC; does not evaluate Samsung Foundry for high-end Dimensity." }
        ]
      },
      {
        title: "Strategic Headwinds & Opportunities",
        icon: "📊",
        trim: "trim-purple",
        items: [
          { label: "Brand Perception Ceiling", desc: "Struggles to command equal prestige to Snapdragon in western premium carrier channels." },
          { label: "Chinese OEM Concentration", desc: "Over 70% of Dimensity revenue is tied to Chinese OEMs (Vivo, Oppo, Xiaomi, Transsion)." },
          { label: "Margin Expansion Push", desc: "Successfully increasing blended ASP from $25 in 2020 to >$42 in 2025 by winning flagships." },
          { label: "Nvidia Partnership Synergy", desc: "Partnering with Nvidia for automotive cockpit processors and custom AI PC silicon." }
        ]
      }
    ],
    notes: "MediaTek is the volume engine of the smartphone world. Their 'All-Big-Core' design philosophy surprised the industry by achieving top thermal efficiency while utilizing standard ARM IP."
  },
  {
    id: 8,
    category: "COMPANY DEEP DIVE",
    title: "Company Deep-Dive: Samsung System LSI & Foundry",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "The IDM Dilemma",
        icon: "🔄",
        trim: "trim-purple",
        items: [
          { label: "Divided House", desc: "System LSI designs the chip; Samsung Foundry manufactures it; both are separate units." },
          { label: "Internal Customer Rebellion", desc: "Samsung Mobile (MX Division) will reject Exynos for Qualcomm if yields lag." },
          { label: "Regional Bifurcation", desc: "Galaxy S flagship line split: Snapdragon in US/Korea, Exynos in Europe/Latin America." },
          { label: "Full Desertion (Galaxy S23)", desc: "Samsung MX completely dropped Exynos 2300, going 100% Snapdragon." }
        ]
      },
      {
        title: "3nm GAA Yield Challenges",
        icon: "⚠️",
        trim: "trim-rose",
        items: [
          { label: "The First to GAA", desc: "Pioneered Gate-All-Around (MBCFET) nanosheet architecture ahead of TSMC at 3nm." },
          { label: "Yield Disasters", desc: "Industry reports indicated initial 3nm GAA yields struggled below 20-30%, causing massive financial bleed." },
          { label: "Customer Defections", desc: "Qualcomm and Nvidia abandoned Samsung Foundry, consolidating on TSMC." },
          { label: "2nm Make-or-Break", desc: "Pouring immense resources into 2nm GAA (SF2) to attempt a leapfrog over TSMC." }
        ]
      },
      {
        title: "Packaging & In-House Advantages",
        icon: "🛡️",
        trim: "trim-blue",
        items: [
          { label: "FOWLP Packaging Pioneer", desc: "First to commercialize Fan-Out Wafer-Level Packaging on Exynos 2400 to reduce heat." },
          { label: "Memory Synergy", desc: "World's #1 DRAM & NAND maker; bundles LPDDR5X and UFS 4.0 storage packages internally." },
          { label: "AMD GPU Collaboration", desc: "Licensed AMD RDNA architecture for Xclipse GPU, bringing ray tracing to mobile." },
          { label: "Geopolitical Sanctuary", desc: "Fabs in S. Korea and Taylor, Texas; insulated from direct Taiwan cross-strait risk." }
        ]
      }
    ],
    notes: "Samsung's integrated model is both a curse and a blessing. When their internal foundry yields dropped below 30%, their mobile phone division abandoned their internal processors."
  },
  {
    id: 9,
    category: "SPECIAL CASES",
    title: "Special Cases: Google Tensor & HiSilicon (Huawei)",
    type: "cards_grid",
    layout: "grid-2-col",
    cards: [
      {
        title: "Google Tensor: Custom TPU Focus to TSMC",
        icon: "🔍",
        trim: "trim-blue",
        items: [
          { label: "Silicon Thesis", desc: "Abandoned Qualcomm off-the-shelf chips in 2021 to build Tensor, prioritizing AI/ML over benchmarks." },
          { label: "Samsung Co-Design Era (G1-G4)", desc: "Tensor G1 through G4 were co-developed with Samsung System LSI on Samsung 5nm/4nm nodes." },
          { label: "Thermal & Efficiency Penalties", desc: "Suffered from Samsung Foundry's higher power leakage and lower modem efficiency." },
          { label: "The Big Pivot: Tensor G5 on TSMC 3nm", desc: "Google took design 100% in-house with full custom RTL and taped out Tensor G5 on TSMC's 3nm N3E node." },
          { label: "Captive Integration Strategy", desc: "Designed exclusively to power Gemini Nano, multimodal models, and computational photography." }
        ]
      },
      {
        title: "HiSilicon (Huawei): Sanctions & Autarky",
        icon: "🛡️",
        trim: "trim-rose",
        items: [
          { label: "The Pre-Sanctions Giant", desc: "In 2020, Kirin 9000 was the world's first 5nm SoC, beating Apple to TSMC's cutting-edge fab line." },
          { label: "US Entity List Impact", desc: "US export controls banned TSMC, ASML, and US EDA tools from supplying HiSilicon." },
          { label: "The Kirin 9000s Miracle", desc: "Huawei shocked the world in late 2023 with Mate 60 Pro powered by a 7nm Kirin 9000s made by SMIC." },
          { label: "DUV Multi-Patterning", desc: "Lacking ASML EUV scanners, SMIC used immersion DUV multi-patterning (SAQP), resulting in low yields (~40%)." },
          { label: "Domestic Substitution Ecosystem", desc: "Replacing US EDA with Chinese EDA (Empyrean) and domestic packaging (JCET)." }
        ]
      }
    ],
    notes: "Two fascinating strategic pivots: Google leaving Samsung Foundry for TSMC to fix power leakage, and Huawei surviving severe US sanctions by building a fully autarkic domestic Chinese supply chain."
  },
  {
    id: 10,
    category: "MARKET DYNAMICS",
    title: "Market Share Dynamics: Unit Volume vs. Revenue Value Capture",
    type: "chart_and_cards",
    chart: "charts/market_share_soc.png",
    cards: [
      {
        title: "The Volume vs. Value Paradox",
        icon: "📊",
        trim: "trim-orange",
        items: [
          { label: "MediaTek Leads Volume (37%)", desc: "Dominates mass shipments across Asia, Africa, and LatAm through price-competitive SoCs." },
          { label: "Apple & Qualcomm Capture Value (72%)", desc: "Together control almost 3/4 of all dollar revenues in the global mobile SoC industry." },
          { label: "Flagship Premiumization", desc: "Consumers holding phones 3.5+ years drives demand for $800+ devices, shifting profits to high-end silicon." }
        ]
      },
      {
        title: "Strategic Key Takeaways",
        icon: "💡",
        trim: "trim-green",
        items: [
          { label: "Margin Asymmetry", desc: "Apple captures ~38% revenue share with only 18% unit volume by internalizing chip profits inside iPhones." },
          { label: "Unisoc in Entry Tier", desc: "Chinese designer Unisoc captures 9% unit share in ultra-budget 4G/entry 5G phones (<$150 retail)." },
          { label: "HiSilicon's Comeback", desc: "Capturing 3% global unit volume entirely within mainland China, taking share away from Qualcomm." }
        ]
      }
    ],
    notes: "Direct the audience's attention to the bar chart: Notice how MediaTek wins the blue bar (volume), but Apple and Qualcomm dominate the orange bars (dollar revenue)."
  },
  {
    id: 11,
    category: "SUPPLY CHAIN TIERS",
    title: "The Multi-Tier Mobile Silicon Supply Chain: Quartz to Device",
    type: "tier_stack",
    tiers: [
      { tag: "TIER 4", title: "Raw Materials & Specialty Chemicals", desc: "Quartz & Electronic-Grade Polysilicon (Shin-Etsu, SUMCO) • Photoresists (JSR, TOK), Ultra-pure HF, Purified Neon gas", cls: "tb-rose" },
      { tag: "TIER 3", title: "Equipment (SME), EDA Software & Architectural IP", desc: "ASML EUV Lithography Monopoly • Applied Materials, Lam Research, Tokyo Electron • Synopsys, Cadence • ARM Holdings", cls: "tb-orange" },
      { tag: "TIER 2", title: "Advanced Wafer Fabrication (Foundries)", desc: "TSMC (Taiwan - >87% sub-5nm mobile fabrication) • Samsung Foundry (S. Korea), SMIC (China) • 16-22 week cleanroom cycle", cls: "tb-blue" },
      { tag: "TIER 1", title: "Advanced Packaging, Assembly & Test (OSAT)", desc: "Wafer-Level Fan-Out (TSMC InFO-PoP) • DRAM stacking on SoC die • OSATs: ASE Group, Amkor, JCET • Advantest ATE testing", cls: "tb-purple" },
      { tag: "TIER 0", title: "OEM Integration & Final Global Logistics", desc: "Surface Mount Technology (SMT) Motherboard Integration (Foxconn, Pegatron, Luxshare) • High-value Air Freight logistics", cls: "tb-green" }
    ],
    notes: "Walk the audience through the 5 distinct tiers of the semiconductor pyramid. Stress that a disruption at any single tier halts the entire downstream supply chain."
  },
  {
    id: 12,
    category: "TIER 4 DEEP DIVE",
    title: "Tier 4 Deep Dive: ASML Lithography & Upstream Monopolies",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "ASML: The Ultimate Chokepoint",
        icon: "🔬",
        trim: "trim-rose",
        items: [
          { label: "The EUV Monopoly", desc: "100% global market share in Extreme Ultraviolet (EUV) lithography scanners (13.5nm wavelength)." },
          { label: "Engineering Complexity", desc: "Pulses tin droplets with CO₂ lasers 50,000 times/sec in high vacuum with Zeiss mirrors." },
          { label: "High-NA EUV Rollout", desc: "Twinscan EXE:5000 scanners cost ~$350M+ each; essential for sub-2nm mass production." },
          { label: "Lead Times", desc: "Order-to-delivery lead time of 18-24 months; capacity capped at ~50-60 machines per year." }
        ]
      },
      {
        title: "Raw Silicon Wafers & Substrates",
        icon: "⚪",
        trim: "trim-blue",
        items: [
          { label: "300mm Ingot Duopoly", desc: "Shin-Etsu Chemical and SUMCO (Japan) control >55% of global electronic-grade silicon wafers." },
          { label: "Extreme Purity Standards", desc: "Requires Eleven-Nines (99.999999999%) purity monocrystalline silicon via Czochralski growth." },
          { label: "Pricing Power", desc: "Wafer manufacturers lock foundries into 3-5 year Long-Term Agreements with take-or-pay clauses." },
          { label: "Substrate Scarcity", desc: "Ajinomoto Build-up Film (ABF) substrates periodically bottleneck advanced packaging." }
        ]
      },
      {
        title: "Critical Gases & Specialty Chemicals",
        icon: "🧪",
        trim: "trim-amber",
        items: [
          { label: "Japanese Chemical Grip", desc: "JSR, TOK, and Shin-Etsu control >80% of cutting-edge fluorinated polyimides and EUV photoresists." },
          { label: "Rare Gases Vulnerability", desc: "Ukraine historically produced ~50% of semiconductor-grade purified Neon gas used in excimer lasers." },
          { label: "Ultra-Pure Acids & Water", desc: "Fabs require billions of gallons of ultra-pure water (UPW) and electronic-grade Hydrogen Fluoride." },
          { label: "Single Point of Failure", desc: "A plant fire or chemical shutdown in Japan or Germany can halt wafer fabrication worldwide." }
        ]
      }
    ],
    notes: "ASML in the Netherlands is the single greatest technological chokepoint on Earth. Without ASML's EUV scanners, not a single modern iPhone or Snapdragon processor could be fabricated."
  },
  {
    id: 13,
    category: "TIER 3 DEEP DIVE",
    title: "Tier 3 Deep Dive: ARM Holdings & The EDA Software Duopoly",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "ARM Holdings: Architectural Hegemony",
        icon: "📐",
        trim: "trim-blue",
        items: [
          { label: "Universal Mobile ISA", desc: "Over 99% of all mobile phone processors globally utilize the ARM architecture (ARMv8 / ARMv9)." },
          { label: "Licensing Models", desc: "Architectural License (allows custom cores e.g. Apple, Oryon) vs Core License (stock Cortex cores)." },
          { label: "ARMv9 Feature Matrix", desc: "Introduced SVE2 vector extensions, Memory Tagging Extension, and Confidential Compute." },
          { label: "Qualcomm vs. Arm Lawsuit", desc: "Legal battle over Nuvia IP licenses threatens Qualcomm's Oryon CPU roadmap." }
        ]
      },
      {
        title: "EDA Software Duopoly (Synopsys & Cadence)",
        icon: "💻",
        trim: "trim-orange",
        items: [
          { label: "Software Gatekeepers", desc: "Synopsys and Cadence control ~70-75% of the Electronic Design Automation market." },
          { label: "Billion-Transistor Synthesis", desc: "Designing a 15-billion transistor SoC is physically impossible without automated EDA place-and-route." },
          { label: "PDK Integration", desc: "Foundries (TSMC, Samsung) release Process Design Kits formatted exclusively for Synopsys/Cadence." },
          { label: "Sanctions Weapon", desc: "US banned export of GAA-capable EDA software to China, severely limiting 3nm design efforts." }
        ]
      },
      {
        title: "The Open-Source Hedge: RISC-V",
        icon: "⚡",
        trim: "trim-green",
        items: [
          { label: "Architectural Independence", desc: "Open-standard instruction set architecture with zero royalty fees and no corporate owner." },
          { label: "Microcontroller Beachhead", desc: "Already pervasive in low-level subsystems (power management, security enclaves)." },
          { label: "The RISC-V Mobile Consortium", desc: "Qualcomm, Google, MediaTek, and NXP formed Quintauris to accelerate the ecosystem." },
          { label: "Android Tier-1 Support", desc: "Google officially committed to treating RISC-V as a tier-1 architecture alongside ARM." }
        ]
      }
    ],
    notes: "Explain the software and licensing layer: Even with foundries and equipment, designers need ARM's architecture and EDA software from Synopsys and Cadence to simulate and verify silicon dies."
  },
  {
    id: 14,
    category: "TIER 2 DEEP DIVE",
    title: "Tier 2 Deep Dive: TSMC's Advanced Node Fabrication Hegemony",
    type: "chart_and_cards",
    chart: "charts/foundry_advanced_nodes.png",
    cards: [
      {
        title: "TSMC: Linchpin of the Digital Age",
        icon: "🏭",
        trim: "trim-blue",
        items: [
          { label: "87% Dominance at <5nm", desc: "TSMC manufactures virtually every cutting-edge mobile processor for Apple, Qualcomm, and MediaTek." },
          { label: "GigaFab Scale", desc: "Fab 18 in Tainan produces >100,000 advanced 300mm wafers per month with unbeatable yield curves." },
          { label: "Pure-Play Trust Advantage", desc: "Never sells consumer hardware, guaranteeing clients that proprietary RTL designs are safe." }
        ]
      },
      {
        title: "Capacity Allocation & The Apple Tax",
        icon: "⚠️",
        trim: "trim-rose",
        items: [
          { label: "Apple Pre-Emption", desc: "Apple consistently secures entire initial production runs of new nodes (N5, N3B, N2 in 2025/2026)." },
          { label: "Android's 1-Year Lag", desc: "Qualcomm and MediaTek must wait 9-12 months for secondary node iterations (N3E/N3P)." },
          { label: "Wafer Price Inflation", desc: "TSMC announced 5-8% annual wafer price increases, which chip designers must absorb." }
        ]
      }
    ],
    notes: "Refer to the pie chart: TSMC's 87% share of sub-5nm wafer manufacturing is the single greatest manufacturing concentration in modern economic history."
  },
  {
    id: 15,
    category: "WAFER ECONOMICS",
    title: "Wafer Economics: The Exponential Cost of Moore's Law",
    type: "chart_and_cards",
    chart: "charts/wafer_cost_escalation.png",
    cards: [
      {
        title: "The Death of Dennard Scaling",
        icon: "📈",
        trim: "trim-orange",
        items: [
          { label: "Wafer Price Doubling", desc: "Processed 300mm wafer costs jumped from $3,000 at 28nm to $20,500 at 3nm, approaching $28,000 at 2nm." },
          { label: "Mask Set Inflation", desc: "Full optical mask set for a 3nm tape-out costs upwards of $50M-$80M alone." },
          { label: "Defect Density vs Die Size", desc: "Larger dies (>120mm²) suffer severe yield penalties, driving designers toward chiplet partitioning." }
        ]
      },
      {
        title: "Impact on Consumer Smartphone Prices",
        icon: "🏷️",
        trim: "trim-green",
        items: [
          { label: "ASP Inflation", desc: "Flagship processor prices rose from ~$70 in 2019 (Snapdragon 855) to ~$180-$200 in 2025 (Snapdragon 8 Elite)." },
          { label: "Margin Compression", desc: "Android OEMs unable to pass $50+ chip cost hikes are forced to downgrade RAM or camera specs." },
          { label: "Premium Polarization", desc: "Only smartphones retailing at $900+ can absorb the margin requirements of cutting-edge silicon." }
        ]
      }
    ],
    notes: "Moore's law is no longer economically free. In the past, shrinking transistors made them cheaper. Today, shrinking transistors makes them vastly more expensive."
  },
  {
    id: 16,
    category: "BOM ECONOMICS",
    title: "Smartphone Bill of Materials (BOM): The SoC as Value Epicenter",
    type: "chart_and_cards",
    chart: "charts/bom_cost_breakdown.png",
    cards: [
      {
        title: "SoC Represents 25-30% of Total BOM",
        icon: "💰",
        trim: "trim-purple",
        items: [
          { label: "Single Costliest Component", desc: "At ~$165, the Application Processor + RF subsystem surpasses the LTPO OLED display ($95) and camera ($88)." },
          { label: "Bundled RF Complexity", desc: "Modem integration requires companion RF Transceivers, Power Amplifiers (Skyworks, Qorvo), and mmWave antennas." },
          { label: "DRAM Packaging Squeeze", desc: "Stacking 16GB-24GB of LPDDR5X directly on the SoC adds another $45-$65 to the processor subsystem." }
        ]
      },
      {
        title: "Tiered Smartphone BOM Comparison",
        icon: "📱",
        trim: "trim-blue",
        items: [
          { label: "Flagship Tier ($1,000+ MSRP)", desc: "BOM: ~$560 | SoC Cost: $160-$190 (TSMC 3nm / N3E) | Represents 28-32% of total hardware cost." },
          { label: "Mid-Tier ($400-$600 MSRP)", desc: "BOM: ~$240 | SoC Cost: $50-$75 (TSMC 4nm / MediaTek Dimensity 8300) | Represents ~22% of BOM." },
          { label: "Budget Tier (<$200 MSRP)", desc: "BOM: ~$95 | SoC Cost: $18-$25 (TSMC 6nm / Unisoc T616) | Highly commoditized silicon margins." }
        ]
      }
    ],
    notes: "The Application Processor is the undisputed king of smartphone hardware costs. It has surpassed the OLED screen and camera modules as the #1 cost driver."
  },
  {
    id: 17,
    category: "TIER 1 DEEP DIVE",
    title: "Tier 1 Deep Dive: Advanced Packaging (OSAT) & InFO-PoP",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "TSMC InFO-PoP Technology",
        icon: "📦",
        trim: "trim-blue",
        items: [
          { label: "Integrated Fan-Out Packaging", desc: "Eliminates organic substrates, using high-density redistribution layers (RDL)." },
          { label: "Apple Exclusivity Engine", desc: "Apple adopted InFO with the A10 Fusion, shaving 30% off package height and boosting heat dissipation." },
          { label: "DRAM Direct Stacking", desc: "LPDDR5X DRAM dies are soldered directly on top of the SoC silicon, enabling 100+ GB/s memory bandwidth." },
          { label: "Chassis Heat Sink", desc: "Thin profile allows the smartphone frame to act as an efficient thermal dissipator." }
        ]
      },
      {
        title: "The OSAT Merchant Ecosystem",
        icon: "🏭",
        trim: "trim-orange",
        items: [
          { label: "Outsourced Assembly & Test", desc: "Independent packaging specialists handle merchant processors (Qualcomm, MediaTek, Unisoc)." },
          { label: "ASE Group (Taiwan)", desc: "World's largest OSAT provider (~30% market share); operations in Kaohsiung and Shanghai." },
          { label: "Amkor Technology (USA/Korea)", desc: "Strategic partner to Qualcomm and Apple; pioneering advanced SiP modules." },
          { label: "JCET & Tongfu (China)", desc: "Dominant packaging houses for domestic Chinese processors and mid-tier silicon." }
        ]
      },
      {
        title: "The Mobile Chiplet Horizon",
        icon: "🧩",
        trim: "trim-green",
        items: [
          { label: "Breaking Monolithic Dies", desc: "Separating compute (CPU/GPU) from I/O modems onto cheaper legacy nodes is the next frontier." },
          { label: "Interconnect Latency Challenges", desc: "Mobile power budgets (3-5W) make inter-die interconnects (UCIe) challenging without battery drain." },
          { label: "3D Hybrid Bonding", desc: "Direct copper-to-copper wafer stacking (TSMC SoIC) will allow SRAM caches under CPU cores by 2027." },
          { label: "Compound Yield Risks", desc: "Multi-die packaging risks scrapping the entire package if one die fails." }
        ]
      }
    ],
    notes: "Packaging is no longer an afterthought—it is the cutting edge of semiconductor performance. Stacking memory directly on top of the processor shaves latency and saves board space."
  },
  {
    id: 18,
    category: "RISKS & RESILIENCE",
    title: "Supply Chain Resilience, Bottlenecks & The Bullwhip Effect",
    type: "chart_and_cards",
    chart: "charts/company_resilience_radar.png",
    cards: [
      {
        title: "The Semiconductor Bullwhip Effect",
        icon: "⚠️",
        trim: "trim-orange",
        items: [
          { label: "Inelastic Lead Times", desc: "From raw silicon wafer start to finished phone in consumer hands takes 20 to 26 weeks; fabs cannot flex overnight." },
          { label: "2021 Shortage vs 2023 Glut", desc: "OEM double-ordering during COVID created phantom demand; inventory took 18 months to clear when demand dipped." },
          { label: "Buffer Stock Shift", desc: "Transition from lean 'Just-in-Time' (JIT) to strategic 'Just-in-Case' (JIC) with 90-120 days of component buffers." }
        ]
      },
      {
        title: "Geopolitical Chokepoints",
        icon: "🌐",
        trim: "trim-rose",
        items: [
          { label: "Taiwan Strait Risk", desc: "A naval blockade or earthquake in Taiwan would halt >85% of advanced global mobile processor supply." },
          { label: "US Export Controls", desc: "Export bans on <14nm tools and EDA divide the global supply chain into Western and Chinese blocs." },
          { label: "Raw Material Sanctions", desc: "China's export restrictions on Gallium, Germanium, and Antimony threaten wafer manufacturing." }
        ]
      }
    ],
    notes: "Examine the radar chart comparing company resilience. Apple has immense pricing power and architectural control, but zero foundry diversification away from Taiwan."
  },
  {
    id: 19,
    category: "FUTURE HORIZONS",
    title: "Future Horizons: 2nm GAA, On-Device AI & Geopolitical Diversification",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "2nm GAA & Backside Power Leap",
        icon: "🔬",
        trim: "trim-blue",
        items: [
          { label: "Nanosheet Transistors", desc: "Transitioning from FinFET to Gate-All-Around (GAA) nanosheets to minimize sub-threshold leakage at 2nm." },
          { label: "Backside Power Delivery (BSPDN)", desc: "Routing power rails on the wafer backside (TSMC A16 / Intel PowerVia) frees interconnect layers for signals (+10% speed)." },
          { label: "Staggering Tool CapEx", desc: "2nm fabs require High-NA EUV scanners ($350M each), driving fab module costs past $20B." },
          { label: "Initial Allocation", desc: "Apple has already locked up TSMC's 2nm pilot and early mass production capacity in Hsinchu Fab 20." }
        ]
      },
      {
        title: "On-Device Generative AI Super-Cycle",
        icon: "🤖",
        trim: "trim-purple",
        items: [
          { label: "Silicon Real Estate Reallocation", desc: "NPU/TPU die area expanding from <8% to >20% of total SoC footprint to run 10B+ parameter LLMs locally." },
          { label: "LPDDR6 Memory Rush", desc: "On-device AI requires memory bandwidth exceeding 150 GB/s, driving rapid adoption of next-gen LPDDR6." },
          { label: "Context Window Cache", desc: "System-level on-die cache expanding to 32MB-48MB to prevent DRAM round-trips that drain mobile batteries." },
          { label: "Autonomous AI Agents", desc: "Silicon optimized for continuous multimodal processing across voice, screen pixels, and sensors." }
        ]
      },
      {
        title: "Geographic De-Risking (CHIPS Acts)",
        icon: "🌍",
        trim: "trim-green",
        items: [
          { label: "TSMC Fab 21 (Arizona, USA)", desc: "$65B investment in three fab modules; Phase 1 producing 4nm wafers, Phase 2 targeting 3nm/2nm." },
          { label: "The Packaging Blindspot", desc: "Arizona-produced wafers still require air-freight back to Taiwan for InFO packaging, leaving supply chains partially exposed." },
          { label: "TSMC JASM (Kumamoto, Japan)", desc: "Specialty logic and image sensor fab operating with Japanese government subsidies (Sony/Denso partner)." },
          { label: "Samsung Taylor Fab (Texas)", desc: "Expanding US advanced foundry footprint with $6.4B US CHIPS Act grants to rival TSMC in North America." }
        ]
      }
    ],
    notes: "Looking ahead: 2nm Gate-All-Around, Backside Power Delivery, and the AI super-cycle will dictate the winners and losers of the next decade."
  },
  {
    id: 20,
    category: "CONCLUSION",
    title: "Strategic Recommendations for Industry Leaders & Conclusion",
    type: "cards_grid",
    layout: "grid-3-col",
    cards: [
      {
        title: "For Smartphone OEMs (Device Makers)",
        icon: "📱",
        trim: "trim-blue",
        items: [
          { label: "Dual-Sourcing Silicon Roads", desc: "Avoid single-merchant dependency; balance Qualcomm and MediaTek portfolios to protect gross margins." },
          { label: "Strategic Buffer Contracts", desc: "Lock in 12-to-18 month component allocations with take-or-pay flexibility to withstand cyclical supply shocks." },
          { label: "Software-Silicon Co-Design", desc: "Optimize proprietary neural runtimes (e.g. Gemini, Apple CoreML) to squeeze max performance out of existing nodes." },
          { label: "Tiered Model Strategy", desc: "Reserve expensive sub-3nm processors exclusively for flagship Pro tiers; utilize mature 4nm/6nm for mass market." }
        ]
      },
      {
        title: "For Chip Designers (Qualcomm, MediaTek)",
        icon: "⚙️",
        trim: "trim-orange",
        items: [
          { label: "Dual-Foundry PDK Portability", desc: "Maintain dual-compatible physical design rules to allow tape-out migration between TSMC and Samsung Foundry." },
          { label: "Accelerate Chiplet Architectures", desc: "Disaggregate I/O and analog modem circuitry onto mature nodes, reserving costly 2nm GAA wafers solely for CPU/GPU dies." },
          { label: "Architectural Royalty Hedging", desc: "Invest aggressively in RISC-V compute engines and custom microarchitectures to reduce exposure to ARM licensing fees." },
          { label: "Automotive & Edge Expansion", desc: "Repurpose high-performance smartphone SoC platforms for automotive cockpits and AI PC markets." }
        ]
      },
      {
        title: "Conclusion & Final Outlook",
        icon: "🎯",
        trim: "trim-green",
        items: [
          { label: "The Sovereign Silicon Era", desc: "Mobile processors are no longer mere consumer electronics parts; they are strategic national assets shaping geopolitical power." },
          { label: "High Barriers to Entry", desc: "With $300M+ tape-outs and $20B+ fab costs, the barrier to entering the cutting-edge mobile SoC race is practically insurmountable." },
          { label: "TSMC Remains Indispensable", desc: "Despite US/EU CHIPS Acts, Taiwan's integrated semiconductor cluster will remain the world's primary silicon foundry through 2030." },
          { label: "The AI Paradigm Shift", desc: "The next decade will be defined not by raw CPU gigahertz, but by TOPS/watt efficiency and memory bandwidth." }
        ]
      }
    ],
    notes: "Conclude by reiterating that mobile silicon has become sovereign critical infrastructure. The winners of tomorrow will be those who balance cutting-edge AI silicon architecture with resilient multi-foundry supply chain risk management."
  }
];

// ==========================================================================
// 2. COMPANY DATA REPOSITORY (FOR COMPARATOR TOOL)
// ==========================================================================
const companiesData = {
  apple: {
    name: "Apple Silicon",
    chip: "A18 Pro / A17 Pro",
    model: "Captive Fabless",
    arch: "Custom Apple ARMv9",
    foundry: "TSMC (Taiwan)",
    node: "3nm (N3B / N3E)",
    unitShare: 18,
    revShare: 38,
    cost: 125,
    packaging: "TSMC InFO-PoP (Wafer-level Fan-out)",
    foundryDiv: 3,  // Out of 10
    geoRisk: 4,     // Out of 10 (High Taiwan vulnerability)
    pricingPower: 10,
    highlight: "Commands the highest margins and 100% initial 3nm node allocation via massive cash prepayments."
  },
  qualcomm: {
    name: "Qualcomm Snapdragon",
    chip: "Snapdragon 8 Elite",
    model: "Merchant Fabless",
    arch: "Custom Oryon (Nuvia)",
    foundry: "TSMC (Ex-Samsung 4nm)",
    node: "3nm (N3E)",
    unitShare: 28,
    revShare: 34,
    cost: 190,
    packaging: "Amkor / ASE / TSMC",
    foundryDiv: 6,
    geoRisk: 6,
    pricingPower: 8,
    highlight: "Standard-bearer for Android flagships; bundles dominant 5G X80 modems with custom Oryon CPU cores."
  },
  mediatek: {
    name: "MediaTek Dimensity",
    chip: "Dimensity 9400",
    model: "Merchant Fabless",
    arch: "Stock ARM Cortex (All-Big-Core)",
    foundry: "TSMC (Taiwan)",
    node: "3nm (N3E)",
    unitShare: 37,
    revShare: 17,
    cost: 130,
    packaging: "TSMC InFO / ASE Group",
    foundryDiv: 4,
    geoRisk: 5,
    pricingPower: 6,
    highlight: "World unit volume leader (~37%); pioneered 'All-Big-Core' flagship architecture with disruptive cost efficiency."
  },
  samsung: {
    name: "Samsung Exynos",
    chip: "Exynos 2400 / 2500",
    model: "Hybrid IDM",
    arch: "Stock ARM Cortex-X4/A720",
    foundry: "Samsung Foundry (S. Korea)",
    node: "4nm FOWLP / 3nm GAA",
    unitShare: 5,
    revShare: 5,
    cost: 110,
    packaging: "Samsung FOWLP (Fan-Out Wafer-Level)",
    foundryDiv: 9,
    geoRisk: 8,
    pricingPower: 5,
    highlight: "Integrated IDM model; insulated from Taiwan, but struggles with sub-30% initial 3nm GAA nanosheet yields."
  },
  google: {
    name: "Google Tensor",
    chip: "Tensor G4 / G5",
    model: "Captive Fabless",
    arch: "Custom TPU + ARM Cores",
    foundry: "TSMC (Switched from Samsung)",
    node: "3nm (N3E for G5)",
    unitShare: 1.5,
    revShare: 1,
    cost: 100,
    packaging: "TSMC InFO-PoP",
    foundryDiv: 5,
    geoRisk: 5,
    pricingPower: 7,
    highlight: "Captive design prioritized for Gemini Nano and camera ISP; migrated from Samsung Foundry to TSMC for efficiency."
  },
  hisilicon: {
    name: "HiSilicon (Huawei)",
    chip: "Kirin 9010 / 9000s",
    model: "Captive (Sanctioned)",
    arch: "Custom Taishan CPU",
    foundry: "SMIC (China Domestic)",
    node: "7nm DUV Multi-pattern (SAQP)",
    unitShare: 3,
    revShare: 3,
    cost: 145,
    packaging: "JCET / Domestic Chinese OSAT",
    foundryDiv: 2,
    geoRisk: 2,
    pricingPower: 7,
    highlight: "Operating under severe US export bans; achieved domestic Chinese autarky via DUV multi-patterning despite yield penalties."
  }
};

// ==========================================================================
// 3. APP STATE & ELEMENT REFERENCES
// ==========================================================================
let currentSlideIndex = 0;
const totalSlides = slidesData.length;

// Autoplay state
let autoplayTimer = null;
let autoplayProgressTimer = null;
let isAutoplayActive = false;
const AUTOPLAY_DURATION = 6500; // 6.5s per slide

// Laser pointer state
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
// 4. SLIDE RENDERING ENGINE WITH STAGGER ANIMATIONS
// ==========================================================================
function renderSlide(index) {
  if (index < 0 || index >= totalSlides) return;
  currentSlideIndex = index;
  const slide = slidesData[index];

  // Update Indicator & Progress Bar
  currentSlideNumEl.textContent = String(slide.id).padStart(2, '0');
  totalSlidesNumEl.textContent = String(totalSlides).padStart(2, '0');
  slideCategoryBadgeEl.textContent = slide.category;
  progressBarEl.style.width = `${((index + 1) / totalSlides) * 100}%`;

  // Reset autoplay timer animation bar
  if (isAutoplayActive) {
    resetAutoplayTimer();
  }

  // Update Speaker Notes
  speakerNotesTextEl.innerHTML = `<strong>Slide ${slide.id}: ${slide.title}</strong><br><br>${slide.notes}`;

  // Build Slide Inner HTML
  let contentHtml = "";

  if (slide.type === "hero") {
    contentHtml = `
      <div class="slide-content-root">
        <div class="slide-hero">
          <div class="hero-tag">⚡ ${slide.category}</div>
          <h1 class="hero-title">${slide.title}</h1>
          <p class="hero-subtitle">${slide.subtitle}</p>
          <div class="hero-meta">Comprehensive Industry Research Project | Academic & Executive Strategy Report 2026</div>
          <div class="metrics-row">
            <div class="metric-card">
              <div class="metric-val">$45B+</div>
              <div class="metric-lbl">Market Size</div>
              <div class="metric-sub">Annual Mobile SoC Revenue</div>
            </div>
            <div class="metric-card">
              <div class="metric-val val-orange">1.2 Billion</div>
              <div class="metric-lbl">Annual Volume</div>
              <div class="metric-sub">Global Smartphone Units</div>
            </div>
            <div class="metric-card">
              <div class="metric-val val-rose">>87%</div>
              <div class="metric-lbl">Foundry Concentration</div>
              <div class="metric-sub">Sub-5nm at TSMC (Taiwan)</div>
            </div>
            <div class="metric-card">
              <div class="metric-val val-purple">16-22 Wks</div>
              <div class="metric-lbl">Fab Cycle Time</div>
              <div class="metric-sub">1,500+ Precision Cleanroom Steps</div>
            </div>
          </div>
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
    renderSlide(0); // Loop back in autoplay
  }
}

function prevSlide() {
  if (currentSlideIndex > 0) {
    renderSlide(currentSlideIndex - 1);
  }
}

// ==========================================================================
// 5. AUTOPLAY & TIMER LOGIC
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

// ==========================================================================
// 6. INTERACTIVE PRESENTER LASER POINTER
// ==========================================================================
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

// Track mouse position on slide stage
slideViewportWrapperEl.addEventListener("mousemove", (e) => {
  if (!isLaserActive) return;
  const rect = slideViewportWrapperEl.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;

  laserPointerEl.style.left = `${x}px`;
  laserPointerEl.style.top = `${y}px`;
});

slideViewportWrapperEl.addEventListener("mouseleave", () => {
  if (isLaserActive) {
    laserPointerEl.style.opacity = "0";
  }
});

slideViewportWrapperEl.addEventListener("mouseenter", () => {
  if (isLaserActive) {
    laserPointerEl.style.opacity = "1";
  }
});

// ==========================================================================
// 7. AMBIENT SILICON CIRCUIT PARTICLE BACKGROUND (CANVAS)
// ==========================================================================
function initAmbientCircuit() {
  const canvas = document.getElementById("ambientCanvas");
  if (!canvas) return;
  const ctx = canvas.getContext("2d");

  let width = (canvas.width = slideViewportWrapperEl.clientWidth);
  let height = (canvas.height = slideViewportWrapperEl.clientHeight);

  window.addEventListener("resize", () => {
    width = canvas.width = slideViewportWrapperEl.clientWidth;
    height = canvas.height = slideViewportWrapperEl.clientHeight;
  });

  const nodeCount = 38;
  const nodes = [];

  for (let i = 0; i < nodeCount; i++) {
    nodes.push({
      x: Math.random() * width,
      y: Math.random() * height,
      vx: (Math.random() - 0.5) * 0.45,
      vy: (Math.random() - 0.5) * 0.45,
      radius: Math.random() * 2 + 1,
      color: Math.random() > 0.4 ? "rgba(56, 189, 248, " : "rgba(167, 139, 250, "
    });
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);

    // Draw connection traces (circuit look)
    for (let i = 0; i < nodes.length; i++) {
      for (let j = i + 1; j < nodes.length; j++) {
        const dx = nodes[i].x - nodes[j].x;
        const dy = nodes[i].y - nodes[j].y;
        const dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 130) {
          const alpha = (1 - dist / 130) * 0.18;
          ctx.beginPath();
          ctx.strokeStyle = `rgba(56, 189, 248, ${alpha})`;
          ctx.lineWidth = 1;

          // Manhattan-style 90-degree bend for semiconductor circuit aesthetic
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[i].x, nodes[j].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.stroke();
        }
      }
    }

    // Draw nodes
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i];
      n.x += n.vx;
      n.y += n.vy;

      if (n.x < 0) n.x = width;
      if (n.x > width) n.x = 0;
      if (n.y < 0) n.y = height;
      if (n.y > height) n.y = 0;

      ctx.beginPath();
      ctx.arc(n.x, n.y, n.radius, 0, Math.PI * 2);
      ctx.fillStyle = `${n.color} 0.55)`;
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  draw();
}

// ==========================================================================
// 8. HEAD-TO-HEAD CHIPMAKER COMPARATOR
// ==========================================================================
function renderComparison() {
  const compAKey = document.getElementById("selectCompA").value;
  const compBKey = document.getElementById("selectCompB").value;

  const a = companiesData[compAKey];
  const b = companiesData[compBKey];
  const container = document.getElementById("comparisonResults");

  function buildColumn(data, otherData) {
    const isHigherCost = data.cost > otherData.cost;
    const isHigherRev = data.revShare > otherData.revShare;
    const isHigherUnit = data.unitShare > otherData.unitShare;

    return `
      <div class="comp-column">
        <div class="comp-col-header">
          <div class="comp-chip-badge">${data.chip} • ${data.node}</div>
          <h4>${data.name}</h4>
          <p style="font-size: 0.8rem; color: var(--text-muted);">${data.model} | Fab: ${data.foundry}</p>
        </div>

        <div class="comp-stat-row">
          <div class="comp-stat-header">
            <span>Global Revenue Share:</span>
            <span class="comp-stat-val" style="color: ${isHigherRev ? 'var(--accent-emerald)' : 'var(--text-white)'}">${data.revShare}%</span>
          </div>
          <div class="comp-bar-bg">
            <div class="comp-bar-fill" style="width: ${data.revShare * 2.5}%; background: ${isHigherRev ? 'var(--accent-emerald)' : 'var(--accent-blue)'}"></div>
          </div>
        </div>

        <div class="comp-stat-row">
          <div class="comp-stat-header">
            <span>Global Unit Volume Share:</span>
            <span class="comp-stat-val" style="color: ${isHigherUnit ? 'var(--accent-emerald)' : 'var(--text-white)'}">${data.unitShare}%</span>
          </div>
          <div class="comp-bar-bg">
            <div class="comp-bar-fill" style="width: ${data.unitShare * 2.5}%; background: ${isHigherUnit ? 'var(--accent-emerald)' : 'var(--accent-orange)'}"></div>
          </div>
        </div>

        <div class="comp-stat-row">
          <div class="comp-stat-header">
            <span>Estimated SoC BOM Cost:</span>
            <span class="comp-stat-val">$${data.cost}</span>
          </div>
          <div class="comp-bar-bg">
            <div class="comp-bar-fill" style="width: ${(data.cost / 200) * 100}%; background: var(--accent-rose)"></div>
          </div>
        </div>

        <div style="font-size: 0.82rem; background: var(--bg-surface); padding: 0.8rem; border-radius: var(--radius-sm); border: 1px solid var(--border-subtle); display: flex; flex-direction: column; gap: 0.4rem;">
          <div><strong>CPU Microarchitecture:</strong> ${data.arch}</div>
          <div><strong>Advanced Packaging:</strong> ${data.packaging}</div>
          <div><strong>Foundry Diversification:</strong> ${data.foundryDiv}/10</div>
          <div><strong>Geopolitical Insulation:</strong> ${data.geoRisk}/10</div>
        </div>

        <div style="font-size: 0.8rem; color: var(--accent-blue); line-height: 1.4; border-top: 1px solid var(--border-subtle); padding-top: 0.6rem;">
          <strong>Strategic Takeaway:</strong> ${data.highlight}
        </div>
      </div>
    `;
  }

  container.innerHTML = buildColumn(a, b) + buildColumn(b, a);
}

// ==========================================================================
// 9. INTERACTIVE SMARTPHONE BOM & HARDWARE MARGIN SIMULATOR
// ==========================================================================
const presets = {
  ultra_flagship: { soc: 185, display: 95, camera: 90, memory: 65, casing: 58, retail: 1199 },
  flagship: { soc: 130, display: 55, camera: 50, memory: 42, casing: 34, retail: 799 },
  midrange: { soc: 75, display: 55, camera: 50, memory: 42, casing: 34, retail: 499 },
  budget: { soc: 22, display: 25, camera: 20, memory: 22, casing: 14, retail: 199 }
};

function calculateBOM() {
  const soc = parseFloat(document.getElementById("simSoC").value);
  const display = parseFloat(document.getElementById("simDisplay").value);
  const camera = parseFloat(document.getElementById("simCamera").value);
  const memory = parseFloat(document.getElementById("simMemory").value);
  const casing = parseFloat(document.getElementById("simCasing").value);
  const retail = parseFloat(document.getElementById("simRetailSlider").value);

  // Other fixed BOM costs (RF passives, battery, power ICs, assembly) ~ $40-$50
  const passivesAndAssembly = 46;
  const totalBOM = soc + display + camera + memory + casing + passivesAndAssembly;

  const socSharePct = ((soc / totalBOM) * 100).toFixed(1);
  const grossMarginDollar = retail - totalBOM;
  const grossMarginPct = ((grossMarginDollar / retail) * 100).toFixed(1);

  // Update UI Elements
  document.getElementById("simRetailVal").textContent = `$${retail.toLocaleString()}`;
  document.getElementById("simTotalBOM").textContent = `$${totalBOM.toFixed(0)}`;
  document.getElementById("simSoCShare").textContent = `${socSharePct}%`;
  document.getElementById("simSoCAmount").textContent = `$${soc.toFixed(2)} allocated`;

  const marginEl = document.getElementById("simGrossMargin");
  const healthEl = document.getElementById("simMarginHealth");

  marginEl.textContent = `$${grossMarginDollar.toFixed(0)} (${grossMarginPct}%)`;

  if (grossMarginPct >= 50) {
    marginEl.className = "out-value accent-emerald";
    healthEl.textContent = "Health: Premium Margin (Strong OEM Profitability)";
  } else if (grossMarginPct >= 35) {
    marginEl.className = "out-value accent-cyan";
    healthEl.textContent = "Health: Balanced Margin (Standard Commercial Health)";
  } else if (grossMarginPct > 0) {
    marginEl.className = "out-value accent-orange";
    healthEl.textContent = "Health: Margin Squeeze (High Risk / Low Net Profits)";
  } else {
    marginEl.className = "out-value accent-rose";
    healthEl.textContent = "Health: Negative Gross Margin (Loss Leader)";
  }

  // Update Stacked Bar Segments
  document.getElementById("segSoC").style.width = `${(soc / totalBOM) * 100}%`;
  document.getElementById("segDisplay").style.width = `${(display / totalBOM) * 100}%`;
  document.getElementById("segCamera").style.width = `${(camera / totalBOM) * 100}%`;
  document.getElementById("segMemory").style.width = `${(memory / totalBOM) * 100}%`;
  document.getElementById("segCasing").style.width = `${(casing / totalBOM) * 100}%`;
  document.getElementById("segOther").style.width = `${(passivesAndAssembly / totalBOM) * 100}%`;

  // Dynamic Insight Text
  const insightBox = document.getElementById("simInsightBox");
  if (soc >= 180) {
    insightBox.innerHTML = `<strong>Executive Reviewer Takeaway:</strong> At $${soc}, cutting-edge 3nm silicon absorbs <strong>${socSharePct}% of total hardware BOM</strong>. At a retail MSRP of $${retail}, the OEM captures a <strong>${grossMarginPct}% gross margin</strong>. Only premium devices above $850-$900 can absorb this silicon cost while preserving marketing, R&D, and retailer margins.`;
  } else if (soc <= 30) {
    insightBox.innerHTML = `<strong>Executive Reviewer Takeaway:</strong> At $${soc}, legacy mature silicon represents only <strong>${socSharePct}% of BOM</strong>. While retail price ($${retail}) is low, the silicon cost structure is highly commoditized, offering limited technological moat but high unit volume elasticity.`;
  } else {
    insightBox.innerHTML = `<strong>Executive Reviewer Takeaway:</strong> Mid-tier silicon at $${soc} represents <strong>${socSharePct}% of BOM</strong>. This is the volume sweet-spot for brands like Xiaomi, Oppo, and Vivo, where dual-sourcing MediaTek Dimensity against Qualcomm is crucial to avoid margin erosion.`;
  }
}

function applyPreset(presetKey) {
  const p = presets[presetKey];
  if (!p) return;

  document.getElementById("simSoC").value = p.soc;
  document.getElementById("simDisplay").value = p.display;
  document.getElementById("simCamera").value = p.camera;
  document.getElementById("simMemory").value = p.memory;
  document.getElementById("simCasing").value = p.casing;
  document.getElementById("simRetailSlider").value = p.retail;

  document.querySelectorAll(".btn-preset").forEach(btn => {
    if (btn.getAttribute("data-preset") === presetKey) {
      btn.classList.add("active");
    } else {
      btn.classList.remove("active");
    }
  });

  calculateBOM();
}

// ==========================================================================
// 10. SLIDE DRAWER & SEARCH FILTER
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

// ==========================================================================
// 11. MODAL TOGGLE HANDLERS
// ==========================================================================
function toggleSpeakerNotes() {
  speakerNotesPanelEl.classList.toggle("open");
}

function openModal(modalEl) {
  modalEl.classList.add("active");
}

function closeModal(modalEl) {
  modalEl.classList.remove("active");
}

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
// 12. EVENT LISTENERS
// ==========================================================================
// Deck Navigation
document.getElementById("btnNextSlide").addEventListener("click", nextSlide);
document.getElementById("btnPrevSlide").addEventListener("click", prevSlide);
document.getElementById("arrowNext").addEventListener("click", nextSlide);
document.getElementById("arrowPrev").addEventListener("click", prevSlide);

// Toolbar Features
document.getElementById("btnToggleAutoplay").addEventListener("click", toggleAutoplay);
document.getElementById("btnToggleLaser").addEventListener("click", toggleLaserPointer);
document.getElementById("btnSlideDrawer").addEventListener("click", openSlideDrawer);
document.getElementById("btnCloseDrawer").addEventListener("click", closeSlideDrawer);
document.getElementById("btnToggleNotes").addEventListener("click", toggleSpeakerNotes);
document.getElementById("btnCloseNotes").addEventListener("click", toggleSpeakerNotes);
document.getElementById("btnToggleFullscreen").addEventListener("click", toggleFullscreen);

// Modals Triggers
document.getElementById("btnOpenShortcuts").addEventListener("click", () => openModal(shortcutsModalOverlayEl));
document.getElementById("btnCloseShortcuts").addEventListener("click", () => closeModal(shortcutsModalOverlayEl));

document.getElementById("btnOpenComparator").addEventListener("click", () => {
  renderComparison();
  openModal(comparatorModalOverlayEl);
});
document.getElementById("btnCloseComparator").addEventListener("click", () => closeModal(comparatorModalOverlayEl));

document.getElementById("btnOpenSimulator").addEventListener("click", () => {
  calculateBOM();
  openModal(simulatorModalOverlayEl);
});
document.getElementById("btnCloseSimulator").addEventListener("click", () => closeModal(simulatorModalOverlayEl));

// Comparator selection listeners
document.getElementById("selectCompA").addEventListener("change", renderComparison);
document.getElementById("selectCompB").addEventListener("change", renderComparison);

// Simulator inputs listeners
["simSoC", "simDisplay", "simCamera", "simMemory", "simCasing"].forEach(id => {
  document.getElementById(id).addEventListener("change", calculateBOM);
});
document.getElementById("simRetailSlider").addEventListener("input", calculateBOM);

// Preset buttons
document.querySelectorAll(".btn-preset").forEach(btn => {
  btn.addEventListener("click", () => {
    applyPreset(btn.getAttribute("data-preset"));
  });
});

// Close modals when clicking overlay backdrop
[slideDrawerOverlayEl, shortcutsModalOverlayEl, comparatorModalOverlayEl, simulatorModalOverlayEl].forEach(overlay => {
  overlay.addEventListener("click", (e) => {
    if (e.target === overlay) {
      closeAllModals();
    }
  });
});

// Keyboard Navigation HUD
document.addEventListener("keydown", (e) => {
  // Ignore shortcuts when typing in search or inputs
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
    calculateBOM();
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

// Navigation View Tabs Switcher
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

// ==========================================================================
// 13. INITIALIZATION ON DOM READY
// ==========================================================================
document.addEventListener("DOMContentLoaded", () => {
  renderSlide(0);
  buildSlideDrawer();
  initAmbientCircuit();
  renderComparison();
  calculateBOM();
  console.log("Silicon Chain Interactive Engine Loaded: Autoplay, Laser, Comparator & BOM Simulator Active.");
});
