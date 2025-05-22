# ✅ 1. Payment Processing System
# ❌ Payment class har method handle karti hai: PayPal, Stripe, Cash

# ✅ Use inheritance:

# PaymentProcessor (base)

# StripePayment, PaypalPayment, CashPayment (extensions)

# Add new method? Just extend, no need to modify base.

from abc import ABC, abstractmethod

class PaymentProcessor():
    @abstractmethod
    def process_payment(self, amount):
        pass
    
class PayPalPayment(PaymentProcessor):
    def process_payment(self, amount):
         print(f"Processing ${amount} payment through PayPal.")   
         
class StripePayment(PaymentProcessor):
    def process_payment(self, amount):
       print(f"Processing ${amount} payment through Stripe.")
       
       
class CashPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing ${amount} payment through Cash.")  
        
        
# 🔹 Client code (does not change!)
def checkout(payment_processor: PaymentProcessor, amount):
    payment_processor.process_payment(amount)

# ✅ Usage:
checkout(PayPalPayment(), 100)
checkout(StripePayment(), 200)
checkout(CashPayment(), 50)             