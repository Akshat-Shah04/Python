"""
Self represents the instance of the class. By using the “self”  we can access the attributes and methods of the class in Python. It binds the attributes with the given arguments.

When working with classes in Python, the term “self” refers to the instance of the class that is currently being used. It is customary to use “self” as the first parameter in instance methods of a class. Whenever you call a method of an object created from a class, the object is automatically passed as the first argument using the “self” parameter. This enables you to modify the object's properties and execute tasks unique to that particular instance.
"""

"""
How to define a class?
Ans...


class <class_name>:
    def __init__(self,para1,para2,...,para_n):
        self.para1 = para1
        self.para2 = para2
        self.para_n = para_n
    
    def <function_name>(self,para1,para2,...,para_n):
        pass
        

obj = class_name(para1,para2,...,para_n)
obj.function_name(para1,para2,...,para_n)



    


"""


class A:
    def fun1(self):
        print("Class A -> Function1..... ")


obj = A()
obj.fun1()

"""
Class A -> Function1..... 
"""
