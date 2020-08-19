# Withdraw Ether from Binance and send to address

import requests

def withdraw():

  url = "https://testnet.binance.vision/wapi/v3/withdraw.html?asset=ETH&address=0x2326D3E915DC4249dD8bD904F02dBE391056f03D&amount=10&timestamp=1597802688956&signature=670269ee2e2782f5f241273f2bddc9cea16576b0b616933670ddf299213c37ca"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
  }

  response = requests.request("POST", url, headers=headers, data = payload)

  print(response.text.encode('utf8'))
  return(response.text.encode('utf8'))

withdraw()