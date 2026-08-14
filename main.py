# 1. Variables and Data Types
name = "Alex"          # str (string)
age = 25               # int (integer)
height = 5.9           # float
is_student = True      # bool (boolean)
nothing = None         # NoneType

#Check type:
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(nothing))

#Multiple assignment:
a, b, c, = "Rishav", 24, 5.9 
print(a,"\n", b,"\n",c)
a = b = c = 100
print(f"Multiple assignement values:\n {a},{b},{c}")

#Basic Operators:

# Arithmetic
print(10 + 3)    # 13
print(10 - 3)    # 7
print(10 * 3)    # 30
print(10 / 3)    # 3.333... (float division)
print(10 // 3)   # 3 (floor division) (Remove values after decimals)
print(10 % 3)    # 1 (modulus) (Gives you Remainder)
print(10 ** 3)   # 1000 (power)

# Comparison
print(5 == 5)    # True
print(5 != 3)    # True
print(5 > 3)     # True

# Logical
print(True and False)  # False 
print(True or False)   # True
print(not True)        # False

#Strings:
text = "Hello Python"

print(text[0])          # H
print(text[-1])         # n
print(text[0:5])        # Hello (slicing) (Very important for data cleaning)
print(len(text))        # 12 (also count blank space)

# Useful methods
print(text.upper())
print(text.lower())
print(text.replace("Python", "World"))
print("Python" in text)  # True

# f-strings (modern way)
name = "Arzun"
age = 22
print(f"My name is {name} and I am {age} years old")

#Control Flow: (if-elif-else)
age = 18

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

#for loop:
for i in range(5):          # 0 to 4
    print(i)

for fruit in ["apple", "banana", "mango"]:
    print(fruit)

#while loop:
count = 0
while count < 5:
    print(count)
    count += 1

#break and continue:
for i in range(10):
    if i == 3:
        continue      # skip 3
    if i == 7:
        break         # stop at 7
    print(i)

#Lists, Tuples, Dictionaries, Sets:
# List (mutable, ordered)
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits[0] = "kiwi"
print(fruits)

# Tuple (immutable, ordered)
point = (10, 20)

# Dictionary (key-value)
person = {
    "name": "Alex",
    "age": 25,
    "city": "Delhi"
}
print(person["name"])
person["age"] = 26

# Set (unique, unordered)
numbers = {1, 2, 3, 3, 4}
print(numbers)   # {1, 2, 3, 4}

#Functions:
def greet(name):
    return f"Hello, {name}!"

print(greet("Alex"))

# Default arguments
def power(base, exp=2):
    return base ** exp

print(power(5))      # 25
print(power(5, 3))   # 125

# *args and **kwargs
def show(*args, **kwargs):
    print(args)
    print(kwargs)

show(1, 2, 3, name="Alex", age=25)