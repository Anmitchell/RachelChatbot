#!/bin/bash
cd frontend
npm i
npm run build
python3.11 -m venv .venv # create virtual environement for python app
source .venv/bin/activate # activate virtual environment
cd ..backend
pip install -r installedPackages.txt # install all python packages
# gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app -b 0.0.0.0:8000
