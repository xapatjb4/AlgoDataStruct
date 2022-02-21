def minMax(nums):
    if len(nums) == 0:
        print('Data source empty')
        return
    min, max = nums[0], nums[0]
    for num in nums:
        if min > num:
            min = num
        if max < num:
            max = num
    return (min, max)


print(minMax([1, 2, 3, 4, 10, 6, 7, 8]))
print(minMax([]))
