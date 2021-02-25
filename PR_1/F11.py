import math

def frst_mul(x, y, z):
    part1 = (46 * (z**3) + (math.e**y)) / (math.log(abs(x) + (x**8))-37 * (x**6))
    part2 = ((x**5) - math.tan(z) - 4) / ((x**5) - (x**7) + 9)
    part3 = (32 * (z**4) - 43 * (x**3))
    print (part1 + part2 - part3)

frst_mul(80, -73, 76)
frst_mul(96, -58, 65)


