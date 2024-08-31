class Animal:
    def __init__(self, name):
        self.name = name

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
b = Cat("Catty")
c = Lion("Shera")

print(f"class dog: {a.voice()}")
print(f"class cat: {b.voice()}")
print(f"class lion: {c.voice()}")

"""
Tom barks..
class dog: None
Catty meows..  
class cat: None
Shera roars..  
class lion: None    
"""
