import json
import os

# Load data from a JSON file
def load_data(filepath = os.getcwd):
    with open(filepath, 'r') as file:
        return json.load(file)

# Normalize data to ensure consistent structure
def normalize_data(data, source):
    normalized_data = []
    transactions = data.get('txrefs', data)  # txrefs for BlockCypher, direct for Blockchain.info
    for tx in transactions:
        normalized_data.append({
            'tx_hash': tx.get('tx_hash', tx.get('hash')),  # Adjust keys based on source data structure
            'value': tx.get('value', tx.get('output_value')),  # Adjust keys based on source data structure
            'date': tx.get('confirmed', tx.get('time')),  # Adjust keys based on source data structure
            'source': source
        })
    return normalized_data


# Cross-reference data to combine information from both sources
def cross_reference_data(data1, data2):
    # Create a dictionary with tx_hash as keys
    all_data = {tx['tx_hash']: tx for tx in data1}
    for tx in data2:
        if tx['tx_hash'] in all_data:
            # If tx_hash exists, merge the data (example: take max value, append sources)
            existing_tx = all_data[tx['tx_hash']]
            existing_tx['value'] = max(existing_tx['value'], tx['value'])
            existing_tx['sources'] = list(set(existing_tx.get('sources', []) + [tx['source']]))
        else:
            # If tx_hash does not exist, add the new transaction
            all_data[tx['tx_hash']] = tx
    return list(all_data.values())

# Save data to a JSON file
def save_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Main function to execute the tasks
def main():
    # Load data from both JSON files
    blockchain_info_data = load_data('1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F_blockchain_info.json')
    blockcypher_data = load_data('1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F_blockcypher.json')
    
    # Normalize the data from both sources
    normalized_blockchain_info = normalize_data(blockchain_info_data, 'blockchain_info')
    normalized_blockcypher = normalize_data(blockcypher_data, 'blockcypher')
    
    # Cross-reference and merge the data
    merged_data = cross_reference_data(normalized_blockchain_info, normalized_blockcypher)
    
    # Save the merged data to a new file
    save_data(merged_data, 'merged_transaction_data.json')

if __name__ == '__main__':
    main()