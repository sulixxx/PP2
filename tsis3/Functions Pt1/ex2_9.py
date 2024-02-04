import math

def volume_of_sphere ( radius ) :
    volume = 4/3 * math.pi * radius ** 3
    return volume

def main () :
    radius = float ( input ("Введите значение радиуса сферы: "))
    volume = volume_of_sphere ( radius )
    print ( f"Значение объёма = {volume}")
    
main()



    
    
    
    

