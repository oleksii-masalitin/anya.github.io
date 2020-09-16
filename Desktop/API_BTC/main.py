import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

print(requests.get("https://chain.api.btc.com/v3/address/15fPSaaCkHsJBBS5WQ7fStsztGNonPqbMn/tx", headers=headers))