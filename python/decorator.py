import time
from functools import cache, wraps


## 1. Example of a function decorator
# The time decorator which measures the execution time of the function
def timer(main_function: callable) -> callable:
    def inner_function(*args, **kwargs):
        start = time.time()
        res = main_function(*args, **kwargs)
        end = time.time()
        elapsed_time = end - start
        print(f"{main_function.__name__} Execution time: {elapsed_time}")
        return res
    return inner_function

# A function which uses timer decorator
@timer
def just_wait(person:str="ali", duration:int=3):
    print(f"waiting {duration} seconds for {person}")
    time.sleep(duration)


## 2. Two builtin and useful decorators, wraps and cache
# 2.1 cache decorator
# cache decorator memorized the last function call result to reduce the calculation time which is useful while writing
# recursive functions.


def fibonacci(n: int) -> int:
    if not isinstance(n, int) or n < 1:
        raise ValueError(f"n({n}) should be a positive integer")
    if n==1 or n==2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


@cache
def cached_fibonacci(n: int) -> int:
    if not isinstance(n, int) or n < 1:
        raise ValueError(f"n({n}) should be a positive integer")
    if n==1 or n==2:
        return 1
    return cached_fibonacci(n-1) + cached_fibonacci(n-2)


@timer
def run_cached_fibonacci(n):
    return cached_fibonacci(n)

@timer
def run_fibonacci(n):
    return fibonacci(n)    


# 2.2 wraps decorator wraps all strings in a class or function while using decorators
# if we simply decorate a function, its docstring becomes as the inner class docstring
# and not the original function docstring. wraps decorator will be used inside the decorator function to solve the issue for us...

def do_nothing(f):
    @wraps(f)
    def inner(*args, **kwargs):
        return f(*args, **kwargs)
    return inner


# In this function func.__name__ and func.__doc__ are special attrs which 
# will be printed with wraps decorator
@do_nothing
def alpha(*args, **kwargs):
    """A function for viewing the arguments."""
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")    
    

if __name__ == "__main__":
    
    n = 35
    
    just_wait("ali", 2)
    
    run_fibonacci(n)
    run_cached_fibonacci(n)
    
    alpha(1,"ali", {10}, has_kwargs=True)
    print(alpha.__doc__)
    print(alpha.__name__)
    