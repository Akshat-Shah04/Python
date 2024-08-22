# Write a Python script to check if a given key already exists in a dictionary.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
key = input("Enter the key : ")
for i in thisdict:
    if key == i:
        print("Key Found!!")
        flag =1 
        break
    else:
        flag = 0
    
if flag == 0:
    print("Key not found!!")
else:
    pass

'''
Enter the key : model
Key Found!!

Enter the key : city 
Key not found!!
'''