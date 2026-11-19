a = int("256")
b = int("256")

print(a==b)
print(a is b)

c = int("257")
d = int("257")
print(c == d)   # true
print(c is d) # false because its outside pre-allocated cached range (-5,256) thats why everytime it create brand new memory

