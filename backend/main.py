import os
import json
from typing import Optional, List
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

try:
    from backend.data_processors import (
        PROCESSORS_DATA,
        get_all_processors,
        get_processor_by_id,
        get_all_phones,
        search_phones_and_processors,
    )
except ImportError:
    from data_processors import (
        PROCESSORS_DATA,
        get_all_processors,
        get_processor_by_id,
        get_all_phones,
        search_phones_and_processors,
    )

app = FastAPI(
    title="ChipFlow Mobile Processor & Smartphone Intelligence API",
    description="Backend API powering the ChipFlow intelligence suite. Provides detailed SoC architectures, foundry allocations, BOM breakdowns, and comprehensive mobile phone mappings across Apple, Qualcomm, MediaTek, Samsung, Google, HiSilicon, and Unisoc.",
    version="2.0.0",
)

# Enable CORS for external access / frontend flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ═══════════════════════════════════════════════════════════════════
# API ENDPOINTS
# ═══════════════════════════════════════════════════════════════════

@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ChipFlow API",
        "processorsCount": len(PROCESSORS_DATA),
        "totalPhonesMapped": len(get_all_phones()),
        "version": "2.0.0"
    }


@app.get("/api/processors")
def list_processors(
    brand: Optional[str] = Query(None, description="Filter by brand (apple, qualcomm, mediatek, samsung, google, hisilicon, unisoc)"),
    tier: Optional[str] = Query(None, description="Filter by tier (Flagship, Premium, Midrange, Budget)"),
    search: Optional[str] = Query(None, description="Search term matching processor or phone model"),
):
    """
    List all mobile processors with full specifications and phone mappings.
    Optional query parameters allow filtering by brand, market tier, or search text.
    """
    results = PROCESSORS_DATA

    if brand and brand.lower() != "all":
        b = brand.lower().strip()
        results = [p for p in results if p.get("filter", "").lower() == b or p["brand"].lower() == b]

    if tier and tier.lower() != "all":
        t = tier.lower().strip()
        results = [p for p in results if t in p.get("tier", "").lower()]

    if search:
        s = search.lower().strip()
        filtered = []
        for p in results:
            # check processor attributes
            p_match = (
                s in p["name"].lower() or
                s in p["brand"].lower() or
                s in p.get("altName", "").lower() or
                s in p.get("node", "").lower() or
                s in p.get("cpu", "").lower() or
                s in p.get("gpu", "").lower() or
                s in p.get("tier", "").lower() or
                s in p.get("foundry", "").lower()
            )
            # check phones using this processor
            phone_match = any(
                s in ph["model"].lower() or s in ph["brand"].lower()
                for ph in p.get("phones", [])
            )
            if p_match or phone_match:
                filtered.append(p)
        results = filtered

    return {
        "count": len(results),
        "total": len(PROCESSORS_DATA),
        "processors": results
    }


@app.get("/api/processors/{proc_id}")
def get_single_processor(proc_id: str):
    """
    Get full detailed specifications, strengths, risks, and mobile phones for a specific processor.
    """
    proc = get_processor_by_id(proc_id)
    if not proc:
        raise HTTPException(status_code=404, detail=f"Processor '{proc_id}' not found")
    return proc


@app.get("/api/phones")
def list_phones(
    brand: Optional[str] = Query(None, description="Filter phones by OEM brand (e.g. Samsung, Apple, Xiaomi, OnePlus, Google)"),
    tier: Optional[str] = Query(None, description="Filter phones by tier"),
    search: Optional[str] = Query(None, description="Search phone model"),
):
    """
    List all mobile phones with their corresponding processor, lithography node, and foundry.
    """
    phones = get_all_phones()

    if brand and brand.lower() != "all":
        b = brand.lower().strip()
        phones = [ph for ph in phones if ph["brand"].lower() == b]

    if tier and tier.lower() != "all":
        t = tier.lower().strip()
        phones = [ph for ph in phones if t in ph["tier"].lower()]

    if search:
        s = search.lower().strip()
        phones = [
            ph for ph in phones
            if s in ph["model"].lower() or s in ph["brand"].lower() or s in ph["processorName"].lower()
        ]

    return {
        "count": len(phones),
        "phones": phones
    }


@app.get("/api/phones/search")
def search_phones(q: str = Query(..., min_length=1, description="Search term")):
    """
    Cross-entity search: searches across phone models and processors simultaneously.
    """
    return search_phones_and_processors(q)


@app.get("/api/brands")
def get_brands_summary():
    """
    Get summary breakdown of brands, processor counts, and phone models mapped.
    """
    summary = {}
    for p in PROCESSORS_DATA:
        b = p["brand"]
        if b not in summary:
            summary[b] = {
                "brand": b,
                "color": p["brandColor"],
                "filter": p["filter"],
                "processorCount": 0,
                "phoneCount": 0,
                "processors": [],
                "foundries": set()
            }
        summary[b]["processorCount"] += 1
        summary[b]["phoneCount"] += len(p.get("phones", []))
        summary[b]["processors"].append(p["name"])
        summary[b]["foundries"].add(p.get("foundry", "").split("(")[0].strip())

    result = []
    for k, v in summary.items():
        v["foundries"] = list(v["foundries"])
        result.append(v)

    return {"brands": result}


@app.get("/api/stats")
def get_system_stats():
    """
    Overall intelligence statistics across all mobile silicon.
    """
    all_phones = get_all_phones()
    tiers = {}
    foundries = {}

    for p in PROCESSORS_DATA:
        tier = p.get("tier", "Midrange")
        tiers[tier] = tiers.get(tier, 0) + 1
        foundry = p.get("foundry", "TSMC").split("(")[0].strip()
        foundries[foundry] = foundries.get(foundry, 0) + 1

    return {
        "totalProcessors": len(PROCESSORS_DATA),
        "totalPhones": len(all_phones),
        "brandCount": len(set(p["brand"] for p in PROCESSORS_DATA)),
        "tierBreakdown": tiers,
        "foundryBreakdown": foundries
    }


@app.get("/api/data")
def get_chipflow_data():
    """
    Full ChipFlow dataset endpoint matching the existing frontend schema
    so the live update mechanism in ChipFlow.html works seamlessly.
    """
    return {
        "meta": {
            "version": 2,
            "description": "ChipFlow Mobile Processor & Smartphone Intelligence Master Dataset",
            "processorsCount": len(PROCESSORS_DATA),
            "phonesMapped": len(get_all_phones())
        },
        "processors": PROCESSORS_DATA
    }


# ═══════════════════════════════════════════════════════════════════
# STATIC FRONTEND ROUTING
# ═══════════════════════════════════════════════════════════════════

@app.get("/")
def serve_root():
    chipflow_path = os.path.join(PROJECT_DIR, "ChipFlow.html")
    if os.path.exists(chipflow_path):
        return FileResponse(chipflow_path)
    return {"message": "ChipFlow API is running. Access /api/processors or /ChipFlow.html"}

@app.get("/ChipFlow.html")
def serve_chipflow():
    chipflow_path = os.path.join(PROJECT_DIR, "ChipFlow.html")
    if os.path.exists(chipflow_path):
        return FileResponse(chipflow_path)
    raise HTTPException(status_code=404, detail="ChipFlow.html not found")

# Mount project root for charts, css, and images if needed
if os.path.exists(PROJECT_DIR):
    app.mount("/static", StaticFiles(directory=PROJECT_DIR), name="static")
