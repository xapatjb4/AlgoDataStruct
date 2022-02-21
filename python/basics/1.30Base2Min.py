# Write a Python program that can take
# a positive integer greater than 2 as input and
# write out the number of times one must repeatedly divide this number by 2
# before getting a value less than 2.

# example
# in 2 div once
# in 4 div twice
# in 3 div once

# brute force, do division until number less than 2
# find a power of 2 greater than half the number

# example 2
# 2^0 < 2/2? no
# 2

# O(log(entry))
def numDiv2(entry):
    # positive ints
    if entry < 2:
        return
    x = 0
    # normally div should be increment x while 2**x <= entry/2
    # in order to avoid division, multiply both sides by 2
    # increment x while 2**x+1 <= entry
    while 2**(x+1) <= entry:
        x += 1
    return x


print(numDiv2(1))
print(numDiv2(3))
print(numDiv2(1000))
