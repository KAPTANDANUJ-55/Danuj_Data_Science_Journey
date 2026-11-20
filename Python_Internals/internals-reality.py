# int: arbitrary precision (never overflows!)
print(2 ** 200)

# float: C's double (IEEE 754, 64-bit)
print(0.1 + 0.2)           # 0.30000000000000004
print(round(0.1 + 0.2, 2)) # 0.3

# str: immutable Unicode sequence
s = "Danuj"
# s[0] = "d"  → TypeError, strings cannot be modified
s2 = s.lower()             # creates a new string object

# bool: is a subclass of int!
print(True + True)         # 2
print(isinstance(True, int))  # True

# None: singleton object (only one instance exists in the entire program)
print(None is None)        # True
print(None==None) # Never Do That Blud
