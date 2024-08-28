# W.A.P to change a key in a dictionary
d = {"name": "Akshat", "age": 20, "country": "INDIA"}
print("Original Dictionary: ", d)
d["first-name"] = d["name"]
del d['name']
print("Modified Dictionary : ", d)

'''
Original Dictionary:  {'name': 'Akshat', 'age': 20, 'country': 'INDIA'}
Modified Dictionary :  {'age': 20, 'country': 'INDIA', 'first-name': 'Akshat'}

'''
