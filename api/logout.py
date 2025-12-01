import os, json
def handler(request):
    # expire cookie
    cookie = "bt_token=deleted; HttpOnly; Path=/; Expires=Thu, 01 Jan 1970 00:00:00 GMT; SameSite=Lax"
    return {"statusCode": 200, "headers": {"Set-Cookie": cookie, "Content-Type": "application/json"}, "body": json.dumps({"ok": True})}
