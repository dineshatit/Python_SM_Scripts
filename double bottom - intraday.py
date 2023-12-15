import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_intraday_data(symbol, interval, days_back):
    end_date = pd.to_datetime("today")
    start_date = end_date - pd.to_timedelta(days_back, unit="D")

    data = yf.download(symbol+ ".BO", start=start_date, end=end_date, interval=interval)
    return data

def find_double_bottom(data):
    # Find local minima in the data (potential bottom points)
    local_minima = (data['Low'] < data['Low'].shift(1)) & (data['Low'] < data['Low'].shift(-1))

    # Filter out the significant minima (customize threshold as needed)
    significant_minima = data[local_minima & (data['Low'] < data['Low'].quantile(0.25))]

    # Plot the intraday data and highlight double bottom points
    plt.figure(figsize=(12, 6))
    plt.plot(data['Low'], label='Low Prices')
    plt.scatter(significant_minima.index, significant_minima['Low'], color='red', label='Double Bottom')
    plt.title('Intraday Prices with Double Bottom Detection')
    plt.xlabel('Time')
    plt.ylabel('Low Price')
    plt.legend()
    plt.show()

    return significant_minima
# NIFTY 50 stock symbols
nifty_symbols = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'ITC', 'KOTAKBANK', 'HDFC', 'SBIN',
                'ASIANPAINT', 'AXISBANK', 'LT', 'MARUTI', 'BAJFINANCE', 'WIPRO', 'ONGC', 'SUNPHARMA', 'BHARTIARTL',
                'NESTLEIND', 'ULTRACEMCO', 'LUPIN', 'BAJAJ-AUTO', 'HCLTECH', 'BAJAJFINSV', 'ADANIPORTS', 'TATAMOTORS',
                'POWERGRID', 'NTPC', 'GAIL', 'JSWSTEEL', 'INDUSINDBK', 'IOC', 'TITAN', 'DRREDDY', 'BPCL', 'GRASIM',
                'COALINDIA', 'M&M', 'UPL', 'TECHM', 'SHREECEM', 'JSPL', 'HEROMOTOCO', 'EICHERMOT', 'DIVISLAB',
                'BAJAJHLDNG', 'ICICIPRULI']
for symbol in nifty_symbols:
    print(f"\nChecking for {symbol}...")

    # Example usage:
    symbol = symbol
    interval = "5m"
    days_back = 1  # Adjust the number of days back as needed

    intraday_data = fetch_intraday_data(symbol, interval, days_back)
    double_bottom_points = find_double_bottom(intraday_data)

    print("Double Bottom Points:")
    print(double_bottom_points)
