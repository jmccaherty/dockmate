import json
from datetime import datetime, timedelta

AVAILABILITY_FILE = "data/availability.json"

def load_availability():
    try:
        with open(AVAILABILITY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_availability(data):
    with open(AVAILABILITY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_available_days(services, days_ahead=14):
    data = load_availability()
    today = datetime.today()
    results = []

    for i in range(days_ahead):
        day = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        if all(data.get(service, {}).get(day, 0) > 0 for service in services):
            results.append(day)
    return results
