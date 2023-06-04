import requests
import os
from dotenv import load_dotenv
import time
import logging

load_dotenv()

logging.basicConfig(
    level=logging.ERROR,
    filename="error.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# API anahtarı env dosyasından çekme
api_key = os.getenv("api")
telegram_token = os.getenv("token")
chat_id = os.getenv("chat_id")

# İşlem geçmişi için BEP-20 token adresini env dosyasından çekme
# Todo: buna incelenecek cüzdan diyelim
token_address = os.getenv("biryar").lower()


def send_message(kim=None, islem=None, token=None, value=None, islem_var=1):
    telegram_token = os.getenv("telegram_token")
    chat_id = os.getenv("chat_id")
    if islem_var == 1:
        message = f"{kim}, {value} adet {token} {islem}"
        message = message + str(time.ctime())
        url_telegram = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
        requests.get(url_telegram).json()


while True:
    try:
        # BscScan API'sine GET isteği göndererek işlem geçmişini alın
        url = f'https://api.bscscan.com/api?module=account&action=tokentx&address={token_address}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}'
        response = requests.get(url)
        data = response.json()

        if data['status'] == '1':
            transactions = data['result']
            islem_sayisi = len(transactions)

            # İşlem geçmişi verilerini işleyin status 0 sa veri çekme başarısız demektir
            if islem_sayisi < len(transactions):
                # 5 saniyede kaç islem yapıldı
                fark = len(transactions) - islem_sayisi
                print(f"eyup az önce {fark} işlem yaptı")
                for i in range(islem_sayisi, len(transactions), 1):
                    if transactions[i]["from"] == token_address:
                        parite = transactions[i]["tokenSymbol"]
                        adet = transactions[i]["value"]
                        # todo:usdt ya da bnb değerini de ekle
                        print(f"{i}.işlem türü satış, işlem paritesi{parite},adedi = {adet}")
                        send_message("eyup", "sattı", token=parite, value=adet)
                    if transactions[i]["to"] == token_address:
                        parite = transactions[i]["tokenSymbol"]
                        adet = transactions[i]["value"]
                        # message = f"{i}.işlem türü satış, işlem paritesi{parite},adedi = {adet}"
                        # todo:usdt ya da bnb değerini de ekle
                        print(f"{i}.işlem türü alış, işlem paritesi{parite},adedi = {adet}")
                        send_message("eyup", "aldı", token=parite, value=adet)
                    else:
                        parite = transactions[i]["tokenSymbol"]
                        print(f"başka bir işlem yapıldı.parite ={parite}")
            else:
                print("yeni işlem yok")
                send_message(islem_var=0)
            time.sleep(2)

        else:
            print('API isteği başarısız oldu. Hata:', data['message'])
            telegram_token = os.getenv("telegram_token")
            chat_id = os.getenv("chat_id")
            message = 'API isteği başarısız oldu. Hata:', data['message']
            message = message + str(time.ctime())
            url_telegram = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={chat_id}&text={message}"
            requests.get(url_telegram).json()
            time.sleep(2)

    except Exception as e:
        print("Bir hata oluştu:", str(e))
        logging.error(f"Bir hata oluştu: {str(e)}")
        # Bekleme süresi
        time.sleep(2)
