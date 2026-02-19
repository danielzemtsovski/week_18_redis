from dal import alerts_by_border_and_priority, top_urgent_zones, distance_distribution, low_visibility_high_activity, hot_zones
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/analytics/alerts-by-border-and-priority")
def get_alerts_by_border_and_priority():
    return alerts_by_border_and_priority()

@app.get("/analytics/top-urgent-zones")
def get_top_urgent_zones():
    return top_urgent_zones()

@app.get("/analytics/distance-distribution")
def get_distance_distribution():
    return distance_distribution()

@app.get("/analytics/low-visibility-high-activity")
def get_low_visibility_high_activity():
    return low_visibility_high_activity()

@app.get("/analytics/hot-zones")
def get_hot_zones():
    return hot_zones()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
