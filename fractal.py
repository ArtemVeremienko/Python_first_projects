def fractal(x):
    if x == 1:
        return x
    else:
        return x * fractal(x - 1)

print( fractal(50) )
