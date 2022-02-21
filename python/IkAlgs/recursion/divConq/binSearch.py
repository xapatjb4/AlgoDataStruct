def binSRec(nums, tar):
    bH(nums, 0, len(nums)-1, tar)


def bH(nums, sta, end, tar):  # [2,3] t 3
    if sta > end:
        return -1
    mid = (sta + end) // 2
    if nums[mid] == tar:
        print(mid)
        return mid
    if nums[mid] < tar:
        return bH(nums, mid+1, end, tar)
    else:
        return bH(nums, sta, mid-1, tar)


vals = [1, 2, 3, 5, 6, 8]
target = -1
binSRec(vals, target)


def binSIt(nums, tar):  # [2,3] t 3
    l = 0
    r = len(nums)-1
    while l <= r:  # 0 1
        mid = (l+r)//2  # 0
        if nums[mid] == tar:  # no
            print(mid)
            return mid
        if nums[mid] < tar:
            l = mid+1
        else:
            r = mid-1
    return -1


binSIt(vals, target)
