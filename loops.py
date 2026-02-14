##For Loop
# Syntax: for item in sequence:
# Iterates over lists, strings, range(), etc.

#Examples
# 1. Basic range (0 to 4)
for i in range(5):
    print(f"Count: {i}")

# 2. List iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# 3. range(start, stop, step)
print("\nEven numbers 0-10:")
for i in range(0, 11, 2):
    print(i)

# 4. Strings
name = "Developer"
for letter in name:
    print(letter)

# 5. With index (enumerate)
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")


# My output -- 
"""
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
I like apple
I like banana
I like cherry

Even numbers 0-10:
0
2
4
6
8
10
D
e
v
e
l
o
p
e
r
0: apple
1: banana
2: cherry
"""


## While Loop
# Syntax: while condition:
# Runs until condition is False.

# Examples
# 1. Basic counter
i = 0
while i < 5:
    print(f"Count: {i}")
    i += 1

# 2. Infinite loop (use break to exit)
while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input == "exit":
        break

# 3. With else
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("Loop finished")

# 4. Counting with while
count = 0
while count < 5:
    print(f"While: {count}")
    count += 1  # Don't forget this!

# 5. User input loop
print("\nType 'quit' to exit:")
while True:
    user = input("Enter word: ")
    if user == "quit":
        break
    print(f"You said: {user}")



# My output -- 
"""
Count: 0
Count: 1
Count: 2
Count: 3
Count: 4
Type 'exit' to quit: hello
Type 'exit' to quit: lkhdjs
Type 'exit' to quit: kjsdfkj
Type 'exit' to quit: quit
Type 'exit' to quit: exit
0
1
2
Loop finished
While: 0
While: 1
While: 2
While: 3
While: 4

Type 'quit' to exit:
Enter word: Preet
You said: Preet
Enter word: yes
You said: yes
Enter word: quit
"""



## Loop Controls
# break: Exits loop
# continue: Skips current iteration
# pass: Placeholder for future code
# else: Runs if no break

# Examples
# 1. break
for i in range(5):
    if i == 3:
        break
    print(i)

# 2. continue
for i in range(5):
    if i == 3:
        continue
    print(i)

# 3. pass
for i in range(5):
    if i == 3:
        pass
    print(i)

# else - runs if no break
for i in range(5):
    print(i)
else:
    print("Loop completed normally!")


# My output -- 
"""
0
1
2
0
1
2
4
0
1
2
3
4
0
1
2
3
4
Loop completed normally!
"""