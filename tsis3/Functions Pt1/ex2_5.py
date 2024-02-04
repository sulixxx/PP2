from itertools import permutations #Импорт функции из модуля iterools

def print_permutations(input_string): #Создание функции с входными данными input_string 
    perms = permutations(input_string) 
    for perm in perms: #Цикл для каждой perm в perms
        print(''.join(perm)) #Метод join для перестановок

input_string = input("Введите строку: ")
print_permutations(input_string)
