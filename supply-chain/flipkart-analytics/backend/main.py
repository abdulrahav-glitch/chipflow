"""
FastAPI Backend Application for Flipkart Catalog Analytics.
Exposes high-speed analytical APIs, simulated order scenarios, unit economics,
and paginated catalog exploration for 20,000 Flipkart products.
"""

import os
from pathlib import Path
from typing import Optional
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from .db import init_db, DB_PATH
from .analytics import (
    get_filter_options,
    get_overview_analytics,
    get_pricing_analytics,
    get_ratings_and_brands_analytics,
    simulate_order_scenario,
    simulate_unit_economics,
    get_products_paginated,
    get_product_detail,
    get_column_dictionary
)
from .schemas import (
    FilterOptionsResponse,
    ScenarioRequest,
    UnitEconomicsRequest,
    ProductDetailResponse
)

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

app = FastAPI(
    title="Flipkart Catalog Analytics API",
    description="Backend analytics engine for 20,000 Flipkart ecommerce listings (Dec 2015 – Jun 2016)",
    version="1.0.0"
)

# Enable CORS for cross-origin frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup_event():
    """Ensure database exists and is properly seeded."""
    if not DB_PATH.exists():
        print("Database not found on startup, initializing...")
        init_db()


# ─────────────────────────────────────────────────────────────
# API Endpoints
# ─────────────────────────────────────────────────────────────

@app.get("/api/health")
def health_check():
    """Health check endpoint and dataset status."""
    return {
        "status": "healthy",
        "service": "Flipkart Catalog Analytics API",
        "database_ready": DB_PATH.exists()
    }


@app.get("/api/filters", response_model=FilterOptionsResponse)
def get_filters():
    """Retrieve unique primary categories, subcategories, and top brands for filter controls."""
    return get_filter_options()


@app.get("/api/analytics/overview")
def get_overview(
    category: Optional[str] = Query(None, description="Primary category filter"),
    sub_category: Optional[str] = Query(None, description="Sub-category filter"),
    fk: Optional[int] = Query(-1, description="-1: All, 1: FK Advantage only, 0: Non-advantage"),
    q: Optional[str] = Query(None, description="Search query across product name, brand, description")
):
    """
    View 0 Analytics:
    Aggregate KPIs, key findings insights, listings by category,
    discount depth distribution, price bands, and crawl month trends.
    """
    return get_overview_analytics(
        category=category,
        sub_category=sub_category,
        is_fk_advantage=fk,
        query=q
    )


@app.get("/api/analytics/pricing")
def get_pricing(
    category: Optional[str] = Query(None),
    sub_category: Optional[str] = Query(None),
    fk: Optional[int] = Query(-1),
    q: Optional[str] = Query(None)
):
    """
    View 1 Analytics:
    Price vs discount scatter plot data (sampled to 2,500 points),
    category average discounts, Flipkart Advantage vs other listings comparison,
    and sub-category drill-down metrics.
    """
    return get_pricing_analytics(
        category=category,
        sub_category=sub_category,
        is_fk_advantage=fk,
        query=q
    )


@app.get("/api/analytics/ratings")
def get_ratings(
    category: Optional[str] = Query(None),
    sub_category: Optional[str] = Query(None),
    fk: Optional[int] = Query(-1),
    q: Optional[str] = Query(None)
):
    """
    View 2 Analytics:
    Rating score distribution (1 to 5 stars), average discount depth by star rating,
    and brand leaderboard of top 30 brands.
    """
    return get_ratings_and_brands_analytics(
        category=category,
        sub_category=sub_category,
        is_fk_advantage=fk,
        query=q
    )


@app.post("/api/analytics/scenario")
def post_scenario(req: ScenarioRequest):
    """
    View 3 Analytics:
    What-if order demand simulator. Multiplies assumed sales volume across listings
    to project Gross Merchandise Value (GMV) and discounts given away.
    """
    return simulate_order_scenario(
        units_per_listing=req.units_per_listing,
        category=req.category,
        sub_category=req.sub_category,
        is_fk_advantage=req.is_fk_advantage,
        query=req.query
    )


@app.post("/api/analytics/unit-economics")
def post_unit_economics(req: UnitEconomicsRequest):
    """
    View 5 Analytics:
    Modelled sales and profit simulator. Computes net margins, COGS, commission,
    shipping per unit, category P&L, crawl month profit, and top/bottom performers.
    """
    return simulate_unit_economics(
        units_per_listing=req.units_per_listing,
        product_cost_pct=req.product_cost_pct,
        commission_pct=req.commission_pct,
        shipping_per_unit=req.shipping_per_unit,
        category=req.category,
        sub_category=req.sub_category,
        is_fk_advantage=req.is_fk_advantage,
        query=req.query
    )


@app.get("/api/products")
def get_products(
    page: int = Query(1, ge=1),
    limit: int = Query(25, ge=1, le=100),
    sort_by: str = Query("discounted_price", description="name, category, retail_price, discounted_price, discount_pct, rating"),
    sort_order: str = Query("desc", description="asc or desc"),
    category: Optional[str] = Query(None),
    sub_category: Optional[str] = Query(None),
    fk: Optional[int] = Query(-1),
    q: Optional[str] = Query(None)
):
    """
    View 4 Data Reference:
    Paginated, sorted, and filtered catalog table.
    """
    return get_products_paginated(
        page=page,
        limit=limit,
        sort_by=sort_by,
        sort_order=sort_order,
        category=category,
        sub_category=sub_category,
        is_fk_advantage=fk,
        query=q
    )


@app.get("/api/products/{uniq_id}", response_model=ProductDetailResponse)
def get_product(uniq_id: str):
    """Retrieve full product listing record, all images, and technical specifications."""
    detail = get_product_detail(uniq_id)
    if not detail:
        raise HTTPException(status_code=404, detail="Product not found")
    return detail


@app.get("/api/dictionary")
def get_dictionary():
    """Metadata schema definition for the 15 dataset columns."""
    return get_column_dictionary()


# ─────────────────────────────────────────────────────────────
# Mount static frontend files if folder exists
# ─────────────────────────────────────────────────────────────
if FRONTEND_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")

    @app.get("/")
    def serve_frontend():
        """Serve the frontend dashboard."""
        index_file = FRONTEND_DIR / "index.html"
        if index_file.exists():
            return FileResponse(str(index_file))
        return {"message": "Frontend not found at " + str(index_file)}
