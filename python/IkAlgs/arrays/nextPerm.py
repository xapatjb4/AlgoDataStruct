'''
Write a program that takes as input a permutation and returns the next permutation under dictionary ordering
Assuming elements are distinct
Constraint:
Input
 String representing a permutation

Output
 String representing next permutation

Examples
0,1 -> 1,0 -> empty
23 -> 132 -> 213 -> 231 -> 312 -> 321 -> emtpy
425 -> 452
643 -> dne
546 -> 564 ->645 -
6758 -> 6785 -> 6857 -> 6875 -> 7568 -> 7586 -> 7658 -> 7685
586
812739 -> 

10 .
01 10 .
123 132  213 231 312 321 

4567 -> 4576 -> 576 -> 567
1 decreasing order, return <>
1123456789
123 -> 132
112 -> 121 -> 211 -> 
2131 -> 2311 -> 3112 -> 3121-> 3211
1123 -> 1132 -> 1213
78 -> 87
8 > 7 swap
12435
if you find a number smaller, reverse then swap with successor number
reverse then find next biggest num
What about duplicate numbers?

bf solution, gen all permutations, put them in sorted order, get next element
worst case revers the whole array
O(n) O1

Outline:
from rtl find first instance where A[x-1] < A[x]
reverse array from A[x:]
swap with successor

swap with success(start index)
  find first number greate then num at start index, swap

'''


def nextPerm(A):
    if len(A) >= 2:
        for x in reversed(range(1, len(A))):
            if A[x-1] < A[x]:
                revSub(A, x)
                swapSuc(A, x-1)
                return A
    return []


def revSub(A, x):
    # reverse array from x onward
    # swap up to mid point
    l = x
    r = len(A)-1
    while l < r:
        A[l], A[r] = A[r], A[l]
        l += 1
        r -= 1


def swapSuc(A, x):
    i = x + 1
    while i < len(A) - 1:  # 79
        if A[x] < A[i]:
            break
        i += 1

    A[x], A[i] = A[i], A[x]


print(nextPerm([3, 2, 1]))
