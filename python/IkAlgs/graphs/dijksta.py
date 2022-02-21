'''
The way dijkstra works is by picking the shortest distance node that has not yet been visited
We need a pq (heap) which will track this shortest distances as they are updated

contraint:
Input: 
graph represented by of vetex to neighbors
map of edge to weight
source vertex

Output:
Map of vertex to shortestPath value and parent

Outline
Create vertex map with source key with value 0 none

Add to priority q
Have a set for done elems

for elem in pq
  if elem not in done: add to done else skip
  check graph for elem neighs
  if weight[neighboor] > weight[elem] + w(elem,neighbor):
    update parentMap to new new weight and parent
    add (newWeight, vertex) to pq



'''
import heapq


def spDijkstra(graph, weights, source):
    sol = {}

    for elem in graph:
        sol[elem] = [float("inf"), None]
    sol[source][0] = 0
    pq = []
    done = set()
    pq.append((0, source))

    while pq:
        elem = heapq.heappop(pq)
        vert = elem[1]
        if vert not in done:
            done.add(vert)
            for neighbor in graph[vert]:
                if neighbor not in done:
                    npw = sol[vert][0] + weights[(vert, neighbor)]
                    if sol[neighbor][0] > npw:
                        sol[neighbor][0] = npw
                        sol[neighbor][1] = vert
                        heapq.heappush(pq, (npw, neighbor))

    return sol


graph = {
    0: [1, 7],
    1: [0, 2, 7],
    2: [1, 3, 5, 8],
    3: [2, 4, 5],
    4: [3, 5],
    5: [2, 3, 4, 6],
    6: [5, 7, 8],
    7: [0, 1, 6, 8],
    8: [2, 6, 7],

}

weights = {
    (0, 1): 4,
    (0, 7): 8,
    #
    (1, 0): 4,
    (1, 2): 8,
    (1, 7): 11,
    #
    (2, 1): 8,
    (2, 3): 7,
    (2, 5): 4,
    (2, 8): 2,
    #
    (3, 2): 7,
    (3, 4): 9,
    (3, 5): 14,
    #
    (4, 3): 9,
    (4, 5): 10,
    #
    (5, 2): 4,
    (5, 3): 14,
    (5, 4): 10,
    (5, 6): 2,
    #
    (6, 5): 2,
    (6, 7): 1,
    (6, 8): 6,
    #
    (7, 0): 8,
    (7, 1): 11,
    (7, 6): 1,
    (7, 8): 7,
    #
    (8, 2): 2,
    (8, 6): 6,
    (8, 7): 7,
}

print(spDijkstra(graph, weights, 0))
