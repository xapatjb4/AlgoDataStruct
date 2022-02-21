# Write a short Python function that takes a positive integer n and returns the sum of the squares of all the odd positive integers smaller than n.
def oddSqare(num):
    return(sum(x*x if x % 2 == 1 else 0 for x in range(0, num)))


print(oddSqare(6))

# String
# s[0] = s[-6]
# s[1] = s[-5]
# s[5] = s[-1]
# pattern = index - (String length)
# s[0] = s[0 - 6]
# s[5] = s[5-6] = s[-1]
