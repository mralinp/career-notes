# Python concepts

- [Decorator](#decorator)
- [Generator](#generator)
- [Async](#async)
- [GIL](#gil)

## Decorators
In Python, a decorator is a design pattern that allows you to modify or extend the behavior of functions or methods without permanently modifying their code. Decorators are implemented using the "@" symbol followed by the name of the decorator function or class, placed above the function or method definition.

Here's a basic example:

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

In this example, `my_decorator` is a decorator function that takes another function func as an argument. It defines a nested function wrapper() which contains code to be executed before and after calling func. The say_hello() function is decorated with `@my_decorator`, so when `say_hello()` is called, it actually executes the `wrapper()` function defined within `my_decorator`, which in turn calls `say_hello()`.

Decorators are commonly used for tasks such as **logging**, **authentication**, **memoization**, and more, providing a clean and concise way to add functionality to functions or methods.

More examples are provided inside `decorator.py` file.

## Generator

In Python, a generator is a special type of iterator that allows you to iterate over a sequence of values without the need to store them all in memory at once. Generators are defined using functions or expressions containing one or more yield statements.

Here's a simple example of a generator function:

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

# Using the generator
for num in count_up_to(5):
    print(num)
```

In this example, count_up_to is a generator function. When called, it returns a generator object. The yield keyword is used to yield (or produce) values one at a time as the generator is iterated over. Each time the yield statement is encountered, the function's state is saved, allowing it to resume from that point when the generator is iterated over again.

Generators are memory efficient because they produce values on-the-fly, only when needed, rather than storing them all in memory. This makes them particularly useful when working with large datasets or when generating an indefinite sequence of values.

You can also create generators using generator expressions, which are similar to list comprehensions but use parentheses instead of square brackets:

```python
my_generator = (x ** 2 for x in range(5))

for num in my_generator:
    print(num)
```

Generator expressions are often more concise than generator functions for simple cases where the logic can be expressed in a single line.

More examples are provided inside `generator.py` file.

## Async
In Python, async and asyncio are features and modules respectively that enable asynchronous programming, particularly in I/O-bound and high-concurrency applications. They are introduced in Python 3.5 and enhanced in subsequent versions.

1. `async/await`:
    - `async` and `await` are used to define asynchronous functions and coroutines.
    - An asynchronous function is defined with the async keyword, and it can contain `await` expressions, which indicate points where the execution can pause and wait for asynchronous operations to complete.
    - When you call an asynchronous function, it returns a coroutine object, which you can then schedule for execution using `asyncio` or other asynchronous frameworks.

    ```python
    import asyncio

    async def my_async_function():
        print("Start")
        await asyncio.sleep(1)
        print("End")

    asyncio.run(my_async_function())
    ```

2. `asyncio`:
    - `asyncio` is a module in Python's standard library that provides infrastructure for writing asynchronous I/O-bound code using coroutines.
    - It includes event loops, which manage the execution of coroutines, and various APIs for asynchronous I/O operations, such as networking and file I/O.
    - With asyncio, you can write non-blocking code that efficiently handles many concurrent tasks without the need for threads.
    ```python
    import asyncio

    async def my_coroutine():
        await asyncio.sleep(1)
        print("Coroutine executed")

    async def main():
        await asyncio.gather(my_coroutine(), my_coroutine())

    asyncio.run(main())
    ```
In these examples, `asyncio.sleep(1)` simulates a `non-blocking` delay of `1` second. While waiting for this operation to complete, the event loop can execute other coroutines concurrently.

Asyncio is especially useful for I/O-bound tasks like web scraping, network programming, or interacting with databases, where the program spends most of its time waiting for external operations to complete. It can significantly improve the efficiency and scalability of such applications compared to traditional synchronous programming models.

## GIL

The GIL (Global Interpreter Lock) in Python is a mutex (mutual exclusion) that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously. In simpler terms, the GIL ensures that only one thread executes Python bytecode at any given time, even on multi-core processors.

This means that in a multi-threaded Python program, while you may have multiple threads running, only one thread is executing Python code at any given moment. The GIL effectively serializes access to Python objects, which can limit the performance improvement that you might expect from adding more threads to your program, especially in CPU-bound tasks.

However, it's essential to note that the GIL only affects threads that are executing Python code. It doesn't prevent multiple threads from running concurrently if they're executing native code (e.g., in C extensions) or performing I/O operations, which often release the GIL.

Despite its reputation for limiting concurrency, the GIL simplifies the implementation of the Python interpreter and makes it easier to integrate with existing C libraries, among other benefits. However, it can become a bottleneck in CPU-bound applications where multi-threading is expected to provide significant performance gains.

To overcome the limitations of the GIL in CPU-bound scenarios, developers often use multiprocessing, concurrent.futures, or other approaches to parallelize their code across multiple processes rather than multiple threads. This way, each process has its own Python interpreter and GIL, allowing better utilization of multi-core processors.
