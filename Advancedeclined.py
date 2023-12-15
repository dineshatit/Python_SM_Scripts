import requests
from bs4 import BeautifulSoup

def get_market_data():
    url = "https://www.moneycontrol.com/stocksmarketsindia/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extracting the advance and declined percentages
        advance_percentage = soup.find('div', {'class': 'adwgray'}).find_all('td', {'class': 'bartxt'})[0].text.strip()
        decline_percentage = soup.find('div', {'class': 'mctable1'}).find_all('td', {'class': 'gld13brd'})[1].text.strip()

        return advance_percentage, decline_percentage
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None, None

if __name__ == "__main__":
    advance_percentage, decline_percentage = get_market_data()

    if advance_percentage is not None and decline_percentage is not None:
        print(f"Advance Percentage: {advance_percentage}")
        print(f"Decline Percentage: {decline_percentage}")
    else:
        print("Unable to fetch data.")
