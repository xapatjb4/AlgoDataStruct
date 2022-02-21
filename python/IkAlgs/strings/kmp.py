'''
Kmp alg consists of build a lps (longest proper suffix) table
to build the kmp table, you do a two pointer passthrough
one for going through every element in the array, the second pointer for spotting where suffix and prefix match
outline:
for j in range (1,len(elem))
  if a[i] == a[j]
    lps[j] = i + 1
    i+=1
  else lps[j] = i = rec(lps, i, j, a) #recursively find lps that matches a[j]

rec(lps, i, j, a):
  if i <= -1 or a[j] == a[i]:
    return i+1
  return rec(lps,lps[i-1], j, a)

it(lps, i,j,a):
  while i > 0:
    if a[j] == a[i]:
       break
    i = lps[i-1]
  if a[j] == a[i]:
    return i+1
  else:
    return 0

[abcabdab]
 00012012
     i  j
012345678
aabaabaaab
0101234523

Once lps is done building:



'''


def buildlps(A):
    lps = [-1] * len(A)
    lps[0] = 0
    i = 0
    for j in range(1, len(A)):
        if A[i] == A[j]:
            i += 1
            lps[j] = i
        else:
            i = it(lps, lps[j-1], j, A)
            lps[j] = i
    return lps


'''
  i
        j
0123456789
aabaabaaab
0101234520
rec(i = 5,j = 8,)
rec(i = 2, j = 8)
rec(i = 1, j = 8) return 2
'''
# [abcabdab]
#  00012012
#      i  j
# 012345678
# aabaabaaab
# 0101234523


def rec(lps, i, j, A):
    if i <= -1 or A[i] == A[j]:
        return i+1
    return rec(lps, lps[i-1], j, A)


def it(lps, i, j, A):
    while i > 0:
        if A[j] == A[i]:
            break
        i = lps[i-1]
    return i+1 if A[j] == A[i] else 0


def findOcc(s, lps, l):
    # got through s and match with l
    # if they match increment lp
    # else find new lp by looking for next matching prefix, done by lindex = lps[lindex-1 if lindex-1>= 0 else 0]
    # if lp >= len(l) we've found of match, print start index, decrement lp
    # increment sp
    lidx = 0
    print(lps)
    sidx = 0
    while sidx < len(s):
        print("{} {}".format(sidx, lidx))
        if s[sidx] == l[lidx]:
            if lidx >= len(l)-1:  # if its the last element
                print('Match at {}'.format(sidx-len(l) + 1))  # aaab aab
                lidx = lps[lidx]
            else:
                lidx += 1
            sidx += 1
        else:
            if lidx-1 < 0:  # if first elem comparison, increment sidx
                sidx += 1
            else:
                lidx = lps[lidx-1]  # else try the previous prefix

        '''
    '''

    # look for next matching prefix (lps, l, charToMatch, lidex):
    # . return the new lindex
    # if lindex < 0 or l[lindex] == charToMatch:
    #   return lindex + 1
    # return (lps, l, charToMatch, lps[lindex-1])

        pass


lps = buildlps("AABA")

findOcc("AABAACAADAABAABA", lps, "AABA")


# for j in range (1,len(elem))
#   if a[i] == a[j]
#     lps[j] = i + 1
#     i+=1
#   else lps[j] = i = rec(lps, i, j, a) #recursively find lps that matches a[j]

# rec(lps, i, j, a):
#   if i <= -1 or a[j] == a[i]:
#     return i+1
#   return rec(lps,lps[i-1], j, a)

# it(lps, i,j,a):
#   while i > 0:
#     if a[j] == a[i]:
#        break
#     i = lps[i-1]
#   if a[j] == a[i]:
#     return i+1
#   else:
#     return 0
