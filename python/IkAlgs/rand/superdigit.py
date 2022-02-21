'''
We define super digit of an integer  using the following rules:

Given an integer, we need to find the super digit of the integer.

If  has only  digit, then its super digit is .
Otherwise, the super digit of  is equal to the super digit of the sum of the digits of .
For example, the super digit of  will be calculated as:

	super_digit(9875)   	9+8+7+5 = 29
	super_digit(29) 	2 + 9 = 11
	super_digit(11)		1 + 1 = 2
	super_digit(2)		= 2

Constraints:
  Input:
    n String rep of a number
    k number of times to concat string to itself
  Output:
    p Superdigit (int)

Ideas
Build a string with repetition amount (may not be needed)
do superdigit with that string then mult by k

recursively split to last digit, add return to self, return self
if final call > 9
restart with final call

'''

from collections import deque


def superDigit(n, k):  # 9875
    ans = shs(n, [])
    lastCall *= k
    lcs = str(lastCall)
    while len(lcs) > 1:
        lcs = shi(lcs)
    return lastCall


def sH(n, i):
    if i == len(n):
        return 0
    return int(n[i]) + sH(n, i+1)


'''
9 + sH(1)
    8 +		sh(2)
		7 +
'''


def shs(n, i, q):
    # mod 10 to get the first digit
    if i >= len(n):
        return
    if q[0] + n[i] > 9:
        # update q0 to unit digit of sum, append 1 to left of q
        q[0] = q[0] + n[i] % 10
        q.appendleft(1)
    else:
        q[0] += n[i]
    shs(n, i-1, q)


'''
Idea
Use a string and append to it when leading digit gets past 9

Outline
for all digits starting at last index of string
if number bigger than 9: update stack to unit, append 10s digit
else update stack to sum

reverse and that should be new string to get

Perform same op with mult
'''


def superDigit(n, k):  # 9875
    nums = [int(e) for e in n]
    ans = [0]
    sdh(nums, ans, len(n) - 1)
    mult(ans, k)
    while len(ans) > 1:
        nums = ans.copy()
        ans = []
        sdh(nums, ans, len(nums) - 1)
    return ans[0]


def sdh(n, ans, i):
    if i <= -1:
        ans.reverse()
        return
    ns = ans[-1] + n[i]
    if ns < 10:
        ans[-1] = ns
    else:
        ans[-1] = ns % 10
        ans.append(ns//10)
    sdh(n, ans, i-1)


def mult(ans, k, i):
    # multiply first digit by k
    # 999 * 9
    # 1 17 9
    # recursive carry op
    if ans[i] * k > 9:
        carry(ans, i)
    else:
        ans[i] *= k
    mult(ans, k, i-1)


'''

99*9
81 + 810
1 8+1 = 9 8

'''
