import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
WORKER = os.getenv("WORKER", "error")

def login(username, password):
    payload = {
        "name": username,
        "pass": password
    }

    try:
        response = requests.post(WORKER+"/login", json=payload, timeout=10)
        
        response.raise_for_status()

        if response.status_code != 200:
            print(f"Status code {response.status_code}. Error logging in")
            return "error"
        else:
            user = json.loads(response.text)
            return (user["name"], user["token"])

        
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return "error"
    