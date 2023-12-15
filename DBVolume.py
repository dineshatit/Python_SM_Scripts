import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_intraday_stock_data(symbol, start_date, end_date, interval):
    # Fetch intraday stock data using yfinance
    stock_data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
    return stock_data

def plot_stock_data(df, title):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.title(title)
    plt.xlabel('Datetime')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def find_double_bottoms(df):
    # Identify potential double bottom reversals
    df['bottom'] = df['Close'].shift(1) > df['Close']
    df['double_bottom'] = df['bottom'] & (df['Close'] > df['Close'].shift(-1))
    double_bottoms = df[df['double_bottom']]
    return double_bottoms

def volume_breakout(df, threshold=1.5):
    # Calculate 20-period average volume
    df['20period_avg_volume'] = df['Volume'].rolling(window=20).mean()
    
    # Detect volume breakout
    df['volume_breakout'] = df['Volume'] > (threshold * df['20period_avg_volume'])
    breakout_dates = df[df['volume_breakout']].index
    return breakout_dates

def main():
    # Replace 'YOUR_STOCK_SYMBOL' with the desired stock symbol (e.g., 'AAPL' for Apple)
    symbol = 'INFY'
    
    # Replace 'START_DATE' and 'END_DATE' with the desired date range
    start_date = '2023-12-01'
    end_date = '2023-12-15'
    
    # Define the interval for 15 minutes
    interval = '15m'

    # Fetch intraday stock data
    intraday_data = fetch_intraday_stock_data(symbol, start_date, end_date, interval)
    
    # Plot intraday stock data
    plot_stock_data(intraday_data, f'{symbol} Intraday Stock Price')

    # Find potential double bottom reversals
    double_bottoms = find_double_bottoms(intraday_data)
    print(f'Potential Double Bottom Reversals:\n{double_bottoms}')

    # Find volume breakouts
    breakout_dates = volume_breakout(intraday_data)
    print(f'Volume Breakout Dates:\n{breakout_dates}')

if __name__ == '__main__':
    main()
