# User input
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))  # Convert to int

# Arithmetic
x = 10
y = 3
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y:.1f}")  # 1 decimal

# Comparisons
if user_age >= 18:
    print(f"{user_name}, you're an adult!")
else:
    print(f"{user_name}, keep learning!")


# My Output was -- 
"""
Enter your name: Preet
Enter your age: 29
10 + 3 = 13
10 - 3 = 7
10 * 3 = 30
10 / 3 = 3.3
Preet, you're an adult!
"""