import requests

def get_top_gainers():
    base_url = 'https://query1.finance.yahoo.com/v7/finance/quote'
    symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']  # Example symbols, replace with NSE symbols

    # Make an API call to get the stock data
    params = {'symbols': ','.join(symbols)}
    
    response = requests.get(base_url, params=params)
    data = response.json()

    # Extract the stock data from the response
    quotes = data.get('quoteResponse', {}).get('result', [])

    # Sort stocks based on the day's percentage change
    sorted_stocks = sorted(quotes, key=lambda x: x.get('regularMarketChangePercent', 0), reverse=True)

    # Print the top 5 gainers
    print(f'Top 5 Gainers on NSE:')
    for i in range(min(5, len(sorted_stocks))):
        stock = sorted_stocks[i]
        symbol = stock.get('symbol', '')
        change_percent = stock.get('regularMarketChangePercent', 0)
        print(f'{i+1}. Symbol: {symbol}, Percentage Change: {change_percent:.2f}%')

# Replace the symbols with NSE symbols
get_top_gainers()
