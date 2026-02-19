from pymongo import MongoClient
import os

mongo_url = os.getenv("REDIS_HOST")

mongo_client = MongoClient(mongo_url)
db = mongo_client.warning_db