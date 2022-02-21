
'''
Two array multiplication
[50] [50]
 123
*123
3* 123
20 * 123+
100* 123

incrementally?
1 2 3
  1 5
ans = 5, 4, 8, 1
in = 2
in + carr + ans[dig] = 8
carry = 0
multiply second from end to start with element from first n to start and add

tc = log10(1)*log10(2)
outline:
check is pos or neg ( check if +- or --

set negs to positive
reverse both
for x in range lenB
function which multiplies and array starting at index
mult(sol, A, dig, val[dig])
reverse
set to neg if needed

mult(sol, A, digit, value)
carry = 0
for x in range from start to end A # 521 * 5
  toAdd = A[x] * val + carry
  if dig >= len(sol) add a 0
  toAdd += sol[dig]
  carry = toAdd//10
  sol[dig] = toAdd % 10
  dig+=1
#add the carries if remnat
while carry % 10 != 0 add to sol

test
sol = [51]
A = 321
dig = 2
val = 5

toadd = 25
carry = 1


'''


def multiply(A, B):
    isANeg = isBNeg = False
    if A[0] < 0:
        isANeg = True
        A[0] *= -1
    if B[0] < 0:
        isBNeg = True
        B[0] *= -1
    isNeg = isANeg ^ isBNeg  # bug, should have used is neg

    A.reverse()
    B.reverse()
    sol = []
    for x in range(len(B)):
        mult(sol, A, x, B[x])
    sol.reverse()
    if isNeg:
        sol[0] *= -1

    B.reverse()
    A.reverse()
    if isANeg:
        A[0] *= -1
    if isBNeg:
        B[0] *= -1
    return sol


def mult(sol, A, digit, value):  # .9999 * 9
    carry = 0
    for x in range(len(A)):
        if digit >= len(sol):
            sol.append(0)
        # bug, typo and forgot to put carry
        # bug, index using x instead of digit
        toAdd = A[x] * value + sol[digit] + carry
        carry = toAdd // 10
        sol[digit] = toAdd % 10
        digit += 1
    if carry != 0:
        if digit >= len(sol):  # bug, should have put append 0, then replace with carry
            sol.append(0)
        sol[digit] = carry


print(multiply([1, 9, 3, 7, 0, 7, 7, 2, 1],
      [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]))
'''
sol[19]
A[...9999]
digit = 3
val = 9
toAdd = 89
carry = 8
highest possible mult of 1 dig is 2 digits
modding will give 1 digit carry


'''
