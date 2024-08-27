# Write a Python function to check whether a number is in a given range
def checkRange(n):
    start = int(input("Enter the start of the range : "))
    end = int(input("Enter the end of the range : "))
    if n >= start and n <= end:
        print(f"{n} is in range({start},{end})")
    else:
        print(f"{n} is not in range({start},{end})")


n = int(input("Enter a number : "))
checkRange(n)

'''
Enter a number : 100
Enter the start of the range : 50
Enter the end of the range : 250
100 is in range(50,250)

'''
