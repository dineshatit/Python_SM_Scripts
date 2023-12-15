import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_intraday_stock_data(ticker_symbol, start_date, end_date, interval):
    # Download intraday stock data from Yahoo Finance
    stock_data = yf.download(ticker_symbol+ ".BO", start=start_date, end=end_date, interval=interval)
    return stock_data['Adj Close']

def calculate_fibonacci_levels(data):
    max_price = max(data)
    min_price = min(data)

    # Calculate Fibonacci retracement levels
    fib_levels = [max_price - level * (max_price - min_price) for level in [0, 0.236, 0.382, 0.5, 0.618, 1]]

    return fib_levels

def plot_fibonacci_levels(data, fib_levels, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data, label="Stock Price")
    for level in fib_levels:
        plt.axhline(y=level, color='r', linestyle='--', label="Fibonacci Level")
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def identify_breakout_reversal(data, fib_levels):
    breakout_points = [i for i in range(1, len(data)-1) if data[i-1] > fib_levels[0] and data[i] < fib_levels[0] and data[i+1] > fib_levels[0]]
    reversal_points = [i for i in range(1, len(data)-1) if data[i-1] < fib_levels[1] and data[i] > fib_levels[1] and data[i+1] < fib_levels[1]]

    return breakout_points, reversal_points

# NIFTY 50 stock symbols
#nifty_symbols = ['NATIONALUM', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'ITC', 'KOTAKBANK', 'SBIN',
#                'ASIANPAINT', 'AXISBANK', 'LT', 'MARUTI', 'BAJFINANCE', 'WIPRO', 'ONGC', 'SUNPHARMA', 'BHARTIARTL',
#                'NESTLEIND', 'ULTRACEMCO', 'LUPIN', 'BAJAJ-AUTO', 'HCLTECH', 'BAJAJFINSV', 'ADANIPORTS', 'TATAMOTORS',
#                'POWERGRID', 'NTPC', 'GAIL', 'JSWSTEEL', 'INDUSINDBK', 'IOC', 'TITAN', 'DRREDDY', 'BPCL', 'GRASIM',
#                'COALINDIA', 'M&M', 'UPL', 'TECHM', 'SHREECEM', 'JSPL', 'HEROMOTOCO', 'EICHERMOT', 'DIVISLAB',
#                'BAJAJHLDNG', 'ICICIPRULI']
nifty_symbols = ['NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM',
                'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM',
                'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'HCLTECH', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM',
                'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'INDUSINDBK', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM',
                'NATIONALUM', 'NATIONALUM&M', 'NATIONALUM', 'NATIONALUM', 'SHREECEM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM', 'NATIONALUM',
                'NATIONALUM', 'NATIONALUM']
for ticker_symbol in nifty_symbols:
        print(f"\nChecking for {ticker_symbol}")
        # Example usage:
        #ticker_symbol = "INFY"
        start_date = "2023-12-15"
        end_date = "2023-12-16"
        interval = "30m"

        intraday_data = fetch_intraday_stock_data(ticker_symbol, start_date, end_date, interval)
        fibonacci_levels = calculate_fibonacci_levels(intraday_data)
        plot_fibonacci_levels(intraday_data, fibonacci_levels, f"Fibonacci Levels for {ticker_symbol} - {interval}")

        breakout_points, reversal_points = identify_breakout_reversal(intraday_data, fibonacci_levels)
        print(f"Breakout points: {breakout_points}")
        print(f"Reversal points: {reversal_points}")
