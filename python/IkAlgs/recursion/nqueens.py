# code generated through text edit
# def nq(n):
#   qs = [0] * n
#   return qsh(qs,0)

# def qsh(qs, n):
#   if n == len(qs):
#     return 1
#   #generate possible moves at row n
#   pm = genMoves(qs,n)
#   for mo in pm:
#     qs[n] = mo
#     nw+=qsh(qs,n+1)
#   return nw

# def genMoves(qs,n):
#   pm = set()
#   for x in range(len(qs):
#     pm.add(x)
#   for x in range(n):
#     if qs[x] in pm:
#       pm.remove(qs[x])
#   for colpm in pm: #bug, cannot modify a set while iterating through elements
#     for row in range(n):
#       if abs(qs[row]-colpm) == abs(row-n):
#         pm.remove(colpm) #bug, did not break after finding a diagonal issue( occurs when a pos is diag to more than one elem)
#   return pm
def nq(n):
    qs = [0] * n
    return qsh(qs, 0)


def qsh(qs, n):
    if n == len(qs):
        return 1
    # generate possible moves at row n
    pm = genMoves(qs, n)
    nw = 0
    for mo in pm:
        qs[n] = mo
        nw += qsh(qs, n+1)
    return nw


def genMoves(qs, n):
    pm = set()
    for x in range(len(qs)):
        pm.add(x)
    for x in range(n):
        if qs[x] in pm:
            pm.remove(qs[x])
    cpm = pm.copy()
    for colpm in cpm:
        for row in range(n):
            if abs(qs[row]-colpm) == abs(row-n):
                pm.remove(colpm)
                break
    return pm


print(nq(8))
