import networkx as nx

WHITE = 0
GRAY  = 1
BLACK = 2

def dfs(graph, u, color):
    color[u] = GRAY                    # discovered, on the stack
    for v in graph.neighbors(u):
        if color[v] == WHITE:
            dfs(graph, v, color)
        elif color[v] == GRAY:
            print(f"back edge: {u} → {v}  (cycle!)")
    color[u] = BLACK                   # finished

def dfs_all(graph):
    color = {u: WHITE for u in graph.nodes()}
    for u in graph.nodes():
        if color[u] == WHITE:
            dfs(graph, u, color)

