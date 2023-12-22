#!/bin/bash
cd backend
source venv/bin/activate
uvicorn main:app --host 127.0.0.1 --port 8000 --workers 4