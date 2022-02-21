'''
turn string rep and return int
constraint
Cannot use int from python lib
input
  strnum: string representing number to convert
output
  num: numerical converstion of string
assuming that all content are nums (no char)
assuming that string will fit in int

example:
[123] -> 123
[-123] -> -123

Idea
check for negative
given a range of indeces from array
from rtl
  get ordinal value of char, subtract ord of 0 # this will give int value
  multiply ordinal value by multiplicant
  multiply multiplicant by 10
mult by -1 if neg
return num

#check for neg
check index 0 for - sign
tc len of string
sc 1
'''


def convertToInt(strnum):
    # preprocessing check for invalid input such as chars, empty array, array with only - sign
    isNeg = strnum[0] == '-'
    start = 0
    end = len(strnum) - 1
    if isNeg:
        start = 1
    mult = 1
    ans = 0
    while start <= end:
        val = ord(strnum[end]) - ord('0')
        ans += val * mult
        mult *= 10
        end -= 1
    if isNeg:
        ans *= -1
    return ans


print(convertToInt('-123'))
'''
-123
isNeg = True
start = 1
end = 1
mult = 100
ans = -123
val = 2

'''
