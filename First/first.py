#12 - 4 сложения
def f1(x):
    x = x + x + x
    x = x + x
    x = x + x
    return x

#16 - 4 сложения
def f2(x):
    x = x + x
    x = x + x
    x = x + x
    x = x + x
    return x

#15 - 4 сложения 1 минус
def f3(x):
    a = x + x
    a = a + a
    a = a + a
    a = a + a
    x = a - x
    return x

#29 - 6 сложений 1 минус
def f4(x):
    a = x + x
    a = a + a
    a = a + x
    a = a + a + a
    x = a + a - x
    return x

def naive_mul(x, y):
   if y == 0:
       return 0
   r = x
   for i in range(y-1):
       x = x + r
   return x

if __name__ == '__main__':
    print(f1(2))
    print(f3(3))
    print(f4(1))
    print(naive_mul(10, 15))