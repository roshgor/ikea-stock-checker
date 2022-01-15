import requests
import json

API_ENDPOINT = ""

def send_chat_alert(message):

    bot_message = {'text': message}
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    r = requests.post(url=API_ENDPOINT, data=json.dumps(bot_message), headers=message_headers)
    print(r)
