filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def fileToLists(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return data


print(fileToLists(filename))
"""
['My name is Akshat Shah\n', 'I am currently 20 years old.\n', 'I reside in Ahmedabad\n', 'I am studying in Silver Oak University\n', 'My dream is to travel to various countries in the world.\n', 'I love Python Programming\n', 'I am currently solving Module 4.\n', 'Hello Akshat Shah!!\n']
"""



