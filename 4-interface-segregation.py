# 4. Interface segregation
# Having multiple interfaces is better than a one big interface

# Now assume we need authentication for our payment methods and 
# for that we need to add an auth method while processing the order



from abc import ABC, abstractmethod

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
    
    
class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self, order):
        pass
    
class PaymentProcessor_SMS(PaymentProcessor):
    
    @abstractmethod
    def auth(self, code):
        pass
    
    
class DebitPaymentProcessor(PaymentProcessor_SMS):
    
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False

        
    def auth(self, code):
        print(f"Verifying security code: {self.security_code}")
        self.verified = True
    
    def pay(self, order):
        print("Processing debit payment type")
        self.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
        
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.status = "paid"
        
        
class PaypalPaymentProcessor(PaymentProcessor_SMS):
    
    def __init__(self, email_address):
        self.email_address = email_address
        self.verified = False
        
            
    def auth(self, code):
        print(f"Verifying security code: {self.security_code}")
        self.verified = True
    
    def pay(self, order):
        print("Processing paypal payment type")
        self.status = "paid"
    
    
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
payment_processor = PaypalPaymentProcessor("me@alinaeriparizi.com")
payment_processor.pay(order)