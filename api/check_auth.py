import os, json, jwt, datetime

SECRET = os.environ.get("JWT_SECRET", "dev-secret")

def handler(request):
    # read cookie header
    headers = request.get("headers", {})
    cookie = headers.get("cookie") or headers.get("Cookie") or ""
    token = None
    for part in cookie.split(";"):
        part = part.strip()
        if part.startswith("bt_token="):
            token = part[len("bt_token="):]
            break
    if not token:
        return {"statusCode": 200, "body": json.dumps({"authenticated": False}), "headers": {"Content-Type": "application/json"}}
    try:
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return {"statusCode": 200, "body": json.dumps({"authenticated": True, "user": payload.get("sub")}), "headers": {"Content-Type": "application/json"}}
    except Exception as e:
        return {"statusCode": 200, "body": json.dumps({"authenticated": False}), "headers": {"Content-Type": "application/json"}}
