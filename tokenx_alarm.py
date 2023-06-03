import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()

#API anahtarı env dosyasından çekme
api_key = os.getenv("api")
telegram_token = os.getenv("token")
chat_id = os.getenv("chat_id")

# İşlem geçmişi için BEP-20 token adresini env dosyasından çekme
#Todo: buna incelenecek cüzdan diyelim
token_address = os.getenv("ben").lower()
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

while True:
    # BscScan API'sine GET isteği göndererek işlem geçmişini alın
    url = f'https://api.bscscan.com/api?module=account&action=tokentx&address={token_address}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == '1':
        transactions = data['result']
        islem_sayısı = len(transactions)

        # İşlem geçmişi verilerini işleyin status 0 sa veri çekme başarısız demektir
        if data['status'] == '1':
            transactions = data['result']

            if islem_sayısı < len(transactions):
                #5 saniyede kaç islem yapıldı
                fark = len(transactions)-islem_sayısı
                print(f"eyup az önce {fark} işlem yaptı")
                for i in range(islem_sayısı, len(transactions), 1):
                    if transactions[i]["from"] == token_address:
                        parite = transactions[i]["tokenSymbol"]
                        adet = transactions[i]["value"]
                        #todo:usdt ya da bnb değerini de ekle
                        print(f"{i}.işlem türü satış, işlem paritesi{parite},adedi = {adet}")
                        send_message("eyup","sattı",token=parite,value = adet)
                    if transactions[i]["to"] == token_address:
                        parite = transactions[i]["tokenSymbol"]
                        adet = transactions[i]["value"]
                        #message = f"{i}.işlem türü satış, işlem paritesi{parite},adedi = {adet}"
                        #todo:usdt ya da bnb değerini de ekle
                        print(f"{i}.işlem türü alış, işlem paritesi{parite},adedi = {adet}")
                        send_message("eyup", "aldı", token=parite, value=adet)
                    else:
                        parite = transactions[i]["tokenSymbol"]
                        print(f"başka bir işlem yapıldı.parite ={parite}")
            else:
                print("yeni işlem yok")
                send_message(islem_var=0)
        time.sleep(5)

    else:
        print('API isteği başarısız oldu. Hata:', data['message'])
        telegram_token = os.getenv("telegram_token")
        chat_id = os.getenv("chat_id")
        message = 'API isteği başarısız oldu. Hata:', data['message']
        url_telegram = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url_telegram).json()
        time.sleep(5)


"""        # Her bir işlemi işleyin
        for tx in transactions:
            # İşlem verilerini alın (örneğin, 'from', 'to', 'value' gibi)
            sender = tx['from']
            receiver = tx['to']
            value = tx['value']
            # İşlem verilerini kullanarak istediğiniz işlemleri yapın
            # ..."""
