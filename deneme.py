import requests
import json
import datetime
import time

api_key = "2SZSC714WDBE2HY3AHPA5DE8RSMIGAA7M7"
address = "0x2FfE5eF40fD39Da23E61Ebef4b68E15fF9843061"

while True:
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={api_key}"
    response = requests.get(url)
    transactions = json.loads(response.text)["result"]
    for transaction in transactions:
        print(f"From: {transaction['from']}")
        print(f"To: {transaction['to']}")
        print(f"Value: {transaction['value']}")
        print(f"Timestamp: {datetime.datetime.fromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')}")
        print("----")
    time.sleep(1) #1 hour



url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={api_key}"
response = requests.get(url)
transactions = json.loads(response.text)["result"]
for transaction in transactions:
    print(f"From: {transaction['from']}")
    print(f"To: {transaction['to']}")
    print(f"Value: {transaction['value']}")
    print(f"Timestamp: {datetime.datetime.fromtimestamp(int(transaction['timeStamp'])).strftime('%Y-%m-%d %H:%M:%S')}")
    print("----")
