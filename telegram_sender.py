import requests
from config import TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID


def send_telegram_message(message):

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

    max_len = 3500

    for i in range(0, len(message), max_len):
        chunk = message[i:i + max_len]

        requests.post(url, data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": chunk,
            "parse_mode": "HTML"
        })