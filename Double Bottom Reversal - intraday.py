import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def fetch_intraday_data(symbol, interval, days_back):
    end_date = pd.to_datetime("today")
    start_date = end_date - pd.to_timedelta(days_back, unit="D")

    data = yf.download(symbol+ ".BO", start=start_date, end=end_date, interval=interval)
    return data

def calculate_percentage(value, percentage):
    return value * (percentage / 100)

def get_high_volume_15min(symbol, threshold=2.0):
    # Download intraday data for the last 5 days (you can adjust the period)
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

def find_double_bottom_reversalAll(data,symbol):
    # Find potential double bottom reversal patterns
    bottom_candidates = (data['Low'] < data['Low'].shift(1)) & (data['Low'] < data['Low'].shift(-1))

    # Filter out the significant candidates based on your criteria
    significant_bottoms = data[bottom_candidates & (data['Low'] < data['Low'].quantile(0.25))]

     # Plot the intraday data and highlight double bottom reversal candidates
    #plt.figure(figsize=(12, 6))
    #plt.plot(data['Low'], label='Low Prices')
    #plt.scatter(significant_bottoms.index, significant_bottoms['Low'], color='red', label='Double Bottom Reversal')
    #plt.title(f'Intraday Prices with Double Bottom Reversal Detection : {symbol}')
    #plt.xlabel('Time')
    #plt.ylabel('Low Price')
    #plt.legend()
    #plt.show()

    return significant_bottoms

def find_double_bottom_reversal(data,symbol):
    # Find potential double bottom reversal patterns
    bottom_candidates = (data['Low'] < data['Low'].shift(1)) & (data['Low'] < data['Low'].shift(-1))

    # Filter out the significant candidates based on your criteria
    significant_bottoms = data[bottom_candidates & (data['Low'] < data['Low'].quantile(0.25))]

     # Plot the intraday data and highlight double bottom reversal candidates
    #plt.figure(figsize=(12, 6))
    #plt.plot(data['Low'], label='Low Prices')
    #plt.scatter(significant_bottoms.index, significant_bottoms['Low'], color='red', label='Double Bottom Reversal')
    #plt.title(f'Intraday Prices with Double Bottom Reversal Detection : {symbol}')
    #plt.xlabel('Time')
    #plt.ylabel('Low Price')
    #plt.legend()
    #plt.show()

    return significant_bottoms['Close']
# NIFTY 50 stock symbols
nifty_symbols = ['RELIANCE', 'TCS', 'HDFCBANK', 'INFY', 'HINDUNILVR', 'ICICIBANK', 'ITC', 'KOTAKBANK', 'HDFC', 'SBIN',
                'ASIANPAINT', 'AXISBANK', 'LT', 'MARUTI', 'BAJFINANCE', 'WIPRO', 'ONGC', 'SUNPHARMA', 'BHARTIARTL',
                'NESTLEIND', 'ULTRACEMCO', 'LUPIN', 'BAJAJ-AUTO', 'HCLTECH', 'BAJAJFINSV', 'ADANIPORTS', 'TATAMOTORS',
                'POWERGRID', 'NTPC', 'GAIL', 'JSWSTEEL', 'INDUSINDBK', 'IOC', 'TITAN', 'DRREDDY', 'BPCL', 'GRASIM',
                'COALINDIA', 'M&M', 'UPL', 'TECHM', 'SHREECEM', 'JSPL', 'HEROMOTOCO', 'EICHERMOT', 'DIVISLAB',
                'BAJAJHLDNG', 'ICICIPRULI']

# Capital 
capital = 33000
with open('output_nifty_vol_W.txt', 'w') as output_file:
    for symbol in nifty_symbols:
        print(f"\nChecking for {symbol}")

        # Example usage:
        symbol = symbol
        interval = "15m"
        days_back = 1  # Adjust the number of days back as needed

        intraday_data = fetch_intraday_data(symbol, interval, days_back)
        double_bottom_reversal_candidates = find_double_bottom_reversal(intraday_data,symbol)
        double_bottom_reversal_candidatesALL = find_double_bottom_reversalAll(intraday_data,symbol)
        # Store closing prices in an array
        closing_prices_array = double_bottom_reversal_candidates.to_numpy()

        # Filter based on the 4th index value
        if len(closing_prices_array) > 4:
            fourth_index_value = closing_prices_array[3]
            #print("Fourth Index Value:", fourth_index_value)
            print("Double Bottom Reversal Candidates:")
            print(double_bottom_reversal_candidatesALL)
            output_file.write(f"{double_bottom_reversal_candidatesALL}\n")
            high_volume_periods, error_message = get_high_volume_15min(symbol)

            if not high_volume_periods.empty:
                #output_file.write(f"\nHigh Volume Periods for {symbol}:\n{high_volume_periods}\n")
                output_file.write(f"{symbol}\n")
                output_file.write(f"Fourth Index Value {symbol}: {fourth_index_value}\n")
                print(f"High Volume Periods for {symbol}:\n{high_volume_periods}")
                profitvalue = calculate_percentage(fourth_index_value,0.50)
                targetvalue = profitvalue + fourth_index_value
                Nshares = capital / fourth_index_value
                output_file.write(f"Target Value {symbol}: {targetvalue}\n")
                output_file.write(f"No of Shares {symbol}: {Nshares}\n\n")
                output_file.write(f"----------------------------------------------------------------------------\n")

            elif error_message:
                output_file.write(f"{error_message}\n")
                print(error_message)
            else:
                output_file.write(f"No data available for {symbol}\n")
                print(f"No data available for {symbol}")
        else:
            print("Not enough data points for filtering.")