def divide_num(a, b):
    try:
        res = a / b
        print("Result : ",res)
    except ZeroDivisionError:
        print("Denominator cannot be Zero...")
    except TypeError:
        print("Only numbers are allowed...")
    finally:
        print("Execution Completed...")


print("a = 10, b = 20")
divide_num(10, 20)
print("a = 10, b = 0")
divide_num(10, 0)
print("a = 10, b = 'c'")
divide_num(10, "c")


"""

a = 10, b = 20
Result :  0.5
Execution Completed...
a = 10, b = 0
Denominator cannot be Zero...
Execution Completed...
a = 10, b = 'c'
Only numbers are allowed...
Execution Completed...


"""
