#This will get all the symbols and a current price for crypto traded on binance



import requests

def get_symbols():

  url = "https://testnet.binance.vision/api/v3/ticker/price?"

  payload = {}
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("GET", url, headers=headers, data = payload)

  print(response.text.encode('utf8'))
  return(response.text.encode('utf8'))

get_symbols()