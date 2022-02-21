'''
Top sort only works when there are no cycles
One way to do top sort is to perform a dfs and adding node to aux stack after all children are explored


'''
graph = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [0, 2]
}

aux = []
parents = {}


def dfs(node, graph, aux, parents, parent):
    if node in parents:
        return
    parents[node] = parent
    for neighbor in graph[node]:
        dfs(neighbor, graph, aux, parents, node)
    aux.append(node)


for node in graph:
    dfs(node, graph, aux, parents, None)

for x in range(len(aux)):
    print(aux.pop())
