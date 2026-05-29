

from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = 8816805339:AAH0Ro98YrXm-fRNpc0gg9tNhIjwOmBT4tk
GROUP_ID = -5019427352

@app.route("/cregis", methods=["POST"])
def cregis():

    data = request.json

    message = f"""
🚀 New Cregis Payment

{data}
"""

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={
            "chat_id": GROUP_ID,
            "text": message
        }
    )

    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)