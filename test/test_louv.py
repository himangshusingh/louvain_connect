from src.louvain_algorithm import louvain
import networkx as nx


# Create a graph
G = nx.Graph()
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 0)]
G.add_edges_from(edges)

# Detect communities using Louvain's algorithm
communities = louvain(G)

# Print the identified communities
for i, community in enumerate(communities):
    print(f"Community {i + 1}: {community}")
