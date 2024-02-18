import os
import requests
from matplotlib import pyplot as plt
from dotenv import load_dotenv

load_dotenv()

DEBANK_API_KEY = os.getenv('DEBANK_API_KEY')
DEBANK_URL = "https://pro-openapi.debank.com/v1/user/all_token_list"

def get_total_balance(user_id):
    """Fetch the total balance for a user from Debank API."""
    try:
        response = requests.get(
            DEBANK_URL,
            headers={'accept': 'application/json', 'AccessKey': DEBANK_API_KEY},
            params={'id': user_id}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching assets for {user_id}: {e}")
        return []

    # You can modify 'threshold' to filter out assets with a lower value
    # It is currently set at $10
def filter_items_by_value_and_sort(data, threshold=10):
    """Filter and sort assets based on their value."""
    filtered_items = [item for item in data if item.get('price', 0) * item.get('amount', 0) >= threshold]
    return sorted(filtered_items, key=lambda item: item.get('price', 0) * item.get('amount', 0), reverse=True)

def print_asset_info(asset):
    """Print information about an asset."""
    worth = asset.get('price', 0) * asset.get('amount', 0)
    print(f"{asset.get('symbol', 'N/A')}: ${worth:,.2f} ({round(asset.get('amount', 0),2)} ${asset.get('symbol','N/A')})")

def plot_pie_chart(token_aggregate):
    """Plot a pie chart of token distribution."""
    total_worth = sum(token_aggregate.values())
    labels, sizes = zip(*[(token, worth) for token, worth in token_aggregate.items() if worth / total_worth >= 0.01])
    other_worth = sum(worth for token, worth in token_aggregate.items() if worth / total_worth < 0.01)
    if other_worth > 0:
        labels += ('Other',)
        sizes += (other_worth,)
    
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.title('Token Distribution')
    plt.show()

def get_assets_for_multiple_users_and_plot(user_ids, plot_pie):
    """Fetch assets for multiple users and optionally plot a pie chart of their aggregated worth."""
    token_aggregate = {}
    token_amounts = {}
    overall_total_worth = 0

    for user_id in user_ids:
        print(f"---\n{user_id}")
        assets = get_total_balance(user_id)
        filtered_and_sorted_assets = filter_items_by_value_and_sort(assets)
        for asset in filtered_and_sorted_assets:
            print_asset_info(asset)

            token = asset.get('symbol', 'N/A')
            worth = asset.get('price', 0) * asset.get('amount', 0)
            amount = asset.get('amount', 0)

            token_aggregate[token] = token_aggregate.get(token, 0) + worth
            token_amounts[token] = token_amounts.get(token, 0) + amount
            overall_total_worth += worth

    sorted_tokens_by_worth = sorted(token_aggregate.items(), key=lambda item: item[1], reverse=True)

    print("---\nTotal Worth:")

    for token, worth in sorted_tokens_by_worth:
        amount = token_amounts[token]
        print(f"{token}: ${worth:,.2f} ({round(amount,2)} ${token})")

    print(f"---\nTotal: ${overall_total_worth:,.2f}")

    if plot_pie == 'yes':
        plot_pie_chart(token_aggregate)


def main():

    ########### ADD/REMOVE WALLET ADDRESSES HERE #####################
    #              VVVVVVVVVVVVVVVVVVVVVVVV
    wallet_addresses = [
"0xeb2993a4e44291da4020102f6d2ed8d14b1cca4c", 
"0x171c53d55b1bcb725f660677d9e8bad7fd084282",
"0x4d36fcc762f773dcc53f072f0b4c3f693bb8a7ce"
                       ]
    
    get_assets_for_multiple_users_and_plot(wallet_addresses, 'yes')

if __name__ == "__main__":
    main()
