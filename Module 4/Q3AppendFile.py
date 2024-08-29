filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def append_file(filename, str):
    file = open(filename, "a")
    file.write(str)
    file.close()


def read_file(filename):
    file = open(filename, "r")
    # print(file.readlines())
    for i in file:
        print(i)
    file.close()


print("original File :::::::: ")
read_file(filename)
print("Appending File.....")
append_file(filename, "Hello Akshat Shah!!\n")
read_file(filename)


"""
My name is Akshat Shah

I am currently 20 years old.

I reside in Ahmedabad

I am studying in Silver Oak University

My dream is to travel to various countries in the world.

I love Python Programming

I am currently solving Module 4.Hello Akshat Shah!!Hello Akshat Shah!!Hello Akshat Shah!!

Appending File.....
My name is Akshat Shah

I am currently 20 years old.

I reside in Ahmedabad

I am studying in Silver Oak University

My dream is to travel to various countries in the world.

I love Python Programming

I am currently solving Module 4.Hello Akshat Shah!!Hello Akshat Shah!!Hello Akshat Shah!!

Hello Akshat Shah!!



"""
