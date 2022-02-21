class Node:
    def __init__(self, x):
        self.x = x
        self.l = None
        self.r = None


side = Node(5)
side.l = Node(6)
side.r = Node(7)

oside = Node(2)
oside.r = side
oside.l = Node(4)

side = Node(1)
side.l = oside
side.r = Node(3)

root = side


def iT(root):
    if root == None:
        return
    iT(root.l)
    print(root.x)
    iT(root.r)


def iTI(root):
    s = []
    s.append(root)
    while len(s) != 0:
        trav = s[len(s)-1]
        while trav.l != None:
            s.append(trav.l)
            prev = trav
            trav = trav.l
            prev.l = None

        print(s.pop().x)

        if trav.r != None:
            s.append(trav.r)
            trav.r = None


iT(root)
iTI(root)
