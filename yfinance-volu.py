import yfinance as yf
import pandas as pd

def get_high_volume_stocks(symbol, threshold=2.0, lookback_days=50):
    # Download historical stock data
    stock_data = yf.download(symbol + ".NS", period='1y')

    # Calculate average volume
    average_volume = stock_data['Volume'].tail(lookback_days).mean()

    # Filter for days with volume higher than the threshold
    high_volume_days = stock_data[stock_data['Volume'] > threshold * average_volume]

    return high_volume_days[['Open', 'High', 'Low', 'Close', 'Volume']]

def main():
    # Example: Check for higher-than-average volume for ICICI Bank (ICICIBANK.NS)
    symbol = 'DIXON'
    high_volume_stocks = get_high_volume_stocks(symbol)

    print(f"High Volume Days for {symbol}:\n{high_volume_stocks}")

if __name__ == "__main__":
    main()
