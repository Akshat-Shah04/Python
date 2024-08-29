filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def read_file(filename, n):
    file = open(filename, "r")
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())
    file.close()


read_file(filename, 5)

"""
My name is Akshat Shah
I am currently 20 years old.
I reside in Ahmedabad
I am studying in Silver Oak University
My dream is to travel to various countries in the world.   

"""
