import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_high_volume_stocks(symbol, start_date, end_date, time_frame_minutes=15):
    # Download historical data
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Resample data to 15-minute intervals
    stock_data_15min = stock_data['Volume'].resample(f'{time_frame_minutes}T').sum()

    # Calculate average volume
    average_volume = stock_data_15min.mean()

    # Filter stocks with volume higher than average
    high_volume_stocks = stock_data_15min[stock_data_15min > average_volume]

    return high_volume_stocks

if __name__ == "__main__":
    # Set the stock symbol and date range
    stock_symbol = 'DIXON'  # Replace with your desired stock symbol
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

    # Get high volume stocks
    high_volume_stocks = get_high_volume_stocks(stock_symbol, start_date, end_date)

    # Display the results
    print(f"High volume stocks for {stock_symbol} in 15-minute intervals:")
    print(high_volume_stocks.head(2))  # Displaying the top 2 entries
