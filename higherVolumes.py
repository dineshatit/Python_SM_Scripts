import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def check_higher_than_average_volume(symbol, lookback_days=10, multiplier=2):
    # Download historical data
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=lookback_days)).strftime('%Y-%m-%d')
    data = yf.download(symbol, start=start_date, end=end_date)

    # Calculate average daily trading volume
    avg_volume = data['Volume'].mean()

    # Resample data to 15-minute intervals
    data_15min = data.resample('15T').sum()

    # Filter for volumes higher than 2 times the average
    high_volume_data = data_15min[data_15min['Volume'] > multiplier * avg_volume]

    return high_volume_data

# Example: Check for higher-than-average volumes for the symbol 'AAPL'
symbol = 'DIXON'
result = check_higher_than_average_volume(symbol)
print(result)
