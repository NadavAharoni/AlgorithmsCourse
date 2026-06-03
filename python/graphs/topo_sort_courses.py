import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Build course prerequisite graph
G = nx.DiGraph()

courses = [
    "Math 101",
    "Intro to CS",
    "Data Structures",
    "Algorithms",
    "Linear Algebra",
    "Probability",
    "Machine Learning",
    "Operating Systems",
    "Computer Networks",
    "Databases",
]

# Edge (A, B) means "A is a prerequisite for B"
prerequisites = [
    ("Math 101",       "Linear Algebra"),
    ("Math 101",       "Probability"),
    ("Intro to CS",    "Data Structures"),
    ("Data Structures","Algorithms"),
    ("Data Structures","Operating Systems"),
    ("Data Structures","Databases"),
    ("Algorithms",     "Machine Learning"),
    ("Linear Algebra", "Machine Learning"),
    ("Probability",    "Machine Learning"),
    ("Operating Systems", "Computer Networks"),
]

G.add_nodes_from(courses)
G.add_edges_from(prerequisites)

# ── Topological sort (DFS-based) ──────────────────────────────────────────────
def topo_sort(graph):
    visited = set()
    result = []

    def dfs(u):
        visited.add(u)
        for v in graph.neighbors(u):
            if v not in visited:
                dfs(v)
        result.append(u)

    for u in graph:
        if u not in visited:
            dfs(u)

    return result[::-1]

order = topo_sort(G)

print("Topological order (valid course schedule):")
for i, course in enumerate(order, 1):
    print(f"  {i}. {course}")

# ── Visualisation ─────────────────────────────────────────────────────────────
# Assign each node a "level" = its position in topo order, for x-axis layout
level = {course: i for i, course in enumerate(order)}

# Spread nodes vertically within each level so labels don't overlap
from collections import defaultdict
level_members = defaultdict(list)
for node in G.nodes():
    level_members[level[node]].append(node)

pos = {}
for lev, members in level_members.items():
    for rank, node in enumerate(members):
        # centre vertically
        y = rank - (len(members) - 1) / 2
        pos[node] = (lev, y)

fig, ax = plt.subplots(figsize=(14, 6))
ax.set_title("Course Prerequisites — Topological Order (left → right)", fontsize=14)

nx.draw_networkx_nodes(G, pos, node_size=2200, node_color="#d0e8ff",
                        edgecolors="#336699", linewidths=1.5, ax=ax)
nx.draw_networkx_labels(G, pos, font_size=8, font_color="#1a1a1a", ax=ax)
nx.draw_networkx_edges(G, pos, arrows=True,
                        arrowstyle="-|>", arrowsize=20,
                        edge_color="#555555", width=1.5,
                        connectionstyle="arc3,rad=0.05", ax=ax)

ax.axis("off")
plt.tight_layout()
plt.savefig("topo_sort_courses.png", dpi=150)
plt.show()
print("Graph saved to topo_sort_courses.png")
