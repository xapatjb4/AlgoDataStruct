def part4(A):
    s, e = part(A, 0, len(A)-1)
    part(A, s, e)


def part(A, s, e):  # bug, forgot a comma
    g1, g1i = A[s], s+1
    g2, g2i = None, e  # we want to discover second group
    other = s+1

    while other <= g2i:
        if A[other] == g1:
            A[g1i], A[other] = A[other], A[g1i]
            g1i += 1
            other += 1
        else:
            if g2 == None:
                g2 = A[other]
            if A[other] == g2:
                A[g2i], A[other] = A[other], A[g2i]
                g2i -= 1
            else:
                other += 1
    return g1i, g2i


A = [2, 1, 3, 4, 2, 1, 3, 4, 2, 3, 2, 3, 4]
part4(A)
print(A)
