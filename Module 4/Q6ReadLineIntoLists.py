filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)
def fileToLists(filename):
    with open(filename,'r') as file:
        data = file.readlines()
    return data

print(fileToLists(filename))            
