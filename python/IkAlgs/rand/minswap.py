'''
Problem:
Given an array of DISTINCT integers from 1 to len(array) find the minimum number of swap to sort the array

Constraints:
Input: int[] from 1 to len(arr)
Ouput: int # min number of swaps to sort array from 1 to len(arr)

Examples:
[1,3,2]
swap 3 and 2
[1,2,3]
returns 1

[4,2,1,3]
swap 1,4
[1,2,4,3]
swap 4,3
[1,2,3,4]

or
swap 1,3
[4,2,3,1]
swap 1 with 4
[1,2,3,4]

both cases return 2

#ideas
swap elements to proper position as they are found
						[7,1,3,2,4,5,6]
[6,1,3,2,4,5,7]  		[1,7,3,2,4,5,6]			[7,2,3,1,4,5,6] [

[6,1,3,2,4,5,7]1
[5,1,3,2,4,6,7]2
[4,1,3,2,5,6,7]3
[2,1,3,4,5,6,7]4
[1,2,3,4,5,6,7]5

Make this a graph problem with the next step being the possible state when moving one element to the next phase
Check that array is sorted this is super bad

How to prove that swapping it to its proper spot results in minimum number of swaps?
#ideal scenario
a[i] = j and a[j] = i so swap a[j] a[i]

'''
