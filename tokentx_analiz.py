import requests
import os
from dotenv import load_dotenv
load_dotenv()
#token_address = os.getenv("ben")

#API anahtarı env dosyasından çekme
api_key = os.getenv("api")

# İşlem geçmişi için BEP-20 token adresini env dosyasından çekme
token_address = os.getenv("ben")



# BscScan API'sine GET isteği göndererek işlem geçmişini alın
url = f'https://api.bscscan.com/api?module=account&action=tokentx&address={token_address}&startblock=0&endblock=999999999&sort=asc&apikey={api_key}'
response = requests.get(url)
data = response.json()



# İşlem geçmişi verilerini işleyin status 0 sa veri çekme başarısız demektir
if data['status'] == '1':
    transactions = data['result']

    # Her bir işlemi işleyin
    for tx in transactions:
        # İşlem verilerini alın (örneğin, 'from', 'to', 'value' gibi)
        sender = tx['from']
        receiver = tx['to']
        value = tx['value']
        # İşlem verilerini kullanarak istediğiniz işlemleri yapın
        # ...

else:
    print('API isteği başarısız oldu. Hata:', data['message'])


#verinin işimize yarayacak başlıklarına göz atmak
transactions[0].keys()
"""
dict_keys(['blockNumber', 'timeStamp', 'hash', 'nonce', 'blockHash', 'from', 'contractAddress', 'to', 'value', 'tokenName', 
'tokenSymbol', 'tokenDecimal', 'transactionIndex', 'gas', 'gasPrice', 'gasUsed', 'cumulativeGasUsed', 'input', 'confirmations'])
"""
print(transactions[20]["input"])

for i in range(len(transactions)):
    print(transactions[i]["tokenSymbol"])

        #burada ne yapıyoruz bilmiiyorıum
        if transactions[i]["value"] != "0":
             print(int(transactions[i]["value"] ) * 307 /10**18)
