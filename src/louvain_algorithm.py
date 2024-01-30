import networkx as nx
from modularity import greedy_modularity_communities

def louvain():
    def calculate_modularity(g, communities):
        m = g.number_of_edges()
        deg = dict(g.degree())
        m2 = 2 * m
        Q = 0
        for community in communities:
            Ec = 0
            Lc = 0
            for u in community:
                for v in community:
                    if g.has_edge(u, v):
                        Lc += 1
                Ec += deg[u]
            Q += (Ec / m2) - ((Lc / m2) ** 2)
        return Q

    def move_nodes(g, communities):
        improvement = True
        while improvement:
            improvement = False
            for node in g.nodes():
                initial_community = None
                for i, community in enumerate(communities):
                    if node in community:
                        initial_community = i
                        break

                max_delta_modularity = 0
                best_community = None

                for neighbor in g.neighbors(node):
                    for i, community in enumerate(communities):
                        if neighbor in community and i != initial_community:
                            communities[initial_community].remove(node)
                            communities[i].add(node)
                            delta_modularity = calculate_modularity(g, communities)
                            if delta_modularity > max_delta_modularity:
                                max_delta_modularity = delta_modularity
                                best_community = i
                            communities[i].remove(node)
                            communities[initial_community].add(node)

                if best_community is not None:
                    communities[initial_community].remove(node)
                    communities[best_community].add(node)
                    improvement = True

        return communities

    communities = list(nx.connected_components(g))
    modularity = calculate_modularity(g, communities)

    while True:
        new_communities = move_nodes(g, communities)
        new_modularity = calculate_modularity(g, new_communities)
        if new_modularity <= modularity:
            break
        communities = new_communities
        modularity = new_modularity

    return communities


# Load your network graph
g = nx.karate_club_graph()

# Detect communities using Louvain method
communities = list(greedy_modularity_communities(g))

# Convert frozensets to normal sets for display
converted_communities = [set(community) for community in communities]

# Print the identified communities
for i, community in enumerate(converted_communities):
    print(f"Community {i + 1}: {community}")
#i have added new features
