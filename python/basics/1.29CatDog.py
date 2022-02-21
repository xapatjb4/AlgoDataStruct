name = 'catdog'
chars = list(name)


def perm(name):
    # move and swap through the array
    # pick index from 0 to end
    # swap with first, call perm

    # swap back and repeat till end
    permHelper(name, [], 0, len(name))


def permHelper(original, soFar, start, end):
    if start == end:
        print(soFar)
        return
    for x in range(start, end):
        original[start], original[x] = original[x], original[start]
        soFar.append(original[start])
        permHelper(original, soFar, start+1, end)
        original[start], original[x] = original[x], original[start]
        soFar.pop()


perm(chars)
