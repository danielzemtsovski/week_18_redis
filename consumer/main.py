from redis_connection import redis_client
import datetime
from mongo_connection import db
import json

def main():
    while True:
        data_from_redis = redis_client.rpop("queue_urgent")
        if not data_from_redis:
            data_from_redis = redis_client.rpop("queue_normal")
                    
        item = json.loads(data_from_redis)
        item["time_insertion"] = datetime.datetime.now()
        db.warning_collection.insert_one(item)

if __name__ == "__main__":
      main()