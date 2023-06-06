import requests
import json
import datetime
import time
import pandas as pd



url = "https://api.bscscan.com/api"

api_key = os.getenv("api")

wallet_address = os.getenv("e")

# İstek parametrelerini hazırlama
params = {
    "module": "account",
    "action": "txlist",
    "address": wallet_address,
    "apikey": api_key,
}

# API isteğini gönderme
response = requests.get(url, params=params)


# İstek başarılı olduysa işlem geçmişini al
if response.status_code == 200:
    transaction_history = response.json()["result"]
else:
    print("İstek başarısız oldu. HTTP kodu:", response.status_code)


#bu döngü ile transfer miktarını alıyoruz ancak, sadece alışlar için çalışıyor
# bnb 307 doalr

for i in range(len(transaction_history)):
    print(transaction_history[i]["functionName"])
    if transaction_history[i]["functionName"] == "multicall(uint256 deadline, bytes[] data)":
        if transaction_history[i]["value"] != "0":
             print(int(transaction_history[i]["value"] ) * 307 /10**18)


transaction_history[i].keys()


(transaction_history[i]["functionName"])









df_data = []

# Her işlem için gerekli bilgileri çek ve DataFrame'e ekle
for tx in transaction:
    tx_type = 'Transfer' if tx['to'] != '' else 'Contract Creation'
    amount = float(tx['value'])
    timestamp = pd.to_datetime(int(tx['timeStamp']), unit='s')

    df_data.append({
        'Transaction Type': tx_type,
        'Amount': amount,
        'Timestamp': timestamp
    })


df = pd.DataFrame(df_data)


df