import math

def regular_polygon_area ( s, n ) : 
    
    area = (n * s ** 2) / (4 * math.tan(math.pi / n))
    
    return area

number_of_sides = int ( input ( "Введите значение количества сторон: "))
length_of_sides = float ( input ( "Введите значение длины стороны: "))

polygon_area = regular_polygon_area ( number_of_sides, length_of_sides )

print ( f"По итогу площадь правильного многоугольника = {polygon_area}" )



 