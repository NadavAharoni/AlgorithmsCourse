import networkx as nx

WHITE = 0
GRAY  = 1
BLACK = 2

def dfs_enhanced(graph, u, color, time, nodes, edges):
    color[u] = GRAY
    time[0] += 1
    nodes[u]['disc'] = time[0]

    for v in graph.neighbors(u):
        if color[v] == WHITE:
            nodes[v]['parent'] = u
            edges.append((u, v, 'tree'))
            dfs_enhanced(graph, v, color, time, nodes, edges)
        elif color[v] == GRAY:
            edges.append((u, v, 'back'))
        elif color[v] == BLACK:
            if nodes[v]['disc'] > nodes[u]['disc']:
                edges.append((u, v, 'forward'))
            else:
                edges.append((u, v, 'cross'))

    color[u] = BLACK
    time[0] += 1
    nodes[u]['finish'] = time[0]

def dfs_enhanced_all(graph):
    color = {u: WHITE for u in graph.nodes()}
    time  = [0]  # mutable int so recursion can modify it
    nodes = {u: {'parent': None, 'disc': None, 'finish': None}
             for u in graph.nodes()}
    edges = []

    for u in graph.nodes():
        if color[u] == WHITE:
            dfs_enhanced(graph, u, color, time, nodes, edges)

    return nodes, edges

def example1():
    G = nx.Graph()
    G.add_edges_from([(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)])
    nodes, edges = dfs_enhanced_all(G)

    print("Example1:")
    print("Nodes with discovery and finish times:")
    for node, info in nodes.items():
        print(f"  {node}: disc={info['disc']}, finish={info['finish']}")

    print("Edges with types:")
    for u, v, edge_type in edges:
        print(f"  ({u}, {v}): {edge_type}")


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

    nodes, edges = dfs_enhanced_all(G)
    print("Example2:")
    print("Nodes with discovery and finish times:")
    for node, info in nodes.items():
        print(f"  {node}: disc={info['disc']}, finish={info['finish']}")
    print("Edges with types:")
    for u, v, edge_type in edges:
        print(f"  ({u}, {v}): {edge_type}")


if __name__ == "__main__":
    example1()
    example2()


