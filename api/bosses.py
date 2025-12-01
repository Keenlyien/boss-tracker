import os
import json
from pymongo import MongoClient

def handler(request):
    try:
        # Load connection string
        MONGO_URI = os.environ.get("MONGO_URI")
        if not MONGO_URI:
            raise Exception("MONGO_URI is missing in Vercel environment variables")

        # Connect
        client = MongoClient(MONGO_URI)
        db = client.bossTracker
        collection = db.bosses

        # Fetch data
        bosses = list(collection.find({}, {"_id": 0}))

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"bosses": bosses})
        }

    except Exception as e:
        # Return the full crash error
        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)})
        }
