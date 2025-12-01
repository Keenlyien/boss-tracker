import os, json, datetime, jwt
from pymongo import MongoClient

SECRET = os.environ.get("JWT_SECRET", "dev-secret")
ADMIN_USER = os.environ.get("ADMIN_USER", "admin")
ADMIN_PASS = os.environ.get("ADMIN_PASS", "password")
# Token expires in 8 hours
EXP_HOURS = int(os.environ.get("JWT_EXP_HOURS", "8"))

def handler(request):
    # Expect POST with JSON {username, password}
    try:
        body = request.get("json") or {}
        username = body.get("username")
        password = body.get("password")
        if not username or not password:
            return {"statusCode": 400, "body": "Missing credentials"}

        if username != ADMIN_USER or password != ADMIN_PASS:
            return {"statusCode": 401, "body": "Invalid credentials"}

        now = datetime.datetime.utcnow()
        exp = now + datetime.timedelta(hours=EXP_HOURS)
        payload = {"sub": username, "exp": exp.timestamp()}
        token = jwt.encode(payload, SECRET, algorithm="HS256")

        # Set token as HttpOnly cookie
        cookie = f"bt_token={token}; HttpOnly; Path=/; SameSite=Lax"
        return {
            "statusCode": 200,
            "headers": {"Set-Cookie": cookie, "Content-Type": "application/json"},
            "body": json.dumps({"ok": True})
        }
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
