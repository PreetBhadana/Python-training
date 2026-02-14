# Day 1

## Basic Print Types
# Simple string: print("Hello") → Hello
print("Hello")


## F-strings
# String with variables: print(f"{name} is {age} years old.") → John is 30 years old.
name = "John"
age = 30
print(f"{name} is {age} years old.")

# String with expressions: print(f"{2 + 2} is the answer.") → 4 is the answer.
print(f"{2 + 2} is the answer.")

# String with formatted numbers: print(f"{10.5:.2f} is the answer.") → 10.50 is the answer.
print(f"{10.5:.2f} is the answer.")


## Math Operations
# Addition: print(2 + 2) → 4
print(2 + 2)

# Subtraction: print(5 - 3) → 2
print(5 - 3)

# Multiplication: print(4 * 2) → 8
print(4 * 2)

# Division: print(10 / 2) → 5.0
print(10 / 2)

# Integer division: print(10 // 3) → 3
print(10 // 3)

# Modulo: print(10 % 3) → 1
print(10 % 3)

# Exponentiation: print(2 ** 3) → 8
print(2 ** 3)

# Order of operations: print(2 + 3 * 4) → 14
print(2 + 3 * 4)


## User Input
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print(f"{name}, you are {age} years old.")


## Multiple objects: print("Age:", 28, "Name:", "Dev") → Age: 28 Name: Dev (space-separated by default).
print("Age:", 28, "Name:", "Dev")

## Multiple with sep
print("Coords", 12.5, 34.7, sep=": ")
