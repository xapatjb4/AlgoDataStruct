

'''
    Given the sorted rotated array nums of unique elements, return the minimum element of this array
Constraint:
input
  A: array of unique int rotated 0 to N time
output
  mini: smalled value in A

Example:
[2,3,1] min is 1, 
[3412] min is 1

bf, look through array for min
optimized
binary search
[2341]
[23 41]
231
s e
[1,2,3,4,5]

if l and r are sorted, go left X
if l is smaller and right is smaller, min found
if r is bigger
check the ends of the array
l < r then array is sorted, return l
if l > r, go to mid

if mid to end is sorted and mid -1 > mid (or out of bounds), return as smallest
else reduce problem to unsorted side

if mid -1 > mid return mid
divide to left of right
if mid to end sorted, go left
else go right
[8945]
1234

Outline
checks#empty
if one element array, return element
init start and end
while start <= end
  if mid -1 < 0 check mid + 1 for validating mid smaller
  if mid -1 > mid return mid
  if mid to end sorted set end to mid -1
  else set start to mid + 1

  
'''


def minRot(A):
    if len(A) == 1:
        return A[0]
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start+end)//2
        if mid - 1 < 0:
            if A[mid] < A[mid+1]:
                return A[mid]
        else:
            if A[mid-1] > A[mid]:
                return A[mid]
        if A[mid] < A[end]:  # if its sorted go left
            end = mid - 1
        else:
            start = mid + 1


'''
[2341]
start = 1
end = 1
mid = 0


'''
