def solve ( numlegs, numheads ) :
    rabbits = (( 2 * numheads  ) - ( numlegs / 2 ))
    chickens = (( numlegs - 2 * numheads) ) / 2 
    return int(rabbits), int(chickens)

def main () :
    try :
        numlegs = int( input ( "Введите кол - во ног ( лап ): "))
        numheads = int( input ( "Введите кол - во голов: "))
        
        chickens, rabbits = solve ( numlegs, numheads )
        
        print ( f"Количество кроликов = {rabbits}")
        print ( f"Количество куриц = {chickens}" )
        
    except ValueError :
        print ( "Допускается ввод только ЦЕЛЫХ значений")
    
main ()





    
    
    