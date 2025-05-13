#Encapsulation
# In Python, encapsulation is a fundamental concept of object-oriented programming (OOP) that restricts direct access to an object's attributes and methods.
#data ko hide karna
#Encapsulation is achieved by using private and public access specifiers.


class BankAccount():
    def __init__(self, balance, account_number):
        self.__balance = balance #private attribute
        self.__account_number = account_number #private attribute
        
    def deposit(self, amount):
        self.__balance += amount
        print("Deposit successful. New balance is:", self.__balance)
        
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful. New balance is:", self.__balance)
            
    def get_balance(self):
        return self.__balance


bank_account_1 = BankAccount(1000, "123456789")
bank_account_1.deposit(500)
bank_account_1.withdraw(200)
print("Current balance is:", bank_account_1.get_balance())
# print(bank_account_1.__balance) # This will raise an AttributeError because __balance is private
