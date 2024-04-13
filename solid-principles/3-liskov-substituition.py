# 3. Liskov substitution
# If we have objects in our class, we could be able to replace
# those objects with instances of their subtypes or subclasses

# The problem with previous code is for paypal we dont need security_code
# but we need email address instead and we have to be able to replace 
# security_code with email address without breaking the correctness 
# of classes

from abc import abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = 'open'
    
    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
        
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i]*self.prices[i]
        return total
    
    
class PaymentProcessor:
        
    @abstractmethod
    def pay(self, order):
        pass
    
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
    
    def pay(self, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
        
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.status = "paid"
        
        
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address):
        self.email_address = email_address
    
    def pay(self, order):
        print("Processing paypal payment type")
        print(f"Verifying security code: {self.email_address}")
        self.status = "paid"
    
    
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
payment_processor = PaypalPaymentProcessor("me@alinaeriparizi.com")
payment_processor.pay(order)