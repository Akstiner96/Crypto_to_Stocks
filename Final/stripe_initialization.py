{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 4
}


import os
import datetime
import json
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import alpaca_trade_api as tradeapi
import requests
import pprint
import stripe

load_dotenv()
def account_creation():
    stripe_public = os.getenv('stripe_public')
    stripe_private = os.getenv('stripe_private')
    stripe.api_key=stripe_private

    print('Who will be the owner of this acccount? Type their email below.')
    account_owner = str(input())

    ## set up the neutral account
    stripe.Account.create(
        type='custom',
        country='US',
        email=account_owner,
        capabilities={
            "card_payments":{"requested":True},
            "transfers":{"requested":True},
        },
        business_type='non_profit'
    )

    print('Type other account owner names below')
    name_list = []
    i=0
    while 1:
        i+=1
        name = input('Enter name %d: '%i)
        if name = '':
            break
        name_list.append(name)
    print(name_list)

    ## Using a Stripe function, create Persons for this account
    for name in name_list:
        stripe.Account.create_person(
            "acct_1HILPbIW2XJXscel",
            first_name=name,
        )

    ## List persons in order to obtain their ID    
    persons = stripe.Account.list_persons(
        "acct_1HILPbIW2XJXscel",
        limit=4,
        )    
    ## Create a list of person ID's
    person_id = []
    for person in persons:
        identity = persons["id"]
        person_id.append(identity)

    ## Make these persons executives of the account
    for person in person_id:
        stripe.Account.modify_person(
            "acct_1HILPbIW2XJXscel",
            person,
            relationship={"executive":True}
        )
    ## Show the previous change on the account information
    stripe.Account.modify(
        "acct_1HILPbIW2XJXscel",
        company={
            "executives_provided":True,
        }
    )

    ## Creating payment sources
    email_list = []
    for name in name_list:
        email=f"{name}@test.com"
        email_list.append(email)
    
    for email in email_list:
        sources = {}
        source = stripe.Source.create(
            type='ach_credit_transfer',
            currency='usd',
            owner={
                'email':email
            }
        )
        sources.append(source)

    ## Grab all the source ID's
    source_list = []
    for source in sources:
        ident = source["id"]
        source_list.append(ident)

    ## Fund the account by charging all persons
    for source in source_list:
        stripe.Charge.create(
            amount=100,
            currency='usd',
            source=source
        )
        
        
    ## Check balance to ensure deposits were successful
    balance = stripe.Balance.retrieve()
    
    return(balance)