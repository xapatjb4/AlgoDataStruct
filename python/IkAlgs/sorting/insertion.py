import random
# insertion sort top down


def insertionSortTop(elems):
    insertionSortTopHelper(elems, len(elems)-1)


def insertionSortTopHelper(elems, end):
    if end <= 0:
        return
    insertionSortTopHelper(elems, end-1)

    valEnd = elems[end]
    while end-1 >= 0 and elems[end-1] > valEnd:
        elems[end] = elems[end-1]
        end -= 1
    elems[end] = valEnd
    return


# test = [random.randint(0, 9) for x in range(10)]
# print(test)
# insertionSortTop(test)
# print(test)


def insertionBottom(elems):
    if len(elems) <= 1:
        return

    for end in range(1, len(elems)):
        valEnd = elems[end]
        while end - 1 >= 0 and elems[end-1] > valEnd:
            elems[end] = elems[end-1]
            end -= 1
        elems[end] = valEnd


test = [random.randint(0, 9) for x in range(10)]
print(test)
insertionBottom(test)
print(test)
