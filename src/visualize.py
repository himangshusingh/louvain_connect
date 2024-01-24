import networkx as nx
import matplotlib.pyplot as plt

def visualize_communities(graph, communities):
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(graph)  # Layout for the visualization

    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']  # Add more colors if needed

    for i, community in enumerate(communities):
        subgraph = graph.subgraph(community)
        nx.draw(subgraph, pos, node_color=colors[i % len(colors)], node_size=300, with_labels=True, label=f'Community {i + 1}')

    plt.title('Visualization of Communities Detected by Louvain Algorithm')
    plt.legend()
    plt.show()