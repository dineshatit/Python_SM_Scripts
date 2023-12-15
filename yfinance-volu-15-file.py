import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_high_volume_15min(symbol, threshold=2.0):
    # Download intraday data for the last 5 days (you can adjust the period)
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=10)).strftime('%Y-%m-%d')

    # Please note that yfinance may not support all Indian stocks for intraday data
    try:
        intraday_data = yf.download(symbol + ".NS", start=start_date, end=end_date, interval='15m')
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return pd.DataFrame()

    # Calculate average volume
    average_volume = intraday_data['Volume'].mean()

    # Filter for 15-minute periods with volume higher than the threshold
    high_volume_periods = intraday_data[intraday_data['Volume'] > threshold * average_volume]

    return high_volume_periods[['Open', 'High', 'Low', 'Close', 'Volume']]

def main():
    # Read stock symbols from a file (one symbol per line)
    with open('stock_symbols.txt', 'r') as file:
        stock_symbols = [line.strip() for line in file.readlines()]


















    for symbol in stock_symbols:
        print(f"\nChecking for {symbol}...")
        high_volume_periods = get_high_volume_15min(symbol)

        if not high_volume_periods.empty:
            print(f"High Volume Periods for {symbol}:\n{high_volume_periods}")
        else:
            print(f"No data available for {symbol}")

if __name__ == "__main__":
    main()
