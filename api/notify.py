import os
import json
import requests
from datetime import datetime, timedelta, timezone

DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK")

def handler(request):
    if not DISCORD_WEBHOOK:
        return {"statusCode": 500, "body": "Webhook not set"}

    with open("data/bosses.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    now = datetime.now(timezone.utc)
    messages = []

    for name, boss in data["bosses"].items():
        last_killed = boss.get("last_killed")
        respawn = boss.get("respawn")

        # Example: simple fixed spawn time (you can expand logic later)
        messages.append(f"Boss {name} in {boss['location']}")

    # Send message to Discord
    payload = {"content": "\n".join(messages)}
    requests.post(DISCORD_WEBHOOK, json=payload)

    return {"statusCode": 200, "body": "Notifications sent"}
