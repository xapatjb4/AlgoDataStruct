'''
Write a program which takes as input an array of digits encoding a nonnegatvie decimal inter D and updates the array to represent the interger d+1
Example
9 should update array to 10

Constaints:
Input:
  array of ints representing positive number 
Oupter
  update array to rep pos num + 1

Are all integers less than 10? assumes yes
Is this array 0 padded? assume no

idea:
add one to last element. If > 10, proceed repeat for next elem.
If at last element, insert at start of array

outline:
Recursively 2 base cases
num at curr ind + 1 < 10 or
if we've reached start of array

set pos call to 0, call with ind - 1

Iterative
for x from end to -1:
  if sum[x]> 10 set to 0
  
if x <

Approach 2
from rtl, Find the first element that's not a 9, update all prev and curr to 0, update curr+1 to A[curr+1] + 1

Edge case where all elements are 9, we need to append left 1

outline:
It
for x from end to -1
  if A[x] != 9, increment by one, break
  else set to 0, decrement x

if x <= -1:
  append left 1

'''


def add1(num):
    x = len(num) - 1
    while x >= 0:
        if num[x] != 9:
            num[x] += 1
            break
        else:
            num[x] = 0
            x -= 1
    if x <= -1:  # improvement, set num[0 to 1] and append a 0
        # num.insert(0, 1) original
        num[0] = 1
        num.append(0)


'''
[1000]
x =-1
'''

num = [8, 9, 9, 9]
add1(num)
print(num)
