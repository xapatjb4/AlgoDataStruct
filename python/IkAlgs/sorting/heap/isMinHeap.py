import heap
import random


def isMinHeap(A):
    return isMinH(A, 0)


def isMinH(A, x):  # [5, 10, 4]
    if left(x) < len(A) and isMinH(A, left(x)):
        if A[x] <= A[left(x)]:
            pass
        else:
            return False

    if right(x) < len(A) and isMinH(A, right(x)):
        if A[x] <= A[right(x)]:
            pass
        else:
            return False
    return True


def left(x):
    return 2*x + 1


def right(x):
    return 2*x + 2


test = [1, 2, 3, 4, 5, 6, 7]
test = [0, 1, 10, 5, 6, 11, 12, 3, 4, 7, 8]
test = [0, 1, 10, 2, 6, 11, 12, 3, 4, 7, 8]
test = [1, 2, 0]
# heapStruct = heap.Heap(test)
print('from is min heap')
print(test)
print(isMinHeap(test))
