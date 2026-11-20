x = 10          # x is pointing to an int
x = "hello"     # now pointing to a str; types belong to objects, not variables variables are label bro
print(type(x))  # <class 'str'>

# Modern Python: type hints (for documentation + tools, not enforced at runtime)
def greet(name: str, times: int = 1) -> str:
    return (f"Hello {name}! " * times).strip()

print(greet("Danuj", 3))
