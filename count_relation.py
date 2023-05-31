import requests
import json
import itertools

api_key = "2SZSC714WDBE2HY3AHPA5DE8RSMIGAA7M7"

# ETH adresleri
addresses = ['0xcfe283ba968b98737199627f507ae2fb93be0c81', '0xAC8606d7019488830bE39825913AB0b0B078e213',
             '0x7EAAfFF7DF5d3C47551ccbFDd70b1ef801655d2b','0xcfe283ba968b98737199627f507ae2fb93be0c81',
             '0xAC8606d7019488830bE39825913AB0b0B078e213','0xf037F020777BF024a4Ea3b7529cf09519d4f7965',
             '0xb8bf69730c7bfe0a8f7cb4c98eed1e62e433ca69','0x2FfE5eF40fD39Da23E61Ebef4b68E15fF9843061']

# Adres kombinasyonları
combinations = itertools.combinations(addresses, 2)

# Kombinasyonlardaki adres ilişki sayıları
for combination in combinations:
    print(f"Adresler: {combination[0]} ve {combination[1]}")
    # Adresler arasındaki transfer işlemlerini burada sayabilirsiniz
    # Address 1 transactions
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={combination[0]}&sort=asc&apikey={api_key}"
    response = requests.get(url)
    transactions1 = json.loads(response.text)["result"]

    # Address 2 transactions
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={combination[1]}&sort=asc&apikey={api_key}"
    response = requests.get(url)
    transactions2 = json.loads(response.text)["result"]

    # Combine transactions
    transactions = sorted(transactions1 + transactions2, key=lambda tx: int(tx["timeStamp"]))

    # Initialize counters
    sent_count = 0
    received_count = 0

    # Count transactions
    for tx in transactions:
        if tx["from"].lower() == address1.lower() and tx["to"].lower() == address2.lower():
            sent_count += 1
        elif tx["from"].lower() == address2.lower() and tx["to"].lower() == address1.lower():
            received_count += 1
    print(f" sent {sent_count}  to ")
    print(f" received {received_count}  from ")

