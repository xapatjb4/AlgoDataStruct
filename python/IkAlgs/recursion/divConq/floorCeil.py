# def fC(arr, target):
# # [1,5,8,10] 6
# #. 0 1 2 3
# #.     l r
# #.     m
# # 6 -> return 5,8
# # 2 -> 1,5
# # 0 -> -1, 1
# # 30 -> 21, -1
# # 5 -> 5,5
#   l=0, r = len(arr) -1 #initialization bug
#   while l <= r:
#     mid = (l+r) //2
#     if arr[mid] == target:
#       l = r = mid
#       break
#     if target > arr[mid]:
#       l = mid +1
#     else:
#       r = mid-1
#   if l >=len(arr):
#     l = -1
#   return r, l #bug, returned indeces instead of values
def fC(arr, target):
    # [1,5,8,10] 6
    # . 0 1 2 3
    # .     l r
    # .     m
    # 6 -> return 5,8
    # 2 -> 1,5
    # 0 -> -1, 1
    # 30 -> 21, -1
    # 5 -> 5,5
    l = 0
    r = len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] == target:
            l = r = mid
            break
        if target > arr[mid]:
            l = mid + 1
        else:
            r = mid-1
    if l >= len(arr):
        l = -1
    else:
        l = arr[l]
    if r >= 0:
        r = arr[r]
    return r, l  # bug, returned indices instead of values


input = [1, 4, 6, 8, 9]
sols = [fC(input, x) for x in range(11)]
print(sols)
