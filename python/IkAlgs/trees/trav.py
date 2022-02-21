class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return self.val


'''
dfs trav
              a
            /   \
          b      c
         / \     \
        d  e      f

out abdecf

rec

if none return

else
append self
work with left
work with right
'''


def dfs(root, trav):
    if not root:
        return
    trav.append(root)
    if root.left:
        dfs(root.left, trav)
    if root.right:
        dfs(root.right, trav)


def dfs_i(root, trav):
    if not root:
        return trav
    stack = [root]
    while stack:
        node = stack.pop()
        trav.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


b = Node("b")
b.left = Node("d")
b.right = Node("e")
c = Node("c")
c.right = Node("f")
a = Node("a")
a.left = b
a.right = c
sol = []
dfs(a, sol)
sol_i = []
dfs_i(a, sol_i)
print(sol)
print(sol_i)
