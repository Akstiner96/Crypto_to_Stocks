import alpaca_functions
import stonk_pull

# This simulates holding a current bank account that can send and receive
# money via ACH transfers to and from Alpaca
# We are assuming we have 100,000 in the bank and we are sending 100,000 to our alpaca algorithm

beginning_deposit = 100000

bank_balance = 100000

send_to_alpaca_amount = 100000

withdraw_from_alpaca_amount = 0

#load alpaca api keys
stonk_pull.load()

#Pull the data from alphavantage
data = stonk_pull.data_pull(api)

#Clean the data
stock_data_df = stonk_pull.data_clean(data)

#Sort earliest to latest.
stock_data_df.sort_index(inplace=True, ascending=True)

#To set up the crossover strategy select the one column we need, "Close", and set to dataframe
signals_df = stock_data_df['SPY Close'].to_frame()
print(signals_df.head())
