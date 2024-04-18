class Person:

    counter = 0 # Class attribute, number of Person objects
    
    def __init__(self, name):
        self.full_name = name
        Person.counter += 1 # increment the class attribute
        
    def introduction(self):
        print(f"Hello!, my name is {self.full_name}. I'm human...")
    
    @classmethod
    def population(cls):
        # Class method uses cls to access the class attribute
        print(f"The current population is {cls.counter}")


p1 = Person("Ali Naderi")
p2 = Person("Ehsan Vakhshoori")      

# Monkey patch attribute
p1.coin = 1618033

# Monkey code method
p1.pass_code = lambda : "1239876298374"

print(dir(p1))
print(dir(p2))

print(dir(Person))