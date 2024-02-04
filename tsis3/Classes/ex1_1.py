class HowToMake : #Создаём класс
    def getString ( self, string ): #Вводим текущей значение + строку в созданной функции getString
        self.string = string #Присваиваем текущее значение для строки
    
    def printString ( self ) : #Создаём функцию printString, внутри которой храним текущее значение
        print ( self.string.upper() ) #Перевод введённой строки в upper case
        
        
string1 = HowToMake () #Создаём объект класса HowToMake
string1.getString (input()) #Строка для ввода функции getString
string1.printString () #Строка для её вывода




