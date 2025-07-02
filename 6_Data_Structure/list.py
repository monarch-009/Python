# ===============================================
# 📚 LISTS IN PYTHON - Complete Guide
# ===============================================

# ✅ What is a List?
# A list is a collection which is ordered and mutable. It allows duplicate values.

# Creating a list
fruits = ["apple", "banana", "mango", "banana"]
print("Original list:", fruits)

# ===============================================
# 📌 1. Accessing Elements
# ===============================================

print("First element:", fruits[0])     # apple
print("Last element:", fruits[-1])     # banana

# ===============================================
# 📌 2. Modifying Elements
# ===============================================

fruits[1] = "orange"
print("After modification:", fruits)   # ['apple', 'orange', 'mango', 'banana']

# ===============================================
# 📌 3. List Length
# ===============================================

print("Length of list:", len(fruits))  # 4

# ===============================================
# 📌 4. Adding Elements
# ===============================================

# append() → adds at the end
fruits.append("grape")
print("After append:", fruits)

# insert() → adds at specific position
fruits.insert(1, "kiwi")
print("After insert:", fruits)

# extend() → add multiple elements
fruits.extend(["papaya", "cherry"])
print("After extend:", fruits)

# ===============================================
# 📌 5. Removing Elements
# ===============================================

# remove() → removes first occurrence
fruits.remove("banana")
print("After remove:", fruits)

# pop() → removes by index (default last)
last_item = fruits.pop()
print("Popped item:", last_item)
print("After pop:", fruits)

# del → delete by index
del fruits[2]
print("After del:", fruits)

# clear() → empties the list
# fruits.clear()
# print("After clear:", fruits)

# ===============================================
# 📌 6. Searching in List
# ===============================================

print("Is 'apple' in list?", "apple" in fruits)
print("Index of 'kiwi':", fruits.index("kiwi"))
print("Count of 'apple':", fruits.count("apple"))

# ===============================================
# 📌 7. Sorting and Reversing
# ===============================================

numbers = [5, 1, 9, 3]
numbers.sort()
print("Sorted list:", numbers)

numbers.sort(reverse=True)
print("Sorted descending:", numbers)

fruits.reverse()
print("Reversed fruits:", fruits)

# ===============================================
# 📌 8. Copying a List
# ===============================================

copy_list = fruits.copy()
print("Copied list:", copy_list)

# ===============================================
# 📌 9. Looping Through a List
# ===============================================

for fruit in fruits:
    print("Fruit:", fruit)

# With index
for i, val in enumerate(fruits):
    print(f"Index {i}: {val}")

# ===============================================
# 📌 10. List Comprehension
# ===============================================

squares = [x ** 2 for x in range(5)]
print("Squares:", squares)

even = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", even)

# ===============================================
# 📌 11. Nested Lists
# ===============================================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print("Matrix:", matrix)
print("Element at row 2, col 1:", matrix[1][0])  # 3

# ===============================================
# 🧠 Summary
# - Lists are ordered, mutable, and allow duplicates.
# - Use [] to define a list.
# - Supports many built-in methods like append, remove, sort, etc.
# - Use list comprehensions for efficient one-line processing.

