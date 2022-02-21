'''
Weighted shortest path
This is a graph where edges have a weight associated with them
When representing a weighted graph, one may use tuples which contain connecting vertex and weight
Assuming a dag
You can perform a topological sort
perform edge relaxations for source
This assumes one graph where all vertices are connected
'''


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


graph = {
    "r": [Edge("s", 5), Edge("t", 3)],
    "s": [Edge("t", 2), Edge("x", 6)],
    "t": [Edge("x", 7), Edge("y", 4)],
    "x": [Edge("y", -1), Edge("z", 1)],
    "y": [Edge("z", -2)],
    "z": [],
}


def ts(graph):
    # perform dfs and add to aux stack when exiting call stack
    ans = []
    parents = {}
    for elem in graph:
        dfs(graph, elem, parents, None, ans)
    ans.reverse()
    return ans


def dfs(graph, node, parents, parent, ans):
    if node in parents:
        return
    parents[node] = parent
    for neighbor in graph[node]:
        dfs(graph, neighbor.vertex, parents, node, ans)
    ans.append(node)


def edgeRelax(tsa, source, graph):
    path = {}
    for elem in tsa:
        # Contains shortest path length and parent
        path[elem] = Edge(None, None)

    sInd = 0
    while tsa[sInd] != source:
        sInd += 1

    # anything up to source is None
    # starting at source
    # set source to 0
    path[tsa[sInd]].weight = 0
    for i in range(sInd, len(tsa)):
        for neigh in graph[tsa[i]]:
            # current weight + edge weight
            upPath = path[tsa[i]].weight + neigh.weight
            # The node is supposed to update child
            # a would update b to path[a] + weight(a,b) if < path[b]
            # same for all other neighbors
            # go to next elem in tsa
            if path[neigh.vertex].weight == None or path[neigh.vertex].weight > upPath:
                path[neigh.vertex].weight = upPath
                path[neigh.vertex].vertex = tsa[i]
            # example
            #  3
            # a -* b
            #  1   *
            # \* c | 2
            #{a:0, b:None, c:None}

    for elem in path:
        print(str(elem) + ": " +
              str(path[elem].vertex) + " " + str(path[elem].weight))


topSort = ts(graph)
print(topSort)
edgeRelax(topSort, 's', graph)
