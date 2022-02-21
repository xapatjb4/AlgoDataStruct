from collections import deque


class Node:
    def __init__(self, x):
        self.x = x
        self.neighbors = []


z = Node("z")
a = Node("a")
z.neighbors.append(a)
a.neighbors.append(z)
s = Node("s")
s.neighbors.append(a)
a.neighbors.append(s)
x = Node("x")
x.neighbors.append(s)
s.neighbors.append(x)
d = Node("d")
c = Node("c")
x.neighbors.append(d)
d.neighbors.append(x)
x.neighbors.append(c)
c.neighbors.append(x)

c.neighbors.append(d)
d.neighbors.append(c)

f = Node("f")
f.neighbors.append(d)
d.neighbors.append(f)

c.neighbors.append(f)
f.neighbors.append(c)

v = Node("v")
v.neighbors.append(c)
c.neighbors.append(v)

v.neighbors.append(f)
f.neighbors.append(v)


def dfs(node):
    visited = {node}
    parents = {node.x: None}
    dq = deque()
    dq.append(node)
    nn = 1
    lvl = 0
    lvlm = {}
    while dq:
        if nn == 0:
            nn = len(dq)
            lvl += 1
        curr = dq.popleft()
        if lvlm.get(lvl):
            lvlm[lvl].append(curr.x)
        else:
            lvlm[lvl] = [curr.x]

        for n in curr.neighbors:
            if n not in visited:
                dq.append(n)
                visited.add(n)
                parents[n.x] = curr.x
        nn -= 1
    print(parents)
    print(lvlm)


dfs(s)
