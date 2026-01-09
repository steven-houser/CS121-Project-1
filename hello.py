# Steven Houser
# Lab 1 - Linux, Vim, and Git
# 01/09/26

# Get the user's name
name = input("What is your name? ")

# Handle empty input so the program still prints a friendly message
if name == "":
    print("I didn't catch your name, so I'll just call you friend.")
    name = "friend"

# Greet the user with their name
print(f"Hello, {name}! Welcome to CS 121!")
