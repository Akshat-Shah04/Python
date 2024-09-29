# What is Instantiation in terms of OOP terminology?

"""
Instantiation in Object-Oriented Programming (OOP) refers to the process of creating 
an instance (i.e., an object) of a class. When a class is defined, it acts as a blueprint 
or template, and instantiation is the step where you create an actual object that follows this template
"""


class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Object Instantiated with parameter {self.name}")

# Object Instantiated...
dog = Animal("Buddy")
cat = Animal("Whiskers")


"""
Object Instantiated with parameter Buddy
Object Instantiated with parameter Whiskers
"""
