import requests
import os
from dotenv import load_dotenv
import time

def send_message(kim=None, islem=None, token=None,value=None,islem_var=1):
    telegram_token = os.getenv("telegram_token")
    chat_id = os.getenv("chat_id")
    if islem_var ==1:
        message = f"{kim}, {value} adet {token} {islem}"
        url_telegram = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url_telegram).json()
    else:
        message = "işlem yok"
        url_telegram = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url_telegram).json()