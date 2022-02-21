# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].

# 0 + 0 = 0
# 0 + 2 = 2
# 2 + 4 = 6
# 6 + 6 = 12
# 12 + 8 = 20

# previous term + 2 * index

# x * 2 for x in range(10)
#

lastRes = 0


def addToLastRes(num):
    global lastRes
    lastRes += num
    return lastRes


def seq():
    return [addToLastRes(x*2) for x in range(10)]


# print(addToLastRes(5))
print(seq())


def fibGen(max):
    #prev + prevprev
    prev = 1
    prevPrev = 1
    yield 1
    yield 1
    # remember to check max

    for x in range(2, max):
        numToYield = prev + prevPrev
        prevPrev = prev
        prev = numToYield
        yield numToYield


print([x for x in fibGen(10)])
