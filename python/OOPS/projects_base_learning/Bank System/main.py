# 🚀 Challenge: Multiple Inheritance – Real-World Bank System

# 🔹 Required Classes & Features
# 1. AccountHolder class:
# Attributes: name, balance

# Method: display_account() – naam aur balance show kare

# 2. KYCVerified class:
# Attribute: kyc_status (True/False)

# Method: verify() – agar kyc_status == True ho to print “KYC Approved” warna “KYC Pending”

# 3. BankCustomer class:
# Inherits from both above classes

# Method: customer_info() – sab kuch display kare (name, balance, kyc_status)


class AccountHolder():
    def __init__ (self, name, balance):
        self.name = name 
        self.balance = balance
        
    def display_account(self):
        print(f"Name: {self.name}, Balance: {self.balance}")    

class KYVerified():
    def __init__(self, kyc_status):
        self.kyc_status = kyc_status
        
    def verify(self):
        if self.kyc_status :
            print("Approved")
        else:
            print("Pending")         
        
class BankCustomer(AccountHolder, KYVerified):
    def __init__(self, name, balance, kyc_status):
        AccountHolder.__init__(self, name, balance)
        KYVerified.__init__(self, kyc_status)
        
    def customer_info(self):
       self.display_account()
       print(f"kyc_status: ", end="")
       self.verify()
        

info1 = BankCustomer("Muhammad", "1000", False)     
info2 = BankCustomer("Rana Zain", "12000", True )

info2.customer_info()   

        
                