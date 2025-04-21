from fastapi import FastAPI
import redis

app = FastAPI()
rd = redis.Redis(host="redis",port=6379)

@app.get("/")
def read_root():
    return {"Hello": "World!, welcome"}

@app.get("/hits")
def read_root():
    rd.incr("hits")
    return {"Number of hits so far": rd.get("hits")}