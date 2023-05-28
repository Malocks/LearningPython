"""
This module is to ask and response
"""

# Create a variable with a string
QUESTION = "Whats your name?: "

# Create a variable with the input function to ask for a name
name = input(QUESTION)
# Concatenation strings using the format method
ANSWER_STR = f"Hello, {name}! Welcome to Learn Python."
# Print the Dialog in the console
print(ANSWER_STR)
