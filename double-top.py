import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol + ".BO", start=start_date, end=end_date)
    return data

def find_double_top(data):
    # Find local maxima in the data (potential top points)
    local_maxima = (data['High'] > data['High'].shift(1)) & (data['High'] > data['High'].shift(-1))

    # Filter out the significant maxima (customize threshold as needed)
    significant_maxima = data[local_maxima & (data['High'] > data['High'].quantile(0.75))]

    # Plot the stock data and highlight double top points
    plt.figure(figsize=(12, 6))
    plt.plot(data['High'], label='High Prices')
    plt.scatter(significant_maxima.index, significant_maxima['High'], color='red', label='Double Top')
    plt.title('Stock Prices with Double Top Detection')
    plt.xlabel('Date')
    plt.ylabel('High Price')
    plt.legend()
    plt.show()

    return significant_maxima

# NIFTY 50 stock symbols
nifty_symbols = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'ITC', 'KOTAKBANK', 'HDFC', 'SBIN',
                'ASIANPAINT', 'AXISBANK', 'LT', 'MARUTI', 'BAJFINANCE', 'WIPRO', 'ONGC', 'SUNPHARMA', 'BHARTIARTL',
                'NESTLEIND', 'ULTRACEMCO', 'LUPIN', 'BAJAJ-AUTO', 'HCLTECH', 'BAJAJFINSV', 'ADANIPORTS', 'TATAMOTORS',
                'POWERGRID', 'NTPC', 'GAIL', 'JSWSTEEL', 'INDUSINDBK', 'IOC', 'TITAN', 'DRREDDY', 'BPCL', 'GRASIM',
                'COALINDIA', 'M&M', 'UPL', 'TECHM', 'SHREECEM', 'JSPL', 'HEROMOTOCO', 'EICHERMOT', 'DIVISLAB',
                'BAJAJHLDNG', 'ICICIPRULI']
for symbol in nifty_symbols:
    print(f"\nChecking for {symbol}")
    # Example usage:
    symbol = symbol
    start_date = "2021-12-13"
    end_date = "2023-12-13"

    stock_data = fetch_stock_data(symbol, start_date, end_date)
    double_bottom_points = find_double_top(stock_data)

    print("Double Bottom Points:")
    print(double_bottom_points)
