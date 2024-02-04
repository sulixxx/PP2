def Convertation ( gramms ) :
    ounces = 28.3495231 * gramms
    return ounces

def main () :
    gramms = float ( input ( "Введите количество граммов: "))
    ounces = Convertation(gramms)  
    print ( f"{gramms} граммов = {ounces} унций" )
    
main()

    