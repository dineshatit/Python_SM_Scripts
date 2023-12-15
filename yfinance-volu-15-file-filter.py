import requests
from bs4 import BeautifulSoup

def get_high_volume_stocks():
    # Moneycontrol URL for the page containing high volume stocks
    moneycontrol_url = "https://www.moneycontrol.com/stocks/marketstats/marketcap/bse/lowvolbse"

    # Send a GET request to the URL
    response = requests.get(moneycontrol_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the relevant section containing stock data
        stock_table = soup.find('table', {'id': 'mcDataTbl'})

        # Extract data from the table
        stocks_data = []
        for row in stock_table.find_all('tr')[1:]:  # Skip the header row
            columns = row.find_all('td')
            stock_name = columns[0].text.strip()
            last_price = columns[1].text.strip()
            volume = columns[4].text.strip()

            # You can add more data points as needed

            # Append data to the list
            stocks_data.append({
                'Stock Name': stock_name,
                'Last Price': last_price,
                'Volume': volume
                # Add more fields as needed
            })

        return stocks_data

    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

# Get high volume stocks
high_volume_stocks = get_high_volume_stocks()

# Display the results
if high_volume_stocks:
    for stock in high_volume_stocks:
        print(stock)
else:
    print("No data available.")
