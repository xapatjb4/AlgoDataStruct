def canSum(nums, target):
    c_sum = [False] * (target + 1)  # logic error, parenthesis around + 1

    # setup bool array
    for num in nums:
        if num <= target:
            c_sum[num] = True
    for val in range(1, target+1):  # syntax bug, no colon
        if not c_sum[val]:
            for num in nums:
                if val - num > 0 and c_sum[val-num]:
                    c_sum[val] = True
                    break
    return c_sum[target]


vals = [13, 17]
print(canSum(vals, 100))
