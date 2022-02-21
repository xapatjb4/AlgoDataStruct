'''
Problem
Write a program that takes an array denoting the daily stock price, and returns the maximum profit that could be made by bying and then selling one share of that stock. return 0 if no profit is possible

Constraints
Input
array of integers denoting stock price, index representing day
Output int representing max profit (0 if not possible)

Examples
[1,2,5,4,2] -> 4 (5 - 1)
[2,3,2,1,4,2,10] -> 9 (10-1)

Looking for greatest peak from ltr
when you find a number <= to peak your looking at, update max peak


Ideas

Bf, calculate every possible combination of nums tc = O(n^2) sc const

div and conquer:
find peak across mid (look for min on left and max on right, find peak at left and right, return tc O(nlogn) sc (log n) for call stack

linear:
set a lowest point (update when you find a lower point)
keep track of max height from lowest point, update global max if bigger
bottom = 1
maxprof = 9
return max prof if > 10

Outline solution
#assuming stock prices are non negative ints
pick first number from array
set maxprofit to 0
from 1 to eos
 if bottom > value at array update bottom
 else calculate profit, update maxprofit if bigger

Code
'''


def maxProfit(A):
    if len(A) < 2:
        return 0
    bottom = A[0]
    maxprofit = 0
    for x in range(1, len(A)):
        if A[x] < bottom:
            bottom = A[x]
        else:
            maxprofit = max(A[x] - bottom, maxprofit)
    return maxprofit


print(maxProfit([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

'''
[2,3,2,1,4,2,10] -> 9 (10-1)
 0 1 2 3 4 5 6 
bottom = 1
mp = 3
x = 5
'''
