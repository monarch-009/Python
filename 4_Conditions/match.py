# ===============================================
# 🎛️ SIMULATING SWITCH STATEMENTS IN PYTHON
# ===============================================

# ⚠️ Python does not have a built-in switch-case,
# but we can simulate it in 3 powerful ways.
# This guide covers:
# 1. Using if-elif-else
# 2. Using dictionary mapping (best for fixed options)
# 3. Using match-case (Python 3.10+ only)

# ===============================================
# 📌 1. Using if-elif-else
# ===============================================

choice = 2

if choice == 1:
    print("Option 1 selected")
elif choice == 2:
    print("Option 2 selected")
elif choice == 3:
    print("Option 3 selected")
else:
    print("Invalid option")

# ===============================================
# 📌 2. Using Dictionary Mapping (Best for Fixed Options)
# ===============================================

def option_one():
    return "You chose option 1"

def option_two():
    return "You chose option 2"

def option_three():
    return "You chose option 3"

switch_dict = {
    1: option_one,
    2: option_two,
    3: option_three
}

# Get function based on key and call it
selected = 2
result = switch_dict.get(selected, lambda: "Invalid option")()
print(result)

# ===============================================
# 📌 3. Using match-case (Python 3.10+ only)
# ===============================================

# ⚠️ This requires Python 3.10 or newer

# Uncomment and run in Python 3.10+
value = "banana"

match value:
    case "apple":
        print("You chose apple")
    case "banana":
        print("You chose banana")
    case "mango":
        print("You chose mango")
    case _:
        print("Invalid choice")

# ===============================================
# 📌 4. Real-Life Example: Calculator Using Dictionary
# ===============================================

def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y if y != 0 else "Cannot divide by zero"

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

op = "*"
a, b = 10, 5

result = operations.get(op, lambda x, y: "Invalid operator")(a, b)
print(f"{a} {op} {b} = {result}")

# ===============================================
# 🧠 Summary
# - ❌ Python has no native switch-case before 3.10
# - ✅ Use if-elif or dictionary mapping
# - ✅ `match-case` is clean and readable (Python 3.10+)
# - ✅ Dictionary mapping is best for fixed options
# - ✅ Use functions for complex logic
# - ✅ Real-life example: calculator using dictionary
# - ✅ Always handle invalid cases gracefully
# - ✅ Use match-case for pattern matching (Python 3.10+)
