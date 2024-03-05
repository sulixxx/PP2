simple_string = input ( "Введите строку: " )

uppercase_count = sum ( 1 for char in simple_string if char.isupper() )
lowercase_count = sum ( 1 for char in simple_string if char.islower() )

print ( "Количество строчных букв = ", lowercase_count )
print ( "Количество заглавных букв = ", uppercase_count )
