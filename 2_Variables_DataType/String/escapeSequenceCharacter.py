# Escape Sequence Characters in Python
# Escape sequences are special characters that allow you to include characters in a string that would otherwise be difficult or impossible to include directly. They are used to represent characters like newlines, tabs, quotes, and backslashes.

# Here are some common escape sequences in Python:

escape_sequences = {
    "\\n": "Newline (Line Break)",
    "\\t": "Tab",
    "\\'": "Single Quote",
    '\\"': "Double Quote",
    "\\\\": "Backslash",
    "\\r": "Carriage Return",
    "\\b": "Backspace",
    "\\f": "Form Feed"
}   

# Example usage of escape sequences
example_string = "Hello,\nWorld!\tThis is a string with escape sequences.\nHere are some examples:\n"

for seq, description in escape_sequences.items():
    example_string += f"{seq}: {description}\n"
print(example_string)