# Numeric types
age = 28                    # int (whole numbers)
height = 5.9                # float (decimals)
complex_num = 3 + 4j        # complex

# Text
name = "Developer"          # str (single/double quotes)
greeting = 'Hi!'            # str (both quotes work)

# Collections
fruits = ["apple", "banana"] # list (mutable, ordered)
point = (10, 20)            # tuple (immutable, ordered)
person = {"name": "Alex", "age": 28}  # dict (key-value)
skills = {"Python", "Ruby"} # set (unique, unordered)

# Logic
is_ready = True             # bool
nothing = None              # NoneType

# Check types
print(type(age))      # <class 'int'>
print(type(name))     # <class 'str'>
print(type(fruits))   # <class 'list'>

# Dynamic typing example
x = 10         # int
x = "ten"      # now str (Python adapts)
print(x, type(x))


# My Output was -- 
"""
<class 'int'>
<class 'str'>
<class 'list'>
ten <class 'str'>
"""