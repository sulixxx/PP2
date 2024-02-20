def squares_generator( N ):
    for i in range( 1, N + 1 ):
        yield i ** 2

N = 7
squares = squares_generator( N )
for square in squares:
    print( square )
    
