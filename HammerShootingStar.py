import yfinance as yf
import pandas as pd
from datetime import date

def find_hammer_shooting_star_weekly(stock_symbol, start_date, end_date):
    # Fetch historical stock data with weekly frequency
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date, interval='1wk')

    # Calculate relevant prices for Hammer and Shooting Star patterns
    stock_data['Body'] = abs(stock_data['Close'] - stock_data['Open'])
    stock_data['UpperShadow'] = stock_data['High'] - stock_data[['Open', 'Close']].max(axis=1)
    stock_data['LowerShadow'] = stock_data[['Open', 'Close']].min(axis=1) - stock_data['Low']

    # Identify Hammer and Shooting Star patterns
    is_hammer = (stock_data['LowerShadow'] >= 2 * stock_data['Body']) & (stock_data['UpperShadow'] <= 0.1 * stock_data['Close'])
    is_shooting_star = (stock_data['UpperShadow'] >= 2 * stock_data['Body']) & (stock_data['LowerShadow'] <= 0.1 * stock_data['Close'])

    # Filter data to show only weeks with Hammer and Shooting Star patterns
    hammer_data = stock_data[is_hammer]
    shooting_star_data = stock_data[is_shooting_star]

    return hammer_data, shooting_star_data

if __name__ == "__main__":
    # Set the stock symbol, start date, and end date
    stock_symbol = "AAPL"  # Apple Inc. stock symbol
    start_date = date(2022, 1, 1)  # Change this to the desired start date
    end_date = date(2022, 12, 31)  # Change this to the desired end date

    # Find Hammer and Shooting Star patterns in the weekly time frame
    hammer_data, shooting_star_data = find_hammer_shooting_star_weekly(stock_symbol, start_date, end_date)

    # Display the results
    print("Hammer Patterns (Weekly):")
    print(hammer_data)

    print("\nShooting Star Patterns (Weekly):")
    print(shooting_star_data)
