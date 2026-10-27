"""
High-performance analytical computation engine for Flipkart Catalog Analytics.
Executes indexed SQL queries and financial scenario simulations.
"""

import sqlite3
from typing import Dict, Any, List, Optional
from .db import get_db_connection


def build_filter_clause(
    category: Optional[str] = None,
    sub_category: Optional[str] = None,
    is_fk_advantage: Optional[int] = None,
    query: Optional[str] = None
):
    """Construct WHERE clause and parameter list from query filters."""
    where_clauses = ["1=1"]
    params = []

    if category and category.lower() not in ("all", "all categories", ""):
        where_clauses.append("category = ?")
        params.append(category)

    if sub_category and sub_category.lower() not in ("all", "all sub-categories", "", "(none)"):
        where_clauses.append("sub_category = ?")
        params.append(sub_category)

    if is_fk_advantage is not None and is_fk_advantage != -1:
        where_clauses.append("is_fk_advantage = ?")
        params.append(int(is_fk_advantage))

    if query and query.strip():
        q_term = f"%{query.strip()}%"
        where_clauses.append("(product_name LIKE ? OR brand LIKE ? OR description LIKE ?)")
        params.extend([q_term, q_term, q_term])

    return " AND ".join(where_clauses), params


def get_filter_options() -> Dict[str, Any]:
    """Return available categories, subcategories, and top brands for dropdowns."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Primary categories
        cursor.execute("""
            SELECT category, count(*) as count 
            FROM products 
            GROUP BY category 
            ORDER BY count DESC
        """)
        cats = [row["category"] for row in cursor.fetchall()]
        
        # Sub-categories
        cursor.execute("""
            SELECT DISTINCT sub_category 
            FROM products 
            WHERE sub_category != '(none)' AND sub_category != ''
            ORDER BY sub_category ASC
        """)
        subs = [row["sub_category"] for row in cursor.fetchall()]
        
        # Top 50 brands
        cursor.execute("""
            SELECT brand, count(*) as cnt 
            FROM products 
            WHERE brand != 'Unbranded' AND brand != ''
            GROUP BY brand 
            ORDER BY cnt DESC 
            LIMIT 50
        """)
        brands = [row["brand"] for row in cursor.fetchall()]

    return {
        "categories": cats,
        "subcategories": subs,
        "brands": brands
    }


def get_overview_analytics(
    category: Optional[str] = None,
    sub_category: Optional[str] = None,
    is_fk_advantage: Optional[int] = None,
    query: Optional[str] = None
) -> Dict[str, Any]:
    """Compute KPIs, category distribution, discount depth, price bands, and crawl trends."""
    where_str, params = build_filter_clause(category, sub_category, is_fk_advantage, query)
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Aggregate KPIs
        cursor.execute(f"""
            SELECT 
                count(*) as total_listings,
                COALESCE(avg(retail_price), 0) as avg_retail_price,
                COALESCE(avg(discounted_price), 0) as avg_selling_price,
                COALESCE(avg(discount_pct), 0) as avg_discount_pct,
                COALESCE(sum(retail_price), 0) as total_retail_value,
                COALESCE(sum(discounted_price), 0) as total_selling_value,
                SUM(CASE WHEN is_fk_advantage = 1 THEN 1 ELSE 0 END) as fk_advantage_count,
                SUM(CASE WHEN product_rating IS NOT NULL THEN 1 ELSE 0 END) as rated_count,
                COALESCE(avg(product_rating), 0) as avg_product_rating,
                count(DISTINCT brand) as total_brands
            FROM products
            WHERE {where_str}
        """, params)
        kpi_row = cursor.fetchone()
        
        total = kpi_row["total_listings"]
        fk_cnt = kpi_row["fk_advantage_count"] or 0
        fk_pct = round((fk_cnt / total * 100.0), 1) if total > 0 else 0.0
        
        rated_cnt = kpi_row["rated_count"] or 0
        rated_pct = round((rated_cnt / total * 100.0), 1) if total > 0 else 0.0
        
        kpis = {
            "total_listings": total,
            "avg_retail_price": round(kpi_row["avg_retail_price"], 2),
            "avg_selling_price": round(kpi_row["avg_selling_price"], 2),
            "avg_discount_pct": round(kpi_row["avg_discount_pct"], 1),
            "total_retail_value": round(kpi_row["total_retail_value"], 2),
            "total_selling_value": round(kpi_row["total_selling_value"], 2),
            "fk_advantage_count": fk_cnt,
            "fk_advantage_pct": fk_pct,
            "rated_count": rated_cnt,
            "rated_pct": rated_pct,
            "avg_product_rating": round(kpi_row["avg_product_rating"], 2),
            "total_brands": kpi_row["total_brands"]
        }
        
        # 2. Category distribution
        cursor.execute(f"""
            SELECT 
                category,
                count(*) as count,
                round(avg(discount_pct), 1) as avg_discount,
                round(avg(discounted_price), 2) as avg_price
            FROM products
            WHERE {where_str}
            GROUP BY category
            ORDER BY count DESC
            LIMIT 15
        """, params)
        cats_data = []
        for r in cursor.fetchall():
            cats_data.append({
                "category": r["category"],
                "count": r["count"],
                "percentage": round((r["count"] / total * 100.0), 1) if total > 0 else 0,
                "avg_discount": r["avg_discount"] or 0.0,
                "avg_price": r["avg_price"] or 0.0
            })
            
        # 3. Discount depth buckets
        cursor.execute(f"""
            SELECT 
                CASE 
                    WHEN discount_pct <= 0 THEN '0% (No discount)'
                    WHEN discount_pct > 0 AND discount_pct <= 20 THEN '1% – 20%'
                    WHEN discount_pct > 20 AND discount_pct <= 40 THEN '21% – 40%'
                    WHEN discount_pct > 40 AND discount_pct <= 60 THEN '41% – 60%'
                    WHEN discount_pct > 60 AND discount_pct <= 80 THEN '61% – 80%'
                    ELSE '> 80%'
                END as bucket,
                CASE 
                    WHEN discount_pct <= 0 THEN 1
                    WHEN discount_pct > 0 AND discount_pct <= 20 THEN 2
                    WHEN discount_pct > 20 AND discount_pct <= 40 THEN 3
                    WHEN discount_pct > 40 AND discount_pct <= 60 THEN 4
                    WHEN discount_pct > 60 AND discount_pct <= 80 THEN 5
                    ELSE 6
                END as sort_order,
                count(*) as count
            FROM products
            WHERE {where_str}
            GROUP BY bucket, sort_order
            ORDER BY sort_order ASC
        """, params)
        discount_buckets = []
        for r in cursor.fetchall():
            discount_buckets.append({
                "label": r["bucket"],
                "count": r["count"],
                "percentage": round((r["count"] / total * 100.0), 1) if total > 0 else 0
            })

        # 4. Selling price bands
        cursor.execute(f"""
            SELECT 
                CASE 
                    WHEN discounted_price < 500 THEN 'Under ₹500'
                    WHEN discounted_price >= 500 AND discounted_price < 1000 THEN '₹500 – ₹1,000'
                    WHEN discounted_price >= 1000 AND discounted_price < 2500 THEN '₹1,000 – ₹2,500'
                    WHEN discounted_price >= 2500 AND discounted_price < 5000 THEN '₹2,500 – ₹5,000'
                    WHEN discounted_price >= 5000 AND discounted_price < 10000 THEN '₹5,000 – ₹10,000'
                    ELSE 'Above ₹10,000'
                END as band,
                CASE 
                    WHEN discounted_price < 500 THEN 1
                    WHEN discounted_price >= 500 AND discounted_price < 1000 THEN 2
                    WHEN discounted_price >= 1000 AND discounted_price < 2500 THEN 3
                    WHEN discounted_price >= 2500 AND discounted_price < 5000 THEN 4
                    WHEN discounted_price >= 5000 AND discounted_price < 10000 THEN 5
                    ELSE 6
                END as sort_order,
                count(*) as count
            FROM products
            WHERE {where_str}
            GROUP BY band, sort_order
            ORDER BY sort_order ASC
        """, params)
        price_bands = []
        for r in cursor.fetchall():
            price_bands.append({
                "label": r["band"],
                "count": r["count"],
                "percentage": round((r["count"] / total * 100.0), 1) if total > 0 else 0
            })

        # 5. Crawl month timeline
        cursor.execute(f"""
            SELECT 
                crawl_month,
                count(*) as count
            FROM products
            WHERE {where_str} AND crawl_month != 'Unknown'
            GROUP BY crawl_month
            ORDER BY crawl_month ASC
        """, params)
        month_rows = cursor.fetchall()
        crawl_months = []
        max_m_count = max([r["count"] for r in month_rows]) if month_rows else 1
        for r in month_rows:
            crawl_months.append({
                "month": r["crawl_month"],
                "count": r["count"],
                "pct_of_max": round((r["count"] / max_m_count * 100.0), 1),
                "percentage": round((r["count"] / total * 100.0), 1) if total > 0 else 0
            })

        # 6. Key analytical findings
        top_cat_name = cats_data[0]["category"] if cats_data else "None"
        top_cat_pct = cats_data[0]["percentage"] if cats_data else 0
        insights = [
            f"<strong>{top_cat_name}</strong> dominates catalog volume, accounting for <strong>{top_cat_pct}%</strong> of all filtered listings.",
            f"The overall average discount depth across listings is <strong>{kpis['avg_discount_pct']}%</strong>, showing aggressive promotional pricing.",
            f"Flipkart Advantage fulfillment represents <strong>{kpis['fk_advantage_pct']}%</strong> ({kpis['fk_advantage_count']:,} items) of the selection.",
            f"Rating coverage stands at <strong>{kpis['rated_pct']}%</strong> with an average score of <strong>{kpis['avg_product_rating']} / 5.0</strong>.",
            f"<strong>{len(cats_data)}</strong> categories active under the current filter slice with an average selling price of <strong>₹{kpis['avg_selling_price']:,}</strong>."
        ]

    return {
        "kpis": kpis,
        "insights": insights,
        "categories": cats_data,
        "discount_depth": discount_buckets,
        "price_bands": price_bands,
        "crawl_months": crawl_months
    }


def get_pricing_analytics(
    category: Optional[str] = None,
    sub_category: Optional[str] = None,
    is_fk_advantage: Optional[int] = None,
    query: Optional[str] = None
) -> Dict[str, Any]:
    """Compute price vs discount scatter points, category discounts, FK advantage comparison, and subcategories."""
    where_str, params = build_filter_clause(category, sub_category, is_fk_advantage, query)
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Price vs Discount Scatter plot (sampled to max 2,500 points for performance)
        cursor.execute(f"""
            SELECT 
                uniq_id,
                product_name,
                category,
                retail_price,
                discounted_price,
                discount_pct,
                is_fk_advantage
            FROM products
            WHERE {where_str} AND retail_price > 0 AND retail_price < 150000
            ORDER BY RANDOM()
            LIMIT 2500
        """, params)
        scatter_points = []
        for r in cursor.fetchall():
            scatter_points.append({
                "id": r["uniq_id"],
                "name": r["product_name"][:40],
                "cat": r["category"],
                "retail": r["retail_price"],
                "price": r["discounted_price"],
                "discount": r["discount_pct"],
                "fk": bool(r["is_fk_advantage"])
            })

        # 2. Average discount by category
        cursor.execute(f"""
            SELECT 
                category,
                count(*) as count,
                round(avg(discount_pct), 1) as avg_discount,
                round(avg(discounted_price), 2) as avg_price
            FROM products
            WHERE {where_str}
            GROUP BY category
            ORDER BY avg_discount DESC
        """, params)
        cat_discounts = [
            {
                "category": r["category"],
                "count": r["count"],
                "avg_discount": r["avg_discount"],
                "avg_price": r["avg_price"]
            }
            for r in cursor.fetchall()
        ]

        # 3. Flipkart Advantage vs Non-Advantage comparison
        cursor.execute(f"""
            SELECT 
                is_fk_advantage,
                count(*) as count,
                round(avg(retail_price), 2) as avg_retail,
                round(avg(discounted_price), 2) as avg_price,
                round(avg(discount_pct), 1) as avg_discount,
                round(avg(product_rating), 2) as avg_rating,
                SUM(CASE WHEN product_rating IS NOT NULL THEN 1 ELSE 0 END) as rated_count
            FROM products
            WHERE {where_str}
            GROUP BY is_fk_advantage
        """, params)
        rows = cursor.fetchall()
        fk_comparison = {
            "advantage": None,
            "non_advantage": None
        }
        for r in rows:
            data = {
                "count": r["count"],
                "avg_retail": r["avg_retail"] or 0,
                "avg_price": r["avg_price"] or 0,
                "avg_discount": r["avg_discount"] or 0,
                "avg_rating": r["avg_rating"] or 0,
                "rated_count": r["rated_count"] or 0
            }
            if r["is_fk_advantage"] == 1:
                fk_comparison["advantage"] = data
            else:
                fk_comparison["non_advantage"] = data

        # 4. Sub-category drill-down
        cursor.execute(f"""
            SELECT 
                sub_category,
                category,
                count(*) as listings_count,
                round(avg(retail_price), 2) as avg_retail,
                round(avg(discounted_price), 2) as avg_price,
                round(avg(discount_pct), 1) as avg_discount,
                round(SUM(CASE WHEN is_fk_advantage = 1 THEN 1.0 ELSE 0.0 END) / count(*) * 100, 1) as fk_pct
            FROM products
            WHERE {where_str} AND sub_category != '(none)'
            GROUP BY sub_category, category
            ORDER BY listings_count DESC
            LIMIT 40
        """, params)
        subcategories = [
            {
                "sub_category": r["sub_category"],
                "category": r["category"],
                "count": r["listings_count"],
                "avg_retail": r["avg_retail"],
                "avg_price": r["avg_price"],
                "avg_discount": r["avg_discount"],
                "fk_pct": r["fk_pct"]
            }
            for r in cursor.fetchall()
        ]

    return {
        "scatter_points": scatter_points,
        "category_discounts": cat_discounts,
        "fk_comparison": fk_comparison,
        "subcategories": subcategories
    }


def get_ratings_and_brands_analytics(
    category: Optional[str] = None,
    sub_category: Optional[str] = None,
    is_fk_advantage: Optional[int] = None,
    query: Optional[str] = None
) -> Dict[str, Any]:
    """Compute rating distribution, discount by rating, and top 30 brand leaderboard."""
    where_str, params = build_filter_clause(category, sub_category, is_fk_advantage, query)
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # 1. Rating distribution (1 to 5 stars + Unrated)
        cursor.execute(f"""
            SELECT 
                CASE 
                    WHEN product_rating IS NULL THEN 'Unrated'
                    WHEN round(product_rating) = 1 THEN '1 Star'
                    WHEN round(product_rating) = 2 THEN '2 Stars'
                    WHEN round(product_rating) = 3 THEN '3 Stars'
                    WHEN round(product_rating) = 4 THEN '4 Stars'
                    WHEN round(product_rating) >= 5 THEN '5 Stars'
                    ELSE 'Other'
                END as star_tier,
                CASE 
                    WHEN round(product_rating) = 1 THEN 1
                    WHEN round(product_rating) = 2 THEN 2
                    WHEN round(product_rating) = 3 THEN 3
                    WHEN round(product_rating) = 4 THEN 4
                    WHEN round(product_rating) >= 5 THEN 5
                    ELSE 0
                END as star_val,
                count(*) as count
            FROM products
            WHERE {where_str}
            GROUP BY star_tier, star_val
            ORDER BY star_val ASC
        """, params)
        rating_dist = []
        rated_total = 0
        all_rows = cursor.fetchall()
        for r in all_rows:
            if r["star_tier"] != "Unrated":
                rated_total += r["count"]
                
        for r in all_rows:
            pct = round((r["count"] / rated_total * 100.0), 1) if rated_total > 0 and r["star_tier"] != "Unrated" else 0
            rating_dist.append({
                "tier": r["star_tier"],
                "count": r["count"],
                "percentage": pct
            })

        # 2. Average discount by star rating
        cursor.execute(f"""
            SELECT 
                round(product_rating) as rating_group,
                round(avg(discount_pct), 1) as avg_discount,
                count(*) as count
            FROM products
            WHERE {where_str} AND product_rating IS NOT NULL
            GROUP BY rating_group
            ORDER BY rating_group ASC
        """, params)
        discount_by_rating = [
            {
                "rating": f"{int(r['rating_group'])} Star{'s' if r['rating_group'] > 1 else ''}",
                "avg_discount": r["avg_discount"],
                "count": r["count"]
            }
            for r in cursor.fetchall()
        ]

        # 3. Brand Leaderboard (Top 30 named brands)
        cursor.execute(f"""
            SELECT 
                brand,
                count(*) as listings_count,
                round(avg(discounted_price), 2) as avg_price,
                round(avg(discount_pct), 1) as avg_discount,
                round(avg(product_rating), 2) as avg_rating,
                SUM(CASE WHEN product_rating IS NOT NULL THEN 1 ELSE 0 END) as rating_count
            FROM products
            WHERE {where_str} AND brand != 'Unbranded' AND brand != ''
            GROUP BY brand
            ORDER BY listings_count DESC
            LIMIT 30
        """, params)
        brands = [
            {
                "brand": r["brand"],
                "count": r["listings_count"],
                "avg_price": r["avg_price"],
                "avg_discount": r["avg_discount"],
                "avg_rating": r["avg_rating"] or 0,
                "rating_count": r["rating_count"]
            }
            for r in cursor.fetchall()
        ]

    return {
        "rating_distribution": rating_dist,
        "discount_by_rating": discount_by_rating,
        "brand_leaderboard": brands
    }


def simulate_order_scenario(
    units_per_listing: int = 5,
    category: Optional[str] = None,
    sub_category: Optional[str] = None,
    is_fk_advantage: Optional[int] = None,
    query: Optional[str] = None
) -> Dict[str, Any]:
    """Model order demand scenario: multiplies price and discount by hypothetical units sold."""
    where_str, params = build_filter_clause(category, sub_category, is_fk_advantage, query)
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Overall Scenario Totals
        cursor.execute(f"""
            SELECT 
                count(*) as listings_count,
                sum(retail_price) as sum_retail,
                sum(discounted_price) as sum_selling
            FROM products
            WHERE {where_str}
        """, params)
        row = cursor.fetchone()
        
        listings = row["listings_count"] or 0
        tot_units = listings * units_per_listing
        tot_gmv = (row["sum_selling"] or 0.0) * units_per_listing
        tot_retail = (row["sum_retail"] or 0.0) * units_per_listing
        tot_discount_given = tot_retail - tot_gmv
        
        # Scenario by category
        cursor.execute(f"""
            SELECT 
                category,
                count(*) as count,
                sum(discounted_price * ?) as gmv,
                sum((retail_price - discounted_price) * ?) as discount_given
            FROM products
            WHERE {where_str}
            GROUP BY category
            ORDER BY gmv DESC
        """, [units_per_listing, units_per_listing] + params)
        cat_scenario = [
            {
                "category": r["category"],
                "count": r["count"],
                "projected_units": r["count"] * units_per_listing,
                "projected_gmv": round(r["gmv"] or 0.0, 2),
                "discount_given": round(r["discount_given"] or 0.0, 2)
            }
            for r in cursor.fetchall()
        ]

    return {
        "units_per_listing": units_per_listing,
        "projected_units": tot_units,
        "projected_gmv": round(tot_gmv, 2),
        "total_retail_value": round(tot_retail, 2),
        "total_discount_given": round(tot_discount_given, 2),
        "category_projections": cat_scenario
    }


def simulate_unit_economics(
    units_per_listing: int = 5,
    product_cost_pct: float = 35.0,
    commission_pct: float = 8.0,
    shipping_per_unit: float = 40.0,
    category: Optional[str] = None,
    sub_category: Optional[str] = None,
    is_fk_advantage: Optional[int] = None,
    query: Optional[str] = None
) -> Dict[str, Any]:
    """
    Simulate financial profit and loss (Unit Economics).
    Profit formula per listing:
    profit = (discounted_price - (retail_price * cost_pct / 100) - (discounted_price * commission_pct / 100) - shipping_per_unit) * units
    """
    where_str, params = build_filter_clause(category, sub_category, is_fk_advantage, query)
    
    cost_factor = product_cost_pct / 100.0
    comm_factor = commission_pct / 100.0
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Aggregated financial totals
        cursor.execute(f"""
            SELECT 
                count(*) as listings_count,
                sum(discounted_price * ?) as total_revenue,
                sum((retail_price * ?) * ?) as total_cogs,
                sum((discounted_price * ?) * ?) as total_commission,
                sum(? * ?) as total_shipping
            FROM products
            WHERE {where_str}
        """, [units_per_listing, cost_factor, units_per_listing, comm_factor, units_per_listing, shipping_per_unit, units_per_listing] + params)
        
        tot_row = cursor.fetchone()
        listings = tot_row["listings_count"] or 0
        rev = round(tot_row["total_revenue"] or 0.0, 2)
        cogs = round(tot_row["total_cogs"] or 0.0, 2)
        comm = round(tot_row["total_commission"] or 0.0, 2)
        ship = round(tot_row["total_shipping"] or 0.0, 2)
        net_profit = round(rev - (cogs + comm + ship), 2)
        net_margin = round((net_profit / rev * 100.0), 1) if rev > 0 else 0.0
        
        # Profit by category
        cursor.execute(f"""
            SELECT 
                category,
                count(*) as count,
                sum(discounted_price * ?) as rev,
                sum((retail_price * ?) * ?) as cogs,
                sum((discounted_price * ?) * ?) as comm,
                sum(? * ?) as ship
            FROM products
            WHERE {where_str}
            GROUP BY category
            ORDER BY rev DESC
        """, [units_per_listing, cost_factor, units_per_listing, comm_factor, units_per_listing, shipping_per_unit, units_per_listing] + params)
        cat_pnl = []
        for r in cursor.fetchall():
            c_rev = round(r["rev"] or 0.0, 2)
            c_cogs = round(r["cogs"] or 0.0, 2)
            c_comm = round(r["comm"] or 0.0, 2)
            c_ship = round(r["ship"] or 0.0, 2)
            c_prof = round(c_rev - (c_cogs + c_comm + c_ship), 2)
            c_mrg = round((c_prof / c_rev * 100.0), 1) if c_rev > 0 else 0.0
            cat_pnl.append({
                "category": r["category"],
                "count": r["count"],
                "revenue": c_rev,
                "cogs": c_cogs,
                "commission": c_comm,
                "shipping": c_ship,
                "profit": c_prof,
                "margin_pct": c_mrg
            })

        # Profit by crawl month
        cursor.execute(f"""
            SELECT 
                crawl_month,
                sum(discounted_price * ? - (retail_price * ? * ?) - (discounted_price * ? * ?) - (? * ?)) as profit
            FROM products
            WHERE {where_str} AND crawl_month != 'Unknown'
            GROUP BY crawl_month
            ORDER BY crawl_month ASC
        """, [units_per_listing, cost_factor, units_per_listing, comm_factor, units_per_listing, shipping_per_unit, units_per_listing] + params)
        profit_by_month = [
            {"month": r["crawl_month"], "profit": round(r["profit"] or 0.0, 2)}
            for r in cursor.fetchall()
        ]

        # Profit by discount depth
        cursor.execute(f"""
            SELECT 
                CASE 
                    WHEN discount_pct <= 0 THEN '0% (No discount)'
                    WHEN discount_pct > 0 AND discount_pct <= 20 THEN '1% – 20%'
                    WHEN discount_pct > 20 AND discount_pct <= 40 THEN '21% – 40%'
                    WHEN discount_pct > 40 AND discount_pct <= 60 THEN '41% – 60%'
                    WHEN discount_pct > 60 AND discount_pct <= 80 THEN '61% – 80%'
                    ELSE '> 80%'
                END as bucket,
                CASE 
                    WHEN discount_pct <= 0 THEN 1
                    WHEN discount_pct > 0 AND discount_pct <= 20 THEN 2
                    WHEN discount_pct > 20 AND discount_pct <= 40 THEN 3
                    WHEN discount_pct > 40 AND discount_pct <= 60 THEN 4
                    WHEN discount_pct > 60 AND discount_pct <= 80 THEN 5
                    ELSE 6
                END as sort_order,
                sum(discounted_price * ? - (retail_price * ? * ?) - (discounted_price * ? * ?) - (? * ?)) as profit
            FROM products
            WHERE {where_str}
            GROUP BY bucket, sort_order
            ORDER BY sort_order ASC
        """, [units_per_listing, cost_factor, units_per_listing, comm_factor, units_per_listing, shipping_per_unit, units_per_listing] + params)
        profit_by_discount = [
            {"bucket": r["bucket"], "profit": round(r["profit"] or 0.0, 2)}
            for r in cursor.fetchall()
        ]

        # Top 10 most profitable listings
        cursor.execute(f"""
            SELECT 
                uniq_id,
                product_name,
                category,
                retail_price,
                discounted_price,
                (discounted_price * ? - (retail_price * ? * ?) - (discounted_price * ? * ?) - (? * ?)) as item_profit
            FROM products
            WHERE {where_str}
            ORDER BY item_profit DESC
            LIMIT 10
        """, [units_per_listing, cost_factor, units_per_listing, comm_factor, units_per_listing, shipping_per_unit, units_per_listing] + params)
        top_profitable = [
            {
                "id": r["uniq_id"],
                "name": r["product_name"][:50],
                "category": r["category"],
                "price": r["discounted_price"],
                "profit": round(r["item_profit"], 2)
            }
            for r in cursor.fetchall()
        ]

        # Top 10 least profitable listings
        cursor.execute(f"""
            SELECT 
                uniq_id,
                product_name,
                category,
                retail_price,
                discounted_price,
                (discounted_price * ? - (retail_price * ? * ?) - (discounted_price * ? * ?) - (? * ?)) as item_profit
            FROM products
            WHERE {where_str}
            ORDER BY item_profit ASC
            LIMIT 10
        """, [units_per_listing, cost_factor, units_per_listing, comm_factor, units_per_listing, shipping_per_unit, units_per_listing] + params)
        least_profitable = [
            {
                "id": r["uniq_id"],
                "name": r["product_name"][:50],
                "category": r["category"],
                "price": r["discounted_price"],
                "profit": round(r["item_profit"], 2)
            }
            for r in cursor.fetchall()
        ]

    return {
        "parameters": {
            "units_per_listing": units_per_listing,
            "product_cost_pct": product_cost_pct,
            "commission_pct": commission_pct,
            "shipping_per_unit": shipping_per_unit
        },
        "kpis": {
            "total_listings": listings,
            "revenue": rev,
            "cogs": cogs,
            "commission": comm,
            "shipping": ship,
            "net_profit": net_profit,
            "net_margin_pct": net_margin
        },
        "pnl_by_category": cat_pnl,
        "profit_by_month": profit_by_month,
        "profit_by_discount": profit_by_discount,
        "top_profitable": top_profitable,
        "least_profitable": least_profitable
    }


def get_products_paginated(
    page: int = 1,
    limit: int = 25,
    sort_by: str = "discounted_price",
    sort_order: str = "desc",
    category: Optional[str] = None,
    sub_category: Optional[str] = None,
    is_fk_advantage: Optional[int] = None,
    query: Optional[str] = None
) -> Dict[str, Any]:
    """Retrieve paginated and filtered product records for the data explorer table."""
    where_str, params = build_filter_clause(category, sub_category, is_fk_advantage, query)
    
    valid_sort_cols = {
        "name": "product_name",
        "category": "category",
        "retail_price": "retail_price",
        "discounted_price": "discounted_price",
        "discount_pct": "discount_pct",
        "rating": "product_rating"
    }
    col = valid_sort_cols.get(sort_by, "discounted_price")
    order = "ASC" if sort_order.lower() == "asc" else "DESC"
    offset = max(0, (page - 1) * limit)
    
    with get_db_connection() as conn:
        cursor = conn.cursor()
        
        # Get filtered total
        cursor.execute(f"SELECT count(*) FROM products WHERE {where_str}", params)
        total_items = cursor.fetchone()[0]
        
        # Get page records
        cursor.execute(f"""
            SELECT 
                uniq_id,
                product_name,
                category,
                sub_category,
                retail_price,
                discounted_price,
                discount_pct,
                primary_image,
                is_fk_advantage,
                product_rating,
                brand,
                description
            FROM products
            WHERE {where_str}
            ORDER BY {col} {order}
            LIMIT ? OFFSET ?
        """, params + [limit, offset])
        
        products = []
        for r in cursor.fetchall():
            desc = r["description"] or ""
            products.append({
                "uniq_id": r["uniq_id"],
                "name": r["product_name"],
                "category": r["category"],
                "sub_category": r["sub_category"],
                "retail_price": r["retail_price"],
                "discounted_price": r["discounted_price"],
                "discount_pct": r["discount_pct"],
                "primary_image": r["primary_image"],
                "is_fk_advantage": bool(r["is_fk_advantage"]),
                "rating": r["product_rating"],
                "brand": r["brand"],
                "description_short": desc[:170] + "..." if len(desc) > 170 else desc
            })
            
    total_pages = (total_items + limit - 1) // limit if total_items > 0 else 1
    
    return {
        "items": products,
        "page": page,
        "limit": limit,
        "total_items": total_items,
        "total_pages": total_pages,
        "has_next": page < total_pages,
        "has_prev": page > 1
    }


def get_product_detail(uniq_id: str) -> Optional[Dict[str, Any]]:
    """Retrieve full metadata, images, and specifications for a single product."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE uniq_id = ?", [uniq_id])
        row = cursor.fetchone()
        if not row:
            return None
        
        import json
        images = []
        try:
            images = json.loads(row["images_json"]) if row["images_json"] else []
        except Exception:
            pass
            
        specs = []
        try:
            specs = json.loads(row["product_specifications"]) if row["product_specifications"] else []
        except Exception:
            pass

        return {
            "uniq_id": row["uniq_id"],
            "product_name": row["product_name"],
            "pid": row["pid"],
            "crawl_timestamp": row["crawl_timestamp"],
            "crawl_month": row["crawl_month"],
            "product_url": row["product_url"],
            "category_tree": row["product_category_tree"],
            "category": row["category"],
            "sub_category": row["sub_category"],
            "retail_price": row["retail_price"],
            "discounted_price": row["discounted_price"],
            "discount_pct": row["discount_pct"],
            "is_fk_advantage": bool(row["is_fk_advantage"]),
            "product_rating": row["product_rating"],
            "overall_rating": row["overall_rating"],
            "brand": row["brand"],
            "description": row["description"],
            "primary_image": row["primary_image"],
            "images": images,
            "specifications": specs
        }


def get_column_dictionary() -> List[Dict[str, str]]:
    """Metadata dictionary describing all 15 dataset columns."""
    return [
        {"column": "uniq_id", "type": "String (Hash)", "description": "Unique listing identifier generated during crawling"},
        {"column": "crawl_timestamp", "type": "Datetime String", "description": "Timestamp when product record was scraped (Dec 2015 – Jun 2016)"},
        {"column": "product_url", "type": "URL String", "description": "Canonical URL of the product page on Flipkart"},
        {"column": "product_name", "type": "Text", "description": "Full product title displayed to customers"},
        {"column": "product_category_tree", "type": "Hierarchy String", "description": "Full category path delimited by '>>' (e.g. Clothing >> Women >> Shorts)"},
        {"column": "pid", "type": "String", "description": "Flipkart internal Product Identification code"},
        {"column": "retail_price", "type": "Numeric (Float)", "description": "Maximum Retail Price (MRP / list price) in Indian Rupees (₹)"},
        {"column": "discounted_price", "type": "Numeric (Float)", "description": "Actual selling price after discounts in Indian Rupees (₹)"},
        {"column": "image", "type": "Array / URL", "description": "List of high-resolution product catalog image URLs"},
        {"column": "is_FK_Advantage_product", "type": "Boolean", "description": "True if fulfilled via Flipkart Advantage (fast dispatch & quality assurance)"},
        {"column": "description", "type": "Text", "description": "Detailed product description and marketing copy"},
        {"column": "product_rating", "type": "Numeric (1-5)", "description": "Average customer rating score (or 'No rating available')"},
        {"column": "overall_rating", "type": "Numeric (1-5)", "description": "Overall merchant / review rating score"},
        {"column": "brand", "type": "String", "description": "Manufacturer or brand name"},
        {"column": "product_specifications", "type": "Key-Value Structure", "description": "Technical attributes and specifications of the item"}
    ]
