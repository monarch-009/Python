# ===============================================
# 🔁 PYTHON WHILE LOOP - FULL GUIDE
# ===============================================

# ✅ A `while` loop repeats as long as the condition is True.

# ===============================================
# 📌 1. Basic While Loop
# ===============================================

count = 1
while (count <= 5):
    print("Count =", count)
    count += 1

# ===============================================
# 📌 2. While Loop with Condition That Fails
# ===============================================

x = 10
while x < 5:
    print("This won't print because x < 5 is False")

# ===============================================
# 📌 3. Infinite Loop (Be Careful!)
# ===============================================

# ⚠️ Don't run this without a break!
# while True:
#     print("I will run forever")

# ===============================================
# 📌 4. Using break to Exit Loop
# ===============================================

i = 1
while True:
    if i > 5:
        break
    print("i =", i)
    i += 1

# ===============================================
# 📌 5. Using continue to Skip Iteration
# ===============================================

j = 0
while j < 5:
    j += 1
    if j == 3:
        continue  # Skip 3
    print("j =", j)

# ===============================================
# 📌 6. Using else with while
# ===============================================

k = 1
while k <= 3:
    print("k =", k)
    k += 1
else:
    print("Loop finished successfully.")

# ===============================================
# 📌 7. Real-Life Examples
# ===============================================

# ✅ Password check with limited attempts
correct_password = "python123"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered = input("Enter password: ")
    if entered == correct_password:
        print("Access Granted ✅")
        break
    else:
        print("Incorrect password ❌")
        attempts += 1
else:
    print("Too many failed attempts. Access Denied.")

# ✅ Sum of numbers until user enters 0
# total = 0
# while True:
#     num = int(input("Enter number (0 to stop): "))
#     if num == 0:
#         break
#     total += num
# print("Total Sum:", total)

# ===============================================
# 📌 8. Nested While Loops
# ===============================================

i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# ===============================================
# 🧠 Summary
# - 🔁 while loops run as long as the condition is True
# - 🛑 Use `break` to exit early
# - ⏩ Use `continue` to skip one iteration
# - ✅ `else` runs if the loop finishes normally (no `break`)
# - 🔄 Be careful of infinite loops!
