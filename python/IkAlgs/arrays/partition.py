def partition(A, x):
    pivot = A[x]
    A[-1], A[x] = A[x], A[-1]
    ps = 0
    pe = len(A)-2
    while ps <= pe:
        if A[ps] <= pivot:
            ps += 1
        else:
            A[ps], A[pe] = A[pe], A[ps]
            pe -= 1
    A[-1], A[ps] = A[ps], A[-1]


A = [2, 1, 3, 5]
partition(A, 3)
print(A)
