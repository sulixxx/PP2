def Convertation ( F ) :
    C = (5 / 9) * (F - 32)
    return C
def main () :
    F = float ( input ("Введите температуру по Фаренгейту: "))
    C = Convertation ( F )
    print ( f"{F} F = {C} C")
    
main()



    
    