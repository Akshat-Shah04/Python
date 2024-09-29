"""
What are oops concepts? Is multiple inheritance supported in python?
"""


class A:
    def fun1(self):
        print("Parent - Class A")


class B:
    def fun2(self):
        print("Parent - Class B")


class C(A, B):
    def fun3(self):
        print("Child - Class C")


obj = C()
obj.fun1()
obj.fun2()
obj.fun3()

"""
Parent - Class A
Parent - Class B
Child - Class C
"""
