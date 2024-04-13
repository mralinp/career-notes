# 4. Interface segregation
# Having multiple interfaces is better than a one big interface

# We can solve this problem with another method instead of classes 
# and subclasses



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
    
class SMSAuth:
    
    authorized = False
    
    def verify_code(self, code):
        print(f"Verifying code {code}")
        self.authorized = True
    
    def is_authorized(self):
        return self.authorized
    
class PaymentProcessor(ABC):
    
    @abstractmethod
    def pay(self, order):
        pass
    
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.security_code = security_code
    
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        self.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    
    def __init__(self, security_code):
        self.security_code = security_code
        
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        self.status = "paid"
        
        
class PaypalPaymentProcessor(PaymentProcessor):
    
    def __init__(self, email_address, authorizer: SMSAuth):
        self.authorizer = authorizer
        self.email_address = email_address
    
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        self.status = "paid"
    
    
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
sms_authorizer = SMSAuth()
payment_processor = PaypalPaymentProcessor("me@alinaeriparizi.com", authorizer=sms_authorizer)
sms_authorizer.verify_code("1534231")
payment_processor.pay(order)