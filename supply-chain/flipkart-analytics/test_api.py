"""
Automated backend verification script.
Tests all endpoints directly using FastAPI TestClient without needing a live network port.
"""

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_endpoints():
    print("Testing /api/health...")
    r = client.get("/api/health")
    assert r.status_code == 200, f"Health check failed: {r.text}"
    print("✓ Health check passed:", r.json())

    print("Testing /api/filters...")
    r = client.get("/api/filters")
    assert r.status_code == 200
    filters = r.json()
    print(f"✓ Filters: {len(filters['categories'])} categories, {len(filters['subcategories'])} subcategories, {len(filters['brands'])} brands")

    print("Testing /api/analytics/overview...")
    r = client.get("/api/analytics/overview")
    assert r.status_code == 200
    ov = r.json()
    print("✓ Overview KPIs:", ov["kpis"]["total_listings"], "listings, avg selling price ₹", ov["kpis"]["avg_selling_price"])
    print("  Insights sample:", ov["insights"][0])

    print("Testing /api/analytics/pricing...")
    r = client.get("/api/analytics/pricing")
    assert r.status_code == 200
    pr = r.json()
    print(f"✓ Pricing: {len(pr['scatter_points'])} scatter points, {len(pr['category_discounts'])} cat discounts")

    print("Testing /api/analytics/ratings...")
    r = client.get("/api/analytics/ratings")
    assert r.status_code == 200
    rt = r.json()
    print(f"✓ Ratings: {len(rt['rating_distribution'])} tiers, top brand: {rt['brand_leaderboard'][0]['brand']}")

    print("Testing /api/analytics/scenario (POST)...")
    r = client.post("/api/analytics/scenario", json={"units_per_listing": 10})
    assert r.status_code == 200
    sc = r.json()
    print(f"✓ Scenario: Projected GMV for 10 units = ₹{sc['projected_gmv']:,}")

    print("Testing /api/analytics/unit-economics (POST)...")
    r = client.post("/api/analytics/unit-economics", json={
        "units_per_listing": 5,
        "product_cost_pct": 35.0,
        "commission_pct": 8.0,
        "shipping_per_unit": 40.0
    })
    assert r.status_code == 200
    ue = r.json()
    print(f"✓ Unit Economics: Revenue = ₹{ue['kpis']['revenue']:,}, Net Profit = ₹{ue['kpis']['net_profit']:,}, Margin = {ue['kpis']['net_margin_pct']}%")

    print("Testing /api/products (pagination)...")
    r = client.get("/api/products?page=1&limit=5")
    assert r.status_code == 200
    prods = r.json()
    print(f"✓ Products: Total {prods['total_items']} items, {len(prods['items'])} in page 1")
    first_id = prods["items"][0]["uniq_id"]

    print(f"Testing /api/products/{first_id}...")
    r = client.get(f"/api/products/{first_id}")
    assert r.status_code == 200
    detail = r.json()
    print(f"✓ Detail: '{detail['product_name'][:40]}' | {len(detail['specifications'])} specifications")

    print("\nALL BACKEND API TESTS PASSED SUCCESSFULLY! 🚀")

if __name__ == "__main__":
    test_endpoints()
