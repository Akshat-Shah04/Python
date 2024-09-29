"""
Explain Inheritance in Python with an example? 
What is init? Or What Is A Constructor In Python?
"""

"""
Inheritance : 
Inheritance allows one class to inherit the properties and methods of another class.
The primary goal of inheritance is to reuse the code and create a hierarchical relationship 
between classes.
"""

"""
__init__() Method (Constructor in Python):
The __init__() method is a special method in Python classes known as the constructor.
It is automatically called when an object of the class is created.
It is used to initialize the instance variables (attributes) of a class.
"""


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Constructor Animal Invoked... {self.name}")

    def voice(self):
        print(self.name, " makes a sound")


class Dog(Animal):
    def voice(self):
        print(f"{self.name} barks..")


class Lion(Animal):
    def voice(self):
        print(f"{self.name} roars..")


class Cat(Animal):
    def voice(self):
        print(f"{self.name} meows..")


a = Dog("Tom")
a.voice()
b = Cat("Catty")
b.voice()
c = Lion("Shera")
c.voice()


"""
Constructor Animal Invoked... Tom
Tom barks..
Constructor Animal Invoked... Catty
Catty meows..
Constructor Animal Invoked... Shera
Shera roars..
"""
