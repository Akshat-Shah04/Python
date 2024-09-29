'''
Write python program that user to enter only odd numbers, else will raise an exception?
'''

class EvenNumException(Exception):
    pass


def get_odd():
    try:
        num = int(input("Enter a number : "))
        if num % 2 == 0:
            raise EvenNumException(f"{num} is not an Odd Number...")
        print(f"{num} is an odd number")
    except EvenNumException as e:
        print(e)
    except ValueError:
        print("ValueError.. Enter a number...")
    finally:
        print("Program Executed....")


get_odd()


"""
Enter a number : 2
2 is not an Odd Number...
Program Executed....

"""

"""
Enter a number : a
ValueError.. Enter a number...
Program Executed....

"""
