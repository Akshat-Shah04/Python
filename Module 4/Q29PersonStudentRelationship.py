"""
What relationship is appropriate for Student and Person?
"""

"""
A Student is a specialized type of Person. In this case, a Student class can inherit from the Person class because a student has all the characteristics of a person (like name, age, etc.) but also has additional attributes or behaviors specific to being a student (like student ID, courses, grades, etc.).

Person : The parent (or superclass) that contains common attributes and methods for all types of persons.
Student : The child (or subclass) that inherits attributes from Person and can have additional student-specific attributes.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")


# Create an instance of Student
student = Student("Akshat", 21, "S12345")

student.display_info()
student.display_student_info()

"""
Name: Akshat, Age: 21
Student ID: S12345
"""
