import json


'''
Example of a trade:

{"product_id": "BTC-USD", "trade_id": "609660206", "price": "63539.61", "size": "0.00151049", "time": "2024-03-04T02:06:16.899405Z", "side": "SELL"}
'''

with open('trades.json', 'r') as file:
    trades = json.load(file)
