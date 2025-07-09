# ===============================================
# 🧠 PYTHON FUNCTIONS - FULL MASTER GUIDE
# ===============================================

# ✅ Functions allow us to group reusable code into blocks.
# They help in organizing code, avoiding repetition, and improving readability.
# Functions can take parameters, return values, and can be nested.
# 📌 Functions are defined using the `def` keyword.

# Type of functions:
# 1. Build in Functions: These are pre-defined functions in Python, like `print()`, `len()`, etc.
# 2. User-defined Functions: These are functions created by the user to perform specific tasks.

# Syntax:
# def function_name(parameters):
#     # code
#     return result

# ===============================================
# 📌 1. Basic Function (No Arguments)
# ===============================================

def greet():
    print("Hello Aditya!")

greet()  # Call function

# ===============================================
# 📌 2. Function with Arguments
# ===============================================

def greet_user(name):
    print(f"Hello {name}!")

greet_user("Esita")

# ===============================================
# 📌 3. Function with Return Value
# ===============================================

def add(x, y):
    return x + y

result = add(5, 3)
print("Sum =", result)

# ===============================================
# 📌 4. Default Arguments
# ===============================================

def welcome(name="Guest"):
    print(f"Welcome, {name}!")

welcome()          # Guest
welcome("Aditya")  # Aditya

# ===============================================
# 📌 5. Keyword Arguments
# ===============================================

def student(name, age, city):
    print(f"{name} is {age} years old from {city}.")

student(age=21, city="Delhi", name="Esita")

# ===============================================
# 📌 6. Variable-Length Arguments
# ===============================================

# *args (non-keyword variable-length arguments)
def total_marks(*marks):
    print("Marks:", marks)
    return sum(marks)

print("Total =", total_marks(70, 85, 90))

# **kwargs (keyword variable-length arguments)
def print_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_profile(name="Aditya", age=23, college="LPU")

# ===============================================
# 📌 7. Nested Functions
# ===============================================

def outer():
    def inner():
        print("Inner function")
    inner()

outer()

# ===============================================
# 📌 8. Function Returning Multiple Values
# ===============================================

def calc(x, y):
    return x + y, x * y, x - y

s, m, d = calc(10, 5)
print("Sum:", s, "Mul:", m, "Diff:", d)

# ===============================================
# 📌 9. Lambda Functions (Anonymous One-liner)
# ===============================================

square = lambda x: x * x
print("Square of 6 =", square(6))

add = lambda a, b: a + b
print("Lambda Add =", add(4, 7))

# Use with map(), filter(), sorted(), etc.
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print("Squared List:", squared)

# ===============================================
# 📌 10. Recursive Functions
# ===============================================

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 =", factorial(5))

# ===============================================
# 📌 11. Real-Life Examples
# ===============================================

# ✅ Greet all names
def greet_all(names):
    for name in names:
        print(f"Hi, {name}!")

greet_all(["Aditya", "Esita", "Rahul"])

# ✅ Check if number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 7 Prime?", is_prime(7))
print("Is 9 Prime?", is_prime(9))

# ===============================================
# 🧠 Summary
# - ✅ Use `def` to define functions
# - 📥 Parameters: normal, default, *args, **kwargs
# - 🔁 Return values with `return`
# - 🔍 Use `lambda` for short one-liner functions
# - 🔂 Recursion = function calling itself