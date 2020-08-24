import requests
import json
import datetime
from datetime import date
from time import mktime
import hmac
import hashlib


def get_account_holdings():
    '''This will get account holdings and other account info from binance'''
    
    #Get timestamp in milliseconds 
    timestamp = str(time.time())*1000
    
    #separate query string from url
#     query string = 'timestamp =' +timestamp+ '&'
    
    #use secret key and query string to create signature
#     secret = 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'

#     signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
#     query string = 'timestamp =' +timestamp+ 
    
#     url = "https://testnet.binance.vision/api/v3/account?timestamp=" +timestamp+ "&signature ="+signature+"
    
    url = "https://testnet.binance.vision/api/v3/account?timestamp=%s&signature=9007daefe7784e05afb3144b41e0cccff3f2a19bdb64608fb671768636475ba4"%(timestamp)
    
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
    
    #Get timestamp in milliseconds 
    timestamp = str(time.time())*1000
   
  
    #separate parameters from url
    query_string = f"symbol=ETHBUSD&side=BUY&type=MARKET&quantity=1&newClientOrderId=my_order_id_1&newOrderRespType=ACK&timestamp=%s{timestamp}" 

    #use secret key and query string to create signature
    secret = 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'

    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
   
    url = f"https://testnet.binance.vision/api/v3/order?symbol=ETHBUSD&side=BUY&type=MARKET&quantity=1&newClientOrderId=my_order_id_1&newOrderRespType=ACK&timestamp={timestamp}&signature={signature}" 

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

#   print(response.text.encode('utf8'))
  return(response.text.encode('utf8'))



def withdraw():
  '''Withdraw Ether from Binance and send to address'''
  
    timestamp = str(time.time())*1000
    url = "https://testnet.binance.vision/wapi/v3/withdraw.html?      asset=ETH&address=0x2326D3E915DC4249dD8bD904F02dBE391056f03D&amount=10&timestamp=1597802688956&signature=670269ee2e2782f5f241273f2bddc9cea16576b0b616933670ddf299213c37ca"

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

    initial_deposit = 100000
    profit = bank_balance - initial_deposit
    balances = []
    if profit > 0:
        bank_balance = bank_balance - profit
        balances.append(bank_balance)
        
        binance_balance = binance_balance + profit
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

    print(response.text.encode('utf8'))
    return (response.text.encode('utf8'))

def create_signature():

    t = datetime.datetime.now()
    unix_secs = mktime(t.timetuple())
    timestamp = unix_secs*1000
    timestamp = int(timestamp)
    timestamp = str(timestamp)
    print(timestamp)

    query_string = "symbol=ETHBUSD&side=BUY&type=MARKET&quantity=1&newClientOrderId=my_order_id_1&newOrderRespType=ACK&timestamp=%s"(timestamp) 
    secret = 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'

    signature = hmac.new(secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
    
    
