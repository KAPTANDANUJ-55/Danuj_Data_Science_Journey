data = [4, 8, 15, 16, 23, 42]

if (n := len(data)) > 5:     # assign + use ek saath
    print(f"Bada data: {n} items")

i = 0
while i < len(data):
    if data[i] % 2 != 0:
        i += 1
        continue             # odd skip
    print(data[i], end=" ")
    i += 1