# String Formating
# String formatting is a way to create strings with dynamic content by inserting variables or expressions into a string. In Python, you can use various methods for string formatting, such as f-strings, the format() method, and the % operator.

# 1. Using f-strings (Python 3.6+)
name = "Aditya"
age = 25

print(f"My name is {name} and I am {age} years old.") 

# 2. Using the .format() method
print("My name is {} and I am {} years old.".format(name, age))  

# 3. Using the % operator (old-style formatting - not recommended for new code)
print("My name is %s and I am %d years old." % (name, age))  # Output: My name is Aditya and I am 25 years old. 

# 4. Using str.format() with positional and keyword arguments
print("My name is {0} and I am {1} years old.".format(name, age))  # Using positional arguments
print("My name is {name} and I am {age} years old.".format(name=name, age=age))  # Using keyword arguments

