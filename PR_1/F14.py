import math

def f(n):
    if n == 0:
        return 7
    elif n == 1:
        return 7
    else:
        return(0.04 * f(n-2)**2 - math.tan(f(n - 1)))

print(f(13))
print(f(16))