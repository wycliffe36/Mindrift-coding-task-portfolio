# Data Engineering Portfolio - Mindrift Coding Task

End-to-end Data Engineering project built on GitHub Codespaces (entirely on mobile) - demonstrating ETL, API design, and containerization.

### 🔗 Live Repo: https://github.com/wycliffe36/Mindrift-coding-task-portfolio

## 📁 Project Structure
- `03_etl.py` - Python ETL pipeline (Extract, Transform, Load) with data cleaning and validation
- `04_docker/` - Dockerized application with Dockerfile & docker-compose
- `05_api/` - FastAPI service with Uvicorn
    - Endpoints: `/health`, `/data`, `/docs`
    - Running: `uvicorn main:app --reload`
- `data/` - Sample datasets

## 🚀 Tech Stack
Python | FastAPI | Uvicorn | Docker | Pandas | ETL | REST API

## ▶️ How to Run
```bash
# API
cd 05_api
pip install fastapi uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000

# ETL
python 03_etl.py
