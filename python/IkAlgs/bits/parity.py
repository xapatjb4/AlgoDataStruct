'''
Parity is 1 if 1s are odd, else 0
How would you compute the parity of a very large number of 64-bit words
Create a table of all possilbe 64 bit ints, map to 0 or 1
2^64 entries
2^64 space
O(N) where n = number of numbers
1101
To reduce the number of entries just store odd or even entries up to 64 bits
this would reduce to 2^63 entries
Constraints:
input list of 64 bit ints

list of parities where index corresponds to input list index entry

outline:
generate all possible 64 bit ints
add to map if num 1s odd

lookup number, if in map, parity is 1, else parity is 1
'''


def genParity(nums):
    paritySet = genParityNums()  # generates all par numbs
    sol = []
    for num in nums:
        if num in paritySet:
            sol.append(1)
        else:
            sol.append(0)
    return sol


def genParityNums():
    parSet = set()
    gH(0, parSet, 0, False)


def gH(bit, parSet, num, isOdd):
    print('in gen call {}'.format(bit))
    if bit >= 64:
        if isOdd:  # isOdd
            parSet.add(num)
            print(parSet)
        return
    # leave as is
    gH(bit+1, parSet, num, isOdd)
    # set bit position to 1
    numW1 = (1 << bit) | num
    gH(bit+1, parSet, numW1, not isOdd)  # bug, use not (don't use "!")


'''
test
parset = 
 (0,0, False)
(1,0, False)	(1,1, True)
		(2,1,True)	(2,3,False)

'''
genParity([1, 2, 3])
