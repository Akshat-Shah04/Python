"""
What is used to check whether an object o is an instance of class A?
"""

"""
the isinstance() function is used to check whether an object is an instance of a specific class or a subclass thereof.
"""


class A:
    def fun1():
        pass


class B:
    def fun2():
        pass


class C(A):
    def fun3():
        pass


a = A()
b = B()
c = C()
print("Class A and object a => ", isinstance(a, A))
print("Class A and object b => ", isinstance(b, A))
print("Class A and object c => ", isinstance(c, A))

print("Class B and object a => ", isinstance(a, B))
print("Class B and object b => ", isinstance(b, B))

print("Class C and object c => ", isinstance(c, C))
print("Class C and object a => ", isinstance(a, C))
print("Class C and object b => ", isinstance(b, C))


"""
Class A and object a =>  True
Class A and object b =>  False
Class A and object c =>  True
Class B and object a =>  False
Class B and object b =>  True
Class C and object c =>  True
Class C and object a =>  False
Class C and object b =>  False
"""
