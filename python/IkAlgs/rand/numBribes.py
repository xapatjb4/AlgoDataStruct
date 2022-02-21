'''
Problem:
q with init pos from 1 to N
Any person can bribe the person in from of them
Each pos can do at most 2 bribes
Determine minimum number of bribes
If anyone bribed more than 2, print "Too chaotic"
Constraints:
Input
  
  array from 1 to N
output:
  print num bribes or too chaotic


Ideas
If a[i] = i + 1
if a[i] > (i+1) + 2 #too chaotic
a[0] > 4
 bribe has occurred
[3,4,2,1,5,6] -. 5 bribes
 0 1 2 3 4
0: possible tiles are 1,2 and 3
1: possible tiles are 1,2,3,4
2: possible tiles are 1,2,3,4,5
3: possible tiles are 1....6
Brute force:
Check that a[i] is in the set of possible entries
if in possible entries, check that a[i]-1 not in  possible entries
[3,4,1,6,5,2,.,.,]
 0 1 2 3 4 5 6 7 8
pe = 278
[3,4,1,6,2,5,7]
 0 1 2 3 4 5 6 7 8
[1,2,3,4,5,6,7]
[3,1,2,4,5,6,7
[3,4,1,2,5,6,7]
pe = 57
bribes = 2 + 2 + 0 + 2
bribes = 6 + 0 = number of spots away from index element-1 = element - 1 - currInd
bribes = number of elements in pe smaller than you
[1,5,3,2,4]
 0 1 2 3 4
1 >  - 3? yes too chaotic

pe ={1,2,3} for a[0] then select and add 4 then 5... up to len(q)
if a[i] no in pe, too much chaos
bribes = number of elements in pe smaller than you

start with a set from 1 up to min(len(q),3)
iterate through elements
if a[i] not in set of possible elemnets print too chaotic
if a[i] is set, count number of elements < a[i] for number of bribes
add up and return

'''


def numBribes(arr):
    nm = set()
    for i in range(1, min(len(arr)+1, 4)):
        nm.add(i)
    bribes = 0
    for x in range(len(arr)):
        if arr[x] not in nm:
            print("Too chaotic")
            return
        nm.remove(arr[x])
        for num in set:
            if num < arr[x]:
                bribes += 1
        if x + 4 <= len(arr):
            nm.add(x+4)
    print(bribes)
