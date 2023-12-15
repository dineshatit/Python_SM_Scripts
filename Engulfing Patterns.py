import pandas as pd
from datetime import date
import yfinance as yf  # You may need to install yfinance: pip install yfinance

def find_engulfing_patterns(stock_symbol, start_date, end_date):
    # Download historical stock data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Identify bullish engulfing patterns
    bullish_engulfing = (stock_data['Close'] > stock_data['Open'].shift(1)) & (stock_data['Open'] < stock_data['Close'].shift(1))

    # Identify bearish engulfing patterns
    bearish_engulfing = (stock_data['Open'] > stock_data['Close'].shift(1)) & (stock_data['Close'] < stock_data['Open'].shift(1))

    # Filter data to show only days with engulfing patterns
    bullish_engulfing_data = stock_data[bullish_engulfing]
    bearish_engulfing_data = stock_data[bearish_engulfing]

    return bullish_engulfing_data, bearish_engulfing_data

if __name__ == "__main__":
    # Set the stock symbol, start date, and end date
    stock_symbol = "AAPL"  # Change this to the desired stock symbol
    start_date = date(2022, 1, 1)  # Change this to the desired start date
    end_date = date(2022, 12, 31)  # Change this to the desired end date

    # Find bullish and bearish engulfing patterns
    bullish_engulfing, bearish_engulfing = find_engulfing_patterns(stock_symbol, start_date, end_date)

    # Display the results
    print("Bullish Engulfing Patterns:")
    print(bullish_engulfing)

    print("\nBearish Engulfing Patterns:")
    print(bearish_engulfing)
