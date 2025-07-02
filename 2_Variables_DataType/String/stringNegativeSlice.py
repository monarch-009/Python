# Negative Slicing in Python allows you to access parts of a string using negative indices, which count from the end of the string. Here's how it works:
name = "Aditya Singh"

# Negative slicing allows you to access characters from the end of the string.
print(name[-1])  # Output: h (last character)
print(name[-2])  # Output: g (second last character)
print(name[-6:-1])  # Output: Sing (from index -6 to -1, excluding the last character)
print(name[-6:])  # Output: Singh (from index -6 to the end