import random


class BoolB:
    def __init__(self, key=False, val=0):
        self.key = key
        self.val = val

    def __str__(self):
        return "key" + str(self.key) + " val" + str(self.val)


def partBool(bools):  # [0t,1f,2f,3t]
    ptrue = len(bools)-1
    ppass = ptrue
    while ppass >= 0:
        if bools[ppass].key:
            # swap
            bools[ppass], bools[ptrue] = bools[ptrue], bools[ppass]
            ptrue -= 1
        ppass -= 1


bools = []
for x in range(5):
    bools.append(BoolB(random.choice([True, False]), x))

print([str(b) for b in bools])
partBool(bools)
print([str(b) for b in bools])
