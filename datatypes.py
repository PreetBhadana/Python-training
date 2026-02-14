## Numeric Types
age = 28                    # int (unlimited size)
pi = 3.14159               # float (decimals)
comp = 3 + 4j              # complex (real + imaginary)


## Text Type
name = "Developer"         # str (Unicode text)
multi = """Line1
Line2"""                  # Multi-line string


## Sequence Types (Ordered Collections)
fruits = ["apple", "banana"]  # list (mutable/changeable)
coords = (10, 20)            # tuple (immutable/fixed)
nums = range(5)              # range (0,1,2,3,4)


## Mapping Type
person = {"name": "Alex", "age": 28}  # dict (key:value pairs)


## Set Types (Unique Items)
skills = {"Python", "Ruby"}         # set (mutable, no duplicates)
frozen = frozenset(["a", "b"])      # frozenset (immutable)


## Boolean & None
active = True                    # bool (True/False)
status = False
nothing = None                   # NoneType (no value)




# All types demo
print("=== NUMERIC ===")
x = 42; print(f"int: {x}, type: {type(x)}")
y = 3.14; print(f"float: {y}, type: {type(y)}")

print("\n=== TEXT ===")
s = "Hello"; print(f"str: {s}, len: {len(s)}")

print("\n=== SEQUENCES ===")
lst = [1,2,3]; print(f"list: {lst}, type: {type(lst)}")
tpl = (1,2,3); print(f"tuple: {tpl}")
rng = range(3); print(f"range: {list(rng)}")

print("\n=== MAPPING/SET ===")
d = {"a":1}; print(f"dict: {d}")
st = {"x","y"}; print(f"set: {st}")

print("\n=== BOOL/NONE ===")
print(f"bool: {True}, type: {type(True)}")
print(f"None: {None}")


# My Output was -- 
"""
=== NUMERIC ===
int: 42, type: <class 'int'>
float: 3.14, type: <class 'float'>

=== TEXT ===
str: Hello, len: 5

=== SEQUENCES ===
list: [1, 2, 3], type: <class 'list'>
tuple: (1, 2, 3)
range: [0, 1, 2]

=== MAPPING/SET ===
dict: {'a': 1}
set: {'y', 'x'}

=== BOOL/NONE ===
bool: True, type: <class 'bool'>
None: None
"""