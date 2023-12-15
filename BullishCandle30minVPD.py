import yfinance as yf
import pandas as pd

def get_bullish_candles(ticker, timeframe='30m', percentage_change_threshold=1):
    # Fetch historical data
    data = yf.download(ticker, period='1d', interval=timeframe)

    # Calculate percentage change
    data['Percentage Change'] = (data['Close'] - data['Open']) / data['Open'] * 100

    # Filter bullish candles
    bullish_candles = data[data['Percentage Change'] > percentage_change_threshold]

    return bullish_candles

if __name__ == "__main__":
    ticker_symbol = 'AAPL'  # Change this to the desired stock symbol
    bullish_candles = get_bullish_candles(ticker_symbol)

    print("Bullish Candles:")
    print(bullish_candles)

from backtesting import Backtest, Strategy
from backtesting.lib import crossover

class BullishCandleStrategy(Strategy):
    def init(self):
        self.buy_signal = crossover(self.data['Close'], self.data['Open'])

    def next(self):
        if self.buy_signal:
            self.buy()

if __name__ == "__main__":
    # Load historical data
    historical_data = yf.download(ticker_symbol, period='1y', interval='30m')

    # Create and run the backtest
    bt = Backtest(historical_data, BullishCandleStrategy, cash=10000, commission=0.001)
    results = bt.run()

    # Print the performance metrics
    print(results)
    bt.plot()
