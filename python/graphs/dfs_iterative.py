import networkx as nx

def dfs(graph, start, visited, component):
    stack = [start]
    while stack:
        u = stack.pop()
        if u in visited:
            continue
        visited.add(u)
        component.append(u)
        for v in graph.neighbors(u):
            if v not in visited:
                stack.append(v)

def dfs_all(graph):
    visited = set()
    components = []
    for u in graph.nodes():
        if u not in visited:
            component = []
            dfs(graph, u, visited, component)
            components.append(component)
    return components

def example1():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)])
    components = dfs_all(G)
    print("Connected components:", components)


def example2():
    G = nx.DiGraph()

    # Component 1: major international hubs
    G.add_edges_from([
        ('TLV', 'JFK'), ('JFK', 'TLV'),
        ('TLV', 'LHR'), ('LHR', 'TLV'),
        ('TLV', 'CDG'), ('CDG', 'TLV'),
        ('JFK', 'LHR'), ('LHR', 'JFK'),
        ('JFK', 'CDG'), ('CDG', 'JFK'),
        ('LHR', 'AMS'), ('AMS', 'LHR'),
        ('CDG', 'AMS'), ('AMS', 'CDG'),
    ])

    # Component 2: domestic Australian network (no international routes)
    G.add_edges_from([
        ('SYD', 'MEL'), ('MEL', 'SYD'),
        ('SYD', 'BNE'), ('BNE', 'SYD'),
        ('MEL', 'ADL'), ('ADL', 'MEL'),
        ('BNE', 'CNS'), ('CNS', 'BNE'),
    ])

    # Component 3: isolated island airport (single node, no routes)
    G.add_node('HNL')

    components = dfs_all(G)
    print("Connected components:", components)

if __name__ == "__main__":
    example1()
    example2()
