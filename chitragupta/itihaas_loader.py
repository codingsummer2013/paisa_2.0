import os
from datetime import datetime

import yfinance as yf
import pandas as pd

# Define a list of NIFTY 50 stock symbols
from chitragupta import historical_data_wrapper
from shoorveer import satya

directory = os.path.dirname(__file__)
filename = os.path.join(directory, '../veda/historical_data.txt')

# Create a DataFrame to store historical data
historical_data = pd.DataFrame()


# Download historical data for each stock
def get_stocks_to_load():
    return satya.read_nifty_50();


def load():
    # Open the file in write mode, which will clear its contents
    with open(filename, "w") as file:
        # Writing nothing effectively clears the file
        pass

    for symbol in get_stocks_to_load():
        stock_data = yf.download(symbol + ".ns", start="2023-07-01", end=datetime.today().strftime("%Y-%m-%d"))
        for index, row in stock_data.iterrows():
            # Extract the time (index) and 'Adj Close' price from each row
            time = index.strftime('%Y-%m-%d')  # Convert the index to a string or use a suitable time format
            price = row['Adj Close']
            # Create a dictionary with time as the key and price as the value
            symbol_data = historical_data_wrapper.get(symbol)
            symbol_day_info = {'time': time, 'price': price}
            symbol_data.append(symbol_day_info)
            historical_data_wrapper.put(symbol, symbol_data)
    historical_data_wrapper.update_db_file()
    print("Historical data downloaded and saved.")
