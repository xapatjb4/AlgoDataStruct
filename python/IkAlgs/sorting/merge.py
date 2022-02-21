import random


def mergeSort(elems):
    mergeHelper(elems, 0, len(elems) - 1)


def mergeHelper(elems, start, end):
    if start >= end:
        return

    mid = (start + end) // 2
    mergeHelper(elems, start, mid)
    mergeHelper(elems, mid + 1, end)
    merge(elems, start, mid, end)


def merge(elems, start, mid, end):
    aux = []
    l, r = start, mid + 1
    while l <= mid and r <= end:
        if elems[l] <= elems[r]:
            aux.append(elems[l])
            l += 1
        else:
            aux.append(elems[r])
            r += 1
    while l <= mid:
        aux.append(elems[l])
        l += 1

    while r <= end:
        aux.append(elems[r])
        r += 1

    for x in range(len(aux)):
        elems[x+start] = aux[x]


# test = [random.randint(0, 9) for x in range(10)]
# print(test)
# mergeSort(test)
# print(test)


def mergeOneParam(elems):
    if len(elems) > 1:
        # mid
        mid = len(elems) // 2

        # copy left
        l = elems[:mid]

        # copy right
        r = elems[mid:]

        mergeOneParam(l)
        mergeOneParam(r)

        li = ri = ei = 0

        while li < len(l) and ri < len(r):
            if l[li] <= r[ri]:
                elems[ei] = l[li]
                li += 1
            else:
                elems[ei] = r[ri]
                ri += 1
            ei += 1

        while li < len(l):
            elems[ei] = l[li]
            li += 1
            ei += 1

        while ri < len(r):
            elems[ei] = r[ri]
            ri += 1
            ei += 1


# test = [random.randint(0, 9) for x in range(10)]
# print(test)
# mergeOneParam(test)
# print(test)


def mergeBottomUp(A):
    subsize = 1
    while subsize < len(A):
        x = 0
        while x < len(A):
            print('in merge portion')
            print(x)
            start = x
            mid = x+subsize - 1

            if mid >= len(A) - 1:
                print('mid is past or at end of array')
                break
            end = start + 2 * subsize - 1
            if end >= len(A):
                end = len(A) - 1
            merge(A, start, mid, end)
            x = end + 1
        subsize *= 2


print('merge bottom up')

test = [random.randint(0, 9) for x in range(10)]
print(test)
mergeBottomUp(test)
print(test)
