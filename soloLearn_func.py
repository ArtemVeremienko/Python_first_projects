def apply_twice(func, arg):
    return func(func(arg))

#print(apply_twice(add_five, 10))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))
