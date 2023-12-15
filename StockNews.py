import requests
from bs4 import BeautifulSoup

def get_moneycontrol_stock_news(stock_symbol):
    base_url = f"https://www.moneycontrol.com/news/tags/{stock_symbol}.html"
    
    # Send a GET request to the URL
    response = requests.get(base_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the elements containing the news headlines
        news_headlines = soup.find_all('h2', {'class': 'arial12'})
        
        # Extract and return the news headlines
        return [headline.text.strip() for headline in news_headlines]

    else:
        # If the request was not successful, print an error message
        print(f"Error: Unable to fetch news. Status code: {response.status_code}")
        return None

# Example usage
stock_symbol = "RELIANCE"  # Replace with the stock symbol you are interested in
news_list = get_moneycontrol_stock_news(stock_symbol)

if news_list:
    print(f"News for {stock_symbol}:")
    for i, news in enumerate(news_list, start=1):
        print(f"{i}. {news}")
