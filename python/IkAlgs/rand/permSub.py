# calculate permutation of subsets
def P(n, k):
    if k == 1:
        return n
    return n * (1 + P(n-1, k-1))


# print(P(7, 7))

# print permutations of a string
def PS(s):
    ph(list(s), 0)


def ph(a, k):
    if k == len(a)-1:
        print(a)

    for x in range(k, len(a)):
        a[k], a[x] = a[x], a[k]
        ph(a, k+1)
        a[k], a[x] = a[x], a[k]


PS('abbc')
