import redis
from fastapi import FastAPI

app = FastAPI()

redis_client = redis.Redis(host='redis', port=6379, db=0)

@app.get("/")
async def read_root():
    redis_client.set('mykey', 'Hello Redis!')
    return {"mensaje": redis_client.get('mykey').decode('utf-8')}



