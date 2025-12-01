import os
from datetime import datetime, timezone
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.bossTracker
collection = db.bosses

def handler(request):
    # Expect query param: ?boss=BossName
    boss_name = request.get("query", {}).get("boss")
    if not boss_name:
        return {"statusCode": 400, "body": "Missing 'boss' parameter"}

    now = datetime.now(timezone.utc).isoformat()
    result = collection.update_one(
        {"name": boss_name},
        {"$set": {"last_killed": now}}
    )

    if result.matched_count == 0:
        return {"statusCode": 404, "body": f"Boss '{boss_name}' not found"}

    return {"statusCode": 200, "body": f"{boss_name} marked dead at {now}"}
