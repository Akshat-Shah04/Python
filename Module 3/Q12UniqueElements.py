def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list

example_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = unique_elements(example_list)
print("Unique elements:", unique_list)


'''
output :
Unique elements: [1, 2, 3, 4, 5]
'''