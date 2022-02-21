from collections import deque
edges = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "v"],
    ["w", "v"],
]


def buildAdjList(edges, graph):
    '''
    For every pair, add to graph map
    ie set map[w].append(x) and map[x].append(w)
    initial array if not present in map
    '''
    for edge in edges:
        if not graph.get(edge[0]):
            graph[edge[0]] = []
        if not graph.get(edge[1]):
            graph[edge[1]] = []

        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])


graph = {}
buildAdjList(edges, graph)

'''
Shortest path between two nodes
do a bfs from src and stop when
 destination is reached or no more nodes to be explored
keep track of parent nodes
go from dst to src then reverse order ( or append left)
'''


def shortestPath(graph, src, dst):
    parents = {src: None}
    q = deque()
    q.append(src)

    while q:
        curr = q.popleft()  # w to y
        for neighbor in graph[curr]:
            if neighbor not in parents:
                parents[neighbor] = curr
                q.append(neighbor)
            if neighbor == dst:
                break

    sol = []
    while dst:
        sol.append(dst)
        dst = parents[dst]

    sol.reverse()
    return sol


print(shortestPath(graph, "w", "z"))
'''
curr = x
Deque[v,y]
Parents[w:none, x:w, v:w, y:x]

'''
