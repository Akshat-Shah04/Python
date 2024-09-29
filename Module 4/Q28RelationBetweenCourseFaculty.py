"""
What relationship is appropriate for Course and Faculty?
"""

"""
One-to-Many Relationship:
A faculty member can teach multiple courses, but each course is generally taught by only one faculty member.
This is a common scenario in universities where each faculty is responsible for multiple courses, but each course has one primary faculty member.
"""


class Faculty:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)


class Course:
    def __init__(self, course_name):
        self.course_name = course_name


# Create instances
faculty1 = Faculty("Akshat Shah")
course1 = Course("Python 101")
course2 = Course("Database Management System 202")

faculty1.assign_course(course1)
faculty1.assign_course(course2)

# Display faculty and their courses
print(f"{faculty1.name} teaches:")
for i in faculty1.courses:
    print(i.course_name)

"""
Akshat Shah teaches:
Python 101
Database Management System 202
"""
