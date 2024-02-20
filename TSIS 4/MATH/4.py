import math

def area_of_paralellogram(h, l):
    area = h * l 
    return area

height_of_paral = float(input("Введите значение высоты: "))
length_of_paral = float(input("Введите значение длины: "))

area_of_paral = area_of_paralellogram(height_of_paral, length_of_paral)
print(f"Итоговое значение площади параллелограма = {area_of_paral}")
