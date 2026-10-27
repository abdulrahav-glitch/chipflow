import matplotlib.pyplot as plt
import numpy as np
import os

# Set working directory
os.makedirs("charts", exist_ok=True)

# Styling configurations for high-end executive charts
plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans'
plt.rcParams['font.size'] = 11

# Palette
c_navy = "#0F172A"
c_blue = "#38BDF8"
c_orange = "#FB923C"
c_emerald = "#34D399"
c_purple = "#A78BFA"
c_rose = "#F43F5E"
c_amber = "#FBBF24"
c_gray = "#94A3B8"

# 1. Market Share by Unit Volume vs Revenue
def plot_market_share():
    companies = ['MediaTek', 'Qualcomm', 'Apple', 'Unisoc', 'Samsung', 'HiSilicon / Other']
    unit_share = [37, 28, 18, 9, 5, 3] # Global unit volume %
    revenue_share = [17, 34, 38, 3, 5, 3] # Global revenue % (Apple & Qualcomm capture value)

    x = np.arange(len(companies))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 5.5), facecolor='#0B1120')
    ax.set_facecolor('#0B1120')

    rects1 = ax.bar(x - width/2, unit_share, width, label='Unit Volume Share (%)', color='#38BDF8', edgecolor='#0284C7', alpha=0.9)
    rects2 = ax.bar(x + width/2, revenue_share, width, label='Revenue Value Share (%)', color='#FB923C', edgecolor='#EA580C', alpha=0.9)

    ax.set_ylabel('Percentage Share (%)', color='#E2E8F0', fontsize=12, labelpad=10)
    ax.set_title('Global Smartphone SoC Market: Unit Volume vs. Revenue Value (2025-2026)', color='#F8FAFC', fontsize=14, weight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(companies, color='#E2E8F0', fontsize=11)
    ax.legend(facecolor='#1E293B', edgecolor='#334155', labelcolor='#F8FAFC', fontsize=11)
    ax.grid(axis='y', linestyle='--', alpha=0.2, color='#94A3B8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#334155')
    ax.spines['bottom'].set_color('#334155')

    # Add data values on bars
    for rect in rects1:
        h = rect.get_height()
        ax.annotate(f'{h}%', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom', color='#38BDF8', fontsize=10, weight='bold')
    for rect in rects2:
        h = rect.get_height()
        ax.annotate(f'{h}%', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                    textcoords="offset points", ha='center', va='bottom', color='#FB923C', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig('charts/market_share_soc.png', dpi=300)
    plt.close()
    print("Generated charts/market_share_soc.png")

# 2. Advanced Semiconductor Foundry Share (<5nm Nodes)
def plot_foundry_share():
    labels = ['TSMC\n(Taiwan)', 'Samsung Foundry\n(South Korea)', 'Intel Foundry\n(US/EU/External)', 'SMIC\n(China - DUV Multi)']
    sizes = [87, 10, 1.5, 1.5]
    colors = ['#38BDF8', '#818CF8', '#34D399', '#F43F5E']
    explode = (0.05, 0.05, 0, 0)

    fig, ax = plt.subplots(figsize=(8.5, 5.5), facecolor='#0B1120')
    ax.set_facecolor('#0B1120')

    wedges, texts, autotexts = ax.pie(
        sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        startangle=140, colors=colors,
        textprops=dict(color="#F8FAFC", fontsize=11),
        wedgeprops=dict(width=0.6, edgecolor='#0B1120', linewidth=2)
    )

    for autotext in autotexts:
        autotext.set_color('#0B1120')
        autotext.set_weight('bold')
        autotext.set_fontsize(11)

    ax.set_title('Sub-5nm Advanced Node Wafer Fabrication Capacity (<5nm)', color='#F8FAFC', fontsize=14, weight='bold', pad=15)
    plt.tight_layout()
    plt.savefig('charts/foundry_advanced_nodes.png', dpi=300)
    plt.close()
    print("Generated charts/foundry_advanced_nodes.png")

# 3. Smartphone BOM Breakdown - Flagship Tier ($1,000+ Device)
def plot_bom_breakdown():
    components = [
        'Application Processor (SoC)\n[Apple A18 / Snap 8 Elite / Dimensity 9400]',
        'Display & Touch Subsystem\n[LTPO OLED Samsung/LG]',
        'Camera Module Subsystem\n[Sony Sensors, Periscope Lenses]',
        'Memory & Storage\n[16GB LPDDR5X + 512GB UFS 4.0 / NVMe]',
        'Mechanical, Casing & Battery\n[Titanium/Alloy frame, Glass]',
        'RF Front-End, Modem & Wi-Fi/BT\n[5G mmWave/Sub-6, Transceivers]',
        'Assembly, Power & Passive ICs\n[PMIC, SMT, Testing, Packaging]'
    ]
    costs = [165, 95, 88, 62, 58, 48, 44] # USD cost estimates
    colors = ['#F43F5E', '#38BDF8', '#A78BFA', '#34D399', '#FBBF24', '#818CF8', '#94A3B8']

    fig, ax = plt.subplots(figsize=(10.5, 5.8), facecolor='#0B1120')
    ax.set_facecolor('#0B1120')

    y_pos = np.arange(len(components))
    bars = ax.barh(y_pos, costs, color=colors, edgecolor='#1E293B', height=0.65)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(components, color='#E2E8F0', fontsize=10)
    ax.invert_yaxis()  # Highest on top
    ax.set_xlabel('Estimated Bill of Materials Cost (USD $)', color='#E2E8F0', fontsize=12, labelpad=10)
    ax.set_title('Estimated Bill of Materials (BOM) Breakdown - Premium Flagship ($560 Total BOM)', color='#F8FAFC', fontsize=14, weight='bold', pad=15)
    ax.grid(axis='x', linestyle='--', alpha=0.2, color='#94A3B8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#334155')
    ax.spines['bottom'].set_color('#334155')

    for bar in bars:
        w = bar.get_width()
        pct = (w / sum(costs)) * 100
        ax.annotate(f'${w} ({pct:.1f}%)',
                    xy=(w, bar.get_y() + bar.get_height()/2),
                    xytext=(5, 0),
                    textcoords="offset points",
                    ha='left', va='center',
                    color='#F8FAFC', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig('charts/bom_cost_breakdown.png', dpi=300)
    plt.close()
    print("Generated charts/bom_cost_breakdown.png")

# 4. Strategic Vulnerability & Resilience Matrix (Radar Chart)
def plot_resilience_radar():
    categories = ['Foundry\nDiversification', 'Geopolitical\nInsulation', 'Margin / Pricing\nPower', 'Architectural\nIndependence', 'Packaging\nControl']
    N = len(categories)
    
    # Values out of 10
    apple = [3, 4, 10, 9, 9]     # TSMC dependent, high margins, custom microarch, InFO packaging
    qualcomm = [6, 6, 8, 8, 6]  # TSMC+Samsung, merchant pricing, Oryon core, OSAT partners
    mediatek = [4, 5, 6, 4, 5]  # TSMC dependent, lower margins, standard ARM cores
    samsung = [9, 8, 5, 5, 7]   # In-house foundry, Korea-based, lower yield/margins
    hisilicon = [2, 2, 4, 7, 5] # Heavily restricted, domestic SMIC reliance, China ecosystem

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1] # close loop

    fig, ax = plt.subplots(figsize=(8, 7.5), subplot_kw=dict(polar=True), facecolor='#0B1120')
    ax.set_facecolor('#0F172A')

    # Draw one axe per variable and add labels
    plt.xticks(angles[:-1], categories, color='#E2E8F0', size=10)
    ax.tick_params(colors='#94A3B8', pad=15)
    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="#64748B", size=9)
    plt.ylim(0, 10)

    # Plot each company
    def add_company(data, label, color):
        d = data + data[:1]
        ax.plot(angles, d, linewidth=2, linestyle='solid', label=label, color=color)
        ax.fill(angles, d, color=color, alpha=0.15)

    add_company(apple, 'Apple Silicon', '#38BDF8')
    add_company(qualcomm, 'Qualcomm', '#FB923C')
    add_company(mediatek, 'MediaTek', '#34D399')
    add_company(samsung, 'Samsung (Exynos)', '#A78BFA')

    plt.title('Supply Chain Resilience & Strategic Control Comparison (Scale 1-10)', color='#F8FAFC', size=14, weight='bold', pad=25)
    plt.legend(loc='upper right', bbox_to_anchor=(1.25, 1.15), facecolor='#1E293B', edgecolor='#334155', labelcolor='#F8FAFC')
    plt.tight_layout()
    plt.savefig('charts/company_resilience_radar.png', dpi=300)
    plt.close()
    print("Generated charts/company_resilience_radar.png")

# 5. Wafer Cost Escalation Across Fabrication Nodes
def plot_wafer_cost():
    nodes = ['28nm\n(2011)', '16/14nm\n(2014)', '10nm\n(2016)', '7nm\n(2018)', '5nm\n(2020)', '3nm\n(2023)', '2nm (GAA)\n(2025-26E)']
    wafer_costs = [3000, 4500, 6000, 9500, 16000, 20500, 28000] # In USD per 300mm processed wafer

    fig, ax = plt.subplots(figsize=(10, 5.2), facecolor='#0B1120')
    ax.set_facecolor('#0B1120')

    x = np.arange(len(nodes))
    line = ax.plot(x, wafer_costs, marker='o', markersize=9, color='#38BDF8', linewidth=3, label='Processed 300mm Wafer Cost ($)')
    ax.fill_between(x, wafer_costs, color='#38BDF8', alpha=0.15)

    ax.set_ylabel('Cost per Wafer (USD $)', color='#E2E8F0', fontsize=12, labelpad=10)
    ax.set_title('Escalation of Advanced Semiconductor Wafer Costs by Fabrication Node', color='#F8FAFC', fontsize=14, weight='bold', pad=15)
    ax.set_xticks(x)
    ax.set_xticklabels(nodes, color='#E2E8F0', fontsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.2, color='#94A3B8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#334155')
    ax.spines['bottom'].set_color('#334155')

    for i, txt in enumerate(wafer_costs):
        ax.annotate(f"${txt:,}", (x[i], wafer_costs[i]), xytext=(0, 10), textcoords="offset points",
                    ha='center', color='#F8FAFC', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig('charts/wafer_cost_escalation.png', dpi=300)
    plt.close()
    print("Generated charts/wafer_cost_escalation.png")

if __name__ == '__main__':
    plot_market_share()
    plot_foundry_share()
    plot_bom_breakdown()
    plot_resilience_radar()
    plot_wafer_cost()
    print("All charts generated successfully!")
