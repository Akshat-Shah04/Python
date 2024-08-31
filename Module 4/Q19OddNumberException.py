class EvenNumberException(Exception):
    pass


def get_odd():
    try:
        num = int(input("Enter a number : "))
        if num % 2 == 0:
            raise EvenNumberException(f"{num} is not an Odd Number...")
        print(f"{num} is an odd number")
    except EvenNumberException as e:
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
