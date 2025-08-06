import requests
import random
import time
from datetime import datetime


url = "http://localhost:5001/api/vitals"

def generate_vitals():
    return {
        "heartRate": random.randint(60, 100),
        "bloodPressure": f"{random.randint(110, 130)}/{random.randint(70, 85)}",
        "oxygenLevel": random.randint(95, 100),
        "temperature": round(random.uniform(97.0, 99.5), 1),
        "timestamp": datetime.utcnow().isoformat()
        
    }


while True:
    data = generate_vitals()
    response = requests.post(url, json = data)
    print(f"Sent: {data} | Status: {response.status_code}")
    time.sleep(2)

