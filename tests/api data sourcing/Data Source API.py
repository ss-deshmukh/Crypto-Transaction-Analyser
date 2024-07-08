import requests
import logging
import json

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# API endpoints
BLOCKCHAIN_INFO_URL = "https://blockchain.info/rawaddr/"
BLOCKCYPHER_URL = "https://api.blockcypher.com/v1/btc/main/addrs/"

def fetch_data(url, address):
    try:
        full_url = f"{url}{address}"
        response = requests.get(full_url)
        response.raise_for_status()  # Raises HTTPError for bad requests
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to retrieve data from {url}: {e}")
        return None

def save_data_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        logging.info(f"Data successfully saved to {filename}")
    except IOError as e:
        logging.error(f"Failed to write data to file {filename}: {e}")

def main():
    addresses = ['1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F'] #, 'example_address2']  # List of Bitcoin addresses to query
    
    for address in addresses:
        logging.info(f"Fetching data for address: {address}")
        
        # Fetch from Blockchain.info
        blockchain_info_data = fetch_data(BLOCKCHAIN_INFO_URL, address)
        if blockchain_info_data:
            save_data_to_file(blockchain_info_data, f"{address}_blockchain_info.json")
        
        # Fetch from BlockCypher
        blockcypher_data = fetch_data(BLOCKCYPHER_URL, address)
        if blockcypher_data:
            save_data_to_file(blockcypher_data, f"{address}_blockcypher.json")

if __name__ == "__main__":
    main()
