
# R-1.4 Write a short Python function that takes a positive integer n and returns the sum of the squares of all the positive integers smaller than n.
def sumSquar(num):
    return sum([x*x for x in range(0, num)])


print(sumSquar(4))
