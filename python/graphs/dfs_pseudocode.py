def dfs(graph, u, visited=None):
    if visited is None:
        visited = set()
    visited.add(u)
    for v in graph[u]:
        if v not in visited:
            dfs(graph, v, visited)
    return visited

# All components:
def dfs_all(graph):
    visited = set()
    for u in graph:
        if u not in visited:
            dfs(graph, u, visited)

