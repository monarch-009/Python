# ===============================================
# 📘 PYTHON CONDITIONAL STATEMENTS - IF, ELIF, ELSE
# ===============================================

# ✅ Used to make decisions in code based on conditions.

# ===============================================
# 📌 1. Basic `if` Statement
# ===============================================

age = 18

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# ===============================================
# 📌 2. if-else Statement
# ===============================================

is_raining = False

if is_raining:
    print("Take an umbrella.")
else:
    print("No need for an umbrella.")

# ===============================================
# 📌 3. if-elif-else (Multiple Conditions)
# ===============================================

marks = 85

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

# ===============================================
# 📌 4. Nested if Statements
# ===============================================

user = "admin"
authenticated = True

if user == "admin":
    if authenticated:
        print("Welcome Admin!")
    else:
        print("Please log in.")
else:
    print("Access denied.")

# ===============================================
# 📌 5. One-line if and if-else (Ternary Operator)
# ===============================================

# One-liner if
num = 10
if num > 5: print("Greater than 5")

# Ternary (conditional expression)
result = "Even" if num % 2 == 0 else "Odd"
print("Number is:", result)

# ===============================================
# 📌 6. Logical Operators in Conditions
# ===============================================

username = "aditya"
password = "1234"

if username == "aditya" and password == "1234":
    print("Login successful.")

age = 25
if age > 18 or age == 18:
    print("Adult")

# not operator
if not False:
    print("This is true.")

# ===============================================
# 📌 7. Comparison Operators in Conditions
# ===============================================

a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# ===============================================
# 📌 8. Real-Life Examples
# ===============================================

# Example 1: Check odd/even
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 2: Check leap year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Example 3: BMI Category
bmi = 23

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal weight")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")

# ===============================================
# 🧠 Summary
# - ✅ Use `if`, `elif`, and `else` to make decisions
# - 🧮 Use comparison (`==`, `!=`, `<`, `>`, etc.) and logical (`and`, `or`, `not`) operators
# - 📦 One-line if and ternary statements can simplify short decisions
# - 🧩 Nest conditions carefully when needed
