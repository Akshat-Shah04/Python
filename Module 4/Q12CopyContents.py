file1 = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo1.txt"
)
file2 = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo2.txt"
)


def copy_content(file1, file2):
    with open(file1, "r") as file:
        # global line
        line = file.readlines()

    with open(file2, "w") as file:
        file.write("".join(line))


def read_file(filename):
    with open(filename, "r") as file:
        for i in file:
            print(i)


print("Reading file 1 : ::: :: :")
read_file(file1)
print("Reading file 2 : ::: :: :")
read_file(file2)
print("Copying file 1 to file 2 : ::: :: :")
copy_content(file1, file2)
print("Reading file 2 :: :: :: :")
read_file(file2)
