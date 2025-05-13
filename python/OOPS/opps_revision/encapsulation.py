class BankAccount():
    def __init__ (self, balance ):
        self.__balance = balance
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")   
        elif amount < 0:
            print("Invalid amount")   
        else:
            self.__balance -= amount
            print(f"Balance after withdrawal: {self.__balance}") 
            
    def deposit(self, amount):
        self.__balance += amount
        print(f"Balance after deposit: {self.__balance}")	
        
    def current_balance(self):
        return self.__balance
            


b1 = BankAccount(10000)
#b1.withdraw(2000)
#b1.deposit(1000)  
print("Current Balance", b1.current_balance())