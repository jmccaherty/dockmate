import json
from datetime import datetime, timedelta

def load_availability():
    try:
        with open("data/availability.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def get_available_days(services, days_ahead=14):
    data = load_availability()
    today = datetime.today()
    results = []

    for i in range(days_ahead):
        day = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        if all(data.get(service, {}).get(day, 0) > 0 for service in services):
            results.append(day)
    return results
