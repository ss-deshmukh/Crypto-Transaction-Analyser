import requests
import json

def fetch_and_save_data(url, filename):
    """Fetch data from the given URL and save it to a specified JSON file."""
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data successfully saved to {filename}")
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")

def main():
    btc_address = '1BoatSLRHtKNngkdXEeobR76b53LETtpyT'  # Example Bitcoin address

    # URLs for API requests
    url1 = f"https://blockchain.info/rawaddr/{btc_address}"
    url2 = f"https://api.blockcypher.com/v1/btc/main/addrs/{btc_address}"

    # Fetch and save data from Blockchain.info
    fetch_and_save_data(url1, 'blockchain_info_data.json')

    # Fetch and save data from BlockCypher
    fetch_and_save_data(url2, 'blockcypher_data.json')

if __name__ == "__main__":
    main()
