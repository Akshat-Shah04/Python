# Write a Python program to check multiple keys exists in a dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict2 = {
    "name" : "Akshat"
}
thisdict3 = {}

def numKeys(dict):
    count = 0
    for i in dict:
        count+=1
    return count
    
a = numKeys(thisdict)
b = numKeys(thisdict2)
c = numKeys(thisdict3)
print(f"Number of Keys in {thisdict} is {a}")
print(f"Number of Keys in {thisdict2} is {b}")
print(f"Number of Keys in {thisdict3} is {c}")

'''
Number of Keys in {'brand': 'Ford', 'model': 'Mustang', 'year': 1964} is 3
Number of Keys in {'name': 'Akshat'} is 1
Number of Keys in {} is 0
'''