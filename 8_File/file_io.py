# ===============================================
# 📁 PYTHON FILE I/O - FULL GUIDE
# ===============================================

# ✅ File I/O allows you to read from or write to files like .txt, .csv, etc.
# Modes:
# "r" = read, "w" = write, "a" = append, "x" = exclusive create
# "b" = binary mode, "+" = read/write both

# ===============================================
# 📌 1. Open and Read a File
# ===============================================

# Assume "sample.txt" exists with some content
file = open("8_File/sample.txt", "r")  # Open in read mode
content = file.read()           # Read full content
print("File Content:\n", content)
file.close()

# ===============================================
# 📌 2. Read Line by Line
# ===============================================

with open("sample.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

# ===============================================
# 📌 3. Read Specific Number of Characters
# ===============================================

with open("sample.txt", "r") as file:
    part = file.read(10)
    print("First 10 chars:", part)

# ===============================================
# 📌 4. Write to a File (overwrite)
# ===============================================

with open("output.txt", "w") as file:
    file.write("This will overwrite any existing content.\n")
    file.write("Hello Aditya!\n")

# ===============================================
# 📌 5. Append to an Existing File
# ===============================================

with open("output.txt", "a") as file:
    file.write("This line is added at the end.\n")

# ===============================================
# 📌 6. Write a List of Lines
# ===============================================

lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("list_output.txt", "w") as file:
    file.writelines(lines)

# ===============================================
# 📌 7. Read a File into a List of Lines
# ===============================================

with open("list_output.txt", "r") as file:
    all_lines = file.readlines()
    print("Lines as list:", all_lines)

# ===============================================
# 📌 8. Check if File Exists (Before Opening)
# ===============================================

import os

if os.path.exists("sample.txt"):
    print("sample.txt exists.")
else:
    print("File not found!")

# ===============================================
# 📌 9. Rename and Delete Files
# ===============================================

# os.rename("old.txt", "new.txt")
# os.remove("output.txt")

# ===============================================
# 📌 10. File Modes Summary
# ===============================================
# Mode | Description
# -----|-------------
# "r"  | Read (default), error if file not found
# "w"  | Write (create new or overwrite)
# "a"  | Append (create if doesn't exist)
# "x"  | Exclusive creation (error if exists)
# "b"  | Binary (e.g., "rb", "wb")
# "+"  | Read and write both (e.g., "r+", "w+")

# ===============================================
# 📌 11. Real-Life Example: Log User Messages
# ===============================================

def log_message(username, message):
    with open("chat_log.txt", "a") as log:
        log.write(f"{username}: {message}\n")

log_message("Aditya", "Hello, this is my first log entry.")
log_message("Esita", "Hi Aditya, welcome to File I/O!")

# ===============================================
# 📌 12. Reading/Writing CSV (Basic)
# ===============================================

import csv

# Write CSV
data = [["Name", "Age"], ["Aditya", 23], ["Esita", 22]]
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print("CSV Row:", row)

# ===============================================
# ⚠️ Always close file or use `with` (auto-closes)
# ===============================================

# Avoid this:
# file = open("data.txt", "r")
# ... forgot to close
# ✅ Use with:
# with open("data.txt") as file:
#     content = file.read()
