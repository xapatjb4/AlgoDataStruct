# Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.

# what creates odd product
# e * e ? = e X
# o * o ? = o Y
# e* o = e X
# are there two odd numbers in the list?

# O(n)
def oddProdPoss(nums):
    numOdds = 0

    for num in nums:
        if num % 2 == 1:  # check that number odd
            numOdds += 1
        if numOdds == 2:  # 2 odds indicates possible odd product
            return True
    return False

# longer approach would have been to multiply each element and determine if product odd
# would be O(n^2)
