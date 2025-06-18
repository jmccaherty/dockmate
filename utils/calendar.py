import json

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
