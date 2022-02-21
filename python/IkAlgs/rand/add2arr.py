def add2Arr(arr1, arr2):
    shortArr = longArr = []
    if len(arr1) < len(arr2):
        shortArr = arr1
        longArr = arr2
    else:
        shortArr = arr2
        longArr = arr1
    ans = []
    for x in range(len(longArr)):
        sum = longArr[x]
        if x < len(shortArr):
            sum += shortArr[x]
        if sum > 9:
            splitSum(ans, sum)
        else:
            ans.append(sum)
    return ans


def splitSum(arr, sum):
    lst = []
    while sum > 0:
        lst.append(sum % 10)
        sum = sum // 10
    for x in range(len(lst)-1, -1, -1):
        arr.append(lst[x])


print(add2Arr([23, 5, 2, 7, 87], [4, 67, 2, 8]))
