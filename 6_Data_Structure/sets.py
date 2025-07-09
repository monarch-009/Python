# ===============================================
# 📘 PYTHON SETS - FULL MASTER GUIDE
# ===============================================

# ✅ What is a Set?
# - A set is an unordered, mutable collection of **unique** elements.
# - It does not allow duplicates.
# - No indexing, slicing, or duplicate elements.
# - Ideal for membership testing, removing duplicates, and mathematical operations like union, intersection, etc.
# - Syntax: `{1, 2, 3}` or `set([1, 2, 3])`
# - Methods: add, update, remove, discard, pop, clear, copy
# - Built-in functions: len(), max(), min(), sum(), sorted(), any(), all(), type() 


# ===============================================
# 📌 1. Creating Sets
# ===============================================

fruits = {"apple", "banana", "mango"}
print("Fruits:", fruits)

# Using set() constructor
numbers = set([1, 2, 2, 3, 4])
print("Unique Numbers:", numbers)

# Mixed data types
mixed = {1, "hello", 3.14}
print("Mixed Set:", mixed)

# Empty set (⚠️ {} creates empty dict)
empty = set()

# From string
chars = set("hello")
print("Unique characters:", chars)

# ===============================================
# 📌 2. Accessing Elements
# ===============================================

# ❌ No indexing
# print(fruits[0]) → Error

# ✅ Looping
for fruit in fruits:
    print("Fruit:", fruit)

# ===============================================
# 📌 3. Adding and Removing Items
# ===============================================

s = {1, 2, 3}
s.add(4)                     # Add one item
s.update([5, 6])             # Add multiple items

s.remove(2)                  # Remove item (Error if not found)
s.discard(10)                # Remove safely (No error if not found)

print("Set after add/remove:", s)

# pop() – removes a random item
removed = s.pop()
print("Popped:", removed)

# clear() – removes everything
copy_s = s.copy()
copy_s.clear()
print("Cleared copy:", copy_s)

# ===============================================
# 📌 4. Set Operations
# ===============================================

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)
print("Intersection:", a & b)
print("Difference (a - b):", a - b)
print("Symmetric Difference:", a ^ b)

# Using methods
print("Union (method):", a.union(b))
print("Intersection (method):", a.intersection(b))
print("Difference (method):", a.difference(b))
print("Symmetric Diff (method):", a.symmetric_difference(b))

# ===============================================
# 📌 5. Set Comparisons
# ===============================================

x = {1, 2}
y = {1, 2, 3, 4}

print("Subset:", x.issubset(y))
print("Superset:", y.issuperset(x))
print("Disjoint:", x.isdisjoint({5, 6}))

# ===============================================
# 📌 6. Set Methods (Full List)
# ===============================================

methods_demo = {10, 20, 30}

methods_demo.add(40)
methods_demo.update([50, 60])
methods_demo.remove(30)
methods_demo.discard(100)       # Safe remove
copy_set = methods_demo.copy()
methods_demo.pop()              # Removes any item
methods_demo.clear()            # Empties set

# Note: All changes are in-place

# ===============================================
# 📌 7. Built-in Functions on Sets
# ===============================================

nums = {10, 20, 30, 40}

print("Length:", len(nums))
print("Max:", max(nums))
print("Min:", min(nums))
print("Sum:", sum(nums))
print("Sorted List:", sorted(nums))
print("Any True?:", any(nums))
print("All True?:", all(nums))
print("Type:", type(nums))

# ===============================================
# 📌 8. Set Comprehension
# ===============================================

# Square of numbers
squares = {x*x for x in range(6)}
print("Squares Set:", squares)

# Vowels from a string
sentence = "this is python"
vowels = {char for char in sentence if char in "aeiou"}
print("Vowels in sentence:", vowels)

# ===============================================
# 📌 9. Real-Life Examples
# ===============================================

# ✅ Remove duplicates from a list
data = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(data))
print("Unique List:", unique)

# ✅ Common attendees
event1 = {"aditya", "esita", "rahul"}
event2 = {"esita", "rahul", "riya"}

common = event1.intersection(event2)
print("Attended both events:", common)

# ✅ Words with no vowels
words = {"sky", "dry", "apple", "try"}
no_vowels = {w for w in words if all(ch not in "aeiou" for ch in w)}
print("No vowel words:", no_vowels)

# ===============================================
# 📌 10. Frozen Sets (Immutable Sets)
# ===============================================

fs = frozenset([1, 2, 3])
print("Frozen Set:", fs)

# fs.add(4) ❌ Error: frozensets are immutable

# Can be used as keys in dictionary or inside other sets
fs_dict = {fs: "immutable set"}
print("Dictionary with frozenset:", fs_dict)

# ===============================================
# 🧠 Summary
# - ✅ Set = unordered, mutable, no duplicates
# - 🔧 Methods: add, update, remove, discard, pop, clear, copy
# - 🔨 Built-in functions: len(), max(), min(), sum(), sorted(), any(), all()
# - 🔁 Use set operations for union, intersection, difference, etc.
# - ❄️ Use frozenset for immutable sets (e.g., as dict keys)
