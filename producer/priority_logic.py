from pydantic import BaseModel
from datetime import date

class Warning(BaseModel):
    border: str
    zone: str
    timestamp: date 
    people_count: int
    weapons_count: int
    vehicle_type: str
    distance_from_fence_m: int
    visibility_quality: float

def determining_urgency(data: dict):
    if (data["weapons_count"] > 0
        or data["distance_from_fence_m"] <= 50
        or data["people_count"] >= 8
        or data["vehicle_type"] == "truck"
        or (data["distance_from_fence_m"] <= 150 and data["people_count"] >= 4)
        or (data["vehicle_type"] == "jeep" and data["people_count"] >= 3)):
        data["priority"] = "URGENT"
    else:
        data["priority"] = "NORMAL"
    return data



