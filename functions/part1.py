def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(type(greet))                       # <class 'function'>
print(greet.__name__)                    # greet
print(greet.__defaults__)                # ('Hello',)
print(greet.__code__.co_varnames)        # ('name', 'greeting')
print(greet.__code__.co_argcount)        # 2

say = greet                              # naya label, same function object
print(say("Danuj"))                      # Hello, Danuj!

def apply(func, value):                  # higher-order function
    return func(value)

print(apply(len, "Python"))              # 6