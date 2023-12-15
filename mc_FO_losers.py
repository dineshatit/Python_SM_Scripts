import requests
from bs4 import BeautifulSoup

def get_top_losers():
    url = "https://www.moneycontrol.com/stocks/fno/marketstats/futures/losers/homebody.php?opttopic=&optinst=allfut&sel_mth=all&sort_order=0"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0"}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        losers_table = soup.find('table', {'class': 'tblList'})
        
        if losers_table:
            rows = losers_table.find_all('tr')
            
            # Skip the header row
            rows = rows[1:]

            top_losers = []
            for row in rows[:5]:  # Top 5 losers
                columns = row.find_all('td')
                stock_name = columns[0].text.strip()
                last_price = columns[1].text.strip()
                change_percentage = columns[2].text.strip()

                top_losers.append(stock_name)
#                top_losers.append({
#                    'Stock Name': stock_name,
#                    'Last Price': last_price,
#                    'Change Percentage': change_percentage,
#                })

            return top_losers
        else:
            print("Error: Unable to find the losers table.")
    else:
        print(f"Error: Unable to fetch data. Status Code: {response.status_code}")

if __name__ == "__main__":
    top_losers = get_top_losers()

    if top_losers:
        print("Top 5 Losers:")
        for loser in top_losers:
            print(loser)
    else:
        print("Failed to retrieve top losers.")
