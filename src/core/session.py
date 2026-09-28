import os
import json
import urllib.request
import urllib.error

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError: # nosec
    pass # nosec

WORKER = os.environ.get("WORKER", "")

import sys

IS_WEB = sys.platform == "emscripten"

if IS_WEB:
    from pyodide.http import pyfetch # type: ignore as this is only for the web which automatically has that: for desktop it isnt needed
    import asyncio

def _post(endpoint, payload):
    if not payload.get("name") and not payload.get("user"):
        return 400, "{}"

    full_url = f"{WORKER}{endpoint}"

    if not full_url.startswith(("http://", "https://")):
        return 500, "{}"

    if IS_WEB:
        async def _async_post():
            try:
                response = await pyfetch(
                    full_url,
                    method="POST",
                    headers={
                        "Content-Type": "application/json",
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                    },
                    body=json.dumps(payload)
                )
                text = await response.string()
                return response.status, text
            except Exception:
                return 500, "{}"

        return asyncio.run(_async_post())

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        full_url,
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as res:
            return res.getcode(), res.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8") if e.fp else "{}"
    except Exception:
        return 500, "{}"
    
def login(username, password):
    payload = {"name": username, "pass": password}
    code, text = _post("/login", payload)

    if code != 200:
        print(f"Status code {code}. Error logging in")
        return "", ""
    
    user = json.loads(text)
    return user["name"], user["token"]

def register(username, password):
    payload = {"name": username, "pass": password}
    code, text = _post("/register", payload)

    if code != 201:
        print(f"Status code {code}. Error registering")
        return "", ""
        
    return login(username, password)

def logout(username, token):
    payload = {"user": username, "token": token}
    _post("/logout", payload)
