from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Hardware Communication API")

# -----------------------------
# Data Model (Sensor Input)
# -----------------------------
class SensorData(BaseModel):
    device_id: str
    temperature: float
    humidity: float

# -----------------------------
# Root Endpoint
# -----------------------------
@app.get("/")
async def root():
    return {
        "message": "FastAPI Hardware API is running",
        "timestamp": datetime.now()
    }

# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
async def health_check():
    return {"status": "OK"}

# -----------------------------
# Receive Sensor Data (POST)
# -----------------------------
@app.post("/sensor")
async def receive_sensor_data(data: SensorData):
    # Simulating processing
    if data.temperature < -50 or data.temperature > 150:
        raise HTTPException(status_code=400, detail="Invalid temperature range")

    return {
        "message": "Sensor data received successfully",
        "device_id": data.device_id,
        "temperature": data.temperature,
        "humidity": data.humidity,
        "received_at": datetime.now()
    }

# -----------------------------
# Simulated Device Status
# -----------------------------
@app.get("/device/{device_id}")
async def get_device_status(device_id: str):
    return {
        "device_id": device_id,
        "status": "connected",
        "last_seen": datetime.now()
    }