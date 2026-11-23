# Creating a tuple (ordered, immutable collection)
point = (10, 20)
single = (5,)        # ⚠️ A trailing comma is mandatory for a single-element tuple!
not_tuple = (5)      # This is just an integer (5), not a tuple
empty = ()           # Empty tuple

# Indexing & Slicing (works just like lists)
print(point[0])      # 10
print(point[-1])     # 20 -> negative indexing works too
print(point[::-1])   # (20, 10) -> returns a new reversed tuple

# Immutability (cannot be changed after creation)
# point[0] = 99      # ❌ TypeError: 'tuple' object does not support item assignment

# Tuple unpacking (very useful for assigning multiple variables at once)
x, y = point
print(x, y)          # 10 20

# Extended unpacking with * (grabs remaining items as a list)
numbers = (1, 2, 3, 4, 5,7,8)
*x, y, z = numbers
print(x)         # 1
print(y)        # [2, 3, 4]
print(z)          # 5

# Pythonic way to swap variables (uses tuple packing/unpacking under the hood)
a, b = 1, 2
a, b = b, a          # No temporary variable needed
print(a, b)          # 2 1

# Tuple concatenation & repetition (creates a new tuple)
t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)       # (1, 2, 3, 4)
print(t1 * 3)        # (1, 2, 1, 2, 1, 2)

# Built-in tuple methods (only 2 exist because tuples are immutable)
sample = (10, 20, 10, 30)
print(sample.count(10))  # 2 -> counts occurrences of 10
print(sample.index(20))  # 1 -> returns the first index of 20
print(len(sample))       # 4 -> total number of elements

# Membership check -> O(n)
print(20 in sample)      # True

# ⚠️ Interview Trap: Mutable elements inside an immutable tuple
tricky = (1, [2, 3])
# tricky[1] = [4, 5]     # ❌ TypeError (cannot replace the list itself)
tricky[1].append(4)      # ✅ Allowed! The list inside can still be modified
print(tricky)            # (1, [2, 3, 4])

# Using tuples as dictionary keys (lists cannot do this because they are unhashable)
locations = {
    (28.61, 77.20): "New Delhi",
    (19.07, 72.87): "Mumbai"
}
print(locations[(28.61, 77.20)])  # New Delhi
