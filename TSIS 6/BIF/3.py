def is_palindrom_or_not ( stroka ) :
    stroka = "".join ( char for char in stroka.lower() if stroka.isalnum() )
    return stroka == stroka[::-1]

our_input = input ( "Введите строку для проверки: ")

if is_palindrom_or_not ( our_input ) :
    print ( "Да, строка является палиндромом")
else :
    print ( "Не, не палиндром")
    