'''
Problem:
Given a number of stairs
find the ways to climb it using 1,2 or 3 steps

Contraints:
Input
  int representing the number of stairs to climb
Ouput
  int number of ways to climb stairs using 1,2 or 3 steps

Example:
(2) -> 2
1,1
2

(3) ->3 
111
12
21
3 ->3

Ideas:
Reduce and conquer, number of ways to climb with 3 + nwtc2 + nwtc1
3^n tc
n space

We could improve using memoization

Tabulation would improve space complexity

Layout:
Try with 321
Base case is we reach step 0
return 1

Generate possible next steps
For possible next steps add to running sum

return running sum


'''


def numWays(steps):
    return nH(steps, {0: 1})


def nH(step, sols):
    if step in sols:
        return sols[step]
    rsum = 0
    for next in getPosSteps(step):
        rsum += nH(step - next, sols)  # bug, did not include map in dp version
    sols[step] = rsum
    return rsum


def getPosSteps(step):
    steps = []
    for x in range(1, min(step+1, 4)):  # 3 => 1,2,3 | 4 => 1,2,3 | 1 => 1 #bug, missing paran
        steps.append(x)
    return steps


'''
Test
1 1 return 1
(0)

2 => 2
1=> 1 | 0 => 1

3 => 4
2=>2 | 1=>1 | 0 =>1

'''
