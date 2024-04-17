import string
import itertools
import sys

def f():
    yield 1
    yield 2
    yield 3
    yield 4
    
print(type(f())) # returns a generator object

for x in f():
    print(x)
    
def letters():
    for c in string.ascii_lowercase:
        yield c

for l in letters():
    print(l, end='-')

# 'yield' passes the control to another process

def prime_numbers():
    yield 2
    
    prime_cache = [2]
    
    for n in itertools.count(3, 2):
        is_prime = True
        for p in prime_cache:
            if n%p == 0:
                is_prime = False
                break
        if is_prime:
            prime_cache.append(n)
            yield n
        
        
for p in prime_numbers():
    print(p)
    if p > 100:
        break

# it calls generator expression which uses () and list expression
# uses [] which creates a list :)
squares = (x**2 for x in itertools.count(1))

print(type(squares))

# generators are memory efficient because the will generate the value
# instead of storing the value in memory
print(sys.getsizeof(squares))
    
for s in squares:
    print(s)
    if s > 500:
        squares.close()
