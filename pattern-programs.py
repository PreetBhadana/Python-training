# 1. Right Triangle Stars (Basic Nested Loop)
# Pattern (n=5):

"""
*
**
***
****
*****
"""
 
n = 5
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()  # New line


# My output -- 
"""
* 
** 
*** 
**** 
***** 
"""



# 2. Number Pyramid (Logic + Increment)
# Pattern (n=4):

"""
1
1 2
1 2 3
1 2 3 4
"""

n = 4
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()


# My output -- 
"""
1
1 2
1 2 3
1 2 3 4
"""



# 3. Inverted Right Triangle (Decrement)
# Pattern (n=5):

"""
*****
****
***
**
*
"""

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# My output -- 
"""
*****
****
***
**
*"""


# 4. Inverted Number Pyramid (Decrement + Logic)
# Pattern (n=4):

"""
4 3 2 1
3 2 1
2 1
1
"""

n = 4
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# My output -- 
"""
4 3 2 1
3 2 1
2 1
1
"""



# 5. Diamond Pattern (Logic + Increment/Decrement)
# Pattern (n=5):

"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
"""
n = 5
# Upper half
for i in range(n):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# Lower half
for i in range(n - 1, -1, -1):
    for j in range(n - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()

# My output -- 
"""
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
""" 


# 6. fizbuzz pattern
# Pattern (n=20):

"""
1
2
Fizz
4
Buzz
"""

n = 20
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()

# My output -- 
"""
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz
"""
