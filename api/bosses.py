import json
import os

def handler(request):
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "bosses.json")

    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data)
    }
