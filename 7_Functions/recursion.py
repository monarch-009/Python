# ===============================================
# 🔁 PYTHON RECURSION - COMPLETE MASTER GUIDE
# ===============================================

# ✅ A function that calls itself is called a **recursive function**.
# Always include a **base case** to stop infinite recursion.

# ===============================================
# 📌 1. Basic Recursion: Print Numbers from N to 1
# ===============================================

def print_desc(n):
    if n == 0:
        return
    print(n)
    print_desc(n - 1)

print("Descending from 5:")
print_desc(5)

# ===============================================
# 📌 2. Factorial using Recursion
# ===============================================

def factorial(n):
    if n == 0 or n == 1:
        return 1  # base case
    return n * factorial(n - 1)  # recursive call

print("Factorial of 5 =", factorial(5))

# ===============================================
# 📌 3. Fibonacci Sequence
# ===============================================

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci of 6 =", fibonacci(6))

# Generate first N fibonacci numbers
def print_fibonacci_series(n):
    for i in range(n):
        print(fibonacci(i), end=" ")

print("\nFirst 7 Fibonacci numbers:")
print_fibonacci_series(7)

# ===============================================
# 📌 4. Sum of First N Natural Numbers
# ===============================================

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print("\nSum of first 5 numbers =", sum_n(5))

# ===============================================
# 📌 5. Reverse a String using Recursion
# ===============================================

def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

print("Reverse of 'aditya' =", reverse_string("aditya"))

# ===============================================
# 📌 6. Check Palindrome Using Recursion
# ===============================================

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print("Is 'madam' Palindrome?", is_palindrome("madam"))
print("Is 'hello' Palindrome?", is_palindrome("hello"))

# ===============================================
# 📌 7. Count Digits of a Number Recursively
# ===============================================

def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

print("Digits in 12345 =", count_digits(12345))

# ===============================================
# 📌 8. Power Calculation: x^n
# ===============================================

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)

print("2^5 =", power(2, 5))

# ===============================================
# ⚠️ Common Mistakes in Recursion
# ===============================================
# ❌ Missing base case → causes infinite recursion & crash
# ❌ Changing input improperly → may never reach base case
# ❌ Too deep recursion → can hit maximum recursion limit

# ✅ To increase recursion depth (if needed):
# import sys
# sys.setrecursionlimit(2000)

# ===============================================
# 🧠 Summary
# - 🔁 Recursion = function calling itself
# - 🛑 Base case is a must!
# - 📚 Use cases: factorial, Fibonacci, reverse, palindrome
# - 🔄 Can replace loops, but be careful with deep calls
