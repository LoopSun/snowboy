import os

from redis import ConnectionPool


REDIS_HOST = os.getenv("REDIS_HOST", "127.0.0.1")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", "")

WAF_REDIS_DB = ConnectionPool(host=REDIS_HOST, port=REDIS_PORT,
                              password=REDIS_PASSWORD, decode_responses=True, db=7)