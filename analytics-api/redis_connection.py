import redis
import os

host = os.getenv("REDIS_HOST")
port = os.getenv("REDIS_PORT")

redis_client = redis.Redis(host, port, decode_responses=True)