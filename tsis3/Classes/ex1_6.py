numbers = [44, 54156, 3, 1, 0, 77, 4, 7, 8, 47, 51] #Объявляем лист с некоторыми переменными

def is_prime ( n ) : #Создание функции is_prime
    if n <= 1 :         #Простая проверка на простые числа
        return False
    for i in range ( 2, (int(n**0.5)) + 1 ) :
        if n % i == 0 :
            return False
    return True 

prime_numbers = list ( filter ( lambda n : is_prime(n), numbers )) #Определение и фильтрация простых чисел

print ( prime_numbers ) #Последующий вывод
    

        