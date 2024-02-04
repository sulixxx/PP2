class Shape():  #Создаётся класс Shape
    def __init__(self): #Принятие текущего значения
        pass            #pass позволяет хранить в этой функции пустоту
    
    def area(self): #Создании функции площади, принятие дефолтного значения площади как 0
        return 0

class Rectangle(Shape): #Создание подкласса ( дочернего класса Shape ), называемого Rectangle
    def __init__(self, length, width): #Создание длины и ширины
        super().__init__() #Инициализация конструктора основного класса Shape 
        self.length = length #Определяем длину
        self.width = width #Определяем ширину
    
    def area(self): 
        return self.length * self.width #Передаём ф-лу нахождения площади для прямоугольника 
    
total_area = Rectangle(3, 4)    #Создание объекта класса Rectangle
print("Total area of rectangle =", total_area.area()) #Итоговое значение площади прямоугольника


   
       