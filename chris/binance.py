import requests

def get_account_holdings():
  '''This will get account holdings and other account info from binance'''
  
  url = "https://testnet.binance.vision/api/v3/account?timestamp=1597799212569&signature=9007daefe7784e05afb3144b41e0cccff3f2a19bdb64608fb671768636475ba4"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
  }

  response = requests.request("GET", url, headers=headers, data = payload)

  print(response.text.encode('utf8'))
  return (response.text.encode('utf8'))



def buy_ETH():
  '''Buy request for binance api, this will buy Ether'''

  url = "https://testnet.binance.vision/api/v3/order?symbol=ETHBUSD&side=BUY&type=MARKET&quantity=1&newClientOrderId=my_order_id_1&newOrderRespType=ACK&timestamp=1597796428553&signature=b861169fb612ccc278ead4f8b3c16b8a80f0df7b54e66bb24fe08af0ae3dfc12"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
  }

  response = requests.request("POST", url, headers=headers, data = payload)

  print(response.text.encode('utf8'))
  return(response.text.encode('utf8'))



def get_symbols():
  '''This will get all the symbols and a current price for crypto traded on binance'''
  
  url = "https://testnet.binance.vision/api/v3/ticker/price?"

  payload = {}
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, data = payload)

 
  return(response.text.encode('utf8'))



def withdraw():
  '''Withdraw Ether from Binance and send to address'''
  
  url = "https://testnet.binance.vision/wapi/v3/withdraw.html?asset=ETH&address=0x2326D3E915DC4249dD8bD904F02dBE391056f03D&amount=10&timestamp=1597802688956&signature=670269ee2e2782f5f241273f2bddc9cea16576b0b616933670ddf299213c37ca"

  payload = {}
  headers = {
    'Content-Type': 'application/json',
    'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
  }

  response = requests.request("POST", url, headers=headers, data = payload)

  print(response.text.encode('utf8'))
  return(response.text.encode('utf8'))

