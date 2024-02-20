def trapezoidal_area ( ) :
    
    height = float ( input ("Введите значение высоты: "))
    length = float ( input ("Введите значение длины: "))
    width = float ( input ("Введите значение ширины: "))
    
    area = 0.5 * ( length + width ) * height 
    
    return area 

trap_area = trapezoidal_area ( )
print ( f"Площадь трапециии = {trap_area} ")

