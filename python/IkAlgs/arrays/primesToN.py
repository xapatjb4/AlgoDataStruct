'''
Write a program that takes in integer argument and returns all the primes between 1 and that integer

Constraint
Input: an int representing prime up to
Output: An array with all the primes up to that number (assuming inclusive)

Example:
5 => 2,3,5
18 => 2,3,5,7,11,13,17

Ideas
Build primes up to 2 then 3 then 4, up to n
primes up to 5 = primes up to 4 + maybe 5
if 5 divisible by any primes up to 4, its not a prime, else it is a prime

recursive approach
if n <= 2 return 2
else for elem in list, mod cur numb, if any have a remainder of 0, don't add to list and return list
tc exponential, because the higher you get, the more number you have to try

Outline
Check that number > 1
if not return empty list
helper func(primes,num)
  if num = 2 add to list and return
  for prime in list, mod and if any = 0, break and return
  add num to list

Could have used sieving for faster time complexity
Makes its so you check off multiples of primes from list of possible solutions
Results in a time complecity of (n/2 + n/3 + n/5...) = nloglogn
 
'''


def primesTo(n):
    ans = []
    if n > 1:
        pH(ans, n)
    return ans


def pH(ans, n):
    if n == 2:
        ans.append(n)
        return
    pH(ans, n-1)
    for prime in ans:
        if n % prime == 0:
            return
    ans.append(n)

# Stack overflow for n = 1000


print(primesTo(18))
'''
ans = [2,3,5]

'''
