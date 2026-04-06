import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENCLAW_API_KEY = os.getenv("OPENCLAW_API_KEY")

TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}"


def send_message(chat_id, text):
    url = f"{TELEGRAM_API_URL}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=payload)


def get_updates(offset=None):
    url = f"{TELEGRAM_API_URL}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    response = requests.get(url, params=params)
    return response.json()


def handle_message(message):
    chat_id = message["chat"]["id"]
    user_text = message.get("text", "")

    # Replace this with OpenClaw integration if already wired
    reply = f"You said: {user_text}"

    send_message(chat_id, reply)


def main():
    print("Bot is running...")

    offset = None

    while True:
        updates = get_updates(offset)

        for update in updates.get("result", []):
            if "message" in update:
                handle_message(update["message"])
                offset = update["update_id"] + 1


if __name__ == "__main__":
    main()