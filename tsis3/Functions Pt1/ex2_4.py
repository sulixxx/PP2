def is_prime ( number ) :
    if number <= 1 :
        return False
    for i in range ( 2, number ) :
        if number % i == 0 :
            return False
    return True

def prime_filters ( num ) :
    prime_numbers = []
    for num in numbers :
        if is_prime ( num ) :
            prime_numbers.append ( num )
    return prime_numbers
    
numbers = [ 1, 2, 3, 4, 5, 6, 77, 88, 47, 33, 323, 11 ]
print ( prime_filters ( numbers )) 


    