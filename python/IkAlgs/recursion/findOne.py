# def findOnes(arr):
#   first = binsearch(arr)
#   if first != -1:
#     return len(arr) - first
#   else:
#     return 0

# def binsearch(arr): #[1,1] -> 0
#   l = 0
#   r = len(arr)-1
#   while l <= r:
#     mid = (l+r)//2
#     if a[mid] == 1 and (mid = 0 or a[mid-1] == 0): #bug, mid ==0 not mid =0
#       return mid
#     if a[mid] == 0: #bug, arr not a
#       #go right
#       l = mid + 1
#     else:
#       r = mid - 1
#   return -1
def findOnes(arr):
    first = binsearch(arr)
    if first != -1:
        return len(arr) - first
    else:
        return 0


def binsearch(arr):  # [1,1] -> 0
    l = 0
    r = len(arr)-1
    while l <= r:
        mid = (l+r)//2
        if arr[mid] == 1 and (mid == 0 or arr[mid-1] == 0):
            return mid
        if arr[mid] == 0:
            # go right
            l = mid + 1
        else:
            r = mid - 1
    return -1


print(findOnes([0, 0, 0, 0, 1, 1, 1]))
