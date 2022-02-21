'''
Write a program that takes an array A of n numbers, and rearranges A's elemts go et a new arry B having the property that B[0] <= B[1] >= B[2] <= B[3] ...

Example
1,2,3 -> 1,3,2
3
Constraints
input Given an array A, create a new array b with flip flop above

Examples
1234
3214

1<4>2<3
3<4>1<2
2<3>1<4


With a sorted array, switch from r and left and fill new array
nlgn tc

2<=3

outline
copy array
sort copy
append to new array l then r till left > right

This assumes that there's a possible solution, if there isn't we could do a check to return that arr is imposible


'''


def flipFlop(A):
    B = A.copy()
    B.sort()
    l = 0
    r = len(B)-1
    ans = []
    x = 0
    while x <= (len(B) - 1) // 2:  # 12345 #bug, math error
        ans.append(B[x])
        end = len(B) - 1 - x
        if end != x:
            ans.append(B[end])
        x += 1
    # we could have a check for validity
    return ans


print(flipFlop([2, 1, 3, 4, 5]))
'''
x = 2 #stop at x = 3
end = 2
ans = 1,5,2,4,3

'''
