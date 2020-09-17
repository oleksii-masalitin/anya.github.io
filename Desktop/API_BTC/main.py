import requests
import json

# I use headers to get info from api.btc.com
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
# function to get a json from api.btc.com
def info(wallet):
    return requests.get(f"https://chain.api.btc.com/v3/address/{wallet}/tx", headers=headers)
#gets transaction fees
def fees(wallet):
    response = response = info(wallet).json()
    fees = []
    for i in response['data']['list']:
         fees.append({'hash': i['hash'],
            'balance_diff': round(i['balance_diff'] * (10 ** (-8)), 8),
            'fee': round(i['fee'] * (10 ** (-8)), 8),
        })
    return fees
#counts summary fee
def total_fee(fees):
    return round(sum(i['fee'] for i in fees), 8)
#counts total balance
def total_balance(fees):
    return round(sum(i['balance_diff'] for i in fees), 8)
#counts number of transactions
def number_transactions(fees):
    return len(fees)
#summary positive fee
#wallet_adress = input()
#wallet_adress = '15fPSaaCkHsJBBS5WQ7fStsztGNonPqbMn'
#print(total_balance(transactions))