'''
Delete dups from sorted array
when encouter dups
[1,1,1,3,3,4]
[1,3,4,0,0,0]
valid = 2
i = 5

O, return num valid, vend-1

Outline
iterate through array
  if prev elem == cur elem set to 0 continue iteration
  else if prev elem != cur elem, swap with validend, increment both
return validend -1


'''


def remDup(A):
    if len(A) == 0:
        return 0
    vEnd = 1
    prev = A[0]
    for x in range(1, len(A)):  # Bug, remember that last number is exclusive
        if A[x] == prev:
            A[x] = 0
        else:
            A[vEnd], A[x] = A[x], A[vEnd]
            prev = A[vEnd]
            vEnd += 1
    return vEnd


A = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print(remDup(A))
print(A)
'''
1 3 4 0 0 0
vEnd = 3
prev = 4
x = 5
prev == 1?
return
'''
