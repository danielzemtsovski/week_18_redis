import json
from priority_logic import determining_urgency
from redis_connection import redis_client

def main():
    with open("data/border_alerts.json", "r") as f:
                data = json.load(f)
        
    for item in data:
        data_with_urgency = determining_urgency(item)

        if data["priority"] == "URGENT":
            redis_client.rpush("queue_urgent",json.dumps(data_with_urgency))
        else:
            redis_client.rpush("queue_normal",json.dumps(data_with_urgency))

if __name__ == "__main__":
      main()