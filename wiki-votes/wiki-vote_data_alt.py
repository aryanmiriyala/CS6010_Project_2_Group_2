import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import json

G = nx.read_edgelist('Wiki-Vote.txt', nodetype=int, create_using=nx.DiGraph())

"""degrees = [G.degree(n) for n in G.nodes()]
plt.hist(degrees, bins=range(min(degrees), max(degrees) + 2))
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.savefig('wiki-degrees-alt.png')

clust = nx.clustering(G)
clust = dict(sorted(clust.items(), key=lambda item: item[1], reverse=True))
with open('wiki-clust-alt.txt', 'w') as f:
    f.writelines([str(item) + ", " + str(clust[item]) + '\n' for item in clust])

bc = nx.betweenness_centrality(G, k=500, seed=42)
bc = dict(sorted(bc.items(), key=lambda item: item[1], reverse=True))
with open('wiki-bc-alt.txt', 'w') as f:
    f.writelines([str(item) + ", " + str(bc[item]) + '\n' for item in bc])
"""
triangles = nx.simple_cycles(G)
for i in triangles:
    print(i)
triangles = sorted(triangles, key=lambda item: item[1], reverse=True)
with open('wiki-triangles-alt.txt', 'w') as f:
    f.writelines([str(item) + ", " + str(triangles[item]) + '\n' for item in triangles])

ccs = list(nx.strongly_connected_components(G))
with open('wiki-ccs-alt.txt', 'w') as f:
    f.writelines([str(item)  + '\n' for item in ccs])

largest_ccs = max(ccs, key=len)
with open('wiki-large-cc-alt.txt', 'w') as f:
    f.writelines("Largest Connected Component: " + '\n')
    f.writelines(str(largest_ccs))

G_lcc = G.subgraph(largest_ccs)
diameter_approx = nx.diameter(G_lcc)
print("Diameter of Largest CC:", diameter_approx)

