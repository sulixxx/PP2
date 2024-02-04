def is_pal_or_not ( s ) :
    s.replace ( " ", "" ).lower() 
    return s == s[::-1]

any_string = input ( "Введите значение:\n")

if is_pal_or_not ( any_string ) :
    print ( f"Уррааа!!! Значение {any_string} - является палиндромом:)")
else :
    print ( f"Данное значение неверно!!!! {any_string} - не является палиндромом:(")
    
    
    

    
    
