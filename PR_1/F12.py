

def scnd_mul(x):
    if x < 45:
        print(55 * (x**8) + 72 * (x**6) + 42)
    elif 45 <= x < 77:
        print((x**2) - 80 * (x**4))
    elif 77 <= x < 93:
        print(64 * (x - abs(x))**4 - 3 * (x**8))
    else:
        print(95 *(x ** 6) - 11 * (x**3))


scnd_mul(143)
scnd_mul(105)
