import requests
from bs4 import BeautifulSoup
import sys

def get_top_gainers():
    url = "https://www.moneycontrol.com/stocks/fno/marketstats/futures/gainers/homebody.php?opttopic=gainers&optinst=allfut&sel_mth=1&sort_order=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    top_gainers = []

    # Find the table containing the top gainers
    gainer_table = soup.find('table', {'class': 'tblList'})

    if gainer_table:
        # Extract rows from the table
        rows = gainer_table.find_all('tr')[1:]  # Skip the header row

        for row in rows[:5]:  # Get top 5 gainers
            columns = row.find_all('td')
            company_name = columns[0].text.strip()
            last_price = columns[2].text.strip()
            change = columns[3].text.strip()
            percent_change = columns[4].text.strip()

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
    file_path = "stock_symbols.txt"
    print("Top 5 Gainers:")
    for idx, gainer in enumerate(top_gainers, start=1):
        print(f"{idx}. {gainer['Company Name']} - {gainer['Percent Change']} - {gainer['Change']}")
#        print(f"{gainer['Company Name']}")
        
        
        with open(file_path, 'w') as file:
            for idx, gainer in enumerate(top_gainers, start=1):
                print(f"{gainer['Company Name']}")    
                file.write(f"{gainer['Company Name']}\n")
        print(f"Content successfully written to '{file_path}'.")
    