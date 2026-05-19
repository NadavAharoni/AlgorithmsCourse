import networkx as nx

def dfs(graph, u, visited):
    visited.add(u)
    for v in graph.neighbors(u):
        if v not in visited:
            dfs(graph, v, visited)

def dfs_all(graph):
    visited = set()
    for u in graph.nodes():
        if u not in visited:
            dfs(graph, u, visited)

# Example usage:
G = nx.Graph()
G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)])
dfs_all(G)
