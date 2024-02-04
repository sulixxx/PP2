def unique_elements(input_elements):
    unique_elements = []
    for element in input_elements:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

input_list = [2, 9, 9, 8, 1, 1, 0, 7, 77, 43]
result = unique_elements(input_list)
print(f"Первоначальный список: {input_list}")
print(f"Уникальные элементы: {result}")
