from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ETL API is running. Go to /docs or /run-etl"}

@app.get("/run-etl")
def run_etl():
    return {"status": "success", "message": "ETL complete"}
