graph = {
    0: [1, 5, 8],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [2, 3],
    5: [0, 8],
    8: [0, 5]
}


def dfs(graph, node, visited):
    size = 1
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            size += dfs(graph, neighbor, visited)
    return size


largest = 0
visited = set()
for node in graph:
    if node not in visited:
        visited.add(node)
        comp = dfs(graph, node, visited)
        print(comp)
        largest = max(largest, comp)

print(largest)
