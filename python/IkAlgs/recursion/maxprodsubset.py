# def maxSubset(nums):
#   #check list greater than 1
#   if len(nums)<2:
#     raise Exception()
#   max = [[nums[0]*[nums[1]] # bug, extra []
#   msh(nums, max, 1, [], 0)
#   return max[0]

# def msh(nums, max, cp, slt, lvl) # bug no :
#   if len(nums) == lvl:
#     if len(slt) !=0:
#       if cp > max[0]:
#         max[0] = cp
#     return
#   #include
#   slt.append(nums[lvl])
#   msh(nums, max, cp*nums[lvl], slt, lvl+1)
#   slt.pop()
#   #exclude
#   msh(nums, max, cp, slt, lvl+1)
# this was the naive approach, just because you can, doensn't mean you should
def maxSubset(nums):
    # check list greater than 1
    if len(nums) < 2:
        raise Exception()
    max = [nums[0]*nums[1]]
    msh(nums, max, 1, [], 0)
    return max[0]


def msh(nums, max, cp, slt, lvl):
    if len(nums) == lvl:
        if len(slt) != 0:
            if cp > max[0]:
                max[0] = cp
        return
    # include
    slt.append(nums[lvl])
    msh(nums, max, cp*nums[lvl], slt, lvl+1)
    slt.pop()
    # exclude
    msh(nums, max, cp, slt, lvl+1)


print(maxSubset([4, -8, 0, 8]))
print(maxSubset([-6, 4, -5, 8, -10, 0, 8]))
