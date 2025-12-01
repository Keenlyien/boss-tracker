import os, json
from datetime import datetime, timezone
from pymongo import MongoClient

MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client.bossTracker
collection = db.bosses

def handler(request):
    # Expect POST JSON: { name, killed_at } where killed_at is ISO string
    try:
        body = request.get("json") or {}
        name = body.get("name")
        killed_at = body.get("killed_at")
        if not name or not killed_at:
            return {"statusCode": 400, "body": "Missing parameters"}
        # validate time
        try:
            dt = datetime.fromisoformat(killed_at)
            # convert to UTC ISO
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            iso = dt.astimezone(timezone.utc).isoformat()
        except Exception:
            return {"statusCode": 400, "body": "Invalid datetime format. Use ISO format."}

        res = collection.update_one({"name": name}, {"$set": {"last_killed": iso}})
        if res.matched_count == 0:
            return {"statusCode": 404, "body": "Boss not found"}
        return {"statusCode": 200, "body": json.dumps({"ok": True, "killed_at": iso}), "headers": {"Content-Type": "application/json"}}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
