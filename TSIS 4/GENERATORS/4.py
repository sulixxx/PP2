def squares ( a, b ) :
    for i in range ( a, b + 1 ) :
        yield i ** 2
        
a = 1
b = 17

print ( f"Here is the squares from {a} to {b} ")

for square in squares ( a, b ) :
    print ( square )
    
    