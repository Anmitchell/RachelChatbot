#!/bin/bash
cd frontend
npm i
npm run build
cd ..
cd backend
source venv/bin/activate
pip install -r installedPackages.txt
# gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0:8000
