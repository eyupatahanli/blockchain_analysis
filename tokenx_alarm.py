import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()
#token_address = os.getenv("ben")

#API anahtarı env dosyasından çekme
api_key = os.getenv("api")
telegram_token = os.getenv("token")
chat_id = os.getenv("chat_id")

# İşlem geçmişi için BEP-20 token adresini env dosyasından çekme
#Todo: buna incelenecek cüzdan diyelim
token_address = os.getenv("ben").lower()


while True:
    #5 saniyede bir döngü çalışsın
    #todo ilk çalışmada sorun olmaması için transactionu sona al

    time.sleep(5)
    islem_sayısı = len(transactions)
    # BscScan API'sine GET isteği göndererek işlem geçmişini alın
    url = f'https://api.bscscan.com/api?module=account&action=tokentx&address={token_address}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

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
                    message = f"{i}.işlem türü satış, işlem paritesi{parite},adedi = {adet}"
                    #todo:usdt ya da bnb değerini de ekle
                    url_telegram = url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
                    requests.get(url_telegram).json()
                    print(f"{i}.işlem türü satış, işlem paritesi{parite},adedi = {adet}")
                if transactions[i]["to"] == token_address:
                    parite = transactions[i]["tokenSymbol"]
                    adet = transactions[i]["value"]
                    message = f"{i}.işlem türü satış, işlem paritesi{parite},adedi = {adet}"
                    #todo:usdt ya da bnb değerini de ekle
                    url_telegram = url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
                    requests.get(url_telegram).json()
                    #todo:usdt ya da bnb değerini de ekle
                    print(f"{i}.işlem türü alış, işlem paritesi{parite},adedi = {adet}")
                else:
                    parite = transactions[i]["tokenSymbol"]
                    print(f"başka bir işlem yapıldı.parite ={parite}")
        else:
            print("yeni işlem yok")
            message = "yeni işlem yok"
            # todo:usdt ya da bnb değerini de ekle
            url_telegram = url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(url_telegram).json()






    else:
        print('API isteği başarısız oldu. Hata:', data['message'])

#todo telegram ekle


"""        # Her bir işlemi işleyin
        for tx in transactions:
            # İşlem verilerini alın (örneğin, 'from', 'to', 'value' gibi)
            sender = tx['from']
            receiver = tx['to']
            value = tx['value']
            # İşlem verilerini kullanarak istediğiniz işlemleri yapın
            # ..."""