#!/usr/bin/env python3
"""
ChipFlow Backend Server Launcher
Runs FastAPI with Uvicorn on port 8000
"""

import sys
import uvicorn

if __name__ == "__main__":
    print("=" * 65)
    print("⚡ Starting ChipFlow Intelligence Server (FastAPI + Uvicorn)")
    print("📊 API Documentation:  http://localhost:8000/docs")
    print("📱 ChipFlow Website:    http://localhost:8000/ChipFlow.html")
    print("=" * 65)
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
