"""
Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
Expected Output: Counter ({'item1': 1150, 'item2': 300})

"""

data = [
    {"item": "item1", "amount": 400},
    {"item": "item2", "amount": 300},
    {"item": "item1", "amount": 750},
]

res = {}

for i in data:
    item = i["item"]
    amt = i["amount"]

    if item in res:
        res[item] += amt
    else:
        res[item] = amt

print(res)

"""
{'item1': 1150, 'item2': 300}

"""
