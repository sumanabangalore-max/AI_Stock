import requests

TOKEN = "8540212486:AAE2c_IwOK_6JgGFhL_grYAW-EbGbalXqhc"
CHAT_ID = "6188796715"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": "Test message from AI stock bot"
    }
)

print(response.text)