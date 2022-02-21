class Node:
    def __init__(self, key):
        self.key = key
        self.l = None
        self.r = None

    def insert(self, node):
        root = self
        while True:
            if node.key < root.key:
                if root.left != None:
                    root = root.left
                else:
                    root.left = node
                    break

            else:
                if root.right != None:
                    root = root.right
                else:
                    root.right = node
                    break


def pI(node):
    if node == None:
        return
    pI(node.l)
    print(node.key)
    pI(node.r)


def fS(root, sk):
    node = root
    ll = None
    while node != None:
        if node.key == sk:
            break
        if sk < node.key:
            ll = node
            node = node.l
        else:
            node = node.r

    if node == None:
        return None

    succ = None
    if node.r != None:
        node = node.r
        while node.l != None:
            node = node.l
        succ = node
    else:
        succ = ll
    return succ


node = Node(3)
node.l = Node(2)
oN = Node(5)
oN.l = node
node = Node(7)
node.l = Node(6)
oN.r = node
pI(oN)
print(fS(oN, 6).key)
