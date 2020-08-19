#This will withdraw from binance
#Variables still need to be filled in the url

import requests

url = "https://testnet.binance.vision/wapi/v3/withdraw.html?asset=&withdrawOrderId=&network=&address=&addressTag=&amount=&transactionFeeFlag=&name=&timestamp=1597796428553&signature=b861169fb612ccc278ead4f8b3c16b8a80f0df7b54e66bb24fe08af0ae3dfc12"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))