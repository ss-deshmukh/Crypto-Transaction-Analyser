import json

# Load the JSON data from the file
def load_data(file_path):
    with open(file_path, 'r') as file:
        address_data = json.load(file)
    return address_data

def calculate_risk_score(address_data):
    risk_score = 0

    # High transaction volume
    if address_data['n_tx'] > 1000:  # Threshold can be adjusted
        risk_score += 10

    # Disproportionate received vs sent ratio
    if address_data['total_received'] > 2 * address_data['total_sent'] or address_data['total_sent'] > 2 * address_data['total_received']:
        risk_score += 20

    # Final balance check
    if address_data['final_balance'] < 0.1 * address_data['total_received']:
        risk_score += 15

    # Check for high fees
    if len(address_data['txs']) > 0:  # Ensure there are transactions to calculate fees
        average_fee = sum(tx['fee'] for tx in address_data['txs']) / len(address_data['txs'])
        if average_fee > 0.0005 * len(address_data['txs']):  # Example fee threshold
            risk_score += 10

    # Frequency of transactions in short time spans
    if len(address_data['txs']) > 50:  # Ensure there are enough transactions for this analysis
        timestamps = [tx['time'] for tx in address_data['txs']]
        if max(timestamps) - min(timestamps) < 3600:  # More than 50 tx in an hour
            risk_score += 15

    # Double spending transactions
    if any(tx['double_spend'] for tx in address_data['txs']):
        risk_score += 30

    return risk_score

# Example file path
file_path = 'blockchain_info_data.json'  # Update this path to your actual file location
address_data = load_data(file_path)
risk_score = calculate_risk_score(address_data)
print("Risk Score:", risk_score)