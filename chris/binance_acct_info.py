
#This will get account holdings and other account info from binance

import requests

url = "https://testnet.binance.vision/api/v3/account?timestamp=1597799212569&signature=9007daefe7784e05afb3144b41e0cccff3f2a19bdb64608fb671768636475ba4"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
