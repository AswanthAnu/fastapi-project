import json
import redis
from app.core.config import settings


redis_client = redis.StrictRedis.from_url(settings.REDIS_URL, decode_responses=True)

def get_cached_output(key: str):
    cached_output = redis_client.get(key)
    if cached_output:
        return eval(cached_output)
    return None

def set_cached_output(key: str, value: dict):
    redis_client.set(key, str(value))