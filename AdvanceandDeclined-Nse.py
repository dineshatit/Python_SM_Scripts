from nsetools import Nse
import matplotlib.pyplot as plt

def get_advance_decline():
    nse = Nse()
    market_status = nse.get_market_status()

    if market_status['marketStatus'] == 'Closed':
        print("Market is closed.")
        return None, None

    indices = nse.get_index_list()
    nifty_50_index = 'NIFTY 50'

    if nifty_50_index in indices:
        advance_decline = nse.get_index_quote(nifty_50_index)
        return advance_decline['advances'], advance_decline['declines']
    else:
        print(f"{nifty_50_index} not found in the list of indices.")
        return None, None

def plot_advance_decline(advances, declines):
    labels = ['Advances', 'Declines']
    values = [advances, declines]

    plt.bar(labels, values, color=['green', 'red'])
    plt.title('Advance and Decline in Nifty 50')
    plt.ylabel('Number of Stocks')
    plt.show()

def main():
    advances, declines = get_advance_decline()

    if advances is not None and declines is not None:
        print(f"Advances: {advances}, Declines: {declines}")
        plot_advance_decline(advances, declines)
    else:
        print("Failed to fetch advance and decline data.")

if __name__ == "__main__":
    main()
