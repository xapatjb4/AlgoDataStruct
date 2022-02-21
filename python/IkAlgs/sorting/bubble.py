import random
# Bubble the lighter elements to the front of the array


def bubblesort(elems):
    # from left to right
    # if left > right swap
    # check until at start of array
    # ex 3 4 2
    # is 4 > 2 ? swap resulting in 324
    # is 3 > 2 ? swap 234
    # start again up to before last elem
    for x in range(len(elems)):
        for y in range(len(elems)-1, x-1, -1):
            if elems[y-1] > elems[y]:
                elems[y-1], elems[y] = elems[y], elems[y-1]


test = [random.randint(0, 10) for x in range(10)]
print(test)
bubblesort(test)
print(test)
