import time
import math

def geemesquare () :
    number = int ( input ( "Введите число: ") )
    msec = int ( input ( "Введите кол-во миллисекунд: " ) )
    
    time.sleep ( msec / 1000 )
    result = math.sqrt ( number )
    print ( f"Квадратный корень из {number} после {msec} миллисекунд, будет = {result}")
    
geemesquare ()


