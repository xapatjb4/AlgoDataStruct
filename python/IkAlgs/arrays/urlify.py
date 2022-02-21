'''
URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith"
'''
'''
Example:
"hey my name "
"hey%20my%20name%20"
Can it end with spaces? assume yes

ideas:
Naive
"hey%2Fmy name"
everytime we encounter a space, starting with last char, move all chars right 2 spaces
Sc 1
Tc len(string) * len(string) O(n^2) where n = len(string)

dividing string len by 3 give number of chars
"hey%2fmy%2fname"
"hey my name       "
|
"hey_my_ _ _ _ _name%2f"
       lc   eos
"hey my

count number of spaces to last char, multiplying by 2
count number of spaces after last. subtract^  then div by 3 will give remnant spaces after last char
from rtl
set remnant spaces to %2f

have to pointers - one for eos and other for curChar
when curChar point to non-space, swap curchar for eos
when curchar points to space, replace 3 spaces with %2f

O(n) linear, constant space
Outline:
lnc = get index of last nonspace char
nsbl = count spaces up to lnc
nsal = len(n) - lnc + 1 "a a_ _"
rs = (nsal - 2*nsbl) // 3

fill with %2f from eos rs times
while lnc >=0:
  if char swap with eos and decrement both
  if space add %2f, decrement eos by 3

TC O(N) where N = len(string)
  
'''


def urlify(url):  # "hey_my_name_ __ __ __"
    lnc = getLastNonSpace(url)
    if lnc < 0:  # no nonspace chars
        # change all spaces to %2f
        x = len(url)-1
        while x >= 0:
            x = addSpace(url, x)  # "_ _ _
        return url
    nsbl = getSpacesTLC(url, lnc)
    nsal = len(url) - lnc + 1  # a _ _ ->  3 -0 + 1 = 2
    rs = (nsal - 2*nsbl) // 3
    eos = len(url) - 1
    for x in range(rs):
        eos = addSpace(url, eos)
    while lnc >= 0:
        if url[lnc] != " ":
            url[lnc], url[eos] = url[eos], url[lnc]  # a
            eos -= 1
        else:
            eos = addSpace(url, eos)
        lnc -= 1
    return url


def getLastNonSpace(url):
    x = len(url)-1
    while x >= 0 and url[x] == " ":
        x -= 1
    return x


def addSpace(url, x):  # return new index after adding space
    url[x] = "f"
    url[x-1] = "2"
    url[x-2] = "%"
    return x - 3


def getSpacesTLC(url, x):
    ans = 0
    for i in range(x):
        if url[i] == " ":
            ans += 1
    return ans


print(urlify(list("hey my name          ")))
