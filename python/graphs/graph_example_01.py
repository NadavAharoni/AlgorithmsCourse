import networkx as nx
import matplotlib.pyplot as plt

# G = nx.karate_club_graph()
G = nx.petersen_graph()

for node in G.nodes():
    print(node)

for edge in G.edges():
    print(edge)

exit()

# pos = nx.spring_layout(G, seed=42)
pos = nx.spectral_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()

from pyvis.network import Network

net = Network(notebook=True)
G = nx.petersen_graph()
for node in G.nodes():
    G.nodes[node]['label'] = str(node)
net.from_nx(G)
net.show("graph.html")  # opens in browser

