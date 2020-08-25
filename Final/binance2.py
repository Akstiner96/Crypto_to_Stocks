import requests
import json
import datetime
from datetime import date
from time import mktime
import hmac
import hashlib
import time
import urllib3
import urllib.request

def get_account_holdings():
    '''This will get account holdings and other account info from binance'''
    
    #Get timestamp in milliseconds 
    timestamp = int(time.time())*1000
    
    #separate query string from url
    query_string = f"timestamp={timestamp}"
    
    #use secret key and query string to create signature
    secret = 'OaMImZjZCv5JHDqRIyaJjYEvhBPdGhUlsKVWN613gPdBMIdFjdnoF4tB98O16BMY' 
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest() 
    
    url = f"https://testnet.binance.vision/api/v3/account?timestamp={timestamp}&signature={signature}"
    
    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'X-MBX-APIKEY': 'ehalnzjFpYi1lIdsGu4236ddOMMypbAyqjMH3FS7XkYNagISeZQGtiyne9hcmrhz'
  }

    response = requests.request("GET", url, headers=headers, data = payload)
    return (response.text.encode('utf8'))


def buy_ETH(quantity):
    
    '''Buy request for binance api, this will buy Ether'''
    
    #Get timestamp in milliseconds 
    timestamp = int(time.time())*1000
   
    #separate parameters from url
    query_string = f"symbol=ETHBUSD&side=BUY&type=MARKET&quantity={quantity}&newClientOrderId=my_order_id_1&newOrderRespType=ACK&timestamp={timestamp}" 

    #use secret key and query string to create signature
  
    secret = 'OaMImZjZCv5JHDqRIyaJjYEvhBPdGhUlsKVWN613gPdBMIdFjdnoF4tB98O16BMY'

    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
   
    url = f"https://testnet.binance.vision/api/v3/order?symbol=ETHBUSD&side=BUY&type=MARKET&quantity={quantity}&newClientOrderId=my_order_id_1&newOrderRespType=ACK&timestamp={timestamp}&signature={signature}" 

    payload = {}
    headers = {
      'Content-Type': 'application/json',
      'X-MBX-APIKEY': 'ehalnzjFpYi1lIdsGu4236ddOMMypbAyqjMH3FS7XkYNagISeZQGtiyne9hcmrhz'
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

#   print(response.text.encode('utf8'))
  return(response.text.encode('utf8'))


def withdraw(quantity):
    '''Withdraw Ether from Binance and send to address'''
    '''Because this is a testnet this function will not work. It should work on the live binance api'''
  
    timestamp = int(time.time())*1000
    
    query_string = "asset=ETH&address=0x2326D3E915DC4249dD8bD904F02dBE391056f03D&amount={quantity}&timestamp={timestamp}"
    
    secret = 'OaMImZjZCv5JHDqRIyaJjYEvhBPdGhUlsKVWN613gPdBMIdFjdnoF4tB98O16BMY'
    
    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    url = "https://testnet.binance.vision/wapi/v3/withdraw.html?asset=ETH&address=0x2326D3E915DC4249dD8bD904F02dBE391056f03D&amount={quantity}&timestamp={timestamp}&signature={signature}"

    payload = {}
    headers = {
    'Content-Type': 'application/json',
    'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
  }

    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    
    return(response.text.encode('utf8'))


def transfer_profits_to_exchange(bank_balance, binance_balance):
    ''' This function sends money to binance and calculates a new bank balance and new binance balance.  
        In reality this would be an ACH transfer or manual credit card entry. '''

    profits_to_transfer = bank_balance
    
    balances = []
    if bank_balance > 0:
        bank_balance = 0
        balances.append(bank_balance)
        
        binance_balance = profits_to_transfer
        balances.append(binance_balance)
        print()
        print(f"Transfer to Binance successful. Your binance_balance is now {binance_balance}.") 
        print(f"Your bank balance is now {bank_balance}.")
        
                           
    else:
        print("Transfer not completed to Binance. There are no profits to transfer")
        print(bank_balance, binance_balance)  
    return balances


def get_eth_price():
    
    #use binance api to get all symbols and prices
    symbols = get_symbols()
    
    #convert bytes object to string
    symbols = symbols.decode("utf-8") 
    
    #convert str to json
    symbols = json.loads(symbols)
    
    #get eth price
    eth_price = float(symbols[2]['price'])  
    
    return eth_price

def get_eth_amount():

    url = "https://testnet.binance.vision/sapi/v1/capital/config/getall?timestamp=1598225404584&signature=57c36cddd17109c3003bef6b6e8e73c458194f50bef31d015e9c47e6432b6620"

    payload = {}
    headers = {
      'Content-Type': 'application/json',
      'X-MBX-APIKEY': 'IfBnaRxLujIJRXGkIgNq2z3g1F8QC9kA59sJ6xRPObURqdCE5jdGDpp8kFv72YcU'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    return (response.text.encode('utf8'))

def test_connectivity():

    url = "https://testnet.binance.vision/api/v3/ping"

    payload = {}
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))
    return (response.text.encode('utf8'))

def check_recent_trades():
    
    url = "https://testnet.binance.vision/api/v3/trades?symbol=ETHBUSD&limit=500"

    payload = {}
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data = payload)

    #print(response.text.encode('utf8'))
    return (response.text.encode('utf8'))


