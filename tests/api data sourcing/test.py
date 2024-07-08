import json
import os

data = {
    "address": "1AJbsFZ64EpEfS5UAjAfcUG8pH8Jn3rn1F",
    "total_received": 11660042466,
    "total_sent": 11657629466,
    "balance": 2413000,
    "unconfirmed_balance": 0,
    "final_balance": 2413000,
    "n_tx": 82,
    "unconfirmed_n_tx": 0,
    "final_n_tx": 82,
    "txrefs": [
        {
            "tx_hash": "8e5e6b898750a7afbe683a953fbf30bd990bb57ccd2d904c76df29f61054e743",
            "block_height": 643714,
            "tx_input_n": -1,
            "tx_output_n": 0,
            "value": 2413000,
            "ref_balance": 2413000,
            "spent": 'false',
            "confirmations": 199985,
            "confirmed": "2020-08-14T17:24:59Z",
            "double_spend": 'false'
        },
        {
            "tx_hash": "b357ef869a27affd4442e57367396dc404b5757da117d8903ef196fd021b57bc",
            "block_height": 183579,
            "tx_input_n": 1,
            "tx_output_n": -1,
            "value": 4678300000,
            "ref_balance": 0,
            "confirmations": 660120,
            "confirmed": "2012-06-08T16:28:26Z",
            "double_spend": 'false'
        }
    ]
}



normalized_data = []

# Normalize data to ensure consistent structure
transactions = data.get('txrefs', data)  # txrefs for BlockCypher, direct for Blockchain.info
for tx in transactions:
    normalized_data.append({
        'tx_hash': tx.get('tx_hash', tx.get('hash')),  # Adjust keys based on source data structure
        'value': tx.get('value', tx.get('output_value')),  # Adjust keys based on source data structure
        'date': tx.get('confirmed', tx.get('time'))  # Adjust keys based on source data structure
    })
    
print(normalized_data)