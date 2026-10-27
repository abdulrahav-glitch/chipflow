/**
 * Flipkart Catalog Analytics — Enterprise Frontend Controller
 * Connects asynchronously with FastAPI backend endpoints.
 */

// Determine API base URL dynamically
const API_BASE = window.location.origin.includes(':8000') 
  ? window.location.origin 
  : 'http://localhost:8000';

// Global application state
const state = {
  currentView: 0,
  category: '',
  subCategory: '',
  searchQuery: '',
  fkAdvantage: -1,
  
  // Pagination & Sorting for View 4
  page: 1,
  limit: 25,
  sortBy: 'discounted_price',
  sortOrder: 'desc',
  
  // Scenario Planner (View 3)
  scenarioUnits: 5,
  
  // Unit Economics (View 5)
  unitEcon: {
    units: 5,
    costPct: 35.0,
    commPct: 8.0,
    shipping: 40.0
  },
  
  isLoading: false,
  scatterData: null
};

// Utilities for formatting
const formatNumber = (num) => (num || 0).toLocaleString();
const formatCurrency = (num) => '₹' + Math.round(num || 0).toLocaleString();
const formatPercent = (num) => (num || 0).toFixed(1) + '%';

// Show/Hide Loading Indicator
function setLoading(loading) {
  state.isLoading = loading;
  const indicator = document.getElementById('loadingIndicator');
  if (indicator) {
    indicator.style.display = loading ? 'flex' : 'none';
  }
}

// Build query parameter string from active filters
function getFilterQueryParams(extra = {}) {
  const params = new URLSearchParams();
  if (state.category) params.append('category', state.category);
  if (state.subCategory) params.append('sub_category', state.subCategory);
  if (state.fkAdvantage !== -1) params.append('fk', state.fkAdvantage);
  if (state.searchQuery.trim()) params.append('q', state.searchQuery.trim());
  
  for (const [k, v] of Object.entries(extra)) {
    if (v !== undefined && v !== null) params.append(k, v);
  }
  return params.toString();
}

// ─────────────────────────────────────────────────────────────
// Initialization & Event Binding
// ─────────────────────────────────────────────────────────────

document.addEventListener('DOMContentLoaded', async () => {
  setupNavigation();
  setupFilterControls();
  setupSliderControls();
  setupPaginationControls();
  
  await checkBackendHealth();
  await loadFilterOptions();
  await loadDataDictionary();
  
  // Load initial active view
  renderCurrentView();
});

async function checkBackendHealth() {
  const statusEl = document.getElementById('backendStatus');
  try {
    const res = await fetch(`${API_BASE}/api/health`);
    if (res.ok) {
      statusEl.textContent = 'Backend Online (FastAPI)';
      statusEl.parentElement.querySelector('.status-dot').style.background = '#39ff84';
    } else {
      throw new Error();
    }
  } catch (err) {
    statusEl.textContent = 'Backend Offline';
    statusEl.parentElement.querySelector('.status-dot').style.background = '#ff4d4f';
  }
}

async function loadFilterOptions() {
  try {
    const res = await fetch(`${API_BASE}/api/filters`);
    if (!res.ok) return;
    const data = await res.json();
    
    // Categories
    const catSelect = document.getElementById('cat');
    catSelect.innerHTML = '<option value="">All Categories</option>';
    data.categories.forEach(cat => {
      const opt = document.createElement('option');
      opt.value = cat;
      opt.textContent = cat;
      catSelect.appendChild(opt);
    });

    // Subcategories
    const subSelect = document.getElementById('sub');
    subSelect.innerHTML = '<option value="">All Sub-categories</option>';
    data.subcategories.forEach(sub => {
      const opt = document.createElement('option');
      opt.value = sub;
      opt.textContent = sub;
      subSelect.appendChild(opt);
    });
  } catch (e) {
    console.error('Failed loading filter options', e);
  }
}

function setupNavigation() {
  const navButtons = document.querySelectorAll('nav button');
  navButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      navButtons.forEach(b => b.classList.remove('on'));
      btn.classList.add('on');
      
      const viewIndex = parseInt(btn.dataset.view, 10);
      switchView(viewIndex);
    });
  });
}

function switchView(index) {
  state.currentView = index;
  document.querySelectorAll('main').forEach(m => m.classList.remove('on'));
  const target = document.getElementById(`v${index}`);
  if (target) target.classList.add('on');
  renderCurrentView();
}

function setupFilterControls() {
  const catSelect = document.getElementById('cat');
  const subSelect = document.getElementById('sub');
  const qInput = document.getElementById('q');
  const fkSelect = document.getElementById('fk');
  const clearBtn = document.getElementById('clearFiltersBtn');
  
  catSelect.addEventListener('change', (e) => {
    state.category = e.target.value;
    state.page = 1;
    renderCurrentView();
  });
  
  subSelect.addEventListener('change', (e) => {
    state.subCategory = e.target.value;
    state.page = 1;
    renderCurrentView();
  });
  
  fkSelect.addEventListener('change', (e) => {
    state.fkAdvantage = parseInt(e.target.value, 10);
    state.page = 1;
    renderCurrentView();
  });
  
  // Debounced search query
  let debounceTimer;
  qInput.addEventListener('input', (e) => {
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(() => {
      state.searchQuery = e.target.value;
      state.page = 1;
      renderCurrentView();
    }, 300);
  });
  
  clearBtn.addEventListener('click', () => {
    state.category = '';
    state.subCategory = '';
    state.searchQuery = '';
    state.fkAdvantage = -1;
    catSelect.value = '';
    subSelect.value = '';
    qInput.value = '';
    fkSelect.value = '-1';
    state.page = 1;
    renderCurrentView();
  });
}

function setupSliderControls() {
  // Scenario Planner (View 3)
  const uSlider = document.getElementById('u');
  const uv = document.getElementById('uv');
  let sTimer;
  uSlider.addEventListener('input', (e) => {
    const val = parseInt(e.target.value, 10);
    state.scenarioUnits = val;
    uv.textContent = val;
    clearTimeout(sTimer);
    sTimer = setTimeout(() => renderView3(), 150);
  });

  // Unit Economics (View 5)
  const pu = document.getElementById('pu');
  const pc = document.getElementById('pc');
  const pm = document.getElementById('pm');
  const ps = document.getElementById('ps');

  const puv = document.getElementById('puv');
  const pcv = document.getElementById('pcv');
  const pmv = document.getElementById('pmv');
  const psv = document.getElementById('psv');

  const updateUE = () => {
    state.unitEcon.units = parseInt(pu.value, 10);
    state.unitEcon.costPct = parseFloat(pc.value);
    state.unitEcon.commPct = parseFloat(pm.value);
    state.unitEcon.shipping = parseFloat(ps.value);

    puv.textContent = state.unitEcon.units;
    pcv.textContent = state.unitEcon.costPct + '%';
    pmv.textContent = state.unitEcon.commPct + '%';
    psv.textContent = '₹' + state.unitEcon.shipping;
  };
  updateUE();

  let ueTimer;
  [pu, pc, pm, ps].forEach(sl => {
    sl.addEventListener('input', () => {
      updateUE();
      clearTimeout(ueTimer);
      ueTimer = setTimeout(() => renderView5(), 200);
    });
  });
}

function setupPaginationControls() {
  document.getElementById('pv').addEventListener('click', () => {
    if (state.page > 1) {
      state.page--;
      renderView4();
    }
  });

  document.getElementById('nx').addEventListener('click', () => {
    state.page++;
    renderView4();
  });

  // Sortable headers in Data Table
  document.querySelectorAll('#dt th.sortable').forEach(th => {
    th.addEventListener('click', () => {
      const field = th.dataset.sort;
      if (state.sortBy === field) {
        state.sortOrder = state.sortOrder === 'asc' ? 'desc' : 'asc';
      } else {
        state.sortBy = field;
        state.sortOrder = 'desc';
      }
      state.page = 1;
      renderView4();
    });
  });
}

// Global View Switcher
function renderCurrentView() {
  switch (state.currentView) {
    case 0: renderView0(); break;
    case 1: renderView1(); break;
    case 2: renderView2(); break;
    case 3: renderView3(); break;
    case 4: renderView4(); break;
    case 5: renderView5(); break;
  }
}

// ─────────────────────────────────────────────────────────────
// VIEW 0: Overview Dashboard
// ─────────────────────────────────────────────────────────────
async function renderView0() {
  setLoading(true);
  try {
    const q = getFilterQueryParams();
    const res = await fetch(`${API_BASE}/api/analytics/overview?${q}`);
    const data = await res.json();
    
    // 1. KPIs
    const k = data.kpis;
    const kpiContainer = document.getElementById('kpis');
    kpiContainer.innerHTML = `
      <div class="kpi">
        <b>${formatNumber(k.total_listings)}</b>
        <span>Total Listings</span>
      </div>
      <div class="kpi">
        <b>${formatCurrency(k.avg_selling_price)}</b>
        <span>Avg Selling Price</span>
      </div>
      <div class="kpi accent">
        <b>${formatPercent(k.avg_discount_pct)}</b>
        <span>Avg Discount Depth</span>
      </div>
      <div class="kpi success">
        <b>${k.fk_advantage_pct}% <small style="font-size:0.9rem">(${formatNumber(k.fk_advantage_count)})</small></b>
        <span>Flipkart Advantage</span>
      </div>
      <div class="kpi">
        <b>${k.avg_product_rating ? k.avg_product_rating + ' ★' : 'N/A'}</b>
        <span>Avg Rating (${k.rated_pct}%)</span>
      </div>
      <div class="kpi">
        <b>${formatNumber(k.total_brands)}</b>
        <span>Active Brands</span>
      </div>
    `;

    // 2. Key Findings
    const insList = document.getElementById('ins');
    insList.innerHTML = data.insights.map(i => `<li>${i}</li>`).join('');

    // 3. Listings by Category (Click to filter)
    renderHorizontalBars('bCat', data.categories.map(c => ({
      label: c.category,
      count: c.count,
      pct: c.percentage,
      valText: `${formatNumber(c.count)} (${c.percentage}%)`,
      clickable: true,
      onClick: () => {
        state.category = c.category;
        document.getElementById('cat').value = c.category;
        renderCurrentView();
      }
    })));

    // 4. Discount Depth
    renderHorizontalBars('bDisc', data.discount_depth.map(d => ({
      label: d.label,
      count: d.count,
      pct: d.percentage,
      valText: `${formatNumber(d.count)} (${d.percentage}%)`
    })));

    // 5. Selling Price Bands
    renderHorizontalBars('bPrice', data.price_bands.map(p => ({
      label: p.label,
      count: p.count,
      pct: p.percentage,
      valText: `${formatNumber(p.count)} (${p.percentage}%)`
    })));

    // 6. Crawl Month Columns
    const cMon = document.getElementById('cMon');
    cMon.innerHTML = data.crawl_months.map(m => `
      <div class="col" title="${m.month}: ${formatNumber(m.count)} listings (${m.percentage}%)">
        <span class="col-val">${formatNumber(m.count)}</span>
        <i style="height: ${Math.max(10, m.pct_of_max)}%"></i>
        <span class="col-lbl">${m.month}</span>
      </div>
    `).join('');

  } catch (err) {
    console.error('Error rendering View 0', err);
  } finally {
    setLoading(false);
  }
}

// ─────────────────────────────────────────────────────────────
// VIEW 1: Pricing & Drill-Down
// ─────────────────────────────────────────────────────────────
async function renderView1() {
  setLoading(true);
  try {
    const q = getFilterQueryParams();
    const res = await fetch(`${API_BASE}/api/analytics/pricing?${q}`);
    const data = await res.json();
    
    // 1. Draw Canvas Scatter Plot
    drawScatterPlot(data.scatter_points);

    // 2. Avg Discount by Category
    renderHorizontalBars('bAD', data.category_discounts.slice(0, 15).map(c => ({
      label: c.category,
      pct: c.avg_discount,
      valText: `${c.avg_discount}%`,
      customClass: 'yel'
    })));

    // 3. Flipkart Advantage Comparison Table
    const fkTbody = document.querySelector('#fkT tbody');
    const adv = data.fk_comparison.advantage || { count: 0, avg_retail: 0, avg_price: 0, avg_discount: 0, avg_rating: 0 };
    const non = data.fk_comparison.non_advantage || { count: 0, avg_retail: 0, avg_price: 0, avg_discount: 0, avg_rating: 0 };
    
    fkTbody.innerHTML = `
      <tr>
        <td><span class="tag adv">Flipkart Advantage</span></td>
        <td class="n">${formatNumber(adv.count)}</td>
        <td class="n">${formatCurrency(adv.avg_retail)}</td>
        <td class="n">${formatCurrency(adv.avg_price)}</td>
        <td class="n">${formatPercent(adv.avg_discount)}</td>
        <td class="n">${adv.avg_rating ? adv.avg_rating + ' ★' : '—'}</td>
      </tr>
      <tr>
        <td><span class="tag none">Standard Seller</span></td>
        <td class="n">${formatNumber(non.count)}</td>
        <td class="n">${formatCurrency(non.avg_retail)}</td>
        <td class="n">${formatCurrency(non.avg_price)}</td>
        <td class="n">${formatPercent(non.avg_discount)}</td>
        <td class="n">${non.avg_rating ? non.avg_rating + ' ★' : '—'}</td>
      </tr>
    `;

    // 4. Sub-category Drill-down Table (Clickable)
    const subTbody = document.querySelector('#subT tbody');
    subTbody.innerHTML = data.subcategories.map(s => `
      <tr class="clickable" title="Click to filter by ${s.sub_category}">
        <td class="nm"><b>${s.sub_category}</b></td>
        <td>${s.category}</td>
        <td class="n">${formatNumber(s.count)}</td>
        <td class="n">${formatCurrency(s.avg_retail)}</td>
        <td class="n">${formatCurrency(s.avg_price)}</td>
        <td class="n">${formatPercent(s.avg_discount)}</td>
        <td class="n">${s.fk_pct}%</td>
      </tr>
    `).join('');

    // Attach row click listeners for drill-down
    subTbody.querySelectorAll('tr').forEach((row, idx) => {
      row.addEventListener('click', () => {
        const item = data.subcategories[idx];
        state.category = item.category;
        state.subCategory = item.sub_category;
        document.getElementById('cat').value = item.category;
        document.getElementById('sub').value = item.sub_category;
        renderCurrentView();
      });
    });

  } catch (err) {
    console.error('Error rendering View 1', err);
  } finally {
    setLoading(false);
  }
}

function drawScatterPlot(points) {
  const canvas = document.getElementById('sc-canvas');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  
  // Set real pixel resolution
  const rect = canvas.parentElement.getBoundingClientRect();
  canvas.width = rect.width * window.devicePixelRatio;
  canvas.height = 360 * window.devicePixelRatio;
  ctx.scale(window.devicePixelRatio, window.devicePixelRatio);
  
  const w = rect.width;
  const h = 360;
  const pad = { top: 20, right: 30, bottom: 40, left: 60 };
  
  ctx.clearRect(0, 0, w, h);
  
  if (!points || points.length === 0) {
    ctx.fillStyle = '#9aa7c2';
    ctx.font = '14px sans-serif';
    ctx.fillText('No listings matching filter criteria', w / 2 - 100, h / 2);
    return;
  }
  
  // Max ranges
  const maxPrice = 30000;
  const maxDisc = 100;
  
  // Draw grid & axes
  ctx.strokeStyle = getComputedStyle(document.body).getPropertyValue('--line') || '#d9e0ec';
  ctx.lineWidth = 1;
  ctx.beginPath();
  ctx.moveTo(pad.left, pad.top);
  ctx.lineTo(pad.left, h - pad.bottom);
  ctx.lineTo(w - pad.right, h - pad.bottom);
  ctx.stroke();
  
  // Y-axis ticks (Discount %)
  ctx.fillStyle = '#9aa7c2';
  ctx.font = '11px sans-serif';
  ctx.textAlign = 'right';
  for (let d = 0; d <= 100; d += 25) {
    const y = h - pad.bottom - (d / maxDisc) * (h - pad.top - pad.bottom);
    ctx.fillText(`${d}%`, pad.left - 8, y + 4);
    ctx.beginPath();
    ctx.strokeStyle = 'rgba(150,150,150,0.15)';
    ctx.moveTo(pad.left, y);
    ctx.lineTo(w - pad.right, y);
    ctx.stroke();
  }
  
  // X-axis ticks (Price in ₹)
  ctx.textAlign = 'center';
  for (let p = 0; p <= maxPrice; p += 10000) {
    const x = pad.left + (p / maxPrice) * (w - pad.left - pad.right);
    ctx.fillText(`₹${p / 1000}k`, x, h - pad.bottom + 20);
  }
  
  // Axis labels
  ctx.fillText('Selling Price (₹)', (w + pad.left) / 2, h - 8);
  
  // Plot dots
  points.forEach(pt => {
    const x = pad.left + Math.min(1, pt.price / maxPrice) * (w - pad.left - pad.right);
    const y = h - pad.bottom - (Math.min(100, Math.max(0, pt.discount)) / maxDisc) * (h - pad.top - pad.bottom);
    
    ctx.beginPath();
    ctx.arc(x, y, 3, 0, Math.PI * 2);
    ctx.fillStyle = pt.fk ? 'rgba(40, 116, 240, 0.75)' : 'rgba(255, 180, 0, 0.45)';
    ctx.fill();
  });
}

// ─────────────────────────────────────────────────────────────
// VIEW 2: Ratings & Brands
// ─────────────────────────────────────────────────────────────
async function renderView2() {
  setLoading(true);
  try {
    const q = getFilterQueryParams();
    const res = await fetch(`${API_BASE}/api/analytics/ratings?${q}`);
    const data = await res.json();
    
    // 1. Rating Distribution Columns
    const cRat = document.getElementById('cRat');
    const ratedTotal = data.rating_distribution
      .filter(r => r.tier !== 'Unrated')
      .reduce((acc, cur) => acc + cur.count, 0) || 1;

    cRat.innerHTML = data.rating_distribution.map(r => {
      const heightPct = r.tier === 'Unrated' 
        ? 15 
        : Math.min(100, Math.max(8, (r.count / ratedTotal) * 100));
      return `
        <div class="col" title="${r.tier}: ${formatNumber(r.count)} listings">
          <span class="col-val">${formatNumber(r.count)}</span>
          <i style="height: ${heightPct}%"></i>
          <span class="col-lbl">${r.tier}</span>
        </div>
      `;
    }).join('');

    // 2. Average Discount by Rating
    renderHorizontalBars('bRD', data.discount_by_rating.map(d => ({
      label: d.rating,
      pct: d.avg_discount,
      valText: `${d.avg_discount}% (${formatNumber(d.count)})`
    })));

    // 3. Brand Leaderboard Table
    const brTbody = document.querySelector('#brT tbody');
    brTbody.innerHTML = data.brand_leaderboard.map(b => `
      <tr>
        <td class="nm"><b>${b.brand}</b></td>
        <td class="n">${formatNumber(b.count)}</td>
        <td class="n">${formatCurrency(b.avg_price)}</td>
        <td class="n">${formatPercent(b.avg_discount)}</td>
        <td class="n">${b.avg_rating ? b.avg_rating + ' ★' : '—'}</td>
        <td class="n">${formatNumber(b.rating_count)}</td>
      </tr>
    `).join('');

  } catch (err) {
    console.error('Error rendering View 2', err);
  } finally {
    setLoading(false);
  }
}

// ─────────────────────────────────────────────────────────────
// VIEW 3: Order Scenario Planner
// ─────────────────────────────────────────────────────────────
async function renderView3() {
  setLoading(true);
  try {
    const payload = {
      units_per_listing: state.scenarioUnits,
      category: state.category || null,
      sub_category: state.subCategory || null,
      is_fk_advantage: state.fkAdvantage,
      query: state.searchQuery || null
    };

    const res = await fetch(`${API_BASE}/api/analytics/scenario`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    
    // 1. Scenario KPIs
    const sk = document.getElementById('sk');
    sk.innerHTML = `
      <div class="kpi">
        <b>${formatNumber(data.projected_units)}</b>
        <span>Total Units Projected</span>
      </div>
      <div class="kpi success">
        <b>${formatCurrency(data.projected_gmv)}</b>
        <span>Projected Sales (GMV)</span>
      </div>
      <div class="kpi accent">
        <b>${formatCurrency(data.total_discount_given)}</b>
        <span>Discount Money Given Away</span>
      </div>
      <div class="kpi">
        <b>${formatCurrency(data.total_retail_value)}</b>
        <span>Total Retail MRP Value</span>
      </div>
    `;

    // 2. Projected GMV by Category
    const maxGMV = Math.max(...data.category_projections.map(c => c.projected_gmv), 1);
    renderHorizontalBars('bGMV', data.category_projections.slice(0, 12).map(c => ({
      label: c.category,
      pct: (c.projected_gmv / maxGMV) * 100,
      valText: formatCurrency(c.projected_gmv),
      customClass: 'grn'
    })));

    // 3. Discount Given Away by Category
    const maxDisc = Math.max(...data.category_projections.map(c => c.discount_given), 1);
    renderHorizontalBars('bDG', data.category_projections.slice(0, 12).map(c => ({
      label: c.category,
      pct: (c.discount_given / maxDisc) * 100,
      valText: formatCurrency(c.discount_given),
      customClass: 'yel'
    })));

  } catch (err) {
    console.error('Error rendering View 3', err);
  } finally {
    setLoading(false);
  }
}

// ─────────────────────────────────────────────────────────────
// VIEW 4: Data Reference & Catalog Explorer
// ─────────────────────────────────────────────────────────────
async function renderView4() {
  setLoading(true);
  try {
    const q = getFilterQueryParams({
      page: state.page,
      limit: state.limit,
      sort_by: state.sortBy,
      sort_order: state.sortOrder
    });

    const res = await fetch(`${API_BASE}/api/products?${q}`);
    const data = await res.json();
    
    document.getElementById('cnt').textContent = `(${formatNumber(data.total_items)} listings total)`;
    document.getElementById('pn').textContent = `Page ${data.page} of ${data.total_pages}`;
    document.getElementById('pv').disabled = !data.has_prev;
    document.getElementById('nx').disabled = !data.has_next;

    const dtTbody = document.querySelector('#dt tbody');
    dtTbody.innerHTML = data.items.map(p => `
      <tr class="clickable" data-id="${p.uniq_id}">
        <td style="width: 48px; text-align: center;">
          <img src="${p.primary_image || 'data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><text y=%2218%22 font-size=%2218%22>📦</text></svg>'}" 
               style="width: 36px; height: 36px; object-fit: contain; border-radius: 4px; border: 1px solid var(--line);" 
               onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><text y=%2218%22 font-size=%2218%22>📦</text></svg>'">
        </td>
        <td class="nm" title="${p.name}"><b>${p.name}</b></td>
        <td>${p.category}</td>
        <td class="n">${formatCurrency(p.retail_price)}</td>
        <td class="n"><b>${formatCurrency(p.discounted_price)}</b></td>
        <td class="n">${formatPercent(p.discount_pct)}</td>
        <td class="n">${p.rating ? p.rating + ' ★' : '—'}</td>
        <td>${p.is_fk_advantage ? '<span class="tag adv">Advantage</span>' : '<span class="tag none">Standard</span>'}</td>
        <td>${p.brand || 'Unbranded'}</td>
      </tr>
    `).join('');

    // Attach row click to show full product drawer
    dtTbody.querySelectorAll('tr').forEach(row => {
      row.addEventListener('click', () => {
        showProductDetail(row.dataset.id);
      });
    });

  } catch (err) {
    console.error('Error rendering View 4', err);
  } finally {
    setLoading(false);
  }
}

async function showProductDetail(uniqId) {
  const det = document.getElementById('det');
  det.innerHTML = `<div style="text-align:center; padding: 20px;">Fetching product record…</div>`;
  det.classList.add('on');
  det.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

  try {
    const res = await fetch(`${API_BASE}/api/products/${uniqId}`);
    if (!res.ok) throw new Error('Product not found');
    const p = await res.json();

    const mainImg = p.images && p.images.length > 0 ? p.images[0] : p.primary_image;
    const thumbsHtml = (p.images || []).slice(0, 5).map(img => `
      <img src="${img}" class="det-thumb" onclick="document.getElementById('detMainImg').src='${img}'" onerror="this.style.display='none'">
    `).join('');

    const specsHtml = (p.specifications || []).map(s => `
      <tr><td style="color:var(--mute); width:40%;">${s.key}</td><td><b>${s.value}</b></td></tr>
    `).join('');

    det.innerHTML = `
      <div class="det-header">
        <div>
          <div style="font-size: 0.8rem; color: var(--mute); margin-bottom: 4px;">${p.category_tree || p.category}</div>
          <div class="det-title">${p.product_name}</div>
        </div>
        <button class="det-close" onclick="document.getElementById('det').classList.remove('on')">✕</button>
      </div>

      <div class="det-grid">
        <div class="det-gallery">
          <img id="detMainImg" class="det-img-main" src="${mainImg || ''}" onerror="this.src='data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 24 24%22><text y=%2218%22 font-size=%2218%22>📦</text></svg>'">
          <div class="det-thumbs">${thumbsHtml}</div>
        </div>

        <div class="det-info">
          <div class="det-meta">
            <span>Selling Price: <b style="color:var(--blue); font-size:1.1rem;">${formatCurrency(p.discounted_price)}</b></span>
            <span>Retail MRP: <s>${formatCurrency(p.retail_price)}</s></span>
            <span>Discount: <b>${formatPercent(p.discount_pct)}</b></span>
            <span>Rating: <b>${p.product_rating ? p.product_rating + ' ★' : 'No rating'}</b></span>
            <span>Brand: <b>${p.brand || 'Unbranded'}</b></span>
            <span>${p.is_fk_advantage ? '<span class="tag adv">Flipkart Advantage</span>' : '<span class="tag none">Standard Seller</span>'}</span>
          </div>

          <p class="det-desc">${p.description || 'No description available for this product.'}</p>
          
          <div style="margin-top: 6px;">
            <a href="${p.product_url}" target="_blank" rel="noopener">Open Listing on Flipkart ↗</a>
          </div>

          ${specsHtml ? `
            <div class="det-specs">
              <h4 style="margin: 8px 0 4px; font-size: 0.85rem; color: var(--mute);">Key Specifications</h4>
              <table class="det-specs-table"><tbody>${specsHtml}</tbody></table>
            </div>
          ` : ''}
        </div>
      </div>
    `;

  } catch (err) {
    det.innerHTML = `<div style="color:var(--red);">Failed to load product details: ${err.message}</div>`;
  }
}

async function loadDataDictionary() {
  try {
    const res = await fetch(`${API_BASE}/api/dictionary`);
    const dict = await res.json();
    const tbody = document.getElementById('dict');
    if (!tbody) return;
    
    tbody.innerHTML = dict.map(d => `
      <tr>
        <td><code>${d.column}</code></td>
        <td><span class="tag none">${d.type}</span></td>
        <td>${d.description}</td>
      </tr>
    `).join('');
  } catch (e) {
    console.error('Failed to load dictionary', e);
  }
}

// ─────────────────────────────────────────────────────────────
// VIEW 5: Unit Economics & Profit Simulator
// ─────────────────────────────────────────────────────────────
async function renderView5() {
  setLoading(true);
  try {
    const payload = {
      units_per_listing: state.unitEcon.units,
      product_cost_pct: state.unitEcon.costPct,
      commission_pct: state.unitEcon.commPct,
      shipping_per_unit: state.unitEcon.shipping,
      category: state.category || null,
      sub_category: state.subCategory || null,
      is_fk_advantage: state.fkAdvantage,
      query: state.searchQuery || null
    };

    const res = await fetch(`${API_BASE}/api/analytics/unit-economics`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    const k = data.kpis;
    
    // 1. Profit KPIs
    const pk = document.getElementById('pk');
    const isProfit = k.net_profit >= 0;
    pk.innerHTML = `
      <div class="kpi">
        <b>${formatCurrency(k.revenue)}</b>
        <span>Total Gross Sales</span>
      </div>
      <div class="kpi ${isProfit ? 'success' : 'danger'}">
        <b style="color: ${isProfit ? 'var(--grn)' : 'var(--red)'}">${formatCurrency(k.net_profit)}</b>
        <span>Estimated Net Profit</span>
      </div>
      <div class="kpi">
        <b>${formatPercent(k.net_margin_pct)}</b>
        <span>Net Operating Margin</span>
      </div>
      <div class="kpi">
        <b>${formatCurrency(k.cogs)}</b>
        <span>Product Cost (COGS)</span>
      </div>
      <div class="kpi">
        <b>${formatCurrency(k.commission)}</b>
        <span>Platform Commission</span>
      </div>
      <div class="kpi">
        <b>${formatCurrency(k.shipping)}</b>
        <span>Logistics / Shipping</span>
      </div>
    `;

    // 2. Sales by Category
    const maxS = Math.max(...data.pnl_by_category.map(c => c.revenue), 1);
    renderHorizontalBars('pS', data.pnl_by_category.slice(0, 10).map(c => ({
      label: c.category,
      pct: (c.revenue / maxS) * 100,
      valText: formatCurrency(c.revenue)
    })));

    // 3. Profit by Category
    const maxP = Math.max(...data.pnl_by_category.map(c => Math.abs(c.profit)), 1);
    renderHorizontalBars('pP', data.pnl_by_category.slice(0, 10).map(c => ({
      label: c.category,
      pct: Math.min(100, Math.max(5, (Math.abs(c.profit) / maxP) * 100)),
      valText: formatCurrency(c.profit),
      customClass: c.profit >= 0 ? 'grn' : 'red'
    })));

    // 4. Profit by Crawl Month
    const maxM = Math.max(...data.profit_by_month.map(m => Math.abs(m.profit)), 1);
    renderHorizontalBars('pM', data.profit_by_month.map(m => ({
      label: m.month,
      pct: Math.min(100, Math.max(5, (Math.abs(m.profit) / maxM) * 100)),
      valText: formatCurrency(m.profit),
      customClass: m.profit >= 0 ? 'grn' : 'red'
    })));

    // 5. Profit by Discount Depth
    const maxD = Math.max(...data.profit_by_discount.map(d => Math.abs(d.profit)), 1);
    renderHorizontalBars('pD', data.profit_by_discount.map(d => ({
      label: d.bucket,
      pct: Math.min(100, Math.max(5, (Math.abs(d.profit) / maxD) * 100)),
      valText: formatCurrency(d.profit),
      customClass: d.profit >= 0 ? 'grn' : 'red'
    })));

    // 6. Top 10 Most Profitable Listings
    const maxTopP = Math.max(...data.top_profitable.map(t => t.profit), 1);
    renderHorizontalBars('pT', data.top_profitable.map(t => ({
      label: t.name,
      pct: Math.min(100, Math.max(5, (t.profit / maxTopP) * 100)),
      valText: formatCurrency(t.profit),
      customClass: 'grn'
    })));

    // 7. Top 10 Least Profitable Listings
    const minLoss = Math.max(...data.least_profitable.map(l => Math.abs(l.profit)), 1);
    renderHorizontalBars('pL', data.least_profitable.map(l => ({
      label: l.name,
      pct: Math.min(100, Math.max(5, (Math.abs(l.profit) / minLoss) * 100)),
      valText: formatCurrency(l.profit),
      customClass: 'red'
    })));

    // 8. Full Profit & Loss Table
    const plTbody = document.querySelector('#plT tbody');
    plTbody.innerHTML = data.pnl_by_category.map(c => `
      <tr>
        <td class="nm"><b>${c.category}</b></td>
        <td class="n">${formatNumber(c.count)}</td>
        <td class="n">${formatCurrency(c.revenue)}</td>
        <td class="n">${formatCurrency(c.cogs)}</td>
        <td class="n">${formatCurrency(c.commission)}</td>
        <td class="n">${formatCurrency(c.shipping)}</td>
        <td class="n"><b style="color: ${c.profit >= 0 ? 'var(--grn)' : 'var(--red)'}">${formatCurrency(c.profit)}</b></td>
        <td class="n"><span class="tag ${c.margin_pct >= 0 ? 'pos' : 'neg'}">${formatPercent(c.margin_pct)}</span></td>
      </tr>
    `).join('');

  } catch (err) {
    console.error('Error rendering View 5', err);
  } finally {
    setLoading(false);
  }
}

// ─────────────────────────────────────────────────────────────
// Reusable Horizontal Bar Renderer
// ─────────────────────────────────────────────────────────────
function renderHorizontalBars(elementId, items) {
  const container = document.getElementById(elementId);
  if (!container) return;
  
  if (!items || items.length === 0) {
    container.innerHTML = '<div style="color:var(--mute); padding: 10px;">No records available</div>';
    return;
  }
  
  container.innerHTML = items.map((it, idx) => `
    <div class="bar ${it.clickable ? 'cl' : ''}" data-idx="${idx}">
      <div class="l" title="${it.label}">${it.label}</div>
      <div class="t">
        <div class="f ${it.customClass || ''}" style="width: ${Math.max(2, Math.min(100, it.pct))}%"></div>
      </div>
      <div class="v">${it.valText}</div>
    </div>
  `).join('');

  if (items.some(i => i.clickable)) {
    container.querySelectorAll('.bar.cl').forEach(bar => {
      bar.addEventListener('click', () => {
        const item = items[bar.dataset.idx];
        if (item && item.onClick) item.onClick();
      });
    });
  }
}
