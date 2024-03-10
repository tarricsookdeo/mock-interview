import json


'''
Example of a trade:

{"product_id": "BTC-USD", "trade_id": "609660206", "price": "63539.61", "size": "0.00151049", "time": "2024-03-04T02:06:16.899405Z", "side": "SELL"}
'''

with open('trades.json', 'r') as file:
    trades = json.load(file)

# 1. Find the highest price of all trades
# 2. The list of prices is currently sorted by time. Sort the list by price in accending order instead, then create a function that takes in a float as an argument and returns the index of the trade with the closest price to the argument.
