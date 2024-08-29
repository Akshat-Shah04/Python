l = ["My name is Akshat Shah...\n", "100101\n", "hii world\n", "Akshat Shah\n"]
filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def write_file(filename, str):
    with open(filename, "w") as file:
        file.writelines(str)


def read_file(filename):
    with open(filename, "r") as file:
        for i in file:
            print(i)


read_file(filename)
print("\n\n\nWriting in the file demo.txt........")
write_file(filename, l)
read_file(filename)

'''
My name is Akshat Shah

I am currently 20 years old.

I reside in Ahmedabad

I am studying in Silver Oak University

My dream is to travel to various countries in the world.

I love Python Programming

I am currently solving Module 4.

Hello Akshat Shah!!



Writing in the file demo.txt........
My name is Akshat Shah...

100101

hii world

Akshat Shah


'''