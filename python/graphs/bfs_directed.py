import networkx as nx
from collections import deque

def bfs(graph, start):
    dist   = {start: 0}
    parent = {start: None}       # ← add this
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph.successors(u):
            if v not in dist:
                dist[v]   = dist[u] + 1
                parent[v] = u            # ← and this
                q.append(v)
    return dist, parent

def reconstruct_path(parent, target):
    """
    Reconstruct the shortest path from the BFS source to target.
    
    parent: the dict returned by bfs(graph, start) —
            must have been built from the same start node
            you want the path from.
    target: the destination node.
    
    Returns the path as a list [start, ..., target],
    or None if target was not reachable from start.
    """
    if target not in parent:
        return None     # target not reachable
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = parent[node]
    path.reverse()
    return path


def example_usage():
    G = nx.DiGraph()
    G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)])
    start = 0
    dist, parent = bfs(G, start)
    print("Distances:", dist)
    print("Parents:", parent)

    target = 4
    path = reconstruct_path(parent, target)
    print(F"Path from {start} to {target}:", path)

if __name__ == "__main__":
    example_usage()

