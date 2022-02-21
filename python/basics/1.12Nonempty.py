# Python’s random module includes a function choice(data) that returns a random element from a non-empty sequence.
# The random module includes a more basic function randrange, with parameterization similar to the built-in range function, that return a random choice from the given range.
# Using only the randrange function, implement your own version of the choice function.

# non empty seq (check for list size)
# use rand range for index

import random


def choice(elems):
    # check for empty list
    if len(elems) == 0:
        return None
    # return rand element from list
    return elems[random.randrange(0, len(elems))]


elems = [1, 2, 4, 6, 3]
print(choice(elems))

# memory not an issue, start from end of array to 0 and copy elems
# memory and issue, swap start with end until start == end
