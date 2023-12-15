import requests
from bs4 import BeautifulSoup
import schedule
import time
import logging
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(filename='moneycontrol.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Lists to store data for plotting
time_stamps = []
advanced_values = []
declined_values = []

def get_advanced_declined():
    url = "https://www.moneycontrol.com/stocksmarketsindia/heat-map-advance-decline-ratio-nse-bse"
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the elements containing the advanced and declined values
        advanced_elem = soup.find('div', {'class': 'PA5 FL'})
        declined_elem = soup.find('div', {'class': 'PA5 FL'})
        
        # Extract the text content of the elements
        advanced_value = int(advanced_elem.text.strip().replace(',', ''))
        declined_value = int(declined_elem.text.strip().replace(',', ''))
        
        # Log the values
        logging.info(f"Advanced: {advanced_value}, Declined: {declined_value}")
        
        # Append values to lists for plotting
        time_stamps.append(time.strftime("%H:%M:%S"))
        advanced_values.append(advanced_value)
        declined_values.append(declined_value)
        
    else:
        # If the request was not successful, log an error message
        logging.error(f"Unable to fetch data. Status code: {response.status_code}")

def job():
    get_advanced_declined()

# Schedule the job to run every 15 minutes
#schedule.every(15).minutes.do(job)

# Run the scheduler for a specific duration (e.g., 1 day)
#end_time = time.time() + 60 * 60 * 24  # 1 day
#while time.time() < end_time:
#    schedule.run_pending()
#    time.sleep(1)

# Plot the graph
plt.plot(time_stamps, advanced_values, label='Advanced')
plt.plot(time_stamps, declined_values, label='Declined')
plt.xlabel('Time')
plt.ylabel('Values')
plt.title('Advanced and Declined Values Over Time')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Save the plot as an image file
plt.savefig('advanced_declined_plot.png')

# Show the plot
plt.show()
