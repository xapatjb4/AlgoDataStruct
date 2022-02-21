# def sol(n):
#   ma = [[] for _ in range n + 1]
#   solh(n, ma, [], 0)
#   gen(ma)

# def solh(n, ma, sla, su):
#   if n == 0:
#     map[su].append("".join(sla))
#   sla.append("0")
#   sol(n-1, ma, sla, su)
#   sla.pop()
#   sla.append("1")
#   sol(n-1, ma, sla, su+1)
#   sla.pop()

# def gen(ma):
#   for key in ma:
#     arr = ma[key]
#     for co in arr:
#       for co2 in arr:
#         print(co + co2)

# Submitted to https://write.geeksforgeeks.org/improve-post/3126123/

def findAllSequences(n):
    # list of strings where index represents sum
    sumToString = [[] for x in range(n+1)]
    generateSequencesWithSum(n, sumToString, [], 0)
    permuteSequences(sumToString)


def generateSequencesWithSum(n, sumToString, sequence, sumSoFar):
    # Base case, if there are no more binary digits to include
    if n == 0:
        # add permutation to list of sequences with sum corresponding to index
        sumToString[sumSoFar].append("".join(sequence))
        return
    # Generate sequence +0
    sequence.append("0")
    generateSequencesWithSum(n-1, sumToString, sequence, sumSoFar)
    sequence.pop()
    # Generate sequence +1
    sequence.append("1")
    generateSequencesWithSum(n-1, sumToString, sequence, sumSoFar+1)
    sequence.pop()


def permuteSequences(sumToString):
    # There are 2^n substring in this list of lists
    for sumIndexArr in sumToString:
        # Append
        for sequence1 in sumIndexArr:
            for sequence2 in sumIndexArr:
                print(sequence1 + sequence2)


findAllSequences(2)
