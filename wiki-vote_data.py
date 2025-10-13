import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


G = nx.read_edgelist('Wiki-Vote.txt', nodetype=int, create_using=nx.Graph())

degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees, bins=range(min(degrees), max(degrees) + 2))
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.savefig('wiki-degrees.png')

clust = nx.clustering(G)
clust = dict(sorted(clust.items(), key=lambda item: item[1], reverse=True))
with open('wiki-clust.txt', 'w') as f:
    f.writelines([str(item) + ", " + str(clust[item]) + '\n' for item in clust])

bc = nx.betweenness_centrality(G, k=500, seed=42)
bc = dict(sorted(bc.items(), key=lambda item: item[1], reverse=True))
with open('wiki-bc.txt', 'w') as f:
    f.writelines([str(item) + ", " + str(bc[item]) + '\n' for item in bc])

triangles = nx.triangles(G)
triangles = dict(sorted(triangles.items(), key=lambda item: item[1], reverse=True))
with open('wiki-triangles.txt', 'w') as f:
    f.writelines([str(item) + ", " + str(triangles[item]) + '\n' for item in triangles])

"""ccs = list(nx.connected_components(G))
largest_ccs = max(ccs, key=len)
G_lcc = G.subgraph(largest_ccs)

diameter_approx = nx.diameter(G_lcc)"""


