import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_high_volume_15min(symbol, threshold=2.0):
    # Download intraday data for the last 5 days (you can adjust the period)
    #end_date = datetime.today().strftime('%Y-%m-%d')
    #start_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    end_date = pd.to_datetime("today")
    start_date = end_date - pd.to_timedelta(1, unit="D")

    try:
        intraday_data = yf.download(symbol + ".NS", start=start_date, end=end_date, interval='15m')
    except Exception as e:
        return pd.DataFrame(), f"Error fetching data for {symbol}: {e}"

    # Calculate average volume
    average_volume = intraday_data['Volume'].mean()

    # Filter for 15-minute periods with volume higher than the threshold
    high_volume_periods = intraday_data[intraday_data['Volume'] > threshold * average_volume]

    return high_volume_periods[['Open', 'High', 'Low', 'Close', 'Volume']], None

def main():
    # NIFTY 50 stock symbols
    nifty_symbols = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'ITC', 'KOTAKBANK', 'HDFC', 'SBIN',
                     'ASIANPAINT', 'AXISBANK', 'LT', 'MARUTI', 'BAJFINANCE', 'WIPRO', 'ONGC', 'SUNPHARMA', 'BHARTIARTL',
                     'NESTLEIND', 'ULTRACEMCO', 'LUPIN', 'BAJAJ-AUTO', 'HCLTECH', 'BAJAJFINSV', 'ADANIPORTS', 'TATAMOTORS',
                     'POWERGRID', 'NTPC', 'GAIL', 'JSWSTEEL', 'INDUSINDBK', 'IOC', 'TITAN', 'DRREDDY', 'BPCL', 'GRASIM',
                     'COALINDIA', 'M&M', 'UPL', 'TECHM', 'SHREECEM', 'JSPL', 'HEROMOTOCO', 'EICHERMOT', 'DIVISLAB',
                     'BAJAJHLDNG', 'ICICIPRULI']

    with open('output_nifty.txt', 'w') as output_file:
        for symbol in nifty_symbols:
            print(f"\nChecking for {symbol}...")
            high_volume_periods, error_message = get_high_volume_15min(symbol)

            if not high_volume_periods.empty:
                output_file.write(f"High Volume Periods for {symbol}:\n{high_volume_periods}\n")
                print(f"High Volume Periods for {symbol}:\n{high_volume_periods}")
            elif error_message:
                output_file.write(f"{error_message}\n")
                print(error_message)
            else:
                output_file.write(f"No data available for {symbol}\n")
                print(f"No data available for {symbol}")

if __name__ == "__main__":
    main()
