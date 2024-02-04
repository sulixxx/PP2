class Account : #Создаём класс нашего банковского аккаунта
    pass #По сути пустая строка, которая ничего в себе не содержит
    def __init__ ( self, owner, balance = 0 ) : #Собственник счёта, текущий баланс
        self.owner = owner
        self.balance = balance 
    
    def deposit ( self, amount ) : #Случай пополнения счёта 
        self.balance += amount
        print ( f"Ваш счёт пополнен на {amount}. Текущий счёт составляет {self.balance}.")
        
    def withdraw ( self, amount ) : #Случай снятия денежных средств
        if self.balance >= amount :
            self.balance -= amount
            print ( f"Снятие {amount} прошло успешно. Текущий счёт составляет {self.balance}.")
        elif self.balance < amount: #Случай, если сумма снятия больше, чем наш банковский счёт:(
            print ( "Транзакция не прошла:(")
            
account = Account ( "Zakariya Sultan" ) #Собственник счёта

account.deposit(6000) #Пополнение+
account.withdraw(4500) #Снятие-
account.withdraw(1501) #Неуспешное снятие-


            
        