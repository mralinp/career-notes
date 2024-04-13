# 2. Open closed principle
# The classes should be open for extension but closed for modification

# Here the issue is if want to add another payment method we need to 
# modify the PaymentProcessor class

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
    def pay(self, order, security_code):
        pass
    
    
class DebitPaymentProcessor(PaymentProcessor):
    
    def pay(self, order, security_code):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        self.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
            
    def pay(self, order, security_code):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        self.status = "paid"
        
        
class PaypalPaymentProcessor(PaymentProcessor):
    
    def pay(self, order, security_code):
        print("Processing paypal payment type")
        print(f"Verifying security code: {security_code}")
        self.status = "paid"
    
    
order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB Cable", 2, 5)

print(order.total_price())
payment_processor = PaypalPaymentProcessor()
payment_processor.pay(order, "0372846")