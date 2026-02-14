# Lists (like JS arrays)
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # First item
fruits.append("date")
print(fruits)     # Whole list

# For loop
print("--- Fruits ---")
for fruit in fruits:
    print(f"- {fruit}")

# Range loop (0 to 4)
print("--- Numbers 0-4 ---")
for i in range(5):
    print(i * 2)


# My Output was -- 
"""
['apple', 'banana', 'cherry', 'date']
--- Fruits ---
- apple
- banana
- cherry
- date
--- Numbers 0-4 ---
0
2
4
6
8
"""