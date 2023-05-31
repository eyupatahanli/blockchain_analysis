import requests
import json
import datetime
import time

api_key = "2SZSC714WDBE2HY3AHPA5DE8RSMIGAA7M7"
address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
last_processed_timestamp = 0

def process_transaction(transaction):
    global last_processed_timestamp
    timestamp = int(transaction['timeStamp'])
    if timestamp > last_processed_timestamp:
        print("Yeni bir işlem alındı:")
        print(f"From: {transaction['from']}")
        print(f"To: {transaction['to']}")
        print(f"Value: {transaction['value']}")
        print(f"Timestamp: {datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')}")
        print("----")
        last_processed_timestamp = timestamp

while True:
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={api_key}"
    response = requests.get(url)
    transactions = json.loads(response.text)["result"]
    for transaction in transactions:
        process_transaction(transaction)
    time.sleep(1)


import requests
import json
import datetime
import time
from telegram import Bot

api_key = "2SZSC714WDBE2HY3AHPA5DE8RSMIGAA7M7"
address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
last_processed_timestamp = 0
telegram_token = "6123291587:AAHnqCp6Me63Ltf01Kic6jkHc678KzpXIsU"
chat_id = "998491858"

bot = Bot(token=telegram_token)

def process_transaction(transaction):
    global last_processed_timestamp
    timestamp = int(transaction['timeStamp'])
    if timestamp > last_processed_timestamp:
        message = f"Yeni bir işlem alındı:\nFrom: {transaction['from']}\nTo: {transaction['to']}\nValue: {transaction['value']}\nTimestamp: {datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')}"
        bot.send_message(chat_id=chat_id, text=message)
        last_processed_timestamp = timestamp

while True:
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={api_key}"
    response = requests.get(url)
    transactions = json.loads(response.text)["result"]
    for transaction in transactions:
        process_transaction(transaction)
    time.sleep(1) #1 hour





import requests
import json
import datetime
import time
import asyncio
from telegram import Bot


api_key = "2SZSC714WDBE2HY3AHPA5DE8RSMIGAA7M7"
address = "0xdAC17F958D2ee523a2206206994597C13D831ec7"
last_processed_timestamp = 0
telegram_token = "6123291587:AAHnqCp6Me63Ltf01Kic6jkHc678KzpXIsU"
chat_id = "998491858"


bot = Bot(token=telegram_token)

async def process_transaction(transaction):
    global last_processed_timestamp
    timestamp = int(transaction['timeStamp'])
    if timestamp > last_processed_timestamp:
        message = f"Yeni bir işlem alındı:\nFrom: {transaction['from']}\nTo: {transaction['to']}\nValue: {transaction['value']}\nTimestamp: {datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')}"
        await bot.send_message(chat_id=chat_id, text=message)
        last_processed_timestamp = timestamp

async def main():
    while True:
        url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={api_key}"
        response = requests.get(url)
        transactions = json.loads(response.text)["result"]
        for transaction in transactions:
            await process_transaction(transaction)
        await asyncio.sleep(3600) #1 hour

asyncio.run(main())
