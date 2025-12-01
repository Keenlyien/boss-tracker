import os
import json
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.bossTracker
collection = db.bosses

def handler(request):
    bosses = list(collection.find({}, {"_id": 0}))  # exclude MongoDB _id
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"bosses": bosses})
    }
