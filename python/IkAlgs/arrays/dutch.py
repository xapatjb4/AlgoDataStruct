'''
Write a program that takes an array A and an index i intoA, and rearranges such that A becomes [ ...(less), k,k,(more)...]
outline
3 pointer, one to track nums bigger and k,one for bigger, one for passthrough
smaller, bigger, pass
while pass <= bigger
  if A[pass] == pivot, inc pass
  else if A[pass] < pivot swap A[smaller] with A[pass], increment smaller, inc pass #[1 1 3 2 2
  else swap A[pass] A[big], decrement big
#[1 1 2 2 3]
      s b 
        p
#[1 1 2 2 1]
      s  b 
    p
'''

# bugs, pass is a keyword, and elif instead of else if
# bug, when writing pseudocode, though I had dec written down, I incremented, could have been avoided by test


def DNC(A, x):
    pivot = A[x]
    small, pas, big = 0, 0, len(A)-1
    while pas <= big:  # [1 1 2 2 1]
        if A[pas] == pivot:
            pas += 1
        elif A[pas] < pivot:
            A[small], A[pas] = A[pas], A[small]
            small += 1
            pas += 1
        else:
            A[big], A[pas] = A[pas], A[big]
            big -= 1


A = [2, 1, 2, 3, 1, 1, 1, 3, 2, 2, 3, 1, 2]
DNC(A, 0)
print(A)
