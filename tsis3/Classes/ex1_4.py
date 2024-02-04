class Point () : #Создается класс Point 
    def __init__ ( self, x, y ) : #Принятие в функцию текущего значения, а также x и y 
        self.x = x
        self.y = y
    def __str__ ( self ) :  #Метод, который будет возвращать сумму значений
        return str(( self.x + self.y ))
    def show ( self ) : #Метод, который будет показывать сумму координат
        print ( "Print coordinates of x and y " ) 
        
coordinates = Point ( 5, 6 ) #Создание объекта класса Point, содержащий заданные значения координат
print ( coordinates ) #Аутпут наших координат


class Point () :    #Создается класс Point 
    def __init__ ( self, x, y ) :  #Принятие в функцию текущего значения, а также x и y 
        self.x = x
        self.y = y
    def move ( self, dx, dy ) :     #Вызов метода move, в котором рассматриваются координаты с текущим значением 
        self.x += dx #Сумма dx 
        self.y += dy #Cумма dy
        
coordinates = Point ( 9, 7 )    #Вызов объекта класса Point c текущим значением 9 и 7
print ( coordinates.x, coordinates.y )  #Аутпут координат

coordinates.move ( 3, 4 )       #Сдвиг наших координат на 3 и 4, соответственно
print ( coordinates.x, coordinates.y ) #Итоговый аутпут



import math #Импортируем бибилотеку math 
class Point () : #Создаём класс Point
    def __init__ ( self, x, y ) : #Принятие текущего значения и координат x, y
        self.x = x
        self.y = y
    def dis ( self, other_point ) : #Метод dis, который позволяет рассчитать расстояние между двумя точками
        distance = math.sqrt = ( self.x - other_point.x ) ** 2 - ( self.y - other_point.y ) ** 2 #Формула разницы координат ( x2 - x1 )**2 - ( y2 - y1 )**2
        return distance #Возвращаем значение расстояние между двумя точками
    
point1 = Point ( 7, 7 ) #Создаем точки для x ( объект класса Point )
point2 = Point ( 6, 9 ) #Создаем точки для y ( объект класса Point )
distance = point1.dis(point2) #Выводим, что расстояние по формуле, при этом нет разницы в каком порядке мы заводим велечины в данный объект
print ( distance ) #Выводим значение



        
        
        