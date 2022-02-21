def maxSubBrute(elems):
    if len(elems) < 1:
        return None
    lo, hi, max = 0, 0, elems[0]
    for x in range(len(elems)):
        runningSum = 0
        for y in range(x, len(elems)):
            runningSum += elems[y]
            if runningSum > max:
                max = runningSum
                lo = x
                hi = y
    return (lo, hi, max)


test = [-1, 2, -1, 2, 4, 3, -100, 101, -100, 10, 1000, -500, 501, -10000]
test = [-1, -2, -100, 0]
test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubBrute(test))


def maxSubDiv(elems):
    if len(elems) < 1:
        return None
    return dHelper(elems, 0, len(elems) - 1)


def dHelper(elems, lo, hi):
    if lo >= hi:  # base case
        return (lo, hi, elems[lo])
    mid = (lo + hi) // 2
    lol, hil, maxl = dHelper(elems, lo, mid)
    lor, hir, maxr = dHelper(elems, mid+1, hi)
    loc, hic, maxc = crossSum(elems, lo, mid, hi)
    if max(maxl, maxr, maxc) == maxl:
        return (lol, hil, maxl)
    elif max(maxl, maxr, maxc) == maxr:
        return (lor, hir, maxr)
    else:
        return (loc, hic, maxc)


def crossSum(elems, lo, mid, hi):
    iLeft = mid
    maxLeft = elems[iLeft]
    rSum = 0
    for x in range(mid, lo-1, -1):  # [1,2,-1 ...]
        rSum += elems[x]
        if rSum > maxLeft:
            maxLeft = rSum
            iLeft = x

    iRight = mid + 1
    maxRight = elems[iRight]
    rSum = 0
    for x in range(mid+1, hi + 1):
        rSum += elems[x]
        if rSum > maxRight:
            maxRight = rSum
            iRight = x

    return(iLeft, iRight, maxLeft + maxRight)


print(maxSubDiv(test))


def maxSubLin(elems):  # calculate max sub in linear time
    if len(elems) == 0:
        return None

    if not nonNegativeExists(elems):
        return maxNeg(elems)  # return index of biggest neg number
    rSum = 0
    sMax, eMax, max = 0, 0, elems[0]
    sr = 0
    for x in range(len(elems)):
        if rSum + elems[x] < 0:
            rSum = 0
            sr = x+1
        else:
            rSum += elems[x]
            if rSum > max:
                max = rSum
                sMax = sr
                eMax = x
    return sMax, eMax, max


def nonNegativeExists(elems):
    for x in elems:
        if x >= 0:
            return True


def maxNeg(elems):
    max = elems[0]
    s = e = 0
    for x in range(len(elems)):
        if elems[x] > max:
            max = elems[x]
            s = e = x
    return s, e, max


print(maxSubLin(test))
