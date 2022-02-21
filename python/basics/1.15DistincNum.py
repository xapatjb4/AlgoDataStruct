# in place in sort then search would give  nlogn (bottle neck being sort)
# Using a set would give N space and O(N)

def isDistinc(nums):
    setOfNums = set()
    for num in nums:
        if num in setOfNums:
            return False
        else:
            setOfNums.add(num)
    return True


print(isDistinc([1, 2, 3, 2]))
print(isDistinc([1, 2, 3, 4]))
