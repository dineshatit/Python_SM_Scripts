import requests
from bs4 import BeautifulSoup

def get_top_gainers():
    url = "https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    top_gainers = []

    # Find the table containing the top gainers
    gainer_table = soup.find('table', {'class': 'tbldata14 bdrtpg'})

    if gainer_table:
        # Extract rows from the table
        rows = gainer_table.find_all('tr')[1:]  # Skip the header row

        for row in rows[:5]:  # Get top 5 gainers
            columns = row.find_all('td')
            company_name = columns[0].text.strip()
            last_price = columns[1].text.strip()
            change = columns[2].text.strip()
            percent_change = columns[3].text.strip()

            # Append data to the top_gainers list
            top_gainers.append({
                'Company Name': company_name,
                'Last Price': last_price,
                'Change': change,
                'Percent Change': percent_change
            })

    return top_gainers

if __name__ == "__main__":
    top_gainers = get_top_gainers()

    print("Top 5 Gainers:")
    for idx, gainer in enumerate(top_gainers, start=1):
        print(f"{idx}. {gainer['Company Name']} - {gainer['Percent Change']}")

