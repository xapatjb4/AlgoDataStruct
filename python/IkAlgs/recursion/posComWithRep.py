# def printCombos(nums, k):
#   pch(nums, 0, k, []) #bug, did not check for duplicate elements in set

# def pch(nums, i, k, slt):
#   if len(slt) == k:
#     print("".join(str(e) for e in slt))
# .   #bug, did not return after print string
#   for x in range(i, len(nums)):
#     slt.append(nums[x])
#     pch(nums, x, k, slt)
#     slt.pop()
def printCombos(nums, k):
    pch(nums, 0, k, [])


def pch(nums, i, k, slt):
    if len(slt) == k:
        print("".join(str(e) for e in slt))
        return
    for x in range(i, len(nums)):
        slt.append(nums[x])
        pch(nums, x, k, slt)
        slt.pop()


printCombos([1, 2, 1], 2)
