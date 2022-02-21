def gcd(a, b):
    if b == 1:
        return 1
    if a % b == 0:
        return b
    return gcd(b, a % b)


print(gcd(500, 35))
