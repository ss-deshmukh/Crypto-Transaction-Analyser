import requests

def fetch_blockchain_info_data():
    url = f'https://blockchain.info/rawblock/$block_hash'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
