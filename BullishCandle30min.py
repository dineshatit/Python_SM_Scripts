import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_intraday_stock_data(symbol, start_date, end_date, interval):
    # Fetch intraday stock data using yfinance
    stock_data = yf.download(symbol+".BO", start=start_date, end=end_date, interval=interval)
    return stock_data

def plot_stock_data(df, title):
    plt.figure(figsize=(12, 6))
    plt.plot(df['Close'], label='Close Price', color='blue')
    plt.title(title)
    plt.xlabel('Datetime')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def find_bullish_candles(df, price_change_threshold=5.0):
    # Identify bullish candles with a price change greater than the threshold
    df['bullish_candle'] = (df['Close'] > df['Open']) & ((df['Close'] / df['Open'] - 1) * 100 > price_change_threshold)
    bullish_candles = df[df['bullish_candle']]
    return bullish_candles

def main():
    # NIFTY 50 stock symbols
    nifty_symbols = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'ITC', 'KOTAKBANK', 'HDFC', 'SBIN',
                'ASIANPAINT', 'AXISBANK', 'LT', 'MARUTI', 'BAJFINANCE', 'WIPRO', 'ONGC', 'SUNPHARMA', 'BHARTIARTL',
                'NESTLEIND', 'ULTRACEMCO', 'LUPIN', 'BAJAJ-AUTO', 'HCLTECH', 'BAJAJFINSV', 'ADANIPORTS', 'TATAMOTORS',
                'POWERGRID', 'NTPC', 'GAIL', 'JSWSTEEL', 'INDUSINDBK', 'IOC', 'TITAN', 'DRREDDY', 'BPCL', 'GRASIM',
                'COALINDIA', 'M&M', 'UPL', 'TECHM', 'SHREECEM', 'JSPL', 'HEROMOTOCO', 'EICHERMOT', 'DIVISLAB',
                'BAJAJHLDNG', 'ICICIPRULI']
    for symbol in nifty_symbols:
        print(f"\nChecking for {symbol}")
        # Replace 'YOUR_STOCK_SYMBOL' with the desired stock symbol (e.g., 'AAPL' for Apple)
        #symbol = 'INFY'
        
        # Replace 'START_DATE' and 'END_DATE' with the desired date range
        start_date = '2023-11-01'
        end_date = '2023-12-14'
        
        # Define the interval for 30 minutes
        interval = '30m'

        # Fetch intraday stock data
        intraday_data = fetch_intraday_stock_data(symbol, start_date, end_date, interval)
        
        # Plot intraday stock data
        #plot_stock_data(intraday_data, f'{symbol} Intraday Stock Price')

        # Find bullish candles with a price change greater than 0.80%
        bullish_candles = find_bullish_candles(intraday_data, price_change_threshold=1.8)
        
        # Display the result
        print(f'Bullish Candles with Price Change > 0.80%:\n{bullish_candles[["Open", "Close"]]}')

if __name__ == '__main__':
    main()
