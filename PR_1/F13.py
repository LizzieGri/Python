

def thrd_mul(n, m):
    s = 0
    for i in range(1, n + 1):
        s += ((i**3) - 77 * (i**8))
    part1 = s / 52
    k = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            k += (j - 95 * (i**3))
    part2 =76 * k
    print(part1 + part2)

thrd_mul(31, 38)
thrd_mul(20, 57)