
# Basic Decorator (Good for initial coder to learn this)
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()


# Decorator with arguments (Also good for all the new coders )
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}")

greet("Amit")


# Using functools.wraps (This part is also very important for the ai role)
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

print(add(10, 20))


# Timing Decorator (Best for us for working!)
import time
from functools import wraps

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} sec")
        return result
    return wrapper

@timing
def slow():
    time.sleep(1)
    print("Done")

slow()


# Class-based Decorator (Class for learning)
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Call number: {self.count}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hi():
    print("Hi")

say_hi()
say_hi()


# ==================== PRACTICE ====================
# 1. Create a decorator that prints "Start" and "End" around any function.
# 2. Create a decorator that only allows a function to run if a password is correct.
# 3. Create a decorator that caches the result of a function (simple memoization).


# Solutions
def start_end(func):
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result
    return wrapper

@start_end
def hello():
    print("Hello World")

hello()


def password_required(func):
    def wrapper(*args, **kwargs):
        pwd = input("Enter password: ")
        if pwd == "python123":
            return func(*args, **kwargs)
        else:
            print("Wrong password!")
    return wrapper

@password_required
def secret():
    print("This is secret data")

# secret()   # Uncomment to test


def simple_cache(func):
    cache = {}
    def wrapper(n):
        if n in cache:
            print("Returning from cache")
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

@simple_cache
def square(n):
    print("Calculating...")
    return n * n

print(square(5))
print(square(5))



# Simple generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for i in countdown(5):
    print(i, end=" ")
print()


# Fibonacci generator
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

print(list(fibonacci(50)))


# Generator expression
squares = (x*x for x in range(1, 6))
print(list(squares))


# yield from
def gen():
    yield from range(3)
    yield from ["a", "b"]

print(list(gen()))


# Infinite generator
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

counter = infinite_counter()
print(next(counter))
print(next(counter))
print(next(counter))


# Generator pipeline
def numbers():
    for i in range(1, 11):
        yield i

def even(seq):
    for i in seq:
        if i % 2 == 0:
            yield i

def square(seq):
    for i in seq:
        yield i * i

pipeline = square(even(numbers()))
print(list(pipeline))


# ==================== PRACTICE ====================
# 1. Create a generator that yields even numbers up to 30.
# 2. Create a generator that yields squares of numbers from 1 to 10.
# 3. Create a generator that reads a file line by line.
# 4. Create a generator that yields the reverse of a list.


# Solutions
def even_upto(n):
    for i in range(2, n+1, 2):
        yield i

print(list(even_upto(30)))


def squares(n):
    for i in range(1, n+1):
        yield i*i

print(list(squares(10)))


def read_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# for line in read_file("sample.txt"):
#     print(line)


def reverse_list(lst):
    for item in reversed(lst):
        yield item

print(list(reverse_list([1, 2, 3, 4, 5])))



# Class based context manager
class MyContext:
    def __enter__(self):
        print("Entering...")
        return "Resource"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting...")
        return False

with MyContext() as r:
    print("Using:", r)


# Using contextlib
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Setup")
    yield "Hello"
    print("Cleanup")

with my_context() as value:
    print(value)


# Timer context manager
import time
from contextlib import contextmanager

@contextmanager
def timer():
    start = time.time()
    yield
    print(f"Time taken: {time.time() - start:.4f} seconds")

with timer():
    time.sleep(1)


# ==================== PRACTICE ====================
# 1. Create a context manager that prints "Open" and "Close".
# 2. Create a context manager that temporarily changes a variable value.
# 3. Create a context manager that measures memory or just time.


# Solutions
@contextmanager
def open_close():
    print("Open")
    yield
    print("Close")

with open_close():
    print("Inside")


@contextmanager
def change_value(original):
    print(f"Original: {original}")
    yield original * 2
    print("Restored")

with change_value(10) as new_val:
    print("Inside:", new_val)



# property, setter, classmethod, staticmethod
class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    @classmethod
    def from_string(cls, data):
        name, salary = data.split("-")
        return cls(name, int(salary))

    @staticmethod
    def is_workday(day):
        return day.lower() not in ["saturday", "sunday"]

emp = Employee("Amit", 50000)
print(emp.salary)
emp.salary = 60000
print(emp.salary)

emp2 = Employee.from_string("Sneha-55000")
print(emp2.name, emp2.salary)
print(Employee.is_workday("Monday"))


# Magic Methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.title} ({self.pages} pages)"

    def __repr__(self):
        return f"Book('{self.title}', {self.pages})"

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __add__(self, other):
        return Book(self.title + " & " + other.title, self.pages + other.pages)

b1 = Book("Python", 300)
b2 = Book("Advanced Python", 450)
print(b1)
print(len(b1))
print(b1 == b2)
print(b1 + b2)


# ==================== PRACTICE ====================
# 1. Create a Temperature class with celsius property and fahrenheit conversion.
# 2. Create a Vector class that supports + operator.
# 3. Create a class that counts how many objects are created.


# Solutions
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

t = Temperature(25)
print(t.fahrenheit)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)
print(v1 + v2)


class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()
print("Total objects:", Counter.count)



from collections import Counter, defaultdict, namedtuple, deque

# Counter
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
c = Counter(data)
print(c)
print(c.most_common(2))


# defaultdict
dd = defaultdict(list)
dd["fruits"].append("apple")
dd["fruits"].append("banana")
dd["vegetables"].append("carrot")
print(dd)


# namedtuple
Point = namedtuple("Point", "x y")
p = Point(10, 20)
print(p.x, p.y)


# deque
d = deque([1, 2, 3])
d.appendleft(0)
d.append(4)
print(d)
print(d.popleft())


# ==================== PRACTICE ====================
# 1. Count frequency of each character in a string using Counter.
# 2. Group list of tuples by first element using defaultdict.
# 3. Use deque to reverse a list.


# Solutions
text = "programming"
print(Counter(text))

pairs = [("A", 1), ("B", 2), ("A", 3), ("C", 4), ("B", 5)]
group = defaultdict(list)
for k, v in pairs:
    group[k].append(v)
print(group)

d = deque([1, 2, 3, 4, 5])
d.reverse()
print(list(d))



from functools import lru_cache, partial, reduce

# lru_cache
@lru_cache(maxsize=128)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(30))
print(fib.cache_info())


# partial
def power(base, exp):
    return base ** exp

square = partial(power, exp=2)
cube = partial(power, exp=3)

print(square(6))
print(cube(4))


# reduce
nums = [1, 2, 3, 4, 5]
print(reduce(lambda a, b: a + b, nums))
print(reduce(lambda a, b: a * b, nums))


# ==================== PRACTICE ====================
# 1. Use lru_cache on a factorial function.
# 2. Use partial to create a function that always multiplies by 10.
# 3. Use reduce to find the maximum number in a list.


# Solutions
@lru_cache
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(10))

multiply_by_10 = partial(lambda x, y: x * y, 10)
print(multiply_by_10(7))

nums = [3, 7, 2, 9, 4]
print(reduce(lambda a, b: a if a > b else b, nums))



from typing import List, Dict, Optional, Union, Callable

def greet(name: str) -> str:
    return f"Hello, {name}"

def total(nums: List[int]) -> int:
    return sum(nums)

def find_user(user_id: int) -> Optional[Dict[str, str]]:
    if user_id == 1:
        return {"name": "Amit"}
    return None

def apply(fn: Callable[[int, int], int], x: int, y: int) -> int:
    return fn(x, y)

print(greet("Sneha"))
print(total([1, 2, 3, 4]))
print(find_user(1))
print(apply(lambda a, b: a * b, 5, 6))


# ==================== PRACTICE ====================
# 1. Write a function with type hints that takes a list of strings and returns the longest string.
# 2. Write a function that takes Optional[int] and returns a string.


# Solutions
def longest(words: List[str]) -> str:
    return max(words, key=len)

print(longest(["apple", "banana", "kiwi"]))

def check(value: Optional[int]) -> str:
    if value is None:
        return "No value"
    return f"Value is {value}"

print(check(10))
print(check(None))



import re

text = "Contact me at amit.kumar@gmail.com or call 9876543210"

# Find phone
phone = re.search(r"\d{10}", text)
print(phone.group() if phone else "Not found")

# Find email
email = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
print(email.group() if email else "Not found")

# Find all
print(re.findall(r"\d+", text))

# Substitute
print(re.sub(r"\d{10}", "XXXXXXXXXX", text))

# Match full string
print(bool(re.fullmatch(r"[6-9]\d{9}", "9876543210")))


# ==================== PRACTICE ====================
# 1. Extract all hashtags from a text.
# 2. Validate an email address.
# 3. Remove all digits from a string.
# 4. Find all words starting with capital letter.


# Solutions
tweet = "I love #Python and #AI #MachineLearning"
print(re.findall(r"#\w+", tweet))

def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.fullmatch(pattern, email))

print(is_valid_email("test@gmail.com"))
print(is_valid_email("invalid@"))

text = "Hello123World456"
print(re.sub(r"\d+", "", text))

sentence = "My Name Is Amit Kumar"
print(re.findall(r"\b[A-Z][a-z]*\b", sentence))



# Threading
import threading
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=task, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
print("All threads done")


# Multiprocessing
from multiprocessing import Process

def square(n):
    print(n * n)

processes = []
for i in range(5):
    p = Process(target=square, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()


# Asyncio
import asyncio

async def say(delay, msg):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    await asyncio.gather(
        say(1, "First"),
        say(2, "Second"),
        say(1, "Third")
    )

# asyncio.run(main())   # Uncomment to run


# ==================== PRACTICE ====================
# 1. Create 5 threads that each print a number after sleeping 1 second.
# 2. Use multiprocessing to calculate squares of numbers 1 to 10.
# 3. Write an async function that downloads (simulates) 3 URLs concurrently.


# Solutions
def print_num(n):
    time.sleep(1)
    print(n)

threads = [threading.Thread(target=print_num, args=(i,)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()


def sq(n):
    print(f"{n}² = {n*n}")

procs = [Process(target=sq, args=(i,)) for i in range(1, 11)]
for p in procs:
    p.start()
for p in procs:
    p.join()


async def fake_download(url):
    await asyncio.sleep(1)
    print(f"Downloaded {url}")

async def download_all():
    urls = ["url1", "url2", "url3"]
    await asyncio.gather(*(fake_download(u) for u in urls))

# asyncio.run(download_all())



from dataclasses import dataclass, field

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0
    tags: list = field(default_factory=list)

    def total(self) -> float:
        return self.price * self.quantity

p1 = Product("Laptop", 55000, 2)
p2 = Product("Laptop", 55000, 2)
print(p1)
print(p1.total())
print(p1 == p2)


@dataclass(order=True)
class Student:
    name: str
    marks: int

s1 = Student("Amit", 85)
s2 = Student("Sneha", 92)
print(s1 < s2)


# ==================== PRACTICE ====================
# 1. Create a dataclass for a Car with brand, model, year and price.
# 2. Add a method to calculate depreciation (assume 10% per year).
# 3. Create a dataclass for Point with x, y and a method to calculate distance from origin.


# Solutions
@dataclass
class Car:
    brand: str
    model: str
    year: int
    price: float

    def depreciated_price(self, current_year: int) -> float:
        age = current_year - self.year
        return self.price * (0.9 ** age)

car = Car("Toyota", "Innova", 2020, 2000000)
print(car.depreciated_price(2026))


@dataclass
class Point:
    x: float
    y: float

    def distance(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

p = Point(3, 4)
print(p.distance())



import unittest

def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ValueError):
            divide(10, 0)

# if __name__ == "__main__":
#     unittest.main()


# ==================== PRACTICE ====================
# 1. Write tests for a function that returns the maximum of three numbers.
# 2. Write tests for a function that checks if a number is prime.


# Solutions
def maximum(a, b, c):
    return max(a, b, c)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

class TestExtra(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(maximum(3, 7, 5), 7)
        self.assertEqual(maximum(-1, -5, -3), -1)

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(1))

# if __name__ == "__main__":
#     unittest.main()


