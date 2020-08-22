import numpy as np

#Generate signals and put in dataframe, each function could be a different strategy.

def generate_sma2_sma13_signals(signals_df):
    
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
    
    return(signals_df)