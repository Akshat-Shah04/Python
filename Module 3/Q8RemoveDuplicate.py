'''
Write a Python program to remove duplicates from a list.
'''

a = []
n = int(input("Enter how many numbers you want to input in list : "))
# Method 1
for i in range(0, n):
    num = int(input(f"Enter a number {i+1} : "))
    a.append(num)
print("Original List : ", a)
newlist = set(a)
newlist = list(newlist)
# Method 2
rem = []
for i in a:
    if i not in rem:
        rem.append(i)

# print("List after removing duplicates : ",newlist)
print("new list:", rem)


"""
output :
Enter how many numbers you want to input in list : 5
Enter a number 1 : 1
Enter a number 2 : 2
Enter a number 3 : 1
Enter a number 4 : 2
Enter a number 5 : 3
Original List :  [1, 2, 1, 2, 3]
new list: [1, 2, 3]
"""
