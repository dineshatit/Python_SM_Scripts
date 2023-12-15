import yfinance as yf
import matplotlib.pyplot as plt

def fetch_stock_data(ticker_symbol, start_date, end_date):
    # Download stock data from Yahoo Finance
    stock_data = yf.download(ticker_symbol+".BO", start=start_date, end=end_date)
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
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def identify_breakout_reversal(data, fib_levels):
    breakout_points = [i for i in range(1, len(data)-1) if data[i-1] > fib_levels[0] and data[i] < fib_levels[0] and data[i+1] > fib_levels[0]]
    reversal_points = [i for i in range(1, len(data)-1) if data[i-1] < fib_levels[1] and data[i] > fib_levels[1] and data[i+1] < fib_levels[1]]

    return breakout_points, reversal_points

# Example usage:
ticker_symbol = "NATIONALUM"
start_date = "2022-12-15"
end_date = "2023-12-16"

stock_data = fetch_stock_data(ticker_symbol, start_date, end_date)
fibonacci_levels = calculate_fibonacci_levels(stock_data)
plot_fibonacci_levels(stock_data, fibonacci_levels, f"Fibonacci Levels for {ticker_symbol}")

breakout_points, reversal_points = identify_breakout_reversal(stock_data, fibonacci_levels)
print(f"Breakout points: {breakout_points}")
print(f"Reversal points: {reversal_points}")
