import matplotlib.pyplot as plt
import numpy as np
import os

os.makedirs("fashion_retail/charts", exist_ok=True)

# Styling configurations for high-end luxury fashion analytics
plt.style.use('dark_background')
plt.rcParams['font.sans-serif'] = 'Helvetica, Arial, DejaVu Sans'
plt.rcParams['font.size'] = 11

# Palette: Luxury gold, rose, emerald, cyan, slate
c_gold = "#F59E0B"
c_rose = "#FB7185"
c_emerald = "#10B981"
c_cyan = "#38BDF8"
c_purple = "#C084FC"
c_dark = "#090D16"

# 1. Fashion Market Share by Revenue (2025-2026)
def plot_fashion_market():
    brands = ['LVMH Fashion\n(Luxury)', 'Inditex / Zara\n(Fast Fashion)', 'Nike Inc.\n(Sportswear)', 'Shein\n(Ultra-Fast)', 'Fast Retailing\n(Uniqlo)', 'H&M Group\n(Fast Fashion)']
    rev_billions = [46.2, 38.5, 51.4, 34.0, 20.8, 22.3] # In Billions USD
    colors = ['#F59E0B', '#FB7185', '#38BDF8', '#C084FC', '#10B981', '#94A3B8']

    fig, ax = plt.subplots(figsize=(10.5, 5.5), facecolor='#090D16')
    ax.set_facecolor('#090D16')

    y_pos = np.arange(len(brands))
    bars = ax.barh(y_pos, rev_billions, color=colors, edgecolor='#1E293B', height=0.6)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(brands, color='#F8FAFC', fontsize=11)
    ax.invert_yaxis()
    ax.set_xlabel('Annual Apparel & Footwear Revenue (USD $ Billions)', color='#E2E8F0', fontsize=12, labelpad=10)
    ax.set_title('Global Fashion Retail Giants: Annual Revenue Benchmarks (2025-2026)', color='#F8FAFC', fontsize=14, weight='bold', pad=15)
    ax.grid(axis='x', linestyle='--', alpha=0.2, color='#94A3B8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#334155')
    ax.spines['bottom'].set_color('#334155')

    for bar in bars:
        w = bar.get_width()
        ax.annotate(f'${w}B',
                    xy=(w, bar.get_y() + bar.get_height()/2),
                    xytext=(6, 0),
                    textcoords="offset points",
                    ha='left', va='center',
                    color='#F8FAFC', fontsize=11, weight='bold')

    plt.tight_layout()
    plt.savefig('fashion_retail/charts/fashion_market_share.png', dpi=300)
    plt.close()
    print("Generated fashion_retail/charts/fashion_market_share.png")

# 2. Omnichannel Retail Sales Channel Evolution
def plot_channel_evolution():
    years = ['2019', '2020', '2021', '2022', '2023', '2024', '2025E', '2026E']
    instore = [78, 62, 64, 61, 58, 55, 52, 50]
    ecommerce = [18, 32, 28, 29, 30, 31, 32, 33]
    social_live = [4, 6, 8, 10, 12, 14, 16, 17]

    fig, ax = plt.subplots(figsize=(10, 5.5), facecolor='#090D16')
    ax.set_facecolor('#090D16')

    ax.plot(years, instore, marker='o', linewidth=3, color='#F59E0B', label='Physical In-Store (%)')
    ax.plot(years, ecommerce, marker='s', linewidth=3, color='#38BDF8', label='E-Commerce / DTC (%)')
    ax.plot(years, social_live, marker='^', linewidth=3, color='#FB7185', label='Social & Live Commerce (%)')

    ax.fill_between(years, instore, color='#F59E0B', alpha=0.1)
    ax.fill_between(years, ecommerce, color='#38BDF8', alpha=0.1)
    ax.fill_between(years, social_live, color='#FB7185', alpha=0.1)

    ax.set_ylabel('Share of Total Fashion Sales (%)', color='#E2E8F0', fontsize=12, labelpad=10)
    ax.set_title('Global Fashion Sales Channel Shift: The Omnichannel Convergence', color='#F8FAFC', fontsize=14, weight='bold', pad=15)
    ax.legend(facecolor='#162036', edgecolor='#334155', labelcolor='#F8FAFC', fontsize=11)
    ax.grid(axis='y', linestyle='--', alpha=0.2, color='#94A3B8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#334155')
    ax.spines['bottom'].set_color('#334155')

    plt.tight_layout()
    plt.savefig('fashion_retail/charts/omnichannel_sales_split.png', dpi=300)
    plt.close()
    print("Generated fashion_retail/charts/omnichannel_sales_split.png")

# 3. Design-to-Rack Lead Time vs Inventory Turns
def plot_speed_vs_turns():
    models = ['Shein (Ultra-Fast)', 'Zara (Agile Fast)', 'Uniqlo (Core Basics)', 'H&M (Fast Fashion)', 'Traditional Apparel']
    lead_times = [7, 15, 45, 60, 180] # In Days (Design to Rack)
    turns = [12.5, 8.2, 5.5, 4.2, 2.8] # Annual Inventory Turns

    fig, ax1 = plt.subplots(figsize=(10.5, 5.5), facecolor='#090D16')
    ax1.set_facecolor('#090D16')

    x = np.arange(len(models))
    width = 0.35

    rects1 = ax1.bar(x - width/2, lead_times, width, label='Design-to-Rack Lead Time (Days - Lower is Better)', color='#FB7185', edgecolor='#E11D48')
    ax1.set_ylabel('Lead Time (Days)', color='#FB7185', fontsize=12)
    ax1.tick_params(axis='y', labelcolor='#FB7185')

    ax2 = ax1.twinx()
    rects2 = ax2.bar(x + width/2, turns, width, label='Annual Inventory Turns (Higher is Better)', color='#10B981', edgecolor='#059669')
    ax2.set_ylabel('Inventory Turns / Year', color='#10B981', fontsize=12)
    ax2.tick_params(axis='y', labelcolor='#10B981')

    ax1.set_xticks(x)
    ax1.set_xticklabels(models, color='#F8FAFC', fontsize=10.5)
    ax1.set_title('Retail Velocity: Design-to-Rack Lead Time vs. Inventory Turns', color='#F8FAFC', fontsize=14, weight='bold', pad=15)

    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax1.spines['left'].set_color('#334155')
    ax1.spines['bottom'].set_color('#334155')

    for rect in rects1:
        h = rect.get_height()
        ax1.annotate(f'{int(h)}d', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                     textcoords="offset points", ha='center', va='bottom', color='#FB7185', fontsize=10, weight='bold')

    for rect in rects2:
        h = rect.get_height()
        ax2.annotate(f'{h}x', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                     textcoords="offset points", ha='center', va='bottom', color='#10B981', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig('fashion_retail/charts/inventory_turnover_leadtime.png', dpi=300)
    plt.close()
    print("Generated fashion_retail/charts/inventory_turnover_leadtime.png")

# 4. Fashion Garment Unit Economics ($100 Retail Price Breakdown)
def plot_unit_economics():
    components = [
        'Raw Materials & Garment Manufacturing (CMT)',
        'Inbound Freight, Duties & Customs',
        'Store Rent, Utilities & Retail Labor',
        'Marketing, Customer Acquisition (CAC) & Ads',
        'Reverse Logistics & Returns Processing (25% rate)',
        'Markdown Discounts & Clearance Write-downs',
        'Net Operating Profit (EBIT Margin)'
    ]
    costs = [22, 6, 24, 14, 11, 13, 10] # Total $100
    colors = ['#F59E0B', '#FBBF24', '#38BDF8', '#C084FC', '#FB7185', '#E11D48', '#10B981']

    fig, ax = plt.subplots(figsize=(10.5, 5.8), facecolor='#090D16')
    ax.set_facecolor('#090D16')

    y_pos = np.arange(len(components))
    bars = ax.barh(y_pos, costs, color=colors, edgecolor='#1E293B', height=0.65)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(components, color='#E2E8F0', fontsize=10)
    ax.invert_yaxis()
    ax.set_xlabel('Dollar Allocation per $100 Retail Garment (USD $)', color='#E2E8F0', fontsize=12, labelpad=10)
    ax.set_title('Fashion Retail Unit Economics: Breakdown of a $100 Retail Garment', color='#F8FAFC', fontsize=14, weight='bold', pad=15)
    ax.grid(axis='x', linestyle='--', alpha=0.2, color='#94A3B8')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#334155')
    ax.spines['bottom'].set_color('#334155')

    for bar in bars:
        w = bar.get_width()
        pct = (w / sum(costs)) * 100
        ax.annotate(f'${w} ({pct:.0f}%)',
                    xy=(w, bar.get_y() + bar.get_height()/2),
                    xytext=(6, 0),
                    textcoords="offset points",
                    ha='left', va='center',
                    color='#F8FAFC', fontsize=10, weight='bold')

    plt.tight_layout()
    plt.savefig('fashion_retail/charts/retail_cost_breakdown.png', dpi=300)
    plt.close()
    print("Generated fashion_retail/charts/retail_cost_breakdown.png")

# 5. Strategic Agility & Business Model Radar
def plot_fashion_radar():
    categories = ['Speed-to-Market', 'Full-Price Sell-Through', 'E-Commerce Penetration', 'Gross Margin Power', 'Sustainability Score']
    N = len(categories)

    zara = [9, 8, 6, 8, 6]       # Inditex/Zara
    shein = [10, 5, 10, 6, 2]     # Shein (Ultra fast, low sustainability)
    nike = [6, 7, 7, 8, 7]       # Nike (High brand equity)
    lvmh = [4, 10, 4, 10, 8]      # Luxury (Highest margin, low discounting)

    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8.5, 7.5), subplot_kw=dict(polar=True), facecolor='#090D16')
    ax.set_facecolor('#0F172A')

    plt.xticks(angles[:-1], categories, color='#E2E8F0', size=10)
    ax.tick_params(colors='#94A3B8', pad=15)
    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8, 10], ["2", "4", "6", "8", "10"], color="#64748B", size=9)
    plt.ylim(0, 10)

    def add_brand(data, label, color):
        d = data + data[:1]
        ax.plot(angles, d, linewidth=2, linestyle='solid', label=label, color=color)
        ax.fill(angles, d, color=color, alpha=0.15)

    add_brand(zara, 'Zara (Inditex)', '#FB7185')
    add_brand(shein, 'Shein (Ultra-Fast)', '#C084FC')
    add_brand(nike, 'Nike Inc.', '#38BDF8')
    add_brand(lvmh, 'LVMH (Luxury)', '#F59E0B')

    plt.title('Fashion Retail Agility & Competitiveness Radar (Scale 1-10)', color='#F8FAFC', size=14, weight='bold', pad=25)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.15), facecolor='#162036', edgecolor='#334155', labelcolor='#F8FAFC')
    plt.tight_layout()
    plt.savefig('fashion_retail/charts/brand_resilience_radar.png', dpi=300)
    plt.close()
    print("Generated fashion_retail/charts/brand_resilience_radar.png")

if __name__ == '__main__':
    plot_fashion_market()
    plot_channel_evolution()
    plot_speed_vs_turns()
    plot_unit_economics()
    plot_fashion_radar()
    print("All fashion retail charts generated successfully!")
