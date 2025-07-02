# Logical Operators in Python
# Logical operators are used to combine conditional statements.
a = True
b = False

# Logical AND
print("Logical AND:", a and b)
# Logical OR
print("Logical OR:", a or b)
# Logical NOT
print("Logical NOT:", not a)

#Truth Table for Logical Operators
# AND: True if both operands are true
# OR: True if at least one operand is true
# NOT: Inverts the truth value of the operand

# Example of Logical Operators
x = 10
y = 20
# Using AND operator
if x > 5 and y > 15:
    print("Both conditions are true.")
# Using OR operator
if x < 5 or y > 15:
    print("At least one condition is true.")
# Using NOT operator
if not (x < 5):
    print("x is not less than 5.")
