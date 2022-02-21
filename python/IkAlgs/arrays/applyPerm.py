def appPerm(A, P):
    newArr = [None] * len(P)
    for x in range(len(P)):
        newArr[P[x]] = A[x]
    # Bug, array should be modified. Ended up changing copy of reference instead of original reference
    A = newArr
    return A
