def posComb(n, ps):
    if n == 0 and 0 in ps:
        return 1
    else:
        return pch(n, ps)


def pch(n, ps):
    if n == 0:
        return 1
    if n < 0:
        return 0
    pct = 0
    for s in ps:
        pct += pch(n-s, ps)
    return pct


print(posComb(10, {2, 4, 5, 8}))
