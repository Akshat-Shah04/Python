filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def longest_word(filename):
    with open(filename, "r") as file:
        longest = ""
        for line in file:
            word = line.split()
            for i in word:
                if len(i) > len(longest):
                    longest = i
    return longest

print("Longest Word in the file is : ", longest_word(filename))


'''
Longest Word in the file is :  Programming
'''