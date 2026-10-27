#!/usr/bin/env bash
# Quick Start Script for Flipkart Catalog Analytics

cd "$(dirname "$0")"

echo "=========================================================="
echo " Starting Flipkart Catalog Analytics Backend (FastAPI)"
echo "=========================================================="

# Check if flipkart.db exists; if not, initialize it
if [ ! -f "data/flipkart.db" ]; then
    echo "Database not found. Seeding SQLite database from CSV..."
    python3 backend/db.py
fi

echo "Launching FastAPI server on http://localhost:8000 ..."
echo "API Docs available at: http://localhost:8000/docs"
echo "Web Dashboard available at: http://localhost:8000/"

python3 -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
