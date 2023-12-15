import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_intraday_data(symbol, interval='1m', days_back=5):
    end_date = pd.Timestamp.now()
    start_date = end_date - pd.DateOffset(days=days_back)
    
    data = yf.download(symbol+".BO", start=start_date, end=end_date, interval=interval)
    
    return data

def find_double_bottom_reversalAll(data):
    # Find potential double bottom reversal patterns
    bottom_candidates = (data['Low'] < data['Low'].shift(1)) & (data['Low'] < data['Low'].shift(-1))
    # Find local maxima in the data (potential top points)
    local_maxima = (data['High'] > data['High'].shift(1)) & (data['High'] > data['High'].shift(-1))
    # Filter out the significant maxima (customize threshold as needed)
    significant_maxima = data[local_maxima & (data['High'] > data['High'].quantile(0.75))]
    # Filter out the significant candidates based on your criteria
    significant_bottoms = data[bottom_candidates & (data['Low'] < data['Low'].quantile(0.25))]

     # Plot the intraday data and highlight double bottom reversal candidates
    plt.figure(figsize=(12, 6))
    plt.plot(data['Low'], label='Low Prices')
    plt.scatter(significant_bottoms.index, significant_bottoms['Low'], color='red', label='Double Bottom Reversal')
    plt.title('Intraday Prices with Double Bottom Reversal Detection')
    plt.xlabel('Time')
    plt.ylabel('Low Price')
    plt.legend()
    #plt.show()
    # Plot the stock data and highlight double top points
    #plt.figure(figsize=(12, 6))
    plt.plot(data['High'], label='High Prices')
    plt.scatter(significant_maxima.index, significant_maxima['High'], color='blue', label='Double Top')
    plt.title('Stock Prices with Double Top Detection')
    plt.xlabel('Date')
    plt.ylabel('High Price')
    plt.legend()
    plt.show()

    return significant_bottoms

    



    

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
    interval = "5m"
    days_back = 1  # Adjust the number of days back as needed

    intraday_data = fetch_intraday_data(symbol, interval, days_back)
    double_bottom_reversal_candidates = find_double_bottom_reversalAll(intraday_data)
    print("Double Top Points:")
    print("Double Bottom Points:")
    print(double_bottom_reversal_candidates)