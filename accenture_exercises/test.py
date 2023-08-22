def decorator(func):
    def pro(*a, **k):
        val = func(*a, **k)
        return val
    
    return pro

@decorator
def num(x, y):
    return x+y

x, y = 5, 2
print(num(x, y))


print("    aaaa    ".lstrip())