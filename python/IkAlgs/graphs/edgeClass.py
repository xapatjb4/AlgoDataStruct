'''
Edge classification
back edge: occurs when traversing and we encounter a node with no end time
forward edge: occurs when traversing and we encounter a node with end time, and encounteredNode.startTime > currentNode.startime
cross edge: occurs when encounter a node with endtime, and encounteredNode.startTime < currentNode.startTime

perform dfs and keep track of start and end (using a map)
check for edge classificaiton along the way

Dfs
if an edge has a start time, it has been visited
how to increment step?
when node called recursively
when node exits
'''

graph = {
    'a': ['f', 'b'],
    'b': ['c'],
    'c': ['e'],
    'd': ['b', 'e'],
    'e': [],
    'f': ['g'],
    'g': ['h', 'l'],
    'h': ['i', 'k', 'f'],
    'i': ['d', 'j'],
    'j': [],
    'k': ['m', 'l'],
    'l': [],
    'm': ['i']
}


def edgeClass(graph):
    start = {}
    end = {}
    step = [0]
    back = set()
    forward = set()
    cross = set()

    dfs(graph, 'a', start, end, step, back, forward, cross)
    print(start, end)
    print('back', back, 'forward ', forward, 'cross', cross)


def dfs(graph, v, start, end, step, back, forward, cross):
    # base case all edges have been classified
    step[0] += 1
    start[v] = step[0]
    for neighbor in graph[v]:
        if neighbor in start:
            # figure out which edge type
            if neighbor not in end:
                back.add((v, neighbor))
            else:
                if start[neighbor] > start[v]:
                    forward.add((v, neighbor))
                else:
                    cross.add((v, neighbor))
            pass
        else:
            dfs(graph, neighbor, start, end, step, back, forward, cross)

    step[0] += 1
    end[v] = step[0]


edgeClass(graph)
