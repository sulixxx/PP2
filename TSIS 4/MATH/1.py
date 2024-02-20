import math 

def degrees_to_radians ( degrees ) :
    radians = degrees * ( math.pi / 180 )
    return radians 

degrees_input = float ( input ( "Введите значение: "))

radians_output = degrees_to_radians ( degrees_input )

print ( f"{degrees_input} грудусов = {radians_output} радиан ")