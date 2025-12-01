import json
import os

def handler(request):
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "bosses.json")

    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    # Example update: change last_killed of Venatus to now
    import datetime
    data["Venatus"]["last_killed"] = datetime.datetime.now().isoformat()

    with open(data_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": "Boss list updated."
    }
