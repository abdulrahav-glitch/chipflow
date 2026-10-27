"""
ChipFlow - Master Processor & Mobile Phone Intelligence Database
Contains complete data for mobile SoCs across Apple, Qualcomm, MediaTek, Samsung, Google, HiSilicon, and Unisoc,
along with confirmed smartphone device mappings, foundry partners, lithography nodes, and BOM estimates.
"""

PROCESSORS_DATA = [
  # ═══════════════════════════════════════════════════════════════════
  # 1. APPLE
  # ═══════════════════════════════════════════════════════════════════
  {
    "id": "apple-a18-pro",
    "brand": "Apple",
    "brandColor": "#a78bfa",
    "name": "A18 Pro",
    "altName": "A18 Pro Bionic",
    "tier": "Flagship",
    "model": "Captive Fabless",
    "node": "TSMC 3nm (N3P/N3E)",
    "foundry": "TSMC (100%)",
    "cpu": "Custom Apple ARMv9 (2x 4.04GHz + 4x 2.2GHz)",
    "gpu": "6-core Apple GPU (Hardware Ray Tracing)",
    "npu": "16-core Neural Engine (35 TOPS, Apple Intelligence)",
    "packaging": "TSMC InFO-PoP",
    "modem": "External Qualcomm Snapdragon X75 5G",
    "unitShare": 18,
    "revenueShare": 38,
    "bomCost": "$110 – $135",
    "bomAvg": 122,
    "riskLevel": "critical",
    "riskLabel": "Single-source Taiwan",
    "filter": "apple",
    "description": "Apple captures ~38% of global smartphone SoC revenue with just 18% unit share. Silicon strategy is holistic: chips are engineered to maximize iOS feature integration, computational photography, battery runtime, and Apple Intelligence.",
    "strengths": [
      "Preferential TSMC 'Alpha Customer' status — first access to every new node",
      "Apple represents 23–25% of TSMC's total revenue",
      "Funded commercialization of TSMC InFO-PoP packaging",
      "Yield risk absorption: pays only for functional dies during early ramps"
    ],
    "risks": "Taiwan Concentration: 100% of advanced silicon is fabricated in Taiwan. Any geopolitical blockade or seismic event would paralyze flagship hardware output within 60–90 days. Still dependent on external Qualcomm 5G modems.",
    "phones": [
      {"brand": "Apple", "model": "iPhone 16 Pro Max", "year": 2024, "tier": "Ultra-Flagship"},
      {"brand": "Apple", "model": "iPhone 16 Pro", "year": 2024, "tier": "Ultra-Flagship"}
    ]
  },
  {
    "id": "apple-a18",
    "brand": "Apple",
    "brandColor": "#a78bfa",
    "name": "A18",
    "altName": "A18 Bionic",
    "tier": "Flagship",
    "model": "Captive Fabless",
    "node": "TSMC 3nm (N3E)",
    "foundry": "TSMC (100%)",
    "cpu": "Custom Apple ARMv9 (2x 4.04GHz + 4x 2.2GHz)",
    "gpu": "5-core Apple GPU",
    "npu": "16-core Neural Engine (Apple Intelligence)",
    "packaging": "TSMC InFO-PoP",
    "modem": "External Qualcomm 5G",
    "unitShare": 12,
    "revenueShare": 18,
    "bomCost": "$95 – $115",
    "bomAvg": 105,
    "riskLevel": "critical",
    "riskLabel": "Single-source Taiwan",
    "filter": "apple",
    "description": "Engineered for mainstream iPhone 16 models with full hardware support for Apple Intelligence on-device LLMs and generative photo editing.",
    "strengths": [
      "Substantial memory bandwidth upgrade (17% increase to support on-device AI)",
      "Direct TSMC N3E manufacturing efficiency leap over previous generation",
      "Shared architectural heritage with A18 Pro"
    ],
    "risks": "Exclusively reliant on TSMC Fab 18 in Tainan, Taiwan. Vulnerable to Pacific logistics disruptions.",
    "phones": [
      {"brand": "Apple", "model": "iPhone 16", "year": 2024, "tier": "Flagship"},
      {"brand": "Apple", "model": "iPhone 16 Plus", "year": 2024, "tier": "Flagship"}
    ]
  },
  {
    "id": "apple-a17-pro",
    "brand": "Apple",
    "brandColor": "#a78bfa",
    "name": "A17 Pro",
    "altName": "A17 Bionic Pro",
    "tier": "Flagship",
    "model": "Captive Fabless",
    "node": "TSMC 3nm (N3B)",
    "foundry": "TSMC (100%)",
    "cpu": "Custom Apple ARMv9 (2x 3.78GHz + 4x 2.11GHz)",
    "gpu": "6-core Apple GPU (Hardware Ray Tracing)",
    "npu": "16-core Neural Engine (35 TOPS)",
    "packaging": "TSMC InFO-PoP",
    "modem": "External Qualcomm X70 5G",
    "unitShare": 15,
    "revenueShare": 25,
    "bomCost": "$120 – $140",
    "bomAvg": 130,
    "riskLevel": "critical",
    "riskLabel": "N3B high wafer cost",
    "filter": "apple",
    "description": "The world's first commercial 3nm smartphone processor. Debuted hardware-accelerated ray tracing for console-grade gaming on mobile devices.",
    "strengths": [
      "First commercial 3nm deployment in consumer electronics history",
      "Hardware-accelerated mesh shading and ray tracing",
      "Dedicated AV1 hardware decoder engine"
    ],
    "risks": "First-generation TSMC N3B process suffered from lower initial yields and astronomical wafer costs exceeding $20,000 per wafer.",
    "phones": [
      {"brand": "Apple", "model": "iPhone 15 Pro Max", "year": 2023, "tier": "Ultra-Flagship"},
      {"brand": "Apple", "model": "iPhone 15 Pro", "year": 2023, "tier": "Ultra-Flagship"},
      {"brand": "Apple", "model": "iPad mini (7th Gen)", "year": 2024, "tier": "Tablet"}
    ]
  },
  {
    "id": "apple-a16-bionic",
    "brand": "Apple",
    "brandColor": "#a78bfa",
    "name": "A16 Bionic",
    "altName": "A16",
    "tier": "Premium",
    "model": "Captive Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "Custom Apple 6-core (2x 3.46GHz + 4x 2.02GHz)",
    "gpu": "5-core Apple GPU",
    "npu": "16-core Neural Engine (17 TOPS)",
    "packaging": "TSMC InFO-PoP",
    "modem": "External Qualcomm Snapdragon X65 5G",
    "unitShare": 16,
    "revenueShare": 22,
    "bomCost": "$85 – $105",
    "bomAvg": 95,
    "riskLevel": "high",
    "riskLabel": "Single-source TSMC",
    "filter": "apple",
    "description": "Built on TSMC 4nm process. Powering millions of devices with exceptional thermal stability and class-leading single-core performance.",
    "strengths": [
      "High yield maturity on TSMC N4P node",
      "Display Engine powering Dynamic Island with 1Hz variable refresh rate",
      "50% higher memory bandwidth than A15 (LPDDR5)"
    ],
    "risks": "Dependence on external Qualcomm modems and TSMC packaging pipeline.",
    "phones": [
      {"brand": "Apple", "model": "iPhone 15", "year": 2023, "tier": "Flagship"},
      {"brand": "Apple", "model": "iPhone 15 Plus", "year": 2023, "tier": "Flagship"},
      {"brand": "Apple", "model": "iPhone 14 Pro Max", "year": 2022, "tier": "Ultra-Flagship"},
      {"brand": "Apple", "model": "iPhone 14 Pro", "year": 2022, "tier": "Ultra-Flagship"}
    ]
  },
  {
    "id": "apple-a15-bionic",
    "brand": "Apple",
    "brandColor": "#a78bfa",
    "name": "A15 Bionic",
    "altName": "A15",
    "tier": "Premium",
    "model": "Captive Fabless",
    "node": "TSMC 5nm (N5P)",
    "foundry": "TSMC (100%)",
    "cpu": "Custom Apple 6-core (2x 3.23GHz + 4x 1.82GHz)",
    "gpu": "4-core / 5-core Apple GPU",
    "npu": "16-core Neural Engine (15.8 TOPS)",
    "packaging": "TSMC InFO-PoP",
    "modem": "External Qualcomm X60 5G",
    "unitShare": 22,
    "revenueShare": 20,
    "bomCost": "$65 – $80",
    "bomAvg": 72,
    "riskLevel": "medium",
    "riskLabel": "Legacy 5nm node",
    "filter": "apple",
    "description": "One of the most widely deployed mobile processors in history, powering six distinct iPhone models across multiple release cycles.",
    "strengths": [
      "Unprecedented battery efficiency benchmark on TSMC 5nm",
      "Immense scale: over 250M units manufactured across 2021-2024",
      "High margin yield efficiency at amortized mask costs"
    ],
    "risks": "5nm capacity is gradually being converted to 3nm/2nm at TSMC fabs.",
    "phones": [
      {"brand": "Apple", "model": "iPhone 14", "year": 2022, "tier": "Flagship"},
      {"brand": "Apple", "model": "iPhone 14 Plus", "year": 2022, "tier": "Flagship"},
      {"brand": "Apple", "model": "iPhone 13 Pro Max", "year": 2021, "tier": "Ultra-Flagship"},
      {"brand": "Apple", "model": "iPhone 13 Pro", "year": 2021, "tier": "Ultra-Flagship"},
      {"brand": "Apple", "model": "iPhone 13", "year": 2021, "tier": "Flagship"},
      {"brand": "Apple", "model": "iPhone 13 mini", "year": 2021, "tier": "Compact Flagship"},
      {"brand": "Apple", "model": "iPhone SE (3rd Gen)", "year": 2022, "tier": "Budget iOS"}
    ]
  },
  {
    "id": "apple-a14-bionic",
    "brand": "Apple",
    "brandColor": "#a78bfa",
    "name": "A14 Bionic",
    "altName": "A14",
    "tier": "Midrange",
    "model": "Captive Fabless",
    "node": "TSMC 5nm (N5)",
    "foundry": "TSMC (100%)",
    "cpu": "Custom Apple 6-core (2x 3.1GHz + 4x 1.8GHz)",
    "gpu": "4-core Apple GPU",
    "npu": "16-core Neural Engine (11 TOPS)",
    "packaging": "TSMC InFO-PoP",
    "modem": "External Qualcomm X55 5G",
    "unitShare": 10,
    "revenueShare": 9,
    "bomCost": "$50 – $65",
    "bomAvg": 56,
    "riskLevel": "low",
    "riskLabel": "Mature 5nm",
    "filter": "apple",
    "description": "First 5nm processor ever launched in a smartphone. Brought 5G connectivity to the iPhone family with the iPhone 12 generation.",
    "strengths": [
      "Pioneered commercial 5nm EUV volume production at TSMC",
      "Introduced Apple ProRAW and Dolby Vision 4K recording pipeline"
    ],
    "risks": "Older Qualcomm X55 modem has higher power draw compared to modern integrated solutions.",
    "phones": [
      {"brand": "Apple", "model": "iPhone 12 Pro Max", "year": 2020, "tier": "Ultra-Flagship"},
      {"brand": "Apple", "model": "iPhone 12 Pro", "year": 2020, "tier": "Ultra-Flagship"},
      {"brand": "Apple", "model": "iPhone 12", "year": 2020, "tier": "Flagship"},
      {"brand": "Apple", "model": "iPhone 12 mini", "year": 2020, "tier": "Compact Flagship"},
      {"brand": "Apple", "model": "iPad (10th Gen)", "year": 2022, "tier": "Tablet"}
    ]
  },

  # ═══════════════════════════════════════════════════════════════════
  # 2. QUALCOMM SNAPDRAGON
  # ═══════════════════════════════════════════════════════════════════
  {
    "id": "snapdragon-8-elite",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 8 Elite",
    "altName": "Snapdragon 8 Gen 4",
    "tier": "Flagship",
    "model": "Merchant Fabless",
    "node": "TSMC 3nm (N3E)",
    "foundry": "TSMC (100%)",
    "cpu": "Custom Oryon 8-core (2x 4.32GHz Prime + 6x 3.53GHz Perf)",
    "gpu": "Adreno 830 (Sliced Architecture)",
    "npu": "Hexagon NPU (45% faster multimodal AI)",
    "packaging": "Amkor / ASE / TSMC",
    "modem": "Integrated Snapdragon X80 5G (10 Gbps peak)",
    "unitShare": 28,
    "revenueShare": 34,
    "bomCost": "$180 – $200",
    "bomAvg": 190,
    "riskLevel": "high",
    "riskLabel": "TSMC allocation & high BOM",
    "filter": "qualcomm",
    "description": "Qualcomm's revolutionary flagship SoC introducing desktop-derived custom Oryon CPU cores, replacing standard ARM Cortex cores. Commands premium pricing across tier-1 Android OEMs.",
    "strengths": [
      "Custom Oryon cores break single-core and multi-core Android performance records",
      "Integrated Snapdragon X80 5G with dedicated tensor accelerator for AI satellite links",
      "Industry-leading Adreno 830 GPU with sliced architecture and Unreal Engine 5.3 support",
      "Unrivaled 100% adoption among top Android flagship devices"
    ],
    "risks": "High $180-$200 BOM pricing strains OEM hardware margins, prompting Xiaomi, Vivo, and Samsung to dual-source with MediaTek Dimensity.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy S25 Ultra", "year": 2025, "tier": "Ultra-Flagship"},
      {"brand": "Samsung", "model": "Galaxy S25+", "year": 2025, "tier": "Ultra-Flagship"},
      {"brand": "Samsung", "model": "Galaxy S25", "year": 2025, "tier": "Flagship"},
      {"brand": "OnePlus", "model": "OnePlus 13", "year": 2024, "tier": "Flagship"},
      {"brand": "Xiaomi", "model": "Xiaomi 15", "year": 2024, "tier": "Flagship"},
      {"brand": "Xiaomi", "model": "Xiaomi 15 Pro", "year": 2024, "tier": "Ultra-Flagship"},
      {"brand": "Realme", "model": "Realme GT 7 Pro", "year": 2024, "tier": "Flagship"},
      {"brand": "iQOO", "model": "iQOO 13", "year": 2024, "tier": "Flagship"},
      {"brand": "ASUS", "model": "ROG Phone 9 / 9 Pro", "year": 2024, "tier": "Gaming Flagship"},
      {"brand": "Nubia", "model": "RedMagic 10 Pro", "year": 2024, "tier": "Gaming Flagship"},
      {"brand": "Honor", "model": "Honor Magic 7 / 7 Pro", "year": 2024, "tier": "Ultra-Flagship"}
    ]
  },
  {
    "id": "snapdragon-8-gen-3",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 8 Gen 3",
    "altName": "SM8650-AB",
    "tier": "Flagship",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "1x Cortex-X4 (3.3GHz) + 5x A720 + 2x A520",
    "gpu": "Adreno 750",
    "npu": "Hexagon NPU (45 TOPS on-device GenAI)",
    "packaging": "Amkor / ASE",
    "modem": "Integrated Snapdragon X75 5G",
    "unitShare": 24,
    "revenueShare": 30,
    "bomCost": "$160 – $180",
    "bomAvg": 170,
    "riskLevel": "medium",
    "riskLabel": "ARM licensing dispute",
    "filter": "qualcomm",
    "description": "The benchmark silicon of the 2024 Android flagship cycle, introducing on-device multimodal generative AI models up to 10 billion parameters.",
    "strengths": [
      "First mobile chip to run multimodal LLMs (Llama 2, Stable Diffusion) entirely on-device",
      "Special 'Snapdragon 8 Gen 3 for Galaxy' variant overclocked to 3.39GHz",
      "Dominant presence in all premier foldables and flagship phones"
    ],
    "risks": "Wafer price increases at TSMC N4P squeezed merchant pricing.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy S24 Ultra", "year": 2024, "tier": "Ultra-Flagship"},
      {"brand": "Samsung", "model": "Galaxy Z Fold6", "year": 2024, "tier": "Foldable Flagship"},
      {"brand": "Samsung", "model": "Galaxy Z Flip6", "year": 2024, "tier": "Flip Foldable"},
      {"brand": "OnePlus", "model": "OnePlus 12", "year": 2024, "tier": "Flagship"},
      {"brand": "Xiaomi", "model": "Xiaomi 14 / 14 Ultra", "year": 2023, "tier": "Ultra-Flagship"},
      {"brand": "Vivo", "model": "Vivo X Fold3 Pro", "year": 2024, "tier": "Foldable Flagship"},
      {"brand": "ASUS", "model": "ROG Phone 8 Pro", "year": 2024, "tier": "Gaming Flagship"},
      {"brand": "Sony", "model": "Xperia 1 VI", "year": 2024, "tier": "Pro Flagship"},
      {"brand": "Meizu", "model": "Meizu 21 / 21 Pro", "year": 2024, "tier": "Flagship"}
    ]
  },
  {
    "id": "snapdragon-8s-gen-3",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 8s Gen 3",
    "altName": "SM8635",
    "tier": "Premium",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "1x Cortex-X4 (3.0GHz) + 4x A720 + 3x A520",
    "gpu": "Adreno 735",
    "npu": "Hexagon NPU",
    "packaging": "ASE / Amkor",
    "modem": "Integrated Snapdragon X70 5G",
    "unitShare": 14,
    "revenueShare": 12,
    "bomCost": "$100 – $120",
    "bomAvg": 110,
    "riskLevel": "low",
    "riskLabel": "Healthy yield",
    "filter": "qualcomm",
    "description": "Qualcomm's 'flagship killer' processor created to bring Cortex-X4 performance and on-device GenAI capabilities to the $400–$600 smartphone price tier.",
    "strengths": [
      "Inherits flagship Cortex-X4 architecture at ~35% lower cost than 8 Gen 3",
      "Tremendous popularity among performance-focused sub-brands (POCO, Redmi Turbo, Realme GT)",
      "High thermal efficiency and sustained gaming performance"
    ],
    "risks": "Faces aggressive direct competition from MediaTek Dimensity 8300-Ultra and 9200+.",
    "phones": [
      {"brand": "POCO", "model": "POCO F6", "year": 2024, "tier": "Flagship Killer"},
      {"brand": "Xiaomi", "model": "Redmi Turbo 3", "year": 2024, "tier": "Performance Mid"},
      {"brand": "Xiaomi", "model": "Xiaomi Civi 4 Pro", "year": 2024, "tier": "Lifestyle Flagship"},
      {"brand": "Motorola", "model": "Edge 50 Ultra", "year": 2024, "tier": "Flagship"},
      {"brand": "Realme", "model": "Realme GT Neo 6", "year": 2024, "tier": "Performance Mid"},
      {"brand": "Honor", "model": "Honor 200 Pro", "year": 2024, "tier": "Premium Mid"},
      {"brand": "iQOO", "model": "iQOO Z9 Turbo", "year": 2024, "tier": "Performance Mid"}
    ]
  },
  {
    "id": "snapdragon-8-gen-2",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 8 Gen 2",
    "altName": "SM8550-AB",
    "tier": "Flagship",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4)",
    "foundry": "TSMC (100%)",
    "cpu": "1x Cortex-X3 (3.2GHz) + 2x A715 + 2x A710 + 3x A510",
    "gpu": "Adreno 740",
    "npu": "Hexagon NPU",
    "packaging": "Amkor / ASE",
    "modem": "Integrated Snapdragon X70 5G",
    "unitShare": 22,
    "revenueShare": 26,
    "bomCost": "$135 – $155",
    "bomAvg": 145,
    "riskLevel": "low",
    "riskLabel": "Mature node",
    "filter": "qualcomm",
    "description": "The processor that restored Qualcomm's thermal dominance after switching completely from Samsung Foundry back to TSMC. Remains a staple in upper-tier smartphones.",
    "strengths": [
      "Outstanding 40% GPU efficiency uplift over 8 Gen 1",
      "Pioneered hardware-accelerated ray tracing in Android titles",
      "Extended lifecycle in 2024 flagship killers (e.g. OnePlus 12R)"
    ],
    "risks": "Older node lifecycle phasing out into secondary capacity.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy S23 Ultra", "year": 2023, "tier": "Ultra-Flagship"},
      {"brand": "Samsung", "model": "Galaxy S23 / S23+", "year": 2023, "tier": "Flagship"},
      {"brand": "Samsung", "model": "Galaxy Z Fold5 / Flip5", "year": 2023, "tier": "Foldable"},
      {"brand": "OnePlus", "model": "OnePlus 12R", "year": 2024, "tier": "Premium Mid"},
      {"brand": "OnePlus", "model": "OnePlus 11", "year": 2023, "tier": "Flagship"},
      {"brand": "Xiaomi", "model": "Xiaomi 13 / 13 Pro", "year": 2023, "tier": "Flagship"},
      {"brand": "Motorola", "model": "Edge 40 Pro", "year": 2023, "tier": "Flagship"},
      {"brand": "ASUS", "model": "Zenfone 10", "year": 2023, "tier": "Compact Flagship"},
      {"brand": "Honor", "model": "Magic5 Pro", "year": 2023, "tier": "Ultra-Flagship"}
    ]
  },
  {
    "id": "snapdragon-8-plus-gen-1",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 8+ Gen 1",
    "altName": "SM8475",
    "tier": "Premium",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4)",
    "foundry": "TSMC (Switched from Samsung)",
    "cpu": "1x Cortex-X2 (3.2GHz) + 3x A710 + 4x A510",
    "gpu": "Adreno 730",
    "npu": "7th Gen Qualcomm AI Engine",
    "packaging": "Amkor / ASE",
    "modem": "Integrated Snapdragon X65 5G",
    "unitShare": 16,
    "revenueShare": 18,
    "bomCost": "$95 – $115",
    "bomAvg": 105,
    "riskLevel": "low",
    "riskLabel": "Stable TSMC node",
    "filter": "qualcomm",
    "description": "Crucial historical pivot chip: Qualcomm switched manufacturing of the 8-series from Samsung 4nm to TSMC 4nm mid-generation, delivering a 30% power reduction and fixing thermal throttling.",
    "strengths": [
      "Demonstrated measurable proof of TSMC's process node superiority over Samsung 4LPE",
      "Became the go-to chip for high-end foldable phones and premium lifestyle devices"
    ],
    "risks": "Older Cortex-X2 architecture lacks modern ARMv9.2 efficiency refinements.",
    "phones": [
      {"brand": "Nothing", "model": "Nothing Phone (2)", "year": 2023, "tier": "Premium Mid"},
      {"brand": "OnePlus", "model": "OnePlus 10T", "year": 2022, "tier": "Performance Flagship"},
      {"brand": "Samsung", "model": "Galaxy Z Fold4", "year": 2022, "tier": "Foldable"},
      {"brand": "Samsung", "model": "Galaxy Z Flip4", "year": 2022, "tier": "Flip Foldable"},
      {"brand": "Motorola", "model": "Razr 40 Ultra", "year": 2023, "tier": "Flip Foldable"},
      {"brand": "POCO", "model": "POCO F5 Pro", "year": 2023, "tier": "Flagship Killer"},
      {"brand": "Realme", "model": "Realme GT3", "year": 2023, "tier": "Fast-charging Flagship"}
    ]
  },
  {
    "id": "snapdragon-7-plus-gen-3",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 7+ Gen 3",
    "altName": "SM7675",
    "tier": "Premium Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "1x Cortex-X4 (2.8GHz) + 4x A720 + 3x A520",
    "gpu": "Adreno 732",
    "npu": "Hexagon NPU",
    "packaging": "Amkor / ASE",
    "modem": "Integrated Snapdragon X63 5G",
    "unitShare": 8,
    "revenueShare": 7,
    "bomCost": "$70 – $85",
    "bomAvg": 78,
    "riskLevel": "low",
    "riskLabel": "TSMC 4nm",
    "filter": "qualcomm",
    "description": "Brings actual flagship Cortex-X4 architecture directly into the premium mid-range $350–$450 tier with Wi-Fi 7 and on-device AI.",
    "strengths": [
      "Inherits Cortex-X4 prime core architecture from 8 Gen 3",
      "Supports LPDDR5X memory up to 4800MHz and UFS 4.0 storage"
    ],
    "risks": "Niche adoption as OEMs balance pricing between 7+ Gen 3 and 8s Gen 3.",
    "phones": [
      {"brand": "OnePlus", "model": "OnePlus Nord 4", "year": 2024, "tier": "Premium Mid"},
      {"brand": "Realme", "model": "Realme GT Neo 6 SE", "year": 2024, "tier": "Performance Mid"},
      {"brand": "Sharp", "model": "Aquos R9", "year": 2024, "tier": "Midrange"}
    ]
  },
  {
    "id": "snapdragon-7-gen-3",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 7 Gen 3",
    "altName": "SM7550-AB",
    "tier": "Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "1x Cortex-A715 (2.63GHz) + 3x A715 + 4x A510",
    "gpu": "Adreno 720",
    "npu": "Hexagon NPU (60% AI boost)",
    "packaging": "ASE / Amkor",
    "modem": "Integrated Snapdragon X63 5G",
    "unitShare": 12,
    "revenueShare": 10,
    "bomCost": "$55 – $70",
    "bomAvg": 62,
    "riskLevel": "low",
    "riskLabel": "Stable supply",
    "filter": "qualcomm",
    "description": "The balanced powerhouse for modern stylish mid-range smartphones with excellent camera ISP and battery efficiency.",
    "strengths": [
      "50% faster GPU than 7 Gen 1 and 20% system power savings",
      "Popular choice for camera-focused portrait phones (Vivo V30/V40 series)"
    ],
    "risks": "Intense competition from MediaTek Dimensity 7200 and 7300.",
    "phones": [
      {"brand": "OnePlus", "model": "OnePlus Nord CE4", "year": 2024, "tier": "Midrange"},
      {"brand": "Vivo", "model": "Vivo V30", "year": 2024, "tier": "Camera Midrange"},
      {"brand": "Vivo", "model": "Vivo V40", "year": 2024, "tier": "Camera Midrange"},
      {"brand": "Motorola", "model": "Edge 50 Pro", "year": 2024, "tier": "Upper Midrange"},
      {"brand": "Honor", "model": "Honor 200", "year": 2024, "tier": "Upper Midrange"}
    ]
  },
  {
    "id": "snapdragon-7s-gen-2",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 7s Gen 2",
    "altName": "SM7435-AB",
    "tier": "Midrange",
    "model": "Merchant Fabless",
    "node": "Samsung 4nm (4LPP)",
    "foundry": "Samsung Foundry",
    "cpu": "4x Cortex-A78 (2.4GHz) + 4x Cortex-A55 (1.95GHz)",
    "gpu": "Adreno 710",
    "npu": "Qualcomm AI Engine",
    "packaging": "Samsung Packaging / ASE",
    "modem": "Integrated Snapdragon X62 5G",
    "unitShare": 18,
    "revenueShare": 12,
    "bomCost": "$40 – $52",
    "bomAvg": 46,
    "riskLevel": "medium",
    "riskLabel": "Samsung 4nm fab yields",
    "filter": "qualcomm",
    "description": "High-volume mid-range SoC manufactured on Samsung 4nm, adopted by Redmi and Realme for million-selling devices.",
    "strengths": [
      "Cost-effective 4nm option allowing OEMs to offer 200MP camera sensors and periscope lenses",
      "Very high volume shipments across Indian and European mid-tier markets"
    ],
    "risks": "Samsung 4LPP has lower power efficiency compared to TSMC N4P.",
    "phones": [
      {"brand": "Xiaomi", "model": "Redmi Note 13 Pro 5G", "year": 2024, "tier": "Midrange"},
      {"brand": "Realme", "model": "Realme 12 Pro+ 5G", "year": 2024, "tier": "Camera Midrange"},
      {"brand": "Realme", "model": "Realme 13 Pro+ 5G", "year": 2024, "tier": "Camera Midrange"},
      {"brand": "Motorola", "model": "Edge 50 Fusion", "year": 2024, "tier": "Midrange"},
      {"brand": "POCO", "model": "POCO X6 5G", "year": 2024, "tier": "Midrange"}
    ]
  },
  {
    "id": "snapdragon-778g",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 778G / 778G+",
    "altName": "SM7325",
    "tier": "Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 6nm (N6)",
    "foundry": "TSMC (100%)",
    "cpu": "4x Kryo 670 (Cortex-A78) + 4x Cortex-A55",
    "gpu": "Adreno 642L",
    "npu": "Hexagon 770 Processor",
    "packaging": "Amkor / ASE",
    "modem": "Integrated Snapdragon X53 5G",
    "unitShare": 20,
    "revenueShare": 15,
    "bomCost": "$36 – $45",
    "bomAvg": 40,
    "riskLevel": "low",
    "riskLabel": "Legendary yield maturity",
    "filter": "qualcomm",
    "description": "One of Qualcomm's most successful mid-range processors ever made, legendary for thermal stability, zero throttling, and reliable gaming performance.",
    "strengths": [
      "Perfect thermal-to-power curve on TSMC 6nm node",
      "Powered breakthrough devices like Nothing Phone (1) and Samsung Galaxy A52s"
    ],
    "risks": "Aging 6nm architecture gradually replaced by Snapdragon 7 Gen series.",
    "phones": [
      {"brand": "Nothing", "model": "Nothing Phone (1)", "year": 2022, "tier": "Design Midrange"},
      {"brand": "Samsung", "model": "Galaxy A52s 5G", "year": 2021, "tier": "Midrange"},
      {"brand": "Motorola", "model": "Edge 30", "year": 2022, "tier": "Midrange"},
      {"brand": "POCO", "model": "POCO X5 Pro 5G", "year": 2023, "tier": "Midrange"},
      {"brand": "Honor", "model": "Honor 50 / 60", "year": 2021, "tier": "Midrange"},
      {"brand": "Xiaomi", "model": "Xiaomi 11 Lite 5G NE", "year": 2021, "tier": "Slim Midrange"}
    ]
  },
  {
    "id": "snapdragon-6-gen-1",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 6 Gen 1",
    "altName": "SM6450",
    "tier": "Budget Midrange",
    "model": "Merchant Fabless",
    "node": "Samsung 4nm (4LPX)",
    "foundry": "Samsung Foundry",
    "cpu": "4x Cortex-A78 (2.2GHz) + 4x Cortex-A55 (1.8GHz)",
    "gpu": "Adreno 710",
    "npu": "Qualcomm AI Engine",
    "packaging": "Samsung / ASE",
    "modem": "Integrated Snapdragon X62 5G",
    "unitShare": 15,
    "revenueShare": 8,
    "bomCost": "$30 – $38",
    "bomAvg": 34,
    "riskLevel": "low",
    "riskLabel": "Samsung fab capacity",
    "filter": "qualcomm",
    "description": "Brings 4nm lithography and 4K HDR video capture down into affordable $200–$300 5G smartphones.",
    "strengths": [
      "Significant 35% GPU and 40% CPU improvement over Snapdragon 695",
      "Triple 12-bit Spectra ISP for multi-camera concurrent captures"
    ],
    "risks": "Samsung foundry node competition against TSMC 6nm alternatives.",
    "phones": [
      {"brand": "Sony", "model": "Xperia 10 VI", "year": 2024, "tier": "Midrange"},
      {"brand": "Honor", "model": "Magic6 Lite", "year": 2024, "tier": "Durable Midrange"},
      {"brand": "Realme", "model": "Realme 12 5G", "year": 2024, "tier": "Budget 5G"},
      {"brand": "Vivo", "model": "Vivo V30e", "year": 2024, "tier": "Slim Midrange"},
      {"brand": "Motorola", "model": "Moto G Stylus 5G (2023)", "year": 2023, "tier": "Stylus Midrange"}
    ]
  },
  {
    "id": "snapdragon-695",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 695 / 6s Gen 3",
    "altName": "SM6375",
    "tier": "Budget Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 6nm (N6)",
    "foundry": "TSMC (100%)",
    "cpu": "2x Cortex-A78 (2.2GHz) + 6x Cortex-A55 (1.8GHz)",
    "gpu": "Adreno 619",
    "npu": "Qualcomm Hexagon 686",
    "packaging": "Amkor / ASE",
    "modem": "Integrated Snapdragon X51 5G",
    "unitShare": 25,
    "revenueShare": 11,
    "bomCost": "$22 – $30",
    "bomAvg": 26,
    "riskLevel": "low",
    "riskLabel": "High maturity",
    "filter": "qualcomm",
    "description": "One of the world's most ubiquitous budget 5G processors. Re-released in 2024 as Snapdragon 6s Gen 3, extending its commercial lifespan past 4 years.",
    "strengths": [
      "Extremely cheap 5G turnkey platform for global carriers",
      "Exceptional battery life due to power-sipping TSMC 6nm node"
    ],
    "risks": "Lacks 4K video recording capability due to hardware ISP limitations.",
    "phones": [
      {"brand": "Motorola", "model": "Moto G85", "year": 2024, "tier": "Budget 5G"},
      {"brand": "Motorola", "model": "Moto G84 5G", "year": 2023, "tier": "Budget 5G"},
      {"brand": "OnePlus", "model": "OnePlus Nord CE 2 Lite 5G", "year": 2022, "tier": "Budget 5G"},
      {"brand": "OnePlus", "model": "OnePlus Nord CE 3 Lite 5G", "year": 2023, "tier": "Budget 5G"},
      {"brand": "POCO", "model": "POCO X4 Pro 5G", "year": 2022, "tier": "Budget 5G"},
      {"brand": "Xiaomi", "model": "Redmi Note 11 Pro 5G", "year": 2022, "tier": "Budget 5G"}
    ]
  },
  {
    "id": "snapdragon-4-gen-2",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 4 Gen 2",
    "altName": "SM4450",
    "tier": "Budget",
    "model": "Merchant Fabless",
    "node": "Samsung 4nm (4LPP)",
    "foundry": "Samsung Foundry",
    "cpu": "2x Cortex-A78 (2.2GHz) + 6x Cortex-A55 (2.0GHz)",
    "gpu": "Adreno 613",
    "npu": "Qualcomm AI Engine",
    "packaging": "Samsung / ASE",
    "modem": "Integrated Snapdragon X61 5G",
    "unitShare": 16,
    "revenueShare": 6,
    "bomCost": "$16 – $22",
    "bomAvg": 19,
    "riskLevel": "low",
    "riskLabel": "Budget volume",
    "filter": "qualcomm",
    "description": "Built to bring reliable 5G mobile broadband to sub-$150 smartphones in emerging markets across India, Southeast Asia, and Latin America.",
    "strengths": [
      "First 4nm processor in the budget Snapdragon 4-series",
      "Mass volume adoption in top-selling budget phones (Redmi 12 5G, POCO M6)"
    ],
    "risks": "Entry-level GPU limits gaming capabilities to casual 2D/3D titles.",
    "phones": [
      {"brand": "Xiaomi", "model": "Redmi 12 5G", "year": 2023, "tier": "Mass 5G"},
      {"brand": "Xiaomi", "model": "Redmi 13 5G", "year": 2024, "tier": "Mass 5G"},
      {"brand": "POCO", "model": "POCO M6 Pro 5G", "year": 2023, "tier": "Mass 5G"},
      {"brand": "POCO", "model": "POCO M6 Plus 5G", "year": 2024, "tier": "Mass 5G"},
      {"brand": "Vivo", "model": "Vivo Y200e 5G", "year": 2024, "tier": "Budget 5G"}
    ]
  },
  {
    "id": "snapdragon-680",
    "brand": "Qualcomm",
    "brandColor": "#f472b6",
    "name": "Snapdragon 680 / 685",
    "altName": "SM6225",
    "tier": "Budget",
    "model": "Merchant Fabless",
    "node": "TSMC 6nm (N6)",
    "foundry": "TSMC (100%)",
    "cpu": "4x Cortex-A73 (2.4GHz/2.8GHz) + 4x Cortex-A53",
    "gpu": "Adreno 610",
    "npu": "Hexagon 686",
    "packaging": "Amkor / ASE",
    "modem": "Integrated Snapdragon X11 LTE (4G)",
    "unitShare": 26,
    "revenueShare": 7,
    "bomCost": "$13 – $18",
    "bomAvg": 15,
    "riskLevel": "low",
    "riskLabel": "Mature 4G supply",
    "filter": "qualcomm",
    "description": "The king of dependable 4G smartphones, delivering multi-day battery endurance across millions of budget handsets worldwide.",
    "strengths": [
      "Ultra-low power drain on TSMC 6nm node",
      "Massive cost advantage for entry-level 4G markets"
    ],
    "risks": "4G only, gradually shrinking as 5G network coverage expands.",
    "phones": [
      {"brand": "Xiaomi", "model": "Redmi Note 13 4G", "year": 2024, "tier": "Budget 4G"},
      {"brand": "Xiaomi", "model": "Redmi Note 12 4G", "year": 2023, "tier": "Budget 4G"},
      {"brand": "Realme", "model": "Realme 9 4G", "year": 2022, "tier": "Budget 4G"},
      {"brand": "Vivo", "model": "Vivo Y36", "year": 2023, "tier": "Budget 4G"},
      {"brand": "Honor", "model": "Honor X7b", "year": 2024, "tier": "Budget 4G"},
      {"brand": "Motorola", "model": "Moto G32", "year": 2022, "tier": "Budget 4G"}
    ]
  },

  # ═══════════════════════════════════════════════════════════════════
  # 3. MEDIATEK DIMENSITY & HELIO
  # ═══════════════════════════════════════════════════════════════════
  {
    "id": "dimensity-9400",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Dimensity 9400",
    "altName": "MT6991",
    "tier": "Flagship",
    "model": "Merchant Fabless",
    "node": "TSMC 3nm (N3E)",
    "foundry": "TSMC (100%)",
    "cpu": "All-Big-Core (1x Cortex-X925 @ 3.63GHz + 3x Cortex-X4 @ 3.3GHz + 4x Cortex-A720 @ 2.4GHz)",
    "gpu": "Immortalis-G925 MC12 (Ray Tracing)",
    "npu": "NPU 890 (50 TOPS generative AI)",
    "packaging": "TSMC InFO / ASE",
    "modem": "Integrated MediaTek 5G Release-17",
    "unitShare": 37,
    "revenueShare": 17,
    "bomCost": "$125 – $145",
    "bomAvg": 135,
    "riskLevel": "medium",
    "riskLabel": "China OEM exposure",
    "filter": "mediatek",
    "description": "MediaTek's breakthrough second-generation All-Big-Core 3nm flagship processor, beating competitors in multi-core ray tracing and thermal efficiency while costing ~30% less than Qualcomm.",
    "strengths": [
      "All-Big-Core innovation eliminates small efficiency cores entirely for lower overall active energy",
      "First deployment of ARM Cortex-X925 core on advanced TSMC N3E node",
      "Tremendous commercial surge winning flagship designs across Vivo and Oppo",
      "World-record ray tracing frame rates in mobile gaming"
    ],
    "risks": "Heavily reliant on Chinese phone manufacturers (Vivo, Oppo, Xiaomi) for flagship sales volume.",
    "phones": [
      {"brand": "Vivo", "model": "Vivo X200 Pro", "year": 2024, "tier": "Ultra-Flagship"},
      {"brand": "Vivo", "model": "Vivo X200", "year": 2024, "tier": "Flagship"},
      {"brand": "Vivo", "model": "Vivo X200 Pro Mini", "year": 2024, "tier": "Compact Flagship"},
      {"brand": "Oppo", "model": "Find X8 Pro", "year": 2024, "tier": "Ultra-Flagship"},
      {"brand": "Oppo", "model": "Find X8", "year": 2024, "tier": "Flagship"},
      {"brand": "Xiaomi", "model": "Redmi K80 Pro", "year": 2024, "tier": "Flagship Killer"}
    ]
  },
  {
    "id": "dimensity-9300",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Dimensity 9300 / 9300+",
    "altName": "MT6989",
    "tier": "Flagship",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "All-Big-Core (1x Cortex-X4 @ 3.4GHz + 3x Cortex-X4 @ 2.85GHz + 4x Cortex-A720 @ 2.0GHz)",
    "gpu": "Immortalis-G720 MC12",
    "npu": "MediaTek APU 790 (45 TOPS)",
    "packaging": "TSMC InFO / ASE",
    "modem": "Integrated MediaTek 5G (Sub-6 + mmWave)",
    "unitShare": 20,
    "revenueShare": 16,
    "bomCost": "$105 – $125",
    "bomAvg": 115,
    "riskLevel": "medium",
    "riskLabel": "All-big thermal load",
    "filter": "mediatek",
    "description": "Pioneered the historic 'All-Big-Core' architecture with four Cortex-X4 and four Cortex-A720 cores, disproving industry skepticism about mobile thermals.",
    "strengths": [
      "Proved that large cache sizes and higher IPC reduce compute latency and save power",
      "Major commercial wins in Xiaomi 14T Pro and Vivo X100 Pro camera flagships"
    ],
    "risks": "Requires aggressive OEM vapor chamber cooling designs under prolonged multi-hour gaming.",
    "phones": [
      {"brand": "Vivo", "model": "Vivo X100 Pro", "year": 2023, "tier": "Ultra-Flagship"},
      {"brand": "Vivo", "model": "Vivo X100 / X100s", "year": 2023, "tier": "Flagship"},
      {"brand": "Xiaomi", "model": "Xiaomi 14T Pro", "year": 2024, "tier": "Flagship"},
      {"brand": "Xiaomi", "model": "Redmi K70 Ultra", "year": 2024, "tier": "Performance Flagship"},
      {"brand": "iQOO", "model": "iQOO Neo 9S Pro", "year": 2024, "tier": "Gaming Flagship"}
    ]
  },
  {
    "id": "dimensity-8300-ultra",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Dimensity 8300-Ultra",
    "altName": "MT6897",
    "tier": "Premium Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "4x Cortex-A715 (3.35GHz) + 4x Cortex-A510 (2.2GHz)",
    "gpu": "Mali-G615 MC6",
    "npu": "APU 780 (Generative AI)",
    "packaging": "ASE / Siliconware",
    "modem": "Integrated MediaTek 5G",
    "unitShare": 15,
    "revenueShare": 11,
    "bomCost": "$60 – $75",
    "bomAvg": 68,
    "riskLevel": "low",
    "riskLabel": "Cost-performance leader",
    "filter": "mediatek",
    "description": "The undisputed performance champion of the $300 price bracket, delivering 1.4 million AnTuTu benchmark scores in the POCO X6 Pro.",
    "strengths": [
      "Delivers previous-generation 8-series flagship performance at mid-range pricing",
      "Full support for LPDDR5X and generative AI diffusion models"
    ],
    "risks": "ARM Cortex licensing fees and OEM concentration in Xiaomi ecosystem.",
    "phones": [
      {"brand": "POCO", "model": "POCO X6 Pro 5G", "year": 2024, "tier": "Midrange Champ"},
      {"brand": "Xiaomi", "model": "Redmi K70E", "year": 2023, "tier": "Midrange"}
    ]
  },
  {
    "id": "dimensity-7300",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Dimensity 7300 / 7300X / Energy",
    "altName": "MT6878",
    "tier": "Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "4x Cortex-A78 (2.5GHz) + 4x Cortex-A55 (2.0GHz)",
    "gpu": "Mali-G615 MC2",
    "npu": "MediaTek NPU 655",
    "packaging": "ASE / SPIL",
    "modem": "Integrated MediaTek 5G",
    "unitShare": 19,
    "revenueShare": 10,
    "bomCost": "$36 – $46",
    "bomAvg": 41,
    "riskLevel": "low",
    "riskLabel": "High efficiency 4nm",
    "filter": "mediatek",
    "description": "MediaTek's breakthrough 4nm energy-efficient workhorse, powering trendy mid-range devices like the Nothing CMF Phone 1 and dual-screen Motorola Razr 50 flip phone.",
    "strengths": [
      "Up to 25% lower power consumption than previous 6nm mid-tier chips",
      "Custom 7300X variant with dual-display support for foldable flip screens",
      "Superb heat management in ultra-thin phone chassis"
    ],
    "risks": "Dual-core GPU limits high-refresh 3D gaming performance.",
    "phones": [
      {"brand": "Nothing", "model": "CMF Phone 1", "year": 2024, "tier": "Design Budget"},
      {"brand": "Motorola", "model": "Razr 50 (2024)", "year": 2024, "tier": "Flip Foldable"},
      {"brand": "Oppo", "model": "Reno 12 5G", "year": 2024, "tier": "Upper Midrange"},
      {"brand": "Oppo", "model": "Reno 12 Pro 5G", "year": 2024, "tier": "Upper Midrange"},
      {"brand": "Realme", "model": "Realme 13+ 5G", "year": 2024, "tier": "Midrange"}
    ]
  },
  {
    "id": "dimensity-7200",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Dimensity 7200 / 7200-Ultra",
    "altName": "MT6886",
    "tier": "Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 4nm (N4P)",
    "foundry": "TSMC (100%)",
    "cpu": "2x Cortex-A715 (2.8GHz) + 6x Cortex-A510 (2.0GHz)",
    "gpu": "Mali-G610 MC4",
    "npu": "MediaTek APU 650",
    "packaging": "ASE / SPIL",
    "modem": "Integrated MediaTek 5G",
    "unitShare": 18,
    "revenueShare": 9,
    "bomCost": "$34 – $44",
    "bomAvg": 39,
    "riskLevel": "low",
    "riskLabel": "Stable TSMC node",
    "filter": "mediatek",
    "description": "Powered high-profile hits like the Nothing Phone (2a) and Redmi Note 13 Pro+ 5G with flagship 4nm architecture in the $250–$350 segment.",
    "strengths": [
      "Modern ARMv9 Cortex-A715 architecture on refined TSMC 4nm",
      "ImMediaTek Imagiq 765 ISP supporting 200MP camera sensors",
      "Exceptional battery efficiency benchmarked in user tests"
    ],
    "risks": "Replaced gradually by 7300 generation.",
    "phones": [
      {"brand": "Nothing", "model": "Nothing Phone (2a)", "year": 2024, "tier": "Design Midrange"},
      {"brand": "Nothing", "model": "Nothing Phone (2a) Plus", "year": 2024, "tier": "Design Midrange"},
      {"brand": "Xiaomi", "model": "Redmi Note 13 Pro+ 5G", "year": 2024, "tier": "Camera Midrange"},
      {"brand": "Vivo", "model": "Vivo T2 Pro 5G", "year": 2023, "tier": "Slim Midrange"},
      {"brand": "iQOO", "model": "iQOO Z7 Pro 5G", "year": 2023, "tier": "Slim Midrange"}
    ]
  },
  {
    "id": "dimensity-7050",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Dimensity 7050 / 7020",
    "altName": "MT6877V",
    "tier": "Budget Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 6nm (N6)",
    "foundry": "TSMC (100%)",
    "cpu": "2x Cortex-A78 (2.6GHz) + 6x Cortex-A55 (2.0GHz)",
    "gpu": "Mali-G68 MC4",
    "npu": "MediaTek APU 3.0",
    "packaging": "ASE / Amkor",
    "modem": "Integrated MediaTek 5G",
    "unitShare": 22,
    "revenueShare": 9,
    "bomCost": "$26 – $34",
    "bomAvg": 30,
    "riskLevel": "low",
    "riskLabel": "Mature 6nm",
    "filter": "mediatek",
    "description": "Widely deployed processor delivering smooth 120Hz AMOLED displays and 5G connectivity for mainstream consumers.",
    "strengths": [
      "Proven TSMC 6nm production with virtually zero defect rate",
      "Turnkey reference design favored by Motorola, Realme, and Infinix"
    ],
    "risks": "A78 architecture getting older in 2025/2026.",
    "phones": [
      {"brand": "Realme", "model": "Realme 11 Pro 5G", "year": 2023, "tier": "Midrange"},
      {"brand": "Realme", "model": "Realme 12+ 5G", "year": 2024, "tier": "Midrange"},
      {"brand": "Motorola", "model": "Moto G54 5G", "year": 2023, "tier": "Budget 5G"},
      {"brand": "Motorola", "model": "Moto G73 5G", "year": 2023, "tier": "Budget 5G"},
      {"brand": "Infinix", "model": "Infinix Note 40 Pro 5G", "year": 2024, "tier": "Midrange"},
      {"brand": "Lava", "model": "Lava Agni 2 5G", "year": 2023, "tier": "Midrange"}
    ]
  },
  {
    "id": "dimensity-6300",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Dimensity 6300 / 6100+",
    "altName": "MT6835",
    "tier": "Budget",
    "model": "Merchant Fabless",
    "node": "TSMC 6nm (N6)",
    "foundry": "TSMC (100%)",
    "cpu": "2x Cortex-A76 (2.4GHz) + 6x Cortex-A55 (2.0GHz)",
    "gpu": "Mali-G57 MC2",
    "npu": "MediaTek NPU lite",
    "packaging": "ASE / UTAC",
    "modem": "Integrated MediaTek 5G UltraSave",
    "unitShare": 32,
    "revenueShare": 11,
    "bomCost": "$17 – $23",
    "bomAvg": 20,
    "riskLevel": "low",
    "riskLabel": "Volume driver",
    "filter": "mediatek",
    "description": "The backbone of entry-level $120–$160 5G smartphones, powering high-volume sales for Samsung, Realme, and Motorola.",
    "strengths": [
      "Sub-$20 BOM cost enables aggressive retail price cuts on 5G handsets",
      "MediaTek 5G UltraSave technology ensures all-day battery life"
    ],
    "risks": "Older Cortex-A76 cores limited in complex multi-tasking.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy A15 5G", "year": 2024, "tier": "Mass 5G"},
      {"brand": "Realme", "model": "Realme Narzo 70x 5G", "year": 2024, "tier": "Mass 5G"},
      {"brand": "Realme", "model": "Realme 12x 5G", "year": 2024, "tier": "Mass 5G"},
      {"brand": "Xiaomi", "model": "Redmi 13C 5G", "year": 2023, "tier": "Budget 5G"},
      {"brand": "Motorola", "model": "Moto G45 5G", "year": 2024, "tier": "Mass 5G"},
      {"brand": "POCO", "model": "POCO M6 5G", "year": 2023, "tier": "Mass 5G"}
    ]
  },
  {
    "id": "helio-g99",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Helio G99 / G99 Ultimate",
    "altName": "MT6789",
    "tier": "Budget",
    "model": "Merchant Fabless",
    "node": "TSMC 6nm (N6)",
    "foundry": "TSMC (100%)",
    "cpu": "2x Cortex-A76 (2.2GHz) + 6x Cortex-A55 (2.0GHz)",
    "gpu": "Mali-G57 MC2",
    "npu": "Integrated APU",
    "packaging": "ASE / Amkor",
    "modem": "Integrated 4G LTE Cat-13",
    "unitShare": 38,
    "revenueShare": 13,
    "bomCost": "$13 – $18",
    "bomAvg": 15,
    "riskLevel": "low",
    "riskLabel": "World 4G leader",
    "filter": "mediatek",
    "description": "The world's highest volume 4G smartphone processor of this decade, dominating budget devices worldwide with flawless 6nm reliability.",
    "strengths": [
      "Over 120 distinct smartphone models powered by Helio G99 across 2022-2025",
      "Tremendous profit margin generation for Transsion (Tecno/Infinix), Xiaomi, and Samsung",
      "Class-leading 4G gaming stability and thermal containment"
    ],
    "risks": "Lacks 5G modem support; transitioning to Dimensity 6300 as 5G takes over.",
    "phones": [
      {"brand": "Xiaomi", "model": "Redmi Note 13 4G", "year": 2024, "tier": "Budget 4G"},
      {"brand": "Samsung", "model": "Galaxy A15 4G", "year": 2024, "tier": "Budget 4G"},
      {"brand": "POCO", "model": "POCO M5", "year": 2022, "tier": "Budget 4G"},
      {"brand": "Infinix", "model": "Infinix Note 30 / 40", "year": 2023, "tier": "Budget 4G"},
      {"brand": "Tecno", "model": "Tecno Camon 20 Pro", "year": 2023, "tier": "Budget 4G"},
      {"brand": "Realme", "model": "Realme 11 4G", "year": 2023, "tier": "Budget 4G"},
      {"brand": "OnePlus", "model": "OnePlus Nord N30 SE", "year": 2024, "tier": "Budget 4G"}
    ]
  },
  {
    "id": "helio-g85",
    "brand": "MediaTek",
    "brandColor": "#fbbf24",
    "name": "Helio G85 / G88",
    "altName": "MT6769V",
    "tier": "Budget",
    "model": "Merchant Fabless",
    "node": "TSMC 12nm (FinFET)",
    "foundry": "TSMC (100%)",
    "cpu": "2x Cortex-A75 (2.0GHz) + 6x Cortex-A55 (1.8GHz)",
    "gpu": "Mali-G52 MC2",
    "npu": "Basic hardware acceleration",
    "packaging": "ASE / SPIL",
    "modem": "Integrated 4G LTE Cat-7",
    "unitShare": 30,
    "revenueShare": 7,
    "bomCost": "$9 – $13",
    "bomAvg": 11,
    "riskLevel": "low",
    "riskLabel": "Legacy 12nm node",
    "filter": "mediatek",
    "description": "Mass-market entry silicon powering smartphones priced under $100 across developing economies.",
    "strengths": [
      "Extremely affordable 12nm pricing with high volume yields",
      "Reliable core everyday functionality for millions of first-time smartphone owners"
    ],
    "risks": "12nm lithography exhibits higher heat dissipation under heavy sustained usage.",
    "phones": [
      {"brand": "Xiaomi", "model": "Redmi 12 4G", "year": 2023, "tier": "Entry Budget"},
      {"brand": "Xiaomi", "model": "Redmi 13C 4G", "year": 2023, "tier": "Entry Budget"},
      {"brand": "Motorola", "model": "Moto G23", "year": 2023, "tier": "Entry Budget"},
      {"brand": "Realme", "model": "Realme C25s", "year": 2021, "tier": "Entry Budget"},
      {"brand": "POCO", "model": "POCO C65", "year": 2023, "tier": "Entry Budget"},
      {"brand": "Infinix", "model": "Infinix Hot 30", "year": 2023, "tier": "Entry Budget"}
    ]
  },

  # ═══════════════════════════════════════════════════════════════════
  # 4. SAMSUNG EXYNOS
  # ═══════════════════════════════════════════════════════════════════
  {
    "id": "exynos-2500",
    "brand": "Samsung",
    "brandColor": "#38bdf8",
    "name": "Exynos 2500",
    "altName": "Exynos 2500 GAA",
    "tier": "Flagship",
    "model": "Hybrid IDM",
    "node": "Samsung 3nm GAA (SF3)",
    "foundry": "Samsung Foundry",
    "cpu": "10-core (Cortex-X5 + Cortex-A730 + Cortex-A520)",
    "gpu": "Xclipse 950 (AMD RDNA 3.5)",
    "npu": "Samsung NPU (Dual Core, 55 TOPS)",
    "packaging": "Samsung FOWLP",
    "modem": "Integrated Exynos 5G (Release-17)",
    "unitShare": 5,
    "revenueShare": 5,
    "bomCost": "$100 – $120",
    "bomAvg": 110,
    "riskLevel": "high",
    "riskLabel": "3nm GAA fab yield ramp",
    "filter": "samsung",
    "description": "Samsung's first flagship mobile processor manufactured on 3nm Gate-All-Around (GAA) MBCFET transistor technology, featuring custom AMD RDNA 3.5 graphics.",
    "strengths": [
      "First mobile chip to adopt Gate-All-Around (GAA) architecture over traditional FinFET",
      "AMD RDNA 3.5 graphics co-engineering provides excellent mobile ray tracing support",
      "Vertical integration with Samsung's internal LPDDR5X DRAM and UFS 4.0 flash divisions"
    ],
    "risks": "Early 3nm GAA wafer yields (below 40% initially) forced Samsung MX to rely primarily on Qualcomm for the Galaxy S25 Ultra.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy S25 (Regional)", "year": 2025, "tier": "Flagship"},
      {"brand": "Samsung", "model": "Galaxy S25+ (Regional)", "year": 2025, "tier": "Flagship"}
    ]
  },
  {
    "id": "exynos-2400",
    "brand": "Samsung",
    "brandColor": "#38bdf8",
    "name": "Exynos 2400 / 2400e",
    "altName": "S5E9945",
    "tier": "Flagship",
    "model": "Hybrid IDM",
    "node": "Samsung 4nm (4LPP+)",
    "foundry": "Samsung Foundry",
    "cpu": "10-core (1x Cortex-X4 @ 3.2GHz + 5x A720 + 4x A520)",
    "gpu": "Xclipse 940 (AMD RDNA 3)",
    "npu": "Samsung NPU (17K MAC)",
    "packaging": "Samsung FOWLP (Fan-Out Wafer Level Packaging)",
    "modem": "Integrated Exynos 5300 5G",
    "unitShare": 7,
    "revenueShare": 7,
    "bomCost": "$95 – $115",
    "bomAvg": 105,
    "riskLevel": "medium",
    "riskLabel": "Regional dual-sourcing",
    "filter": "samsung",
    "description": "Successfully marked the return of Exynos silicon to Samsung flagships, powering the Galaxy S24 and S24+ in Europe and Asia with FOWLP thermal packaging.",
    "strengths": [
      "Fan-Out Wafer-Level Packaging (FOWLP) significantly improved heat dissipation",
      "Competitive 10-core configuration matched Snapdragon 8 Gen 3 in real-world benchmarks",
      "Powering Galaxy AI suite features directly on-device"
    ],
    "risks": "Consumer perception in select markets still prefers Qualcomm Snapdragon variants.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy S24 (Europe/Global)", "year": 2024, "tier": "Flagship"},
      {"brand": "Samsung", "model": "Galaxy S24+ (Europe/Global)", "year": 2024, "tier": "Flagship"},
      {"brand": "Samsung", "model": "Galaxy S24 FE", "year": 2024, "tier": "Flagship Lite"}
    ]
  },
  {
    "id": "exynos-2200",
    "brand": "Samsung",
    "brandColor": "#38bdf8",
    "name": "Exynos 2200",
    "altName": "S5E9925",
    "tier": "Flagship",
    "model": "Hybrid IDM",
    "node": "Samsung 4nm (4LPE)",
    "foundry": "Samsung Foundry",
    "cpu": "8-core (1x Cortex-X2 + 3x A710 + 4x A510)",
    "gpu": "Xclipse 920 (AMD RDNA 2)",
    "npu": "Dual NPU",
    "packaging": "Samsung Packaging",
    "modem": "Integrated Exynos 5123 5G",
    "unitShare": 6,
    "revenueShare": 6,
    "bomCost": "$80 – $95",
    "bomAvg": 88,
    "riskLevel": "high",
    "riskLabel": "4LPE thermal throttling",
    "filter": "samsung",
    "description": "First mobile chip to debut an AMD RDNA 2 GPU on a smartphone, later repurposed with refined thermals in the Galaxy S23 FE.",
    "strengths": [
      "Pioneered hardware-accelerated ray tracing in Android before any other chipmaker",
      "Repurposed successfully for high-margin Galaxy S23 FE distribution"
    ],
    "risks": "Suffered from thermal throttling on initial Samsung 4LPE fab node.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy S22 Ultra (Europe)", "year": 2022, "tier": "Ultra-Flagship"},
      {"brand": "Samsung", "model": "Galaxy S22 / S22+ (Europe)", "year": 2022, "tier": "Flagship"},
      {"brand": "Samsung", "model": "Galaxy S23 FE (Global)", "year": 2023, "tier": "Fan Edition"}
    ]
  },
  {
    "id": "exynos-1480",
    "brand": "Samsung",
    "brandColor": "#38bdf8",
    "name": "Exynos 1480 / 1580",
    "altName": "S5E8845",
    "tier": "Upper Midrange",
    "model": "Hybrid IDM",
    "node": "Samsung 4nm (4LPP)",
    "foundry": "Samsung Foundry",
    "cpu": "4x Cortex-A78 (2.75GHz) + 4x Cortex-A55 (2.05GHz)",
    "gpu": "Xclipse 530 (AMD RDNA Architecture)",
    "npu": "Samsung 4-core NPU",
    "packaging": "Samsung Packaging",
    "modem": "Integrated Exynos 5G (Sub-6 + mmWave)",
    "unitShare": 12,
    "revenueShare": 8,
    "bomCost": "$42 – $52",
    "bomAvg": 47,
    "riskLevel": "low",
    "riskLabel": "High yield stability",
    "filter": "samsung",
    "description": "Brought AMD Xclipse graphics to Samsung's premier mid-range phone, the Galaxy A55 5G, delivering 53% higher GPU performance.",
    "strengths": [
      "First mid-range chip to incorporate AMD RDNA graphics architecture",
      "Substantial 30% battery efficiency gains on mature Samsung 4LPP",
      "Best-selling premium mid-ranger across Europe and Southeast Asia"
    ],
    "risks": "Confined almost exclusively to Samsung's own Galaxy A-series lineup.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy A55 5G", "year": 2024, "tier": "Upper Midrange"},
      {"brand": "Samsung", "model": "Galaxy A56 5G", "year": 2025, "tier": "Upper Midrange"}
    ]
  },
  {
    "id": "exynos-1380",
    "brand": "Samsung",
    "brandColor": "#38bdf8",
    "name": "Exynos 1380",
    "altName": "S5E8835",
    "tier": "Midrange",
    "model": "Hybrid IDM",
    "node": "Samsung 5nm (5LPE)",
    "foundry": "Samsung Foundry",
    "cpu": "4x Cortex-A78 (2.4GHz) + 4x Cortex-A55 (2.0GHz)",
    "gpu": "Mali-G68 MP5",
    "npu": "Triple NPU (4.9 TOPS)",
    "packaging": "Samsung Packaging",
    "modem": "Integrated Exynos 5G",
    "unitShare": 16,
    "revenueShare": 9,
    "bomCost": "$32 – $40",
    "bomAvg": 36,
    "riskLevel": "low",
    "riskLabel": "Mature 5nm",
    "filter": "samsung",
    "description": "Mass-market 5nm mid-range SoC powering millions of Galaxy A54 and M-series phones and Galaxy Tab S9 FE tablets.",
    "strengths": [
      "Equipped with 4 performance cores (up from 2 in Exynos 1280)",
      "Supports 120Hz displays and 4K 30fps stabilization"
    ],
    "risks": "Mali-G68 GPU struggles under sustained intense gaming sessions.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy A54 5G", "year": 2023, "tier": "Midrange"},
      {"brand": "Samsung", "model": "Galaxy M54 5G", "year": 2023, "tier": "Midrange"},
      {"brand": "Samsung", "model": "Galaxy F54 5G", "year": 2023, "tier": "Midrange"},
      {"brand": "Samsung", "model": "Galaxy Tab S9 FE", "year": 2023, "tier": "Tablet"}
    ]
  },
  {
    "id": "exynos-1280",
    "brand": "Samsung",
    "brandColor": "#38bdf8",
    "name": "Exynos 1280",
    "altName": "S5E8825",
    "tier": "Budget Midrange",
    "model": "Hybrid IDM",
    "node": "Samsung 5nm (5LPE)",
    "foundry": "Samsung Foundry",
    "cpu": "2x Cortex-A78 (2.4GHz) + 6x Cortex-A55 (2.0GHz)",
    "gpu": "Mali-G68 MP4",
    "npu": "Dual NPU",
    "packaging": "Samsung Packaging",
    "modem": "Integrated Exynos 5G",
    "unitShare": 14,
    "revenueShare": 7,
    "bomCost": "$24 – $30",
    "bomAvg": 27,
    "riskLevel": "low",
    "riskLabel": "High amortized margin",
    "filter": "samsung",
    "description": "Reliable 5nm silicon deployed across Samsung's volume-driving A33, A53, and newer A25 5G smartphones.",
    "strengths": [
      "Turnkey internal cost advantage for Samsung's budget 5G portfolio",
      "Extended software update compatibility for 4 generations of Android"
    ],
    "risks": "Modest CPU multi-core score compared to newer Dimensity alternatives.",
    "phones": [
      {"brand": "Samsung", "model": "Galaxy A25 5G", "year": 2024, "tier": "Budget 5G"},
      {"brand": "Samsung", "model": "Galaxy A53 5G", "year": 2022, "tier": "Midrange"},
      {"brand": "Samsung", "model": "Galaxy A33 5G", "year": 2022, "tier": "Budget 5G"},
      {"brand": "Samsung", "model": "Galaxy M33 5G", "year": 2022, "tier": "Budget 5G"}
    ]
  },

  # ═══════════════════════════════════════════════════════════════════
  # 5. GOOGLE TENSOR
  # ═══════════════════════════════════════════════════════════════════
  {
    "id": "tensor-g5",
    "brand": "Google",
    "brandColor": "#34d399",
    "name": "Tensor G5",
    "altName": "Laguna SoC",
    "tier": "Flagship",
    "model": "Captive Fabless",
    "node": "TSMC 3nm (N3E)",
    "foundry": "TSMC (Switched from Samsung)",
    "cpu": "Custom Google ARMv9 (1x Cortex-X4 + 5x A725 + 2x A520)",
    "gpu": "Imagination Technologies DXT GPU",
    "npu": "Google Edge TPU 5th Gen (Gemini Nano on-device)",
    "packaging": "TSMC InFO",
    "modem": "Integrated / External 5G Modem",
    "unitShare": 1.8,
    "revenueShare": 1.2,
    "bomCost": "$95 – $115",
    "bomAvg": 105,
    "riskLevel": "medium",
    "riskLabel": "New TSMC design transition",
    "filter": "google",
    "description": "Google's first fully custom in-house mobile silicon manufactured on TSMC 3nm, severing ties with Samsung Foundry co-design for complete architectural autonomy.",
    "strengths": [
      "Switch to TSMC 3nm resolves all historic thermal and modem battery-drain complaints",
      "Custom 5th Gen TPU optimized to run multimodal Gemini Nano models on-device",
      "Full hardware pipeline control for Google Pixel camera algorithms"
    ],
    "risks": "Small unit scale (~2% share) limits foundry volume discounting compared to Apple and Qualcomm.",
    "phones": [
      {"brand": "Google", "model": "Pixel 10 Pro XL", "year": 2025, "tier": "Ultra-Flagship"},
      {"brand": "Google", "model": "Pixel 10 Pro", "year": 2025, "tier": "Flagship"},
      {"brand": "Google", "model": "Pixel 10", "year": 2025, "tier": "Flagship"}
    ]
  },
  {
    "id": "tensor-g4",
    "brand": "Google",
    "brandColor": "#34d399",
    "name": "Tensor G4",
    "altName": "Zumapro",
    "tier": "Flagship",
    "model": "Captive Fabless",
    "node": "Samsung 4nm (4LPP+)",
    "foundry": "Samsung Foundry",
    "cpu": "8-core (1x Cortex-X4 @ 3.1GHz + 3x A720 + 4x A520)",
    "gpu": "Mali-G715 MP7",
    "npu": "Google Edge TPU (45 TOPS)",
    "packaging": "Samsung FOWLP",
    "modem": "Samsung Exynos 5400 5G (Satellite SOS)",
    "unitShare": 1.5,
    "revenueShare": 1.1,
    "bomCost": "$90 – $105",
    "bomAvg": 98,
    "riskLevel": "medium",
    "riskLabel": "Modem power consumption",
    "filter": "google",
    "description": "Co-designed with Google DeepMind to deliver the fastest multimodal on-device AI token processing on a smartphone in the Pixel 9 series.",
    "strengths": [
      "First mobile chip engineered from ground up for Gemini Nano multimodal processing",
      "Satellite SOS messaging capability enabled by new Exynos 5400 modem",
      "FOWLP packaging drastically reduced idle temperatures compared to Pixel 8"
    ],
    "risks": "Peak raw graphics benchmark scores lag behind Qualcomm Snapdragon 8 Gen 3.",
    "phones": [
      {"brand": "Google", "model": "Pixel 9 Pro XL", "year": 2024, "tier": "Ultra-Flagship"},
      {"brand": "Google", "model": "Pixel 9 Pro", "year": 2024, "tier": "Ultra-Flagship"},
      {"brand": "Google", "model": "Pixel 9", "year": 2024, "tier": "Flagship"},
      {"brand": "Google", "model": "Pixel 9 Pro Fold", "year": 2024, "tier": "Foldable Flagship"}
    ]
  },
  {
    "id": "tensor-g3",
    "brand": "Google",
    "brandColor": "#34d399",
    "name": "Tensor G3",
    "altName": "Zuma",
    "tier": "Flagship",
    "model": "Captive Fabless",
    "node": "Samsung 4nm (4LPP)",
    "foundry": "Samsung Foundry",
    "cpu": "9-core (1x Cortex-X3 + 4x A715 + 4x A510)",
    "gpu": "Mali-G715 with Ray Tracing",
    "npu": "Google Edge TPU 3rd Gen",
    "packaging": "Samsung FOWLP",
    "modem": "Samsung Exynos 5300 5G",
    "unitShare": 1.4,
    "revenueShare": 1.0,
    "bomCost": "$80 – $95",
    "bomAvg": 88,
    "riskLevel": "medium",
    "riskLabel": "Samsung 4nm thermals",
    "filter": "google",
    "description": "Introduced Best Take, Audio Magic Eraser, and on-device generative voice transcription for the Pixel 8 generation.",
    "strengths": [
      "Unique 9-core architecture designed specifically for AI workflow concurrency",
      "Enables 7 years of full Android OS updates on Pixel 8 hardware"
    ],
    "risks": "Thermal throttling observed during 4K 60fps recording in direct sunlight.",
    "phones": [
      {"brand": "Google", "model": "Pixel 8 Pro", "year": 2023, "tier": "Ultra-Flagship"},
      {"brand": "Google", "model": "Pixel 8", "year": 2023, "tier": "Flagship"},
      {"brand": "Google", "model": "Pixel 8a", "year": 2024, "tier": "Affordable Flagship"}
    ]
  },
  {
    "id": "tensor-g2",
    "brand": "Google",
    "brandColor": "#34d399",
    "name": "Tensor G2",
    "altName": "Cloudripper",
    "tier": "Premium",
    "model": "Captive Fabless",
    "node": "Samsung 5nm (5LPE)",
    "foundry": "Samsung Foundry",
    "cpu": "2x Cortex-X1 (2.85GHz) + 2x A78 + 4x A55",
    "gpu": "Mali-G710 MP7",
    "npu": "Google Edge TPU 2nd Gen",
    "packaging": "Samsung Packaging",
    "modem": "Samsung Exynos 5300 5G",
    "unitShare": 1.3,
    "revenueShare": 0.9,
    "bomCost": "$65 – $80",
    "bomAvg": 72,
    "riskLevel": "low",
    "riskLabel": "Mature generation",
    "filter": "google",
    "description": "Refined the dual-Cortex-X1 architecture to power Photo Unblur, Cinematic Blur, and Real Tone algorithms in Pixel 7.",
    "strengths": [
      "Dual prime core setup excels at burst machine learning inference",
      "Powering Google's first foldable device (Pixel Fold)"
    ],
    "risks": "Higher battery consumption on cellular networks compared to Qualcomm X65/X70.",
    "phones": [
      {"brand": "Google", "model": "Pixel 7 Pro", "year": 2022, "tier": "Flagship"},
      {"brand": "Google", "model": "Pixel 7", "year": 2022, "tier": "Flagship"},
      {"brand": "Google", "model": "Pixel 7a", "year": 2023, "tier": "Midrange"},
      {"brand": "Google", "model": "Pixel Fold", "year": 2023, "tier": "Foldable"},
      {"brand": "Google", "model": "Pixel Tablet", "year": 2023, "tier": "Tablet"}
    ]
  },

  # ═══════════════════════════════════════════════════════════════════
  # 6. HISILICON (HUAWEI)
  # ═══════════════════════════════════════════════════════════════════
  {
    "id": "kirin-9010",
    "brand": "HiSilicon (Huawei)",
    "brandColor": "#fb923c",
    "name": "Kirin 9010",
    "altName": "Hi36A0",
    "tier": "Flagship",
    "model": "Captive Fabless (Sanctioned)",
    "node": "SMIC 7nm DUV Multi-pattern (N+2)",
    "foundry": "SMIC (China Domestic)",
    "cpu": "Custom Taishan (12-thread: 1x 2.3GHz + 3x 2.18GHz + 4x 1.55GHz)",
    "gpu": "Maleoon 910 MP4 (Huawei In-house)",
    "npu": "DaVinci NPU (Dual Big Core + Micro Core)",
    "packaging": "JCET / Domestic Chinese OSAT",
    "modem": "Integrated Balong 5G with Beidou Satellite Calling",
    "unitShare": 3.2,
    "revenueShare": 3.5,
    "bomCost": "$140+ estimated",
    "bomAvg": 145,
    "riskLevel": "critical",
    "riskLabel": "ASML EUV export embargo",
    "filter": "hisilicon",
    "description": "Huawei's technological sovereignty symbol, manufactured completely within China without Western equipment access. Features simultaneous satellite telephony voice calling in the Pura 70 series.",
    "strengths": [
      "Proved domestic Chinese semiconductor viability under severe US Entity List sanctions",
      "Seamless integration with HarmonyOS NEXT bare-metal microkernel",
      "Direct satellite voice and image communication via Tiantong-1 and Beidou satellites"
    ],
    "risks": "Absence of ASML EUV lithography forces SMIC into DUV multi-patterning (SAQP), resulting in high defect rates, low wafer throughput, and estimated costs exceeding $140/die.",
    "phones": [
      {"brand": "Huawei", "model": "Pura 70 Ultra", "year": 2024, "tier": "Ultra-Flagship"},
      {"brand": "Huawei", "model": "Pura 70 Pro", "year": 2024, "tier": "Flagship"},
      {"brand": "Huawei", "model": "Pura 70 Pro+", "year": 2024, "tier": "Flagship"}
    ]
  },
  {
    "id": "kirin-9000s",
    "brand": "HiSilicon (Huawei)",
    "brandColor": "#fb923c",
    "name": "Kirin 9000s",
    "altName": "Hi36A0-S",
    "tier": "Flagship",
    "model": "Captive Fabless (Sanctioned)",
    "node": "SMIC 7nm (N+2)",
    "foundry": "SMIC (China Domestic)",
    "cpu": "Custom Taishan (8-core / 12-thread: 1x 2.62GHz + 3x 2.15GHz + 4x 1.53GHz)",
    "gpu": "Maleoon 910",
    "npu": "DaVinci NPU",
    "packaging": "JCET",
    "modem": "Integrated Balong 5G",
    "unitShare": 2.8,
    "revenueShare": 3.0,
    "bomCost": "$135 – $150",
    "bomAvg": 142,
    "riskLevel": "critical",
    "riskLabel": "Sanctions & low yield",
    "filter": "hisilicon",
    "description": "The historic chip that shocked global geopolitical analysts in August 2023 when Huawei launched the Mate 60 Pro with full 5G speeds despite stringent export bans.",
    "strengths": [
      "Custom Taishan CPU architecture implementing multi-threading (SMT) on mobile",
      "Catalyzed $47.5 Billion China Big Fund III for domestic semiconductor tooling"
    ],
    "risks": "Low wafer throughput and thermal inefficiency compared to TSMC 3nm.",
    "phones": [
      {"brand": "Huawei", "model": "Mate 60 Pro", "year": 2023, "tier": "Ultra-Flagship"},
      {"brand": "Huawei", "model": "Mate 60", "year": 2023, "tier": "Flagship"},
      {"brand": "Huawei", "model": "Mate 60 Pro+", "year": 2023, "tier": "Ultra-Flagship"},
      {"brand": "Huawei", "model": "Mate X5", "year": 2023, "tier": "Foldable Flagship"}
    ]
  },
  {
    "id": "kirin-9000",
    "brand": "HiSilicon (Huawei)",
    "brandColor": "#fb923c",
    "name": "Kirin 9000 / 9000E",
    "altName": "Hi36A0 TSMC",
    "tier": "Flagship",
    "model": "Captive Fabless (Pre-Sanction)",
    "node": "TSMC 5nm (N5)",
    "foundry": "TSMC (Stockpiled before Sept 2020 ban)",
    "cpu": "1x Cortex-A77 (3.13GHz) + 3x A77 + 4x A55",
    "gpu": "Mali-G78 MP24 (24 cores)",
    "npu": "DaVinci NPU (Dual Big Core + 1 Tiny)",
    "packaging": "TSMC InFO",
    "modem": "Integrated Balong 5000 5G",
    "unitShare": 2.0,
    "revenueShare": 2.2,
    "bomCost": "$110 – $130",
    "bomAvg": 120,
    "riskLevel": "critical",
    "riskLabel": "Exhausted stockpiles",
    "filter": "hisilicon",
    "description": "The world's first 5nm 5G SoC ever released, stockpiled in massive volume (estimated 10-15 million units) before the US cut off TSMC manufacturing on September 15, 2020.",
    "strengths": [
      "World's first commercial integrated 5nm 5G SoC",
      "Legendary Mali-G78 24-core GPU delivered astonishing gaming efficiency"
    ],
    "risks": "Stockpiles fully exhausted; can never be manufactured again at TSMC.",
    "phones": [
      {"brand": "Huawei", "model": "Mate 40 Pro", "year": 2020, "tier": "Ultra-Flagship"},
      {"brand": "Huawei", "model": "P50 Pro", "year": 2021, "tier": "Ultra-Flagship"},
      {"brand": "Huawei", "model": "MatePad Pro 12.6", "year": 2021, "tier": "Tablet"}
    ]
  },

  # ═══════════════════════════════════════════════════════════════════
  # 7. UNISOC
  # ═══════════════════════════════════════════════════════════════════
  {
    "id": "unisoc-t820",
    "brand": "Unisoc",
    "brandColor": "#38bdf8",
    "name": "Unisoc T820 / T760",
    "altName": "UMS9620",
    "tier": "Budget Midrange",
    "model": "Merchant Fabless",
    "node": "TSMC 6nm (EUV)",
    "foundry": "TSMC (100%)",
    "cpu": "1x Cortex-A76 (2.7GHz) + 3x A76 (2.3GHz) + 4x A55 (2.1GHz)",
    "gpu": "Mali-G57 MC4",
    "npu": "NPU (4.8 TOPS)",
    "packaging": "JCET / ASE",
    "modem": "Integrated Unisoc 5G Sub-6",
    "unitShare": 4.5,
    "revenueShare": 2.0,
    "bomCost": "$24 – $32",
    "bomAvg": 28,
    "riskLevel": "low",
    "riskLabel": "TSMC mature EUV",
    "filter": "unisoc",
    "description": "Unisoc's premier 5G platform built on TSMC 6nm EUV, enabling budget gaming phones like the Nubia Neo 5G and HMD Crest 5G with 108MP camera capture.",
    "strengths": [
      "Brings 5G and 120Hz display refresh rates into the sub-$180 price segment",
      "TSMC 6nm EUV manufacturing provides reliable power efficiency"
    ],
    "risks": "Smaller developer and custom ROM support community compared to Qualcomm.",
    "phones": [
      {"brand": "Nubia", "model": "Nubia Neo 5G", "year": 2023, "tier": "Budget Gaming"},
      {"brand": "Nubia", "model": "Nubia Focus 5G / Pro", "year": 2024, "tier": "Budget Camera"},
      {"brand": "HMD", "model": "HMD Crest 5G", "year": 2024, "tier": "Budget 5G"},
      {"brand": "HMD", "model": "HMD Crest Max 5G", "year": 2024, "tier": "Budget 5G"},
      {"brand": "Teclast", "model": "Teclast T50 Pro", "year": 2023, "tier": "Tablet"}
    ]
  },
  {
    "id": "unisoc-t606",
    "brand": "Unisoc",
    "brandColor": "#38bdf8",
    "name": "Unisoc T606 / T616",
    "altName": "UMS9230",
    "tier": "Budget",
    "model": "Merchant Fabless",
    "node": "TSMC 12nm (FinFET)",
    "foundry": "TSMC (100%)",
    "cpu": "2x Cortex-A75 (1.6 - 2.0GHz) + 6x Cortex-A55 (1.6 - 1.8GHz)",
    "gpu": "Mali-G57 MP1",
    "npu": "Software AI acceleration",
    "packaging": "JCET / UTAC",
    "modem": "Integrated 4G LTE Cat-7",
    "unitShare": 18,
    "revenueShare": 4,
    "bomCost": "$9 – $14",
    "bomAvg": 11,
    "riskLevel": "low",
    "riskLabel": "Entry volume king",
    "filter": "unisoc",
    "description": "The foundation of sub-$100 smartphones globally. Powers hundreds of millions of ultra-budget devices from Motorola, Realme, Infinix, Tecno, and itel.",
    "strengths": [
      "Incredible price-to-performance ratio enabling sub-$80 smartphone pricing",
      "Proven TSMC 12nm supply chain with abundant wafer capacity"
    ],
    "risks": "Entry-level single core GPU limits modern high-frame-rate games.",
    "phones": [
      {"brand": "Motorola", "model": "Moto E13", "year": 2023, "tier": "Ultra Budget"},
      {"brand": "Motorola", "model": "Moto G04 / G04s", "year": 2024, "tier": "Ultra Budget"},
      {"brand": "Realme", "model": "Realme C53 / C51", "year": 2023, "tier": "Entry Budget"},
      {"brand": "Realme", "model": "Realme C35", "year": 2022, "tier": "Entry Budget"},
      {"brand": "Infinix", "model": "Infinix Smart 8 / 8 HD", "year": 2023, "tier": "Ultra Budget"},
      {"brand": "Tecno", "model": "Tecno Spark Go 2024", "year": 2024, "tier": "Ultra Budget"},
      {"brand": "itel", "model": "itel S23 / P55+", "year": 2023, "tier": "Ultra Budget"},
      {"brand": "HMD / Nokia", "model": "Nokia G22", "year": 2023, "tier": "Repairable Budget"}
    ]
  }
]


def get_all_processors():
    return PROCESSORS_DATA

def get_processor_by_id(proc_id: str):
    for p in PROCESSORS_DATA:
        if p["id"] == proc_id:
            return p
    return None

def get_all_phones():
    phones_list = []
    for p in PROCESSORS_DATA:
        for ph in p.get("phones", []):
            phones_list.append({
                "model": ph["model"],
                "brand": ph["brand"],
                "year": ph["year"],
                "tier": ph["tier"],
                "processorId": p["id"],
                "processorName": p["name"],
                "processorBrand": p["brand"],
                "processorNode": p["node"],
                "processorFoundry": p["foundry"]
            })
    return phones_list

def search_phones_and_processors(query: str):
    q = query.lower().strip()
    matched_processors = []
    matched_phones = []

    for p in PROCESSORS_DATA:
        # Check if processor matches
        proc_match = (
            q in p["name"].lower() or
            q in p["brand"].lower() or
            q in p.get("altName", "").lower() or
            q in p.get("node", "").lower() or
            q in p.get("cpu", "").lower() or
            q in p.get("tier", "").lower()
        )
        
        # Check if any phone inside processor matches
        phone_matches = []
        for ph in p.get("phones", []):
            if q in ph["model"].lower() or q in ph["brand"].lower():
                phone_matches.append({
                    "model": ph["model"],
                    "brand": ph["brand"],
                    "year": ph["year"],
                    "tier": ph["tier"],
                    "processorId": p["id"],
                    "processorName": p["name"]
                })
        
        if proc_match or phone_matches:
            matched_processors.append(p)
            matched_phones.extend(phone_matches)
            
    return {
        "query": query,
        "matchedProcessors": matched_processors,
        "matchedPhones": matched_phones,
        "count": len(matched_processors)
    }
