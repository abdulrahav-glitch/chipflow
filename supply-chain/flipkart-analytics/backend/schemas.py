"""
Pydantic schemas and request models for Flipkart Catalog Analytics API.
"""

from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field


class FilterOptionsResponse(BaseModel):
    categories: List[str]
    subcategories: List[str]
    brands: List[str]


class ScenarioRequest(BaseModel):
    units_per_listing: int = Field(5, ge=1, le=100, description="Hypothetical units sold per listing")
    category: Optional[str] = None
    sub_category: Optional[str] = None
    is_fk_advantage: Optional[int] = -1
    query: Optional[str] = None


class UnitEconomicsRequest(BaseModel):
    units_per_listing: int = Field(5, ge=1, le=100)
    product_cost_pct: float = Field(35.0, ge=0.0, le=100.0, description="Product cost as % of retail list price")
    commission_pct: float = Field(8.0, ge=0.0, le=50.0, description="Platform commission as % of selling price")
    shipping_per_unit: float = Field(40.0, ge=0.0, le=500.0, description="Shipping cost per unit in ₹")
    category: Optional[str] = None
    sub_category: Optional[str] = None
    is_fk_advantage: Optional[int] = -1
    query: Optional[str] = None


class ProductListItem(BaseModel):
    uniq_id: str
    name: str
    category: str
    sub_category: str
    retail_price: float
    discounted_price: float
    discount_pct: float
    primary_image: str
    is_fk_advantage: bool
    rating: Optional[float]
    brand: str
    description_short: str


class ProductDetailResponse(BaseModel):
    uniq_id: str
    product_name: str
    pid: str
    crawl_timestamp: str
    crawl_month: str
    product_url: str
    category_tree: str
    category: str
    sub_category: str
    retail_price: float
    discounted_price: float
    discount_pct: float
    is_fk_advantage: bool
    product_rating: Optional[float]
    overall_rating: Optional[float]
    brand: str
    description: str
    primary_image: str
    images: List[str]
    specifications: List[Dict[str, Any]]
