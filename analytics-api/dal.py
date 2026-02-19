from mongo_connection import db
from redis_connection import redis_client
import json

my_data = 
data = redis_client.get(my_data)
if not data:
    mongo_data = db.orders.find_one(my_data, {"_id": 0})
    redis_client.setex("order:123", 300, json.dumps(mongo_data))
    data = mongo_data
data = json.loads(data)







def alerts_by_border_and_priority():
    return

def top_urgent_zones():
    return

def distance_distribution():
    return

def low_visibility_high_activity():
    return

def hot_zones():
    return


