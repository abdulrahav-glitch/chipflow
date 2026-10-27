/* ═══════════════════════════════════════════════════════════════════
   ChipFlow — App Logic, Data, Charts, Search & Interactions
   ═══════════════════════════════════════════════════════════════════ */

// ─── PROCESSOR DATA ───
const PROCESSORS = [
  {
    id: 'apple-a18-pro',
    brand: 'Apple',
    brandColor: '#a78bfa',
    name: 'A18 Pro',
    altName: 'A17 Pro',
    model: 'Captive Fabless',
    node: 'TSMC 3nm (N3B / N3E)',
    foundry: 'TSMC (100%)',
    cpu: 'Custom Apple ARMv9',
    packaging: 'TSMC InFO-PoP',
    modem: 'External Qualcomm 5G',
    unitShare: 18,
    revenueShare: 38,
    bomCost: '$110 – $135',
    bomAvg: 122,
    riskLevel: 'critical',
    riskLabel: 'Single-source Taiwan',
    filter: 'apple',
    description: 'Apple captures ~38% of global smartphone SoC revenue with just 18% unit share. Silicon strategy is holistic: chips are engineered to maximize iOS feature integration, computational photography, battery runtime, and Apple Intelligence.',
    strengths: [
      'Preferential TSMC "Alpha Customer" status — first access to every new node',
      'Apple represents 23–25% of TSMC\'s total revenue',
      'Funded commercialization of TSMC InFO-PoP packaging',
      'Yield risk absorption: pays only for functional dies during early ramps'
    ],
    risks: 'Taiwan Concentration: 100% of advanced silicon is fabricated in Taiwan. Any geopolitical blockade or seismic event would paralyze flagship hardware output within 60–90 days. Still dependent on external Qualcomm 5G modems despite $1B Intel modem division acquisition.'
  },
  {
    id: 'snapdragon-8-elite',
    brand: 'Qualcomm',
    brandColor: '#f472b6',
    name: 'Snapdragon 8 Elite',
    altName: 'Snapdragon 8 Gen 3',
    model: 'Merchant Fabless',
    node: 'TSMC 3nm (N3E)',
    foundry: 'TSMC (Ex-Samsung)',
    cpu: 'Custom Oryon (Nuvia)',
    packaging: 'Amkor / ASE / TSMC',
    modem: 'Integrated Snapdragon X80',
    unitShare: 28,
    revenueShare: 34,
    bomCost: '$180 – $200',
    bomAvg: 190,
    riskLevel: 'high',
    riskLabel: 'TSMC allocation & ARM legal',
    filter: 'qualcomm',
    description: 'Qualcomm is the premier merchant silicon provider, setting the performance standard for Android flagships with ~34% of global SoC dollar revenues. The custom Oryon CPU architecture (from Nuvia acquisition) broke reliance on ARM standard roadmap.',
    strengths: [
      'Custom Oryon cores deliver desktop-class IPC and power optimization',
      'Integrated 5G mmWave + Sub-6 modem with RF front-end (complete platform)',
      'Successfully pivoted from Samsung Foundry to TSMC after SD 8 Gen 1 thermal issues',
      'Dominant position in premium Android tier with strong OEM partnerships'
    ],
    risks: 'ARM Holdings sued Qualcomm over Nuvia architectural license transfer, threatening to terminate Qualcomm\'s architectural rights. At $180–$200 per unit, pricing strains relationships with Chinese OEMs, encouraging dual-sourcing with MediaTek.'
  },
  {
    id: 'dimensity-9400',
    brand: 'MediaTek',
    brandColor: '#fbbf24',
    name: 'Dimensity 9400',
    altName: 'Dimensity 9300',
    model: 'Merchant Fabless',
    node: 'TSMC 3nm (N3E)',
    foundry: 'TSMC (100%)',
    cpu: 'Stock ARM Cortex (All-Big)',
    packaging: 'TSMC InFO / ASE',
    modem: 'Integrated MediaTek 5G',
    unitShare: 37,
    revenueShare: 17,
    bomCost: '$120 – $140',
    bomAvg: 130,
    riskLevel: 'medium',
    riskLabel: 'China OEM exposure',
    filter: 'mediatek',
    description: 'The undisputed unit volume champion at ~37% of global mobile processors. Successfully transitioned from budget to flagship tier with the revolutionary "All-Big-Core" architecture eliminating small efficiency cores.',
    strengths: [
      'Hsinchu proximity to TSMC — frictionless engineering collaboration',
      'Fast-follower economics: adopts refined N3E keeping costs ~30% below Qualcomm',
      'All-Big-Core innovation (1x X925 + 3x X4 + 4x A720) achieves superior thermals',
      'Largest SoC supplier by unit volume globally'
    ],
    risks: 'Over 70% of mobile revenues from Chinese brands (Vivo, Oppo, Xiaomi, Transsion). Uses standard ARM Cortex cores leaving it exposed to ARM licensing restructuring.'
  },
  {
    id: 'exynos-2500',
    brand: 'Samsung',
    brandColor: '#38bdf8',
    name: 'Exynos 2500',
    altName: 'Exynos 2400',
    model: 'Hybrid IDM',
    node: 'Samsung 3nm GAA / 4nm',
    foundry: 'Samsung Foundry',
    cpu: 'Stock ARM Cortex-X/A',
    packaging: 'Samsung FOWLP',
    modem: 'Integrated Exynos 5G',
    unitShare: 5,
    revenueShare: 5,
    bomCost: '$100 – $120',
    bomAvg: 110,
    riskLevel: 'high',
    riskLabel: 'Low 3nm GAA fab yields',
    filter: 'samsung',
    description: 'Samsung\'s unique IDM structure creates friction between Samsung System LSI (design), Samsung Foundry (fabrication), and Samsung MX (device division). 3nm GAA yields below 30% during initial runs forced delays.',
    strengths: [
      'Memory & Packaging co-location: leading LPDDR5X DRAM and UFS manufacturer',
      'Geopolitical independence from Taiwan with fabs in Pyeongtaek and Hwaseong',
      'First foundry to introduce Gate-All-Around (GAA) MBCFET architecture',
      'Fan-Out Wafer-Level Packaging (FOWLP) improved thermal dissipation'
    ],
    risks: 'Persistently low 3nm GAA yields (reportedly <30% initially). Internal rivalry: Samsung MX has repeatedly abandoned Exynos in favor of Qualcomm Snapdragon due to thermal and yield issues.'
  },
  {
    id: 'tensor-g5',
    brand: 'Google',
    brandColor: '#34d399',
    name: 'Tensor G5',
    altName: 'Tensor G4',
    model: 'Captive Fabless',
    node: 'TSMC 3nm (N3E)',
    foundry: 'TSMC (Switched from Samsung)',
    cpu: 'Custom / Stock ARM',
    packaging: 'TSMC InFO',
    modem: 'External/Integrated Exynos/TSMC',
    unitShare: 1.5,
    revenueShare: 1,
    bomCost: '$90 – $110',
    bomAvg: 100,
    riskLevel: 'medium',
    riskLabel: 'Small unit scale',
    filter: 'google',
    description: 'Google transitioned from Samsung co-design (Tensor G1–G4) to fully in-house architecture on TSMC 3nm for G5. Focus on custom ML/TPU and ISP tailored to Android Pixel software suite.',
    strengths: [
      'Custom ML accelerators (TPU) optimized for Google AI models',
      'Switched to TSMC 3nm from Samsung, improving thermals and efficiency',
      'Full architecture control for Android + Pixel Camera pipeline optimization',
      'Deep software-hardware co-optimization for on-device AI'
    ],
    risks: 'Very small production scale (~1.5% unit share) limits foundry negotiation leverage. Transitioning away from Samsung design blocks requires significant in-house silicon engineering investment.'
  },
  {
    id: 'kirin-9010',
    brand: 'HiSilicon (Huawei)',
    brandColor: '#fb923c',
    name: 'Kirin 9010',
    altName: 'Kirin 9000s',
    model: 'Captive Fabless (Sanctioned)',
    node: 'SMIC 7nm DUV Multi-pattern',
    foundry: 'SMIC (China Domestic)',
    cpu: 'Custom Taishan (ARMv8/v9)',
    packaging: 'JCET / Domestic OSAT',
    modem: 'Integrated Balong 5G',
    unitShare: 3,
    revenueShare: 3,
    bomCost: '$140+ estimated',
    bomAvg: 145,
    riskLevel: 'critical',
    riskLabel: 'ASML EUV export embargo',
    filter: 'hisilicon',
    description: 'Pre-2020, HiSilicon was world-class — introducing the first 5nm 5G SoC (Kirin 9000) on TSMC. US export bans forced domestic substitution via SMIC DUV multi-patterning at 7nm-equivalent, proving technological resilience but at steep cost.',
    strengths: [
      'Proved technological resilience under US sanctions with domestic SMIC fabrication',
      'DUV multi-patterning (SAQP) achieved 7nm-equivalent transistor densities without EUV',
      'Fully integrated Balong 5G modem — complete self-sufficiency',
      'Backed by China Big Fund III ($47.5B) national semiconductor initiative'
    ],
    risks: 'ASML EUV export embargo prevents access to advanced lithography. DUV multi-patterning incurs high defect rates, low wafer throughput, and estimated costs exceeding $140/die. Banned from TSMC and any foundry using US-origin technology.'
  }
];

// ─── SEARCHABLE DATA ───
const SEARCH_DATA = [
  // Processors
  ...PROCESSORS.map(p => ({
    category: 'Processors',
    icon: '🔲',
    title: `${p.brand} ${p.name}`,
    desc: `${p.node} · ${p.model} · ${p.bomCost}`,
    badge: p.brand,
    badgeColor: p.brandColor,
    action: () => openProcessorModal(p.id),
    keywords: `${p.brand} ${p.name} ${p.altName} ${p.cpu} ${p.node} ${p.foundry} ${p.model} ${p.modem} ${p.packaging}`.toLowerCase()
  })),
  // Foundries
  { category: 'Foundries', icon: '🏭', title: 'TSMC', desc: '87% of sub-5nm advanced node manufacturing · Taiwan', badge: 'Foundry', badgeColor: '#f87171', action: () => scrollToSection('supply-chain'), keywords: 'tsmc taiwan semiconductor manufacturing company foundry 3nm 2nm n3e n3p wafer fab fabrication' },
  { category: 'Foundries', icon: '🏭', title: 'Samsung Foundry', desc: '3nm GAA MBCFET · Pyeongtaek, South Korea', badge: 'Foundry', badgeColor: '#38bdf8', action: () => scrollToSection('supply-chain'), keywords: 'samsung foundry gaa gate all around mbcfet 3nm 4nm pyeongtaek hwaseong south korea' },
  { category: 'Foundries', icon: '🏭', title: 'SMIC', desc: '7nm DUV multi-patterning · China domestic', badge: 'Foundry', badgeColor: '#fb923c', action: () => scrollToSection('supply-chain'), keywords: 'smic semiconductor manufacturing international corp china domestic duv 7nm sanctions huawei' },
  // Equipment & IP
  { category: 'Equipment & IP', icon: '🔬', title: 'ASML', desc: '100% monopoly on EUV lithography scanners · $180M–$350M+ per machine', badge: 'Monopoly', badgeColor: '#f43f5e', action: () => scrollToSection('geopolitics'), keywords: 'asml euv extreme ultraviolet lithography scanner veldhoven netherlands monopoly high-na' },
  { category: 'Equipment & IP', icon: '💻', title: 'ARM Holdings', desc: 'Foundational ISA for 99%+ of mobile processors', badge: 'IP', badgeColor: '#a78bfa', action: () => scrollToSection('geopolitics'), keywords: 'arm holdings isa instruction set architecture cortex cpu ip licensing risc-v' },
  { category: 'Equipment & IP', icon: '🖥️', title: 'Synopsys & Cadence', desc: 'EDA duopoly — 70%+ of Electronic Design Automation market', badge: 'EDA', badgeColor: '#34d399', action: () => scrollToSection('supply-chain'), keywords: 'synopsys cadence eda electronic design automation software placement timing' },
  // Technologies
  { category: 'Technologies', icon: '⚡', title: 'InFO-PoP Packaging', desc: 'TSMC Integrated Fan-Out Package-on-Package — DRAM stacking on SoC', badge: 'Packaging', badgeColor: '#06b6d4', action: () => scrollToSection('supply-chain'), keywords: 'info pop integrated fan out package on package tsmc dram stacking rdl redistribution' },
  { category: 'Technologies', icon: '🧬', title: 'Gate-All-Around (GAA)', desc: '2nm nanosheet architecture — gate surrounds channel on all 4 sides', badge: 'Next-Gen', badgeColor: '#8b5cf6', action: () => scrollToSection('roadmap'), keywords: 'gaa gate all around nanosheet 2nm transistor architecture mbcfet samsung tsmc n2' },
  { category: 'Technologies', icon: '🔋', title: 'Backside Power Delivery (BSPDN)', desc: 'Power rails moved to wafer backside — 15%+ density improvement', badge: 'Future', badgeColor: '#10b981', action: () => scrollToSection('roadmap'), keywords: 'bspdn backside power delivery network tsmc a16 intel powervia ir drop routing density' },
  { category: 'Technologies', icon: '🧩', title: 'Mobile Chiplets (UCIe)', desc: '2nm compute + 6nm I/O modem chiplets via Universal Chiplet Interconnect', badge: 'Future', badgeColor: '#f59e0b', action: () => scrollToSection('roadmap'), keywords: 'chiplets ucie universal chiplet interconnect express disaggregated soc modular 3d hybrid bonding' },
  // Geopolitics
  { category: 'Geopolitics', icon: '🛡️', title: 'US CHIPS Act', desc: '$52.7B for domestic semiconductor manufacturing', badge: '$52.7B', badgeColor: '#6366f1', action: () => scrollToSection('geopolitics'), keywords: 'chips act us united states semiconductor manufacturing onshore domestic subsidies' },
  { category: 'Geopolitics', icon: '🇹🇼', title: 'Taiwan Silicon Shield', desc: '60% of all semiconductors, 87% of sub-5nm from Taiwan', badge: 'Risk', badgeColor: '#f43f5e', action: () => scrollToSection('geopolitics'), keywords: 'taiwan silicon shield concentration risk cross strait geopolitical tsmc hsinchu' },
  { category: 'Geopolitics', icon: '🚫', title: 'US Export Controls', desc: 'Entity list bans on EUV, EDA tools to China — BIS sanctions', badge: 'Sanctions', badgeColor: '#f59e0b', action: () => scrollToSection('geopolitics'), keywords: 'us export controls entity list bis sanctions china huawei hisilicon euv eda ban embargo' },
  // Supply Chain
  { category: 'Supply Chain', icon: '📊', title: 'Bullwhip Effect', desc: 'Demand amplification: ±5% retail → ±60% fab CapEx swings', badge: 'Risk', badgeColor: '#f43f5e', action: () => scrollToSection('analytics'), keywords: 'bullwhip effect demand amplification inventory semiconductor supply chain shortage glut' },
  { category: 'Supply Chain', icon: '💰', title: 'BOM Cost Analysis', desc: 'SoC = 29.5% of flagship smartphone BOM ($165 out of $560)', badge: 'Analytics', badgeColor: '#06b6d4', action: () => scrollToSection('analytics'), keywords: 'bom bill of materials cost analysis flagship smartphone processor display camera' },
];

// ─── CHART COLORS ───
const COLORS = {
  indigo: '#6366f1',
  cyan: '#06b6d4',
  violet: '#8b5cf6',
  rose: '#f43f5e',
  amber: '#f59e0b',
  emerald: '#10b981',
  sky: '#38bdf8',
  orange: '#fb923c',
  pink: '#f472b6',
  teal: '#14b8a6',
};

const CHART_FONT = { family: "'Inter', sans-serif" };

// ─── CHART.JS DEFAULTS ───
Chart.defaults.color = '#9da3b4';
Chart.defaults.font.family = CHART_FONT.family;
Chart.defaults.font.size = 12;
Chart.defaults.plugins.legend.labels.usePointStyle = true;
Chart.defaults.plugins.legend.labels.pointStyleWidth = 10;
Chart.defaults.plugins.legend.labels.padding = 16;
Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(12, 14, 22, 0.95)';
Chart.defaults.plugins.tooltip.titleFont = { size: 13, weight: '600', family: CHART_FONT.family };
Chart.defaults.plugins.tooltip.bodyFont = { size: 12, family: CHART_FONT.family };
Chart.defaults.plugins.tooltip.borderColor = 'rgba(99, 102, 241, 0.2)';
Chart.defaults.plugins.tooltip.borderWidth = 1;
Chart.defaults.plugins.tooltip.cornerRadius = 8;
Chart.defaults.plugins.tooltip.padding = 12;
Chart.defaults.elements.arc.borderWidth = 0;
Chart.defaults.scale.grid = { color: 'rgba(255, 255, 255, 0.04)' };
Chart.defaults.scale.border = { color: 'rgba(255, 255, 255, 0.06)' };

// Register datalabels plugin
Chart.register(ChartDataLabels);

// ─── PRELOADER ───
window.addEventListener('load', () => {
  setTimeout(() => {
    document.getElementById('preloader').classList.add('hidden');
  }, 2000);
});

// ─── NAVBAR SCROLL ───
const navbar = document.getElementById('navbar');
const navLinks = document.querySelectorAll('.nav-link');

window.addEventListener('scroll', () => {
  navbar.classList.toggle('scrolled', window.scrollY > 50);
  updateActiveNav();
});

function updateActiveNav() {
  const sections = document.querySelectorAll('.section, .hero');
  let current = '';
  sections.forEach(section => {
    const top = section.offsetTop - 100;
    if (window.scrollY >= top) {
      current = section.id;
    }
  });
  navLinks.forEach(link => {
    link.classList.toggle('active', link.dataset.section === current);
  });
}

// ─── HAMBURGER ───
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');

hamburger.addEventListener('click', () => {
  hamburger.classList.toggle('active');
  mobileNav.classList.toggle('open');
});

document.querySelectorAll('.mobile-nav-link').forEach(link => {
  link.addEventListener('click', () => {
    hamburger.classList.remove('active');
    mobileNav.classList.remove('open');
  });
});

// ─── SEARCH ───
const searchTrigger = document.getElementById('searchTrigger');
const searchOverlay = document.getElementById('searchOverlay');
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

function openSearch() {
  searchOverlay.classList.add('open');
  setTimeout(() => searchInput.focus(), 100);
}

function closeSearch() {
  searchOverlay.classList.remove('open');
  searchInput.value = '';
  renderSearchResults('');
}

searchTrigger.addEventListener('click', openSearch);

searchOverlay.addEventListener('click', (e) => {
  if (e.target === searchOverlay) closeSearch();
});

document.addEventListener('keydown', (e) => {
  if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
    e.preventDefault();
    openSearch();
  }
  if (e.key === 'Escape') closeSearch();
});

searchInput.addEventListener('input', (e) => {
  renderSearchResults(e.target.value.trim().toLowerCase());
});

function renderSearchResults(query) {
  if (!query) {
    searchResults.innerHTML = `
      <div class="search-empty">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" opacity="0.3"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <p>Type to search across processors, technologies, and supply chain data</p>
      </div>`;
    return;
  }

  const filtered = SEARCH_DATA.filter(item =>
    item.keywords.includes(query) ||
    item.title.toLowerCase().includes(query) ||
    item.desc.toLowerCase().includes(query)
  );

  if (filtered.length === 0) {
    searchResults.innerHTML = `
      <div class="search-empty">
        <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1" opacity="0.3"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <p>No results found for "${query}"</p>
      </div>`;
    return;
  }

  // Group by category
  const grouped = {};
  filtered.forEach(item => {
    if (!grouped[item.category]) grouped[item.category] = [];
    grouped[item.category].push(item);
  });

  let html = '';
  Object.entries(grouped).forEach(([category, items]) => {
    html += `<div class="search-category-label">${category}</div>`;
    items.forEach(item => {
      html += `
        <div class="search-result-item" data-action="${item.title}">
          <div class="search-result-icon">${item.icon}</div>
          <div class="search-result-info">
            <div class="search-result-title">${highlightMatch(item.title, query)}</div>
            <div class="search-result-desc">${item.desc}</div>
          </div>
          <span class="search-result-badge" style="background: ${item.badgeColor}15; color: ${item.badgeColor}; border: 1px solid ${item.badgeColor}30">${item.badge}</span>
        </div>`;
    });
  });

  searchResults.innerHTML = html;

  // Add click events
  searchResults.querySelectorAll('.search-result-item').forEach((el) => {
    el.addEventListener('click', () => {
      const title = el.dataset.action;
      const item = SEARCH_DATA.find(d => d.title === title);
      if (item) {
        closeSearch();
        item.action();
      }
    });
  });
}

function highlightMatch(text, query) {
  const idx = text.toLowerCase().indexOf(query);
  if (idx === -1) return text;
  return text.substring(0, idx) + '<strong style="color: var(--accent-indigo)">' + text.substring(idx, idx + query.length) + '</strong>' + text.substring(idx + query.length);
}

function scrollToSection(id) {
  const el = document.getElementById(id);
  if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// ─── HERO PARTICLES ───
function createParticles() {
  const container = document.getElementById('heroParticles');
  for (let i = 0; i < 30; i++) {
    const particle = document.createElement('div');
    particle.className = 'hero-particle';
    particle.style.left = Math.random() * 100 + '%';
    particle.style.bottom = '-10px';
    particle.style.animationDuration = (4 + Math.random() * 6) + 's';
    particle.style.animationDelay = Math.random() * 5 + 's';
    particle.style.width = (1 + Math.random() * 2) + 'px';
    particle.style.height = particle.style.width;
    particle.style.background = Math.random() > 0.5 ? COLORS.indigo : COLORS.cyan;
    container.appendChild(particle);
  }
}
createParticles();

// ─── HERO COUNTER ANIMATION ───
function animateCounters() {
  const counters = [
    { el: document.getElementById('statRevenue'), target: 45, prefix: '$', suffix: 'B', decimals: 0 },
    { el: document.getElementById('statShipments'), target: 1.2, prefix: '', suffix: 'B', decimals: 1 },
    { el: document.getElementById('statTSMC'), target: 87, prefix: '', suffix: '%', decimals: 0 },
    { el: document.getElementById('statTransistors'), target: 20, prefix: '', suffix: 'B', decimals: 0 },
  ];

  counters.forEach(c => {
    let current = 0;
    const step = c.target / 60;
    const interval = setInterval(() => {
      current += step;
      if (current >= c.target) {
        current = c.target;
        clearInterval(interval);
      }
      c.el.textContent = c.prefix + current.toFixed(c.decimals) + c.suffix;
    }, 25);
  });
}

// Trigger on hero visibility
const heroObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      animateCounters();
      heroObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.3 });
heroObserver.observe(document.getElementById('hero'));

// ─── FADE IN OBSERVER ───
const fadeObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

document.querySelectorAll('.model-card, .chart-card, .tier-card, .risk-card, .invest-card, .timeline-item, .proc-card').forEach(el => {
  el.classList.add('fade-in');
  fadeObserver.observe(el);
});

// ─── PROCESSOR CARDS ───
function renderProcessorCards() {
  const grid = document.getElementById('processorGrid');
  grid.innerHTML = PROCESSORS.map(p => `
    <div class="proc-card fade-in" data-id="${p.id}" data-filter="${p.filter}">
      <div class="proc-card-header">
        <div>
          <div class="proc-brand" style="color: ${p.brandColor}">${p.brand}</div>
          <div class="proc-name">${p.name}</div>
          <div class="proc-node">${p.node}</div>
        </div>
      </div>
      <div class="proc-specs">
        <div class="proc-spec">
          <span class="proc-spec-label">Unit Share</span>
          <span class="proc-spec-value">${p.unitShare}%</span>
        </div>
        <div class="proc-spec">
          <span class="proc-spec-label">Revenue</span>
          <span class="proc-spec-value">${p.revenueShare}%</span>
        </div>
        <div class="proc-spec">
          <span class="proc-spec-label">BOM Cost</span>
          <span class="proc-spec-value">${p.bomCost}</span>
        </div>
        <div class="proc-spec">
          <span class="proc-spec-label">Foundry</span>
          <span class="proc-spec-value" style="font-size:12px">${p.foundry.split('(')[0].trim()}</span>
        </div>
      </div>
      <div class="proc-risk-badge risk-${p.riskLevel}-badge">${p.riskLabel}</div>
    </div>
  `).join('');

  // Add click events
  grid.querySelectorAll('.proc-card').forEach(card => {
    card.addEventListener('click', () => openProcessorModal(card.dataset.id));
    fadeObserver.observe(card);
  });
}
renderProcessorCards();

// ─── PROCESSOR FILTERS ───
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    const filter = btn.dataset.filter;
    document.querySelectorAll('.proc-card').forEach(card => {
      if (filter === 'all' || card.dataset.filter === filter) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  });
});

// ─── PROCESSOR MODAL ───
const processorModal = document.getElementById('processorModal');
const modalContent = document.getElementById('modalContent');
const modalClose = document.getElementById('modalClose');

function openProcessorModal(id) {
  const p = PROCESSORS.find(pr => pr.id === id);
  if (!p) return;

  modalContent.innerHTML = `
    <span class="modal-brand" style="color: ${p.brandColor}">${p.brand}</span>
    <h2>${p.name}</h2>
    <div class="modal-section">
      <h3>Specifications</h3>
      <div class="modal-specs-grid">
        <div class="modal-spec">
          <div class="modal-spec-label">Process Node</div>
          <div class="modal-spec-value">${p.node}</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-label">Business Model</div>
          <div class="modal-spec-value">${p.model}</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-label">CPU Architecture</div>
          <div class="modal-spec-value">${p.cpu}</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-label">Primary Foundry</div>
          <div class="modal-spec-value">${p.foundry}</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-label">Advanced Packaging</div>
          <div class="modal-spec-value">${p.packaging}</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-label">Modem Integration</div>
          <div class="modal-spec-value">${p.modem}</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-label">Unit Market Share</div>
          <div class="modal-spec-value" style="color: ${p.brandColor}">${p.unitShare}%</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-label">Revenue Market Share</div>
          <div class="modal-spec-value" style="color: ${p.brandColor}">${p.revenueShare}%</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-label">BOM Cost (Per Unit)</div>
          <div class="modal-spec-value">${p.bomCost}</div>
        </div>
      </div>
    </div>
    <div class="modal-section">
      <h3>Overview</h3>
      <p class="modal-desc">${p.description}</p>
    </div>
    <div class="modal-section">
      <h3>Key Strengths</h3>
      <div class="modal-strengths">
        <ul>${p.strengths.map(s => `<li>${s}</li>`).join('')}</ul>
      </div>
    </div>
    <div class="modal-section">
      <h3>Primary Risk Factors</h3>
      <div class="modal-risk">
        <p>${p.risks}</p>
      </div>
    </div>
  `;

  processorModal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeProcessorModal() {
  processorModal.classList.remove('open');
  document.body.style.overflow = '';
}

modalClose.addEventListener('click', closeProcessorModal);
processorModal.addEventListener('click', (e) => {
  if (e.target === processorModal) closeProcessorModal();
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeProcessorModal();
});

// ═══════════════════════════════════════════════════════════════════
// CHARTS
// ═══════════════════════════════════════════════════════════════════

// ─── Unit Market Share (Doughnut) ───
new Chart(document.getElementById('chartUnitShare'), {
  type: 'doughnut',
  data: {
    labels: ['MediaTek', 'Qualcomm', 'Apple', 'Samsung', 'HiSilicon', 'Google', 'Others'],
    datasets: [{
      data: [37, 28, 18, 5, 3, 1.5, 7.5],
      backgroundColor: [COLORS.amber, COLORS.pink, COLORS.violet, COLORS.sky, COLORS.orange, COLORS.emerald, '#3f4255'],
      hoverOffset: 8,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: '65%',
    plugins: {
      legend: { position: 'bottom', labels: { padding: 14, font: { size: 11 } } },
      datalabels: {
        color: '#f0f1f5',
        font: { weight: '600', size: 11 },
        formatter: (v) => v >= 5 ? v + '%' : '',
      }
    }
  }
});

// ─── Revenue Market Share (Doughnut) ───
new Chart(document.getElementById('chartRevenueShare'), {
  type: 'doughnut',
  data: {
    labels: ['Apple', 'Qualcomm', 'MediaTek', 'Samsung', 'HiSilicon', 'Google', 'Others'],
    datasets: [{
      data: [38, 34, 17, 5, 3, 1, 2],
      backgroundColor: [COLORS.violet, COLORS.pink, COLORS.amber, COLORS.sky, COLORS.orange, COLORS.emerald, '#3f4255'],
      hoverOffset: 8,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    cutout: '65%',
    plugins: {
      legend: { position: 'bottom', labels: { padding: 14, font: { size: 11 } } },
      datalabels: {
        color: '#f0f1f5',
        font: { weight: '600', size: 11 },
        formatter: (v) => v >= 5 ? v + '%' : '',
      }
    }
  }
});

// ─── BOM Breakdown (Horizontal Bar) ───
new Chart(document.getElementById('chartBOM'), {
  type: 'bar',
  data: {
    labels: ['SoC + 5G Modem', 'Display (OLED)', 'Camera Modules', 'Memory (DRAM+Flash)', 'Enclosure', 'RF/Wi-Fi/BT', 'Power/Battery/Misc'],
    datasets: [{
      data: [165, 95, 88, 62, 58, 48, 44],
      backgroundColor: [COLORS.indigo, COLORS.cyan, COLORS.rose, COLORS.violet, COLORS.amber, COLORS.emerald, COLORS.sky],
      borderRadius: 6,
      barThickness: 28,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y',
    plugins: {
      legend: { display: false },
      datalabels: {
        anchor: 'end',
        align: 'end',
        color: '#9da3b4',
        font: { weight: '600', size: 11 },
        formatter: (v) => '$' + v,
      }
    },
    scales: {
      x: {
        beginAtZero: true,
        max: 200,
        ticks: { callback: v => '$' + v },
      },
      y: {
        ticks: { font: { size: 11 } }
      }
    }
  }
});

// ─── SoC Cost by Tier (Grouped Bar) ───
new Chart(document.getElementById('chartSoCCost'), {
  type: 'bar',
  data: {
    labels: ['Ultra-Flagship\n($1,000+ MSRP)', 'Premium Mid\n($400–$600)', 'Budget\n(<$200)'],
    datasets: [
      {
        label: 'Low Range',
        data: [150, 50, 18],
        backgroundColor: COLORS.indigo + '99',
        borderRadius: 6,
      },
      {
        label: 'High Range',
        data: [200, 75, 28],
        backgroundColor: COLORS.cyan + '99',
        borderRadius: 6,
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'bottom' },
      datalabels: {
        color: '#f0f1f5',
        font: { weight: '600', size: 11 },
        formatter: (v) => '$' + v,
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: { callback: v => '$' + v },
      }
    }
  }
});

// ─── Wafer Cost Progression (Line) ───
new Chart(document.getElementById('chartWaferCost'), {
  type: 'line',
  data: {
    labels: ['28nm', '16nm', '10nm', '7nm', '5nm', '3nm', '2nm (est.)'],
    datasets: [{
      label: 'Cost per 300mm Wafer',
      data: [3200, 5400, 8500, 12000, 16600, 20500, 29000],
      borderColor: COLORS.indigo,
      backgroundColor: COLORS.indigo + '15',
      fill: true,
      tension: 0.4,
      pointBackgroundColor: COLORS.indigo,
      pointBorderColor: COLORS.indigo,
      pointRadius: 5,
      pointHoverRadius: 8,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      datalabels: {
        color: '#9da3b4',
        font: { weight: '600', size: 10 },
        anchor: 'end',
        align: 'top',
        formatter: (v) => '$' + (v / 1000).toFixed(1) + 'K',
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: { callback: v => '$' + (v / 1000) + 'K' },
      }
    }
  }
});

// ─── Bullwhip Effect (Bar) ───
new Chart(document.getElementById('chartBullwhip'), {
  type: 'bar',
  data: {
    labels: ['Retail\nPhone Sales', 'OEM\nOrders', 'Fabless\nTape-Out', 'Foundry\nWafer Starts'],
    datasets: [{
      label: 'Demand Amplification',
      data: [5, 15, 30, 60],
      backgroundColor: [COLORS.emerald + 'cc', COLORS.cyan + 'cc', COLORS.amber + 'cc', COLORS.rose + 'cc'],
      borderRadius: 8,
      barThickness: 48,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      datalabels: {
        color: '#f0f1f5',
        font: { weight: '700', size: 14 },
        anchor: 'end',
        align: 'top',
        formatter: (v) => '±' + v + '%',
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 80,
        ticks: { callback: v => '±' + v + '%' },
        title: { display: true, text: 'Demand Shift Amplification', color: '#5f6580', font: { size: 11 } }
      }
    }
  }
});

// ─── Foundry Comparison (Radar) ───
new Chart(document.getElementById('chartFoundryComparison'), {
  type: 'radar',
  data: {
    labels: ['Yield Rate', 'Process Node', 'Capacity', 'Packaging', 'Cost Efficiency', 'Customer Trust'],
    datasets: [
      {
        label: 'TSMC',
        data: [95, 98, 90, 95, 85, 98],
        borderColor: COLORS.indigo,
        backgroundColor: COLORS.indigo + '20',
        pointBackgroundColor: COLORS.indigo,
        pointBorderColor: COLORS.indigo,
      },
      {
        label: 'Samsung Foundry',
        data: [55, 85, 65, 70, 75, 50],
        borderColor: COLORS.sky,
        backgroundColor: COLORS.sky + '20',
        pointBackgroundColor: COLORS.sky,
        pointBorderColor: COLORS.sky,
      },
      {
        label: 'SMIC',
        data: [45, 40, 50, 35, 60, 30],
        borderColor: COLORS.orange,
        backgroundColor: COLORS.orange + '20',
        pointBackgroundColor: COLORS.orange,
        pointBorderColor: COLORS.orange,
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'bottom' },
      datalabels: { display: false }
    },
    scales: {
      r: {
        beginAtZero: true,
        max: 100,
        ticks: {
          stepSize: 20,
          color: '#5f6580',
          backdropColor: 'transparent',
          font: { size: 10 }
        },
        grid: { color: 'rgba(255, 255, 255, 0.04)' },
        angleLines: { color: 'rgba(255, 255, 255, 0.06)' },
        pointLabels: { color: '#9da3b4', font: { size: 12, weight: '500' } }
      }
    }
  }
});

// ─── Lead Times (Horizontal Bar) ───
new Chart(document.getElementById('chartLeadTimes'), {
  type: 'bar',
  data: {
    labels: ['Design Cycle (RTL → Tape-Out)', 'Photomask Fabrication', 'Wafer Fabrication', 'OSAT Packaging & Test', 'Logistics & Integration'],
    datasets: [{
      label: 'Lead Time (Weeks)',
      data: [96, 6, 19, 4, 6],
      backgroundColor: [COLORS.violet + 'cc', COLORS.rose + 'cc', COLORS.indigo + 'cc', COLORS.cyan + 'cc', COLORS.emerald + 'cc'],
      borderRadius: 6,
      barThickness: 32,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    indexAxis: 'y',
    plugins: {
      legend: { display: false },
      datalabels: {
        anchor: 'end',
        align: 'end',
        color: '#9da3b4',
        font: { weight: '600', size: 11 },
        formatter: (v) => {
          if (v >= 8) return Math.round(v / 4.33) + ' months';
          return v + ' weeks';
        }
      }
    },
    scales: {
      x: {
        beginAtZero: true,
        ticks: {
          callback: v => {
            if (v >= 8) return Math.round(v / 4.33) + 'mo';
            return v + 'wk';
          }
        },
        title: { display: true, text: 'Duration', color: '#5f6580', font: { size: 11 } }
      },
      y: {
        ticks: { font: { size: 11 } }
      }
    }
  }
});

// ─── ESG Environmental Impact (Polar Area) ───
new Chart(document.getElementById('chartESG'), {
  type: 'polarArea',
  data: {
    labels: ['Water Usage (UPW)', 'Energy (EUV)', 'Carbon Emissions', 'Conflict Minerals', 'Chemical Waste'],
    datasets: [{
      data: [85, 92, 70, 55, 65],
      backgroundColor: [COLORS.cyan + '80', COLORS.amber + '80', COLORS.rose + '80', COLORS.violet + '80', COLORS.emerald + '80'],
      borderWidth: 0,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'bottom', labels: { font: { size: 11 }, padding: 12 } },
      datalabels: {
        color: '#f0f1f5',
        font: { weight: '600', size: 11 },
        formatter: v => v + '/100',
      }
    },
    scales: {
      r: {
        beginAtZero: true,
        max: 100,
        ticks: { display: false },
        grid: { color: 'rgba(255, 255, 255, 0.04)' },
      }
    }
  }
});

// ─── TSMC Energy (Line) ───
new Chart(document.getElementById('chartEnergy'), {
  type: 'line',
  data: {
    labels: ['2020', '2021', '2022', '2023', '2024', '2025', '2026 (est.)', '2028 (proj.)'],
    datasets: [{
      label: 'TSMC % of Taiwan Grid',
      data: [5.5, 6.2, 6.8, 7.2, 7.8, 8, 9.2, 13],
      borderColor: COLORS.amber,
      backgroundColor: COLORS.amber + '15',
      fill: true,
      tension: 0.4,
      pointBackgroundColor: COLORS.amber,
      pointBorderColor: COLORS.amber,
      pointRadius: 4,
      pointHoverRadius: 7,
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false },
      datalabels: {
        color: '#9da3b4',
        font: { weight: '600', size: 10 },
        anchor: 'end',
        align: 'top',
        formatter: v => v + '%',
      }
    },
    scales: {
      y: {
        beginAtZero: true,
        max: 16,
        ticks: { callback: v => v + '%' },
        title: { display: true, text: '% of Taiwan Total Electricity', color: '#5f6580', font: { size: 11 } }
      }
    }
  }
});

// ─── Tech Roadmap (Multi-Line) ───
new Chart(document.getElementById('chartRoadmap'), {
  type: 'line',
  data: {
    labels: ['7nm\n(2018)', '5nm\n(2020)', '3nm\n(2023)', '2nm\n(2026)', '1.4nm\n(2028)', 'A14\n(2030)'],
    datasets: [
      {
        label: 'Performance (rel. to 7nm)',
        data: [100, 118, 140, 160, 185, 210],
        borderColor: COLORS.indigo,
        backgroundColor: COLORS.indigo + '15',
        fill: false,
        tension: 0.3,
        pointBackgroundColor: COLORS.indigo,
        pointRadius: 5,
      },
      {
        label: 'Power Efficiency',
        data: [100, 130, 160, 200, 240, 280],
        borderColor: COLORS.emerald,
        backgroundColor: COLORS.emerald + '15',
        fill: false,
        tension: 0.3,
        pointBackgroundColor: COLORS.emerald,
        pointRadius: 5,
      },
      {
        label: 'Transistor Density',
        data: [100, 180, 330, 500, 700, 950],
        borderColor: COLORS.cyan,
        backgroundColor: COLORS.cyan + '15',
        fill: false,
        tension: 0.3,
        pointBackgroundColor: COLORS.cyan,
        pointRadius: 5,
      },
      {
        label: 'Wafer Cost',
        data: [100, 138, 171, 242, 310, 380],
        borderColor: COLORS.rose,
        backgroundColor: COLORS.rose + '15',
        fill: false,
        tension: 0.3,
        borderDash: [6, 4],
        pointBackgroundColor: COLORS.rose,
        pointRadius: 5,
      }
    ]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'bottom' },
      datalabels: { display: false }
    },
    scales: {
      y: {
        beginAtZero: true,
        ticks: { callback: v => v + '%' },
        title: { display: true, text: 'Relative Index (7nm = 100%)', color: '#5f6580', font: { size: 11 } }
      }
    }
  }
});

// ─── SMOOTH SCROLL FOR ALL NAV LINKS ───
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      const offset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-height')) || 72;
      const top = target.offsetTop - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    }
  });
});

console.log('%c ChipFlow Analytics Loaded ✦', 'color: #6366f1; font-weight: bold; font-size: 14px;');
