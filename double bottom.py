import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol + ".BO", start=start_date, end=end_date)
    return data

def find_double_bottom(data):
    # Find local minima in the data (potential bottom points)
    local_minima = (data['Low'] < data['Low'].shift(1)) & (data['Low'] < data['Low'].shift(-1))

    # Filter out the significant minima (customize threshold as needed)
    significant_minima = data[local_minima & (data['Low'] < data['Low'].quantile(0.25))]

    # Plot the stock data and highlight double bottom points
    plt.figure(figsize=(12, 6))
    plt.plot(data['Low'], label='Low Prices')
    plt.scatter(significant_minima.index, significant_minima['Low'], color='red', label='Double Bottom')
    plt.title('Stock Prices with Double Bottom Detection')
    plt.xlabel('Date')
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
#for symbol in nifty_symbols:
#    print(f"\nChecking for {symbol}...")
    # Example usage:
symbol = "AAPL"
start_date = "2022-12-13"
end_date = "2023-12-13"

stock_data = fetch_stock_data(symbol, start_date, end_date)
double_bottom_points = find_double_bottom(stock_data)

print("Double Bottom Points:")
print(double_bottom_points)
