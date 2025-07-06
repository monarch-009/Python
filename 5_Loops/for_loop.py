# ===============================================
# 🔁 PYTHON FOR LOOP - FULL GUIDE
# ===============================================

# ✅ `for` loop is used to iterate over a sequence (list, tuple, string, dict, set)

# ===============================================
# 📌 1. Basic For Loop
# ===============================================

names = ["Aditya", "Esita", "Rahul"]

for name in names:
    print("Name:", name)

# ===============================================
# 📌 2. Looping Through String
# ===============================================

word = "Python"

for char in word:
    print("Char:", char)

# ===============================================
# 📌 3. Looping with `range()`
# ===============================================

# range(start, stop, step)

for i in range(5):  # 0 to 4
    print("i =", i)

for i in range(1, 6):  # 1 to 5
    print("Number:", i)

for i in range(10, 0, -2):  # 10 to 2 (step -2)
    print("Countdown:", i)

# ===============================================
# 📌 4. Using `enumerate()`
# ===============================================

fruits = ["apple", "banana", "mango"]

for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# ===============================================
# 📌 5. Looping Through Tuples
# ===============================================

tup = (10, 20, 30)

for item in tup:
    print("Tuple item:", item)

# ===============================================
# 📌 6. Looping Through Sets
# ===============================================

s = {1, 2, 3, 4}

for value in s:
    print("Set Value:", value)

# ===============================================
# 📌 7. Looping Through Dictionary
# ===============================================

person = {"name": "Aditya", "age": 23, "city": "Delhi"}

for key in person:
    print("Key:", key, "→", person[key])

for key, value in person.items():
    print(f"{key} = {value}")

for value in person.values():
    print("Value:", value)

# ===============================================
# 📌 8. Nested For Loops
# ===============================================

for i in range(1, 4):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("---")

# ===============================================
# 📌 9. Using break, continue, pass
# ===============================================

# break – stop the loop
for i in range(1, 10):
    if i == 5:
        break
    print("Break Loop:", i)

# continue – skip current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print("Continue Loop:", i)

# pass – do nothing (placeholder)
for i in range(3):
    pass  # Used when loop is empty for now

# ===============================================
# 📌 10. Real-Life Examples
# ===============================================

# ✅ Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print("Even:", i)

# ✅ Calculate sum of numbers
total = 0
for num in [10, 20, 30, 40]:
    total += num
print("Total Sum:", total)

# ✅ Character frequency in a word
word = "banana"
freq = {}
for ch in word:
    freq[ch] = freq.get(ch, 0) + 1
print("Char Frequency:", freq)

# ===============================================
# 🧠 Summary
# - 🔁 Use `for` to loop through list, tuple, dict, string, set
# - 🔢 Use `range(start, stop, step)` for numbers
# - 🔍 Use `enumerate()` to get index with value
# - 🧩 Use `break`, `continue`, `pass` for control
# - 💡 Use nested loops for patterns or tables
