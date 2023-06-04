import pandas as pd
import requests
import os
from dotenv import load_dotenv
import time
import logging
import sys


wallets = pd.DataFrame({'id':[0,1,2,3],
                        'name':['d1','b1','d2','e'],
                        'wallet':['0x2ffe5ef40fd39da23e61ebef4b68e15ff9843061',
                                  '0xdc586eef0e3dd38b6894ce2c6dce4b7c1909890e',
                                  '0x99c388b40c0bcfc88abf7e9ce52d87de5a788050',
                                  '0x2bed2ad1aefe1ec04764391b1c5fd4602a67026f'],
                        'number':[0,0,0,0]
                        })
api_key = 'AHYIZA4CHJ7QZHK8Z79NE3GVR4BR6FQIR1'
telegram_token = '6123291587:AAHnqCp6Me63Ltf01Kic6jkHc678KzpXIsU'
chat_id = '998491858'

def send_message(kim=None, islem=None, token=None, value=None, islem_var=1):
    telegram_token = '6123291587:AAHnqCp6Me63Ltf01Kic6jkHc678KzpXIsU'
    chat_id = '998491858'
    if islem_var == 1:
        message = f"{kim}, {value} adet {token} {islem}"
        message = message + '\n' + str(time.ctime())
        url_telegram = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url_telegram).json()


for x in range(len(wallets)):
    wallet = wallets.loc[x, 'wallet']
    url = f'https://api.bscscan.com/api?module=account&action=tokentx&address={wallet}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == '1':
        transactions = data['result']
        wallets.loc[x, 'number'] = len(transactions)



while True:
    time.sleep(1)
    try:
        for i in range(len(wallets)):
            wallet = wallets.loc[i, 'wallet']
            url = f'https://api.bscscan.com/api?module=account&action=tokentx&address={wallet}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}'
            response = requests.get(url)
            data = response.json()
            transactions = data['result']
            if wallets.iloc[i]['number'] < len(transactions):
                for tx in range((wallets.iloc[i]['number']),len(transactions),1):

                    parite = transactions[tx]["tokenSymbol"]
                    adet = transactions[tx]["value"]
                    if transactions[tx]["from"] == wallet:
                        print(f"{tx}.işlem türü satış, işlem paritesi{parite},adedi = {adet}")
                        send_message(kim=wallets.iloc[i]['name'],islem='sattı',token=parite,value=adet)
                    elif transactions[tx]["to"] == wallet:
                        print(f"{tx}.işlem türü aldı, işlem paritesi{parite},adedi = {adet}")
                        send_message(kim=wallets.iloc[i]['name'],islem='aldı',token=parite,value=adet)
                    else:
                        parite = transactions[tx]["tokenSymbol"]
                        print(f"başka bir işlem yapıldı.parite ={parite}")
                        send_message(kim=wallets.iloc[i]['name'], islem='başka işlem yapıldı ', token=parite)
                wallets.loc[i, 'number'] = len(transactions)

            else:
                print('başka işlem yok')

    except Exception as e:
        print('Hata oluştu:', str(e))
        telegram_token = '6123291587:AAHnqCp6Me63Ltf01Kic6jkHc678KzpXIsU'
        chat_id = '998491858'
        message_err = str(e)
        message_err = message_err + '\n' + str(time.ctime())
        url_telegram = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message_err}"
        requests.get(url_telegram).json()
