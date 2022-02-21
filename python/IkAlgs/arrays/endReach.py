'''
Problem
Given an array of ints denoting the max number of steps that can taken from curr index, return if it is possible to advace to the last index from start of array

Contrainst:
Input
  array ints rep max steps from index: A

Ouput
  boolean for if we can move from A[0] to end of A: isWinnable

Idea:
Create a graph and perform a dfs from start to end
Create graph Potentially huge if num step is big, for each position every position after is accessible,
TC O(N^2)
DFS O(


Greedy dfs
No graph creation
DFS(N
all possible step from 0, from V+E


Outline:

take in int array
return greedybfs(array, 0)

greedybfs(array, pos)
  if pos is eos return true
  generate possible steps
  for possible step, if one returns true return true
  else return false

possibleStep(array, pos)
  add to pos + i for i in a[pos]
'''


def advancePossible(A):
    return DFS(A, 0)


def DFS(A, pos):
    if pos == len(A) - 1:
        return True
    nextMoves = genNext(A, pos)
    for move in nextMoves:
        if DFS(A, move):
            return True
    return False


def genNext(A, pos):  # 0 [3,0,1,1]
    next = []
    cap = min(pos+1+A[pos], len(A))
    for i in reversed(range(pos+1, cap)):  # reversed not reverse
        next.append(i)
    return next


print(advancePossible([3, 3, 1, 0, 2, 0, 1]))
print(advancePossible([3, 2, 0, 0, 2, 0, 1]))
'''
pos = 0
cap = 4 or 4/
next = range(1,4 -> 1,2,3
'''
'''
There is a linear time solution to this problem
 by computing the max distance a every index, if we get to a point wher max distance >= eos, we found a sol
 else if we get to a point where max distance < index we're iterating through, it's impossible to reach end
 this gives a linear time solution ( instead of graph time solution above)
 Outline:
 for i in iteration(arr)
  if i > maxsofar, return false
  if maxsofar >= len(arr) -1 return True

  maxsofar = max(maxsofar, ar[i] +i) # [2,3,4,0,0,0,0,1], i = 7, maxsofar = 6
'''


def isReachLin(A):
    maxsf = 0
    i = 0
    while i < len(A):  # [1,2,1,0,0] maxsf = 3, i = 4, len(A)-1 = 4
        maxsf = max(maxsf, A[i] + i)
        i += 1
        if maxsf >= len(A) - 1:
            return True
        if maxsf < i:
            return False


print(isReachLin([3, 3, 1, 0, 2, 0, 1]))
print(isReachLin([3, 2, 0, 0, 2, 0, 1]))
