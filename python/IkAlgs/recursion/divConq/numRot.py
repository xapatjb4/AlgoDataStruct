# This is straight up wroooong
# def numRot(arr):
#   l, r = 0, len(arr) #BUUUUUUUUUUUUG, Wrong bounds for binary search
#   iS = 0
#   while l <=r:
# Bug, because we did not check for sorted subarray, when we would divide the problem in half we woul discard the left subhalf if its already sorted
# but that left subhalf could have contained the solution
#     mid = r - (r-l)//2
#     if arr[mid-1] > nums[mid]: # bug, wrong array name
#       iS = mid
#       break
#     if arr[l] < arr[mid]:
#       l = mid + 1
#     else:
#       r = mid - 1 #bug, misinterpreted going to the left subhalf as going right
#   return (len(arr) - iS) % len(arr)
def numRot(arr):
    l, r = 0, len(arr)-1
    iS = 0
    while l <= r:
        if arr[l] < arr[r]:
            iS = l
            break
        mid = r - (r-l)//2
        if arr[mid-1] > arr[mid]:
            iS = mid
            break
        if arr[l] < arr[mid]:  # Go right subset
            l = mid + 1
        else:  # Go left subset
            r = mid - 1
    return (len(arr) - iS) % len(arr)


print(numRot([8, 9, 10, 2, 5, 6]))
print(numRot([8, 9, 10, 1, 2, 3, 4, 5, 6, 7]))
