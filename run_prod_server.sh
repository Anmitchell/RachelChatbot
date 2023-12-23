#!/bin/bash
cd backend
source venv/bin/activate
gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0:8000
