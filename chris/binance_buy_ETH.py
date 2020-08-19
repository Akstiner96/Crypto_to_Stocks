##BUY request for binance api, this will buy Ether

import requests

url = "https://testnet.binance.vision/api/v3/order?symbol=ETHBUSD&side=BUY&type=MARKET&quantity=1&newClientOrderId=my_order_id_1&newOrderRespType=ACK&timestamp=1597796428553&signature=b861169fb612ccc278ead4f8b3c16b8a80f0df7b54e66bb24fe08af0ae3dfc12"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
