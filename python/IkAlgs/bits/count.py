def one_count(x):
    ones = 0
    while x:
        print('b4rs')
        print(x)
        # add to ones if lsb == 1
        if x & 1:
            ones += 1
        x >>= 1
        print('afrs')
        print(x)
    return ones


print('wtf')
print(one_count(2))
print(1 | 2)
print(-16 << 1)
print(~0)
print(15 ^ 15)
print(-1 ^ -5)
