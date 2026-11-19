# int x = 10
# C/Java me int x = 10; ka matlab hai “x naam ka memory box, usme 10”. Python me aisa nahi hai.
# in python 10 is object x is just name (label)

import sys

a = 10
b = a  # no new object same object gets another label means 10 has label a at first now label is b


print(id(a),id(b))
print(id(a)==id(b))
print(sys.getrefcount(a))

a = a+1
print(a,b)