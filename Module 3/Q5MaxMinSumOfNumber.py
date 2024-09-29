# Write a Python function to get the largest number, smallest num and sum of all from a list.
def maximum(a):
    max = a[0]
    for i in a:
        if i > max:
            max = i
    return max


def minimum(a):
    min = a[0]
    for i in a:
        if i < min:
            min = i
    return min


def summation(a):
    sum = 0
    for i in a:
        sum = sum + i
    return sum


list1 = []
n = int(input("How many numbers you want to enter in the list : "))
for i in range(n):
    num = int(input(f"Enter any number {i + 1}: "))
    list1.append(num)

max = maximum(list1)
min = minimum(list1)
sum = summation(list1)

print(f"Original List : {list1}")
print(f"Maximum : {max}")
print(f"Minimum : {min}")
print(f"Summation : {sum}")

"""
output :

How many numbers you want to enter in the list : 5
Enter any number 1: 10
Enter any number 2: 5
Enter any number 3: 99
Enter any number 4: 100
Enter any number 5: 33
Original List : [10, 5, 99, 100, 33]
Maximum : 100
Minimum : 5
Summation : 247

"""
