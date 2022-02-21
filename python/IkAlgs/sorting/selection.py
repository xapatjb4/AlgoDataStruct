import random

# Selection sort
# Step 1 − Set MIN to location 0
# Step 2 − Search the minimum element in the list
# Step 3 − Swap with value at location MIN
# Step 4 − Increment MIN to point to next element
# Step 5 − Repeat until list is sorted

# O(n) = n**2
# S(n) = n for copy, constant for in place


def selection(elems):
    for x in range(len(elems)):
        minInd = x
        for y in range(x, len(elems)):
            if elems[y] < elems[x]:
                elems[x], elems[y] = elems[y], elems[x]


def selectionNew(elems):
    sorted = elems[:]
    for x in range(len(sorted)):
        minInd = x
        for y in range(x, len(sorted)):
            if sorted[y] < sorted[minInd]:
                minInd = y
        sorted[x], sorted[minInd] = sorted[minInd], sorted[x]
    return sorted


test = [random.randint(0, 10) for x in range(10)]
print(test)
print(selectionNew(test))
print(test)
selection(test)
print(test)
