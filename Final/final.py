{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}

import binance2
import stonk_pull
import stripe_initialization
import numpy as np
import pandas as pd
import time
import requests
import os
from dotenv import load_dotenv

load_dotenv()

## Create account and initialize all the persons related to the account - from stripe_initialization.py
account_creation()

## Send money from Stripe to Alpaca
def deposit(balance):
    stripe.Payout.create(amount=balance, currency="usd")
    
    ##Get account balance from Alpaca
    account = api.get_account()
    balance = account.equity()
    return(balance)

## Trade securities
def conduct_trades(deposit):
    #from stonk_pull.py - pull in data and initialize the details of our investments
    load()
    data_pull(api)
    data_clean(data)
    api=load()
    data=data_pull(api)
    cleaned = data_clean(data)
    
    while True:
        ## Stream stock data - Alpaca kinda sucks so this is only sorta what it would look like
        {
            "action": "listen",
            "data": {
                "streams": ["trade_updates"]
            }
        }
        
        ## Trade signals and buy/sell orders
        if SPY_pct_change <= -2:
            api.submit_order(
                symbol='SPY',
                qty='',
                side='buy',
                type='market',
                time_in_force='gtc'
            )
        elif SPY_pct_change >= 2:
            api.submit_order(
                symbol='SPY',
                qty='',
                side='sell',
                type='market',
                time_in_force='gtc'
            )
        else:
            do nothing
            
        ## Check account balance
        account = api.get_account()
        ## Withdraw profits
        equity = account.equity()
        if equity > balance:
            profit = equity - balance
            #some function here that withdraws profit from you alpaca account that alpaca does not have
            
        ##Pretending money is now back in the Stripe account, this will send to binance
        stripe.Payout.create(amount=balance, currency="usd")
        
        ## Call trade functions from the binance.py file
        get_account_holdings()
        buy_ETH()
        #withdraw function sends money straight to a smart contract which will immediately disperse funds
        withdraw()
        
        
        # Break loop if strategy does not make profits
        if equity < balance:
            break
            
            
        