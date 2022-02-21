import random


def insertionSort(A):
    if len(A) <= 0:
        return
    for x in range(1, len(A)):
        key = A[x]
        while x > 0 and A[x-1] > key:
            A[x] = A[x-1]
            x -= 1
        A[x] = key


for x in range(1000):
    test = [random.randint(0, 9) for x in range(random.randint(0, 10))]
    print(test)
    insertionSort(test)

    isSorted = all(test[i] <= test[i+1] for i in range(len(test)-1))
    print(test)
    if not isSorted:
        print('is not sorted')
        break
