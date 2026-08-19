from fastapi import FastAPI
import redis
app = FastAPI()
r = redis.Redis(host='redis', port=6379, db=0)
@app.get("/cache")
def get_cache():
    return {"value": r.get("key")}
