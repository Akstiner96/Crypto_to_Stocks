
#example from internet

import the relevant modules
import pandas as pd
import numpy as np
from pandas_datareader import data
import requests
from math import sqrt
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
%matplotlib inline
#read the stock tickers and names into a DataFrame
stocks = pd.read_csv('NYSE.txt',delimiter="\t")
stocks_list = []
#iterate through stock list and append tickers into our empty list
for symbol in stocks['Symbol']:
    stocks_list.append(symbol)
#create empty list to hold our return series DataFrame for each stock
frames = []
 
for stock in stocks_list:
    
    try:
 
        #download stock data and place in DataFrame
        df = data.DataReader(stock, 'yahoo',start='1/1/2000')
        
        #create column to hold our 90 day rolling standard deviation
        df['Stdev'] = df['Close'].rolling(window=90).std()
        #create a column to hold our 20 day moving average
        df['Moving Average'] = df['Close'].rolling(window=20).mean()
        #create a column which holds a TRUE value if the gap down from previous day's low to next 
        #day's open is larger than the 90 day rolling standard deviation
        df['Buy1'] = (df['Open'] - df['Low'].shift(1)) < -df['Stdev'] 
        #create a column which holds a TRUE value if the opening price of the stock is above the 20 day moving average 
        df['Buy2'] = df['Open'] > df['Moving Average']
        #create a column that holds a TRUE value if both buy criteria are also TRUE
        df['BUY'] = df['Buy1'] & df['Buy2']
        
        #create a column which holds a TRUE value if the gap up from previous day's high to next 
        #day's open is larger than the 90 day rolling standard deviation
        df['Sell1'] = (df['Open'] - df['High'].shift(1)) > df['Stdev'] 
        #create a column which holds a TRUE value if the opening price of the stock is below the 20 day moving average 
        df['Sell2'] = df['Open'] < df['Moving Average']
        #create a column that holds a TRUE value if both sell criteria are also TRUE
        df['SELL'] = df['Sell1'] & df['Sell2']
        
        #calculate daily % return series for stock
        df['Pct Change'] = (df['Close'] - df['Open']) / df['Open']
        
        #create a strategy return series by using the daily stock returns mutliplied by 1 if we are long and -1 if we are short
        df['Rets'] = np.where(df['BUY'],df['Pct Change'], 0)
        df['Rets'] = np.where(df['SELL'],-df['Pct Change'], df['Rets'])
        
        #append the strategy return series to our list
        frames.append(df['Rets'])
        
        
    except:
        pass
#concatenate the individual DataFrames held in our list- and do it along the column axis
masterFrame = pd.concat(frames,axis=1)
 
#create a column to hold the sum of all the individual daily strategy returns
masterFrame['Total'] = masterFrame.sum(axis=1)
#fill 'NaNs' with zeros to allow our "count" function below to work properly
masterFrame.fillna(0,inplace=True)
#create a column that hold the count of the number of stocks that were traded each day
#we minus one from it so that we dont count the "Total" column we added as a trade.
masterFrame['Count'] = (masterFrame != 0).sum(axis=1) - 1
#create a column that divides the "total" strategy return each day by the number of stocks traded that day to get equally weighted return.
masterFrame['Return'] = masterFrame['Total'] / masterFrame['Count']
#plot the strategy returns
masterFrame['Return'].dropna().cumsum().plot()