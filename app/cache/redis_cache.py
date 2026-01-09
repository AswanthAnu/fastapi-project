import json
import redis
from app.core.config import REDIS_URL


redis_client = redis.Redis.get_url(REDIS_URL)

def get_cached_output(key: str):
    cached_output = redis_client.get(key)
    if cached_output:
        return json.loads(cached_output)
    return None

def set_cached_output(key: str, value: dict, exp: int = 3600):
    redis_client.setex(key, exp, json.dumps(value))