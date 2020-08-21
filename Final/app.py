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

# Send money to alpaca. This function calculates a new bank balance after we send money to alpaca
# In reality this would be an ACH transfer from our bank to alpaca.
send_to_alpaca(send_to_alpaca_amount, bank_balance) 

#Pull the data from alphavantage
data = stonk_pull.data_pull(api)

#Clean the data
stock_data_df = stonk_pull.data_clean(data)

#Sort earliest to latest.
stock_data_df.sort_index(inplace=True, ascending=True)

#To set up the crossover strategy select the one column we need, "Close", and set to dataframe
signals_df = stock_data_df['SPY Close'].to_frame()
print(signals_df.head())

#Generate signals and put in dataframe

# Set the short window and long windows
short_window = 2
long_window = 13

#Set names of the windows
short_name = "SMA2"
long_name = "SMA13"

# Generate the short and long moving averages 
signals_df[short_name] = signals_df["SPY Close"].rolling(window=short_window).mean()
signals_df[long_name] = signals_df["SPY Close"].rolling(window=long_window).mean()
signals_df["Signal"] = 0.0

# Generate the trading signal 0 or 1,
# where 0 is when the short SMA is under the long SMA, and
# where 1 is when the short SMA is higher (or crosses over) the long SMA
signals_df["Signal"][short_window:] = np.where(
    signals_df[short_name][short_window:] > signals_df[long_name][short_window:], 1.0, 0.0
)

# Calculate the points in time at which a position should be taken, 1 or -1
signals_df["Buy/Sell"] = signals_df["Signal"].diff()

signals_df.to_csv('signals_2_13.csv') 
signals_df.tail(5)

#Send Buy and Sell orders using the signal, 1 = buy, -1 = sell, 0 = hold

if signals_df['Buy/Sell'].iloc[-1] == 0.0:
    symbol = "SPY"
    alpaca_functions.buy(symbol)
    
elif signals_df['Buy/Sell'].iloc[-1] == -1.0:
    symbol = "SPY"
    alpaca_functions.sell(symbol)
    
elif signals_df['Buy/Sell'].iloc[-1] == 1:
    pass

print(f"Current positions are: {api.list_positions()}")