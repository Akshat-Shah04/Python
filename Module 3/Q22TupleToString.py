# Write a Python program to convert a tuple to a string
t = ("a", "b", "123ad1")
str = ""
for i in t:
    str += i

print(t)
print(str)

"""
('a', 'b', '123ad1')
123ad1ba
"""
