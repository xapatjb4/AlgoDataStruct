'''
Generate all top sort of a graph
Usa khans algo to generate the in and out degrees
First pass through will go iterate through each node
  if node not in map, add and set in to 0
  go through each element and increment in degrees of neighbors (set to 1 if neigh not in map)


Permute array of 0s
'''
from collections import deque
graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2]
}

indeg = {}
for elem in graph:
    indeg[elem] = 0

for node in graph:
    for neigbhor in graph[node]:
        indeg[neigbhor] += 1
q = []
for node in indeg:
    if indeg[node] == 0:
        q.append(node)

print(indeg)


def perm(q, slate, graph, indeg):
    if not q:
        print(slate)
        return

    for x in range(len(q)):
        # swap with the last element copy, then pop from list
        q[-1], q[x] = q[x], q[-1]
        slate.append(q.pop())
        # decrease in degree of neighbors of removed node
        for neighbor in graph[slate[-1]]:
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                q.append(neighbor)

        perm(q, slate, graph, indeg)
        # undo everything for next group
        for neighbor in graph[slate[-1]]:
            if indeg[neighbor] == 0:
                q.pop()
            indeg[neighbor] += 1
        q.append(slate.pop())
        q[-1], q[x] = q[x], q[-1]


perm(q, [], graph, indeg)
