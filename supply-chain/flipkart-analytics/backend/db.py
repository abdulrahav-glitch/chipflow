"""
Database setup, schema definition, and CSV data ingestion for Flipkart Catalog Analytics.
Loads 20,000 product records into an optimized, indexed SQLite database.
"""

import os
import csv
import json
import re
import sqlite3
from pathlib import Path
from typing import Optional, List, Dict, Any

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "flipkart.db"
CSV_PATH = DATA_DIR / "flipkart_com-ecommerce_sample.csv"

# Predefined primary categories aligned with Flipkart's catalog structure
PRIMARY_CATEGORIES = [
    "Clothing",
    "Jewellery",
    "Footwear",
    "Mobiles & Accessories",
    "Automotive",
    "Home Decor & Festive Needs",
    "Beauty and Personal Care",
    "Home Furnishing",
    "Kitchen & Dining",
    "Computers",
    "Watches",
    "Baby Care"
]


def get_db_connection() -> sqlite3.Connection:
    """Return a connection to the SQLite database with Row factory enabled."""
    conn = sqlite3.connect(str(DB_PATH), check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def parse_category_tree(tree_raw: str):
    """
    Extract primary category, sub-category, and clean path hierarchy
    from Flipkart's product_category_tree string.
    Example: ["Clothing >> Women's Clothing >> Western Wear >> Dresses >> ..."]
    """
    if not tree_raw or not isinstance(tree_raw, str):
        return "Other", "(none)", ""
    
    # Extract string inside brackets/quotes
    matches = re.findall(r'\"([^\"]+)\"', tree_raw)
    raw_str = matches[0] if matches else tree_raw.strip('[]" \'\n')
    
    parts = [p.strip() for p in raw_str.split('>>') if p.strip()]
    if not parts:
        return "Other", "(none)", ""
    
    first = parts[0]
    # Match against top categories
    matched_cat = "Other"
    for cat in PRIMARY_CATEGORIES:
        if cat.lower() == first.lower() or cat.lower() in first.lower():
            matched_cat = cat
            break
    
    if matched_cat == "Other":
        # Keep prominent category name if clean
        if len(first) < 40 and not any(c in first for c in ["{", "}", ":", "="]):
            matched_cat = first
    
    sub_cat = parts[1] if len(parts) > 1 else "(none)"
    clean_tree = " > ".join(parts)
    
    return matched_cat, sub_cat, clean_tree


def parse_specifications(specs_raw: str) -> str:
    """Clean and parse product_specifications ruby-like hash into valid JSON string."""
    if not specs_raw or specs_raw == "NA":
        return json.dumps([])
    try:
        # Convert => to : and clean up syntax
        converted = re.sub(r'=>', ':', specs_raw)
        # Parse if valid JSON
        data = json.loads(converted)
        if isinstance(data, dict) and "product_specification" in data:
            return json.dumps(data["product_specification"])
        return json.dumps(data if isinstance(data, list) else [])
    except Exception:
        # Fallback regex extraction of key-value pairs
        pairs = []
        matches = re.findall(r'"key"\s*=>\s*"([^"]+)",\s*"value"\s*=>\s*"([^"]+)"', specs_raw)
        for k, v in matches:
            pairs.append({"key": k, "value": v})
        return json.dumps(pairs)


def parse_images(img_raw: str) -> List[str]:
    """Parse Flipkart image array string into a list of clean URLs."""
    if not img_raw or img_raw == "NA":
        return []
    try:
        urls = re.findall(r'https?://[^\s",\]]+', img_raw)
        return [u.rstrip('\'"\\') for u in urls if u]
    except Exception:
        return []


def parse_float(val: Any) -> Optional[float]:
    """Safely parse float numbers."""
    if val is None:
        return None
    val_str = str(val).strip().replace(',', '')
    if not val_str or val_str.lower() in ('na', 'null', 'none', 'no rating available'):
        return None
    try:
        f = float(val_str)
        return f if f >= 0 else None
    except ValueError:
        return None


def init_db(force_reseed: bool = False):
    """Initialize database schema and populate with CSV data if needed."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    if DB_PATH.exists() and not force_reseed:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT count(*) FROM products")
                count = cursor.fetchone()[0]
                if count >= 19000:
                    print(f"Database already seeded with {count} listings.")
                    return
            except sqlite3.OperationalError:
                pass
    
    print(f"Initializing Flipkart database at {DB_PATH}...")
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("""
        CREATE TABLE products (
            uniq_id TEXT PRIMARY KEY,
            crawl_timestamp TEXT,
            crawl_month TEXT,
            product_url TEXT,
            product_name TEXT,
            product_category_tree TEXT,
            category TEXT,
            sub_category TEXT,
            pid TEXT,
            retail_price REAL,
            discounted_price REAL,
            discount_pct REAL,
            primary_image TEXT,
            images_json TEXT,
            is_fk_advantage INTEGER,
            description TEXT,
            product_rating REAL,
            overall_rating REAL,
            brand TEXT,
            product_specifications TEXT
        )
    """)
    
    if not CSV_PATH.exists():
        print(f"Error: CSV file not found at {CSV_PATH}")
        conn.close()
        return

    print("Parsing CSV and seeding records...")
    records = []
    with open(CSV_PATH, mode='r', encoding='utf-8', errors='replace') as f:
        reader = csv.DictReader(f)
        for row in reader:
            uniq_id = row.get('uniq_id', '').strip()
            if not uniq_id:
                continue
            
            raw_ts = row.get('crawl_timestamp', '').strip()
            crawl_month = raw_ts[:7] if len(raw_ts) >= 7 else "Unknown"
            
            cat, sub_cat, clean_tree = parse_category_tree(row.get('product_category_tree', ''))
            
            rp = parse_float(row.get('retail_price'))
            dp = parse_float(row.get('discounted_price'))
            
            # Discount percentage calculation
            disc_pct = 0.0
            if rp and dp and rp > 0:
                if rp >= dp:
                    disc_pct = round(((rp - dp) / rp) * 100.0, 1)
                else:
                    disc_pct = 0.0
            elif rp and not dp:
                dp = rp
            elif dp and not rp:
                rp = dp
                
            fk_raw = str(row.get('is_FK_Advantage_product', '')).strip().lower()
            is_fk = 1 if fk_raw in ('true', '1', 'yes') else 0
            
            images = parse_images(row.get('image', ''))
            primary_img = images[0] if images else ""
            
            prod_rating = parse_float(row.get('product_rating'))
            overall_rating = parse_float(row.get('overall_rating'))
            
            brand = row.get('brand', '').strip()
            if not brand or brand.lower() in ('na', 'null', 'none'):
                brand = "Unbranded"
                
            specs_json = parse_specifications(row.get('product_specifications', ''))
            
            records.append((
                uniq_id,
                raw_ts,
                crawl_month,
                row.get('product_url', '').strip(),
                row.get('product_name', '').strip(),
                clean_tree,
                cat,
                sub_cat,
                row.get('pid', '').strip(),
                rp or 0.0,
                dp or 0.0,
                disc_pct,
                primary_img,
                json.dumps(images),
                is_fk,
                row.get('description', '').strip(),
                prod_rating,
                overall_rating,
                brand,
                specs_json
            ))
            
            if len(records) >= 1000:
                cursor.executemany("""
                    INSERT OR REPLACE INTO products VALUES 
                    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, records)
                records = []
                
        if records:
            cursor.executemany("""
                INSERT OR REPLACE INTO products VALUES 
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, records)
            
    print("Creating database indexes for instant query execution...")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_cat ON products(category)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_sub ON products(sub_category)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_fk ON products(is_fk_advantage)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_brand ON products(brand)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_month ON products(crawl_month)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_price ON products(discounted_price)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_disc ON products(discount_pct)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_rating ON products(product_rating)")
    
    conn.commit()
    
    cursor.execute("SELECT count(*) FROM products")
    total = cursor.fetchone()[0]
    print(f"Database successfully created and indexed: {total} products stored.")
    conn.close()


if __name__ == "__main__":
    init_db(force_reseed=True)
