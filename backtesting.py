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
