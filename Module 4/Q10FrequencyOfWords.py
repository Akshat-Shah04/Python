filename = (
    "C:\\Users\\pathi\\Desktop\\Program\\Tops\\Assignments\\Python\\Module 4\\demo.txt"
)


def frequency(filename):
    word_count = {}
    with open(filename, "r") as file:
        for line in file:
            words = line.split()
            for i in words:
                i = i.lower()
                if i in word_count:
                    word_count[i] += 1
                else:
                    word_count[i] = 1
    return word_count


print("Frequency of Words is:", frequency(filename))
