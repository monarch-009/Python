# ===============================================
# 📘 PYTHON DICTIONARIES - FULL MASTER GUIDE
# ===============================================

# ✅ What is a Dictionary?
# - Unordered, mutable collection of key-value pairs
# - Keys must be unique and immutable
# - Values can be of any type
# - Accessed via keys, not indices
# - Ideal for structured data like JSON, configurations, etc.
# - Syntax: `{"key1": "value1", "key2": "value2"}`
# - Methods: get, keys, values, items, update, pop, copy, setdefault, fromkeys
# - Built-in functions: len(), max(), min(), sorted(), sum(), type()

# ===============================================
# 📌 1. Creating Dictionaries
# ===============================================

# Basic
person = {"name": "Aditya", "age": 23, "is_student": True}
print("Person:", person)

# Using dict()
user = dict(name="Esita", age=21)
print("User:", user)

# Empty dictionary
empty = {}

# From list of tuples
pairs = [("a", 1), ("b", 2)]
d_from_pairs = dict(pairs)
print("From pairs:", d_from_pairs)

# ===============================================
# 📌 2. Accessing Values
# ===============================================

print("Name:", person["name"])
print("Using get():", person.get("email", "Not Found"))

# ===============================================
# 📌 3. Adding / Updating Entries
# ===============================================

person["city"] = "Delhi"
person["age"] = 24  # update existing
person.update({"email": "aditya@example.com", "age": 25})

# setdefault() – only sets if key is missing
person.setdefault("country", "India")

print("After updates:", person)

# ===============================================
# 📌 4. Removing Items
# ===============================================

person.pop("is_student")              # Removes by key
del person["city"]                    # Deletes key
# person.clear()                      # Removes all items

# ===============================================
# 📌 5. Dictionary Methods
# ===============================================

student = {
    "name": "Esita",
    "skills": ["Python", "C++"],
    "age": 21
}

# 🔑 keys()
print("Keys:", student.keys())

# 📦 values()
print("Values:", student.values())

# 🧺 items()
print("Items:", student.items())

# 🆙 update()
student.update({"college": "LPU", "age": 22})

# 🛑 pop() / popitem()
removed = student.pop("skills")
print("Removed:", removed)

# popitem() removes last inserted key-value
last = student.popitem()
print("Last removed:", last)

# 💾 copy()
student_copy = student.copy()
print("Copied:", student_copy)

# 🌱 setdefault()
student.setdefault("gender", "female")
print("With setdefault:", student)

# 📥 fromkeys()
defaults = dict.fromkeys(["name", "city", "age"], "unknown")
print("Fromkeys:", defaults)

# ===============================================
# 📌 6. Looping Through Dictionary
# ===============================================

for key in student:
    print("Key:", key, "→", student[key])

for key, value in student.items():
    print(f"{key}: {value}")

for value in student.values():
    print("Value:", value)

# ===============================================
# 📌 7. Checking Keys
# ===============================================

print("Has key 'age'?", "age" in student)
print("Has key 'email'?", "email" not in student)

# ===============================================
# 📌 8. Nested Dictionary
# ===============================================

employees = {
    "emp1": {"name": "Alice", "role": "Dev"},
    "emp2": {"name": "Bob", "role": "Manager"}
}
print("Employee 1 Name:", employees["emp1"]["name"])

# ===============================================
# 📌 9. Dictionary Comprehension
# ===============================================

squares = {x: x * x for x in range(6)}
print("Squares:", squares)

evens = {x: x for x in range(10) if x % 2 == 0}
print("Even Numbers:", evens)

# Convert list to frequency dict
names = ["aditya", "esita", "aditya", "rahul"]
freq = {name: names.count(name) for name in set(names)}
print("Frequency:", freq)

# ===============================================
# 📌 10. Built-in Functions for Dictionaries
# ===============================================

sample = {"a": 10, "b": 20, "c": 30}

print("Length:", len(sample))               # Total key-value pairs
print("Max key:", max(sample))             # Based on key
print("Min key:", min(sample))
print("Sum of values:", sum(sample.values()))
print("Sorted keys:", sorted(sample))      # Returns sorted list of keys
print("Type:", type(sample))               # <class 'dict'>

# ===============================================
# 📌 11. Real-Life Examples
# ===============================================

# ✅ Count character frequency
text = "banana"
char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1
print("Char Frequency:", char_freq)

# ✅ Group names by starting letter
words = ["apple", "ant", "banana", "bat", "cat"]
grouped = {}
for word in words:
    first = word[0]
    grouped.setdefault(first, []).append(word)
print("Grouped Words:", grouped)

# ===============================================
# 🧠 Summary
# - ✅ Dictionaries = key-value pairs
# - 🔑 Keys must be immutable & unique
# - 🔧 Methods: get, keys, values, items, update, pop, copy, setdefault, fromkeys
# - 🔨 Built-in functions: len(), max(), min(), sorted(), sum(), type()
# - 🎯 Use for structured, searchable, modifiable data
