# ===============================================
# 📘 PYTHON TUPLES - FULL MASTER GUIDE
# ===============================================

# ✅ What is a Tuple?
# - Tuple is an ordered, immutable collection.
# - Defined using () or just commas.
# - Faster and safer than lists when you don’t need to change data.

# ===============================================
# 📌 1. Creating Tuples
# ===============================================

empty_tuple = ()
single = ("one",)        # Tuple with one item requires a trailing comma
multi = (10, 20, 30)
mixed = (1, "hello", 3.14)
auto_tuple = 1, 2, 3      # Without parentheses

nested = ((1, 2), (3, 4))

print("Empty:", empty_tuple)
print("Single:", single)
print("Multi:", multi)
print("Mixed:", mixed)
print("Auto Tuple:", auto_tuple)
print("Nested:", nested)

# ===============================================
# 📌 2. Accessing Elements
# ===============================================

print("First:", multi[0])
print("Last:", multi[-1])
print("Slice:", multi[1:3])

# ===============================================
# 📌 3. Immutability
# ===============================================

immutable = (10, 20, 30)
# immutable[1] = 100  ❌ Error: Tuple is immutable

# Modify by converting to list
temp = list(immutable)
temp[1] = 100
immutable = tuple(temp)
print("Modified Tuple:", immutable)

# ===============================================
# 📌 4. Tuple Methods (Only 2)
# ===============================================

t = (1, 2, 3, 1, 4, 1)
print("Count of 1:", t.count(1))    # 3
print("Index of 4:", t.index(4))    # 4

# ===============================================
# 📌 5. Built-in Functions on Tuple
# ===============================================

sample = (5, 2, 9, 1)

print("Length:", len(sample))
print("Max:", max(sample))
print("Min:", min(sample))
print("Sum:", sum(sample))
print("Sorted:", sorted(sample))      # Returns list
print("Any True?:", any(sample))
print("All True?:", all(sample))
print("Type:", type(sample))

# Convert to/from tuple
my_list = [1, 2, 3]
print("To Tuple:", tuple(my_list))
print("From String:", tuple("abc"))   # ('a', 'b', 'c')

# ===============================================
# 📌 6. Looping Through Tuple
# ===============================================

for item in mixed:
    print("Item:", item)

for i, val in enumerate(mixed):
    print(f"Index {i}: {val}")

# ===============================================
# 📌 7. Tuple Packing and Unpacking
# ===============================================

person = ("Aditya", 23, "Engineer")
name, age, job = person
print("Name:", name)
print("Age:", age)
print("Job:", job)

# Unpacking with *
t = (1, 2, 3, 4, 5)
a, *b, c = t
print("a:", a)
print("b (middle):", b)
print("c:", c)

# ===============================================
# 📌 8. Use Cases of Tuple
# ===============================================

# - Returning multiple values
# - Dictionary keys
# - Immutable fixed collections
# - Faster lookup than lists

def get_stats(x, y):
    return (x + y, x * y)

add, product = get_stats(3, 4)
print("Sum:", add, "Product:", product)

# ===============================================
# 🔍 9. Searching in Tuples
# ===============================================

t = (10, 20, 30, 40, 50)
print(20 in t)        # True
print(99 in t)        # False
print(99 not in t)    # True

# All indexes of a value
multi = (1, 2, 3, 1, 4, 1)
target = 1
indexes = [i for i, val in enumerate(multi) if val == target]
print(f"Indexes of {target}:", indexes)

# Sub-tuple search
def contains_subtuple(big, sub):
    for i in range(len(big) - len(sub) + 1):
        if big[i:i+len(sub)] == sub:
            return True
    return False

big_tuple = (1, 2, 3, 4, 5)
sub_tuple = (3, 4)
print("Sub-tuple found?", contains_subtuple(big_tuple, sub_tuple))

# ===============================================
# 🧠 Summary
# - ✅ Tuples are ordered and immutable
# - 🔧 Only methods: count(), index()
# - 🛠 Built-in functions: len(), sum(), max(), min(), sorted(), any(), all()
# - 🎯 Use for fixed collections, function returns, as dictionary keys
# - 🔍 Searching possible with `in`, `index()`, loop, slicing
