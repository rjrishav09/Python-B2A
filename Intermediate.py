
# ---------- Example 1: Using built-in modules ----------
import math
import random
from datetime import datetime

print("Square root of 49:", math.sqrt(49))
print("Ceiling of 4.2:", math.ceil(4.2))
print("Random number between 1-10:", random.randint(1, 10))
print("Current date and time:", datetime.now())


# ---------- Example 2: Creating your own module ----------
# First create a file named "mymodule.py" with this content:
"""
def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}! Welcome to Intermediate Python."
"""

# Then in another file (main.py):
# import mymodule
# print(mymodule.add(10, 20))
# print(mymodule.greet("Amit"))


# ---------- Example 3: Using alias and from-import ----------
import math as m
from math import pi, factorial

print("Value of pi:", pi)
print("5! =", factorial(5))
print("Using alias - square root:", m.sqrt(81))


# ==================== PRACTICE TASKS ====================
# Task 1: Use the random module to generate 5 random numbers between 1 and 100.
# Task 2: Use datetime to print today's date in the format DD-MM-YYYY.
# Task 3: Create your own module with a function that calculates area of a circle.


# ---------- SOLUTIONS ----------
# Task 1
import random
print([random.randint(1, 100) for _ in range(5)])

# Task 2
from datetime import datetime
print(datetime.now().strftime("%d-%m-%Y"))

# Task 3 (create circle.py)
# def area(radius):
#     return 3.14159 * radius * radius



# ---------- Example 1: Writing to a file ----------
with open("sample.txt", "w") as file:
    file.write("Hello, this is Intermediate Python.\n")
    file.write("Learning file handling is important.\n")
    file.write("Practice makes perfect.\n")

print("File written successfully!")


# ---------- Example 2: Reading entire file ----------
with open("sample.txt", "r") as file:
    content = file.read()
    print("\n--- Full Content ---")
    print(content)


# ---------- Example 3: Reading line by line ----------
with open("sample.txt", "r") as file:
    print("\n--- Line by Line ---")
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")


# ---------- Example 4: Appending to a file ----------
with open("sample.txt", "a") as file:
    file.write("This line was appended.\n")

print("\nData appended successfully!")


# ---------- Example 5: Reading and writing together (r+) ----------
with open("sample.txt", "r+") as file:
    content = file.read()
    file.write("\n--- Extra line added using r+ mode ---")


# ==================== PRACTICE TASKS ====================
# Task 1: Create a file "students.txt" and write names of 5 students (one per line).
# Task 2: Read the file and print only those names that start with letter 'A' or 'S'.
# Task 3: Count the total number of words in the file.
# Task 4: Create a program that copies content from one file to another.


# ---------- SOLUTIONS ----------

# Task 1
with open("students.txt", "w") as f:
    f.write("Amit\nSneha\nRahul\nPriya\nSohan\n")

# Task 2
with open("students.txt", "r") as f:
    print("\nNames starting with A or S:")
    for name in f:
        name = name.strip()
        if name.startswith(("A", "S")):
            print(name)

# Task 3
with open("students.txt", "r") as f:
    content = f.read()
    words = content.split()
    print("Total words:", len(words))

# Task 4
with open("students.txt", "r") as source:
    content = source.read()

with open("students_copy.txt", "w") as destination:
    destination.write(content)

print("File copied successfully!")



# ---------- Example 1: Basic try-except ----------
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")


# ---------- Example 2: Multiple exceptions ----------
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ValueError:
    print("Please enter only numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("An unexpected error occurred:", e)


# ---------- Example 3: else and finally ----------
try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("Number cannot be negative")
except ValueError as e:
    print("Error:", e)
else:
    print("Great! You entered a valid positive number:", num)
finally:
    print("This block always executes.")


# ---------- Example 4: Raising custom exception ----------
class AgeError(Exception):
    """Custom exception for invalid age"""
    pass

def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative")
    if age > 120:
        raise AgeError("Age seems unrealistic")
    print("Age is valid:", age)

try:
    check_age(25)
    check_age(-5)
except AgeError as e:
    print("Custom Error:", e)


# ==================== PRACTICE TASKS ====================
# Task 1: Write a program that takes two numbers and divides them.
#         Handle ZeroDivisionError and ValueError.
# Task 2: Create a custom exception called InsufficientBalanceError
#         for a banking withdrawal system.
# Task 3: Write a program that tries to open a file. If file does not exist,
#         catch FileNotFoundError and create the file.


# ---------- SOLUTIONS ----------

# Task 1
try:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    print("Result =", x / y)
except ValueError:
    print("Invalid number entered")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Task 2
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance!")
    return balance - amount

try:
    print("Remaining balance:", withdraw(1000, 1500))
except InsufficientBalanceError as e:
    print(e)

# Task 3
try:
    with open("data.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found. Creating new file...")
    with open("data.txt", "w") as f:
        f.write("This is a new file created after exception.")



# ---------- Example 1: Simple Class and Object ----------
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Name: {self.name} | Age: {self.age} | Course: {self.course}")

    def is_adult(self):
        return self.age >= 18

s1 = Student("Priya", 21, "Python")
s2 = Student("Rahul", 17, "Java")

s1.display()
print("Is adult?", s1.is_adult())
s2.display()
print("Is adult?", s2.is_adult())


# ---------- Example 2: Inheritance ----------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):                      # Method Overriding
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")

dog = Dog("Tommy")
cat = Cat("Kitty")

dog.speak()
cat.speak()


# ---------- Example 3: Encapsulation (using private variables) ----------
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance          # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

account = BankAccount("Amit", 5000)
account.deposit(1500)
account.withdraw(2000)
print("Current Balance:", account.get_balance())
# print(account.__balance)   # This will give error (private)


# ---------- Example 4: Polymorphism ----------
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

shapes = [Rectangle(10, 5), Circle(7)]

for shape in shapes:
    print("Area:", shape.area())


# ==================== PRACTICE TASKS ====================
# Task 1: Create a class Car with attributes brand, model, year.
#         Add a method display_info().
# Task 2: Create a parent class Person and child class Employee.
#         Employee should have extra attribute salary.
# Task 3: Create a BankAccount class with deposit, withdraw and get_balance.
#         Make balance private.
# Task 4: Demonstrate method overriding with a parent and child class.


# ---------- SOLUTIONS ----------

# Task 1
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.brand} {self.model} ({self.year})")

my_car = Car("Toyota", "Fortuner", 2023)
my_car.display_info()

# Task 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def show(self):
        print(f"{self.name}, {self.age} years, Salary: {self.salary}")

emp = Employee("Sneha", 28, 60000)
emp.show()

# Task 3 (already shown above in Example 3)

# Task 4
class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow can fly high")

s = Sparrow()
s.fly()



# ---------- Example 1: List Comprehension ----------
# Traditional way
squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print("Traditional:", squares)

# List comprehension way
squares = [i ** 2 for i in range(1, 11)]
print("Comprehension:", squares)

# With condition
even_squares = [i ** 2 for i in range(1, 11) if i % 2 == 0]
print("Even squares:", even_squares)

# if-else inside comprehension
result = ["Even" if i % 2 == 0 else "Odd" for i in range(1, 6)]
print(result)


# ---------- Example 2: Dictionary Comprehension ----------
# Create dictionary of numbers and their cubes
cubes = {x: x ** 3 for x in range(1, 6)}
print("Cubes:", cubes)

# From existing list
names = ["Amit", "Sneha", "Rahul"]
name_length = {name: len(name) for name in names}
print("Name lengths:", name_length)


# ---------- Example 3: Set Comprehension ----------
numbers = [1, 2, 2, 3, 3, 4, 5, 5]
unique_squares = {x ** 2 for x in numbers}
print("Unique squares:", unique_squares)


# ---------- Example 4: Nested Comprehension ----------
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened:", flattened)


# ==================== PRACTICE TASKS ====================
# Task 1: Create a list of squares of even numbers from 1 to 20 using comprehension.
# Task 2: Create a dictionary where keys are numbers 1-10 and values are "Even" or "Odd".
# Task 3: From a list of words, create a set of words that have length > 4.
# Task 4: Flatten a 2D list using list comprehension.


# ---------- SOLUTIONS ----------

# Task 1
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(even_squares)

# Task 2
even_odd = {x: "Even" if x % 2 == 0 else "Odd" for x in range(1, 11)}
print(even_odd)

# Task 3
words = ["apple", "hi", "python", "code", "learning", "AI"]
long_words = {word for word in words if len(word) > 4}
print(long_words)

# Task 4
matrix = [[10, 20], [30, 40], [50, 60]]
flat = [item for row in matrix for item in row]
print(flat)


# ---------- Example 1: Lambda functions ----------
add = lambda a, b: a + b
print("Sum:", add(10, 20))

square = lambda x: x ** 2
print("Square of 7:", square(7))

# Lambda with if-else
max_num = lambda a, b: a if a > b else b
print("Maximum:", max_num(45, 78))


# ---------- Example 2: map() ----------
numbers = [1, 2, 3, 4, 5]

# Using normal function
def square(x):
    return x ** 2

squared = list(map(square, numbers))
print("Squared (normal):", squared)

# Using lambda
squared = list(map(lambda x: x ** 2, numbers))
print("Squared (lambda):", squared)

# Multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
summed = list(map(lambda x, y: x + y, a, b))
print("Summed lists:", summed)


# ---------- Example 3: filter() ----------
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Filter names starting with 'A'
names = ["Amit", "Sneha", "Ankit", "Rahul", "Asha"]
a_names = list(filter(lambda name: name.startswith("A"), names))
print("Names starting with A:", a_names)


# ---------- Example 4: reduce() ----------
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum of all numbers
total = reduce(lambda a, b: a + b, numbers)
print("Sum:", total)

# Find maximum
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Maximum:", maximum)

# Multiply all numbers
product = reduce(lambda a, b: a * b, numbers)
print("Product:", product)


# ==================== PRACTICE TASKS ====================
# Task 1: Use lambda to create a function that returns the last character of a string.
# Task 2: Use map to convert a list of temperatures from Celsius to Fahrenheit.
# Task 3: Use filter to get all numbers divisible by 3 from a list.
# Task 4: Use reduce to find the sum of squares of numbers in a list.


# ---------- SOLUTIONS ----------

# Task 1
last_char = lambda s: s[-1]
print(last_char("Python"))

# Task 2
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

# Task 3
nums = [3, 6, 7, 9, 12, 14, 15, 18]
div_by_3 = list(filter(lambda x: x % 3 == 0, nums))
print(div_by_3)

# Task 4
from functools import reduce
nums = [1, 2, 3, 4]
sum_of_squares = reduce(lambda a, b: a + b**2, nums, 0)
print(sum_of_squares)


# ---------- Example 1: Iterator ----------
numbers = [10, 20, 30, 40]
iterator = iter(numbers)

print(next(iterator))      # 10
print(next(iterator))      # 20
print(next(iterator))      # 30
print(next(iterator))      # 40
# print(next(iterator))    # StopIteration error


# ---------- Example 2: Creating custom iterator ----------
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for num in CountDown(5):
    print(num, end=" ")
print()


# ---------- Example 3: Generator using yield ----------
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for value in countdown(5):
    print(value, end=" ")
print()


# ---------- Example 4: Generator expression ----------
squares_gen = (x**2 for x in range(1, 6))
print(list(squares_gen))


# ---------- Example 5: Infinite generator (useful concept) ----------
def infinite_counter():
    num = 1
    while True:
        yield num
        num += 1

counter = infinite_counter()
print(next(counter))
print(next(counter))
print(next(counter))


# ---------- Example 6: Memory efficient Fibonacci generator ----------
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

print("Fibonacci series:")
for num in fibonacci(50):
    print(num, end=" ")
print()


# ==================== PRACTICE TASKS ====================
# Task 1: Create a generator that yields even numbers up to 20.
# Task 2: Create a generator that yields the squares of numbers from 1 to 10.
# Task 3: Create a custom iterator class that returns numbers from 1 to n.
# Task 4: Write a generator function that yields the reverse of a string character by character.


# ---------- SOLUTIONS ----------

# Task 1
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

print(list(even_numbers(20)))

# Task 2
def squares(n):
    for i in range(1, n + 1):
        yield i ** 2

print(list(squares(10)))

# Task 3
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

print(list(NumberIterator(5)))

# Task 4
def reverse_string(text):
    for char in reversed(text):
        yield char

print("".join(reverse_string("Python")))

