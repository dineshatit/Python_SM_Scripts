import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_intraday_data(symbol, interval='1m', days_back=1):
    end_date = pd.Timestamp.now()
    start_date = end_date - pd.DateOffset(days=days_back)
    
    data = yf.download(symbol+".BO", start=start_date, end=end_date, interval=interval)
    
    return data

def find_double_top(data,symbol):
    # Find local maxima in the data (potential top points)
    local_maxima = (data['High'] > data['High'].shift(1)) & (data['High'] > data['High'].shift(-1))

    # Filter out the significant maxima (customize threshold as needed)
    significant_maxima = data[local_maxima & (data['High'] > data['High'].quantile(0.75))]

    # Plot the stock data and highlight double top points
    #plt.figure(figsize=(12, 6))
    #plt.plot(data['High'], label='High Prices')
    #plt.scatter(significant_maxima.index, significant_maxima['High'], color='red', label='Double Top')
    #plt.title(f'Stock Prices with Double Top Detection : {symbol}')
    #plt.xlabel('Date')
    #plt.ylabel('High Price')
    #plt.legend()
    #plt.show()

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
    interval = "15m"
    days_back = 1  # Adjust the number of days back as needed

    intraday_data = fetch_intraday_data(symbol, interval, days_back)
    double_top_points = find_double_top(intraday_data,symbol)

    print("Double Top Points:")
    print(double_top_points)
