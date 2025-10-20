# wiki_vote_undirected_five_props_csv.py
# Undirected Wiki-Vote (exact, no sampling/approx), writes exactly 5 CSVs with headers.
# Input kept as requested: ../Wiki-Vote.txt

import time
from collections import Counter
import numpy as np
import networkx as nx

START = time.time()

# ---------- Load as UNDIRECTED ----------
# SNAP edges "i j" become an undirected edge {i,j}
Gu = nx.read_edgelist(
    "../Wiki-Vote.txt",            # your original path
    nodetype=int,
    create_using=nx.Graph(),
    comments="#",
)
print(f"[load] (undirected) V={Gu.number_of_nodes()} E={Gu.number_of_edges()}  ({time.time()-START:.2f}s)")

# ============================================================
# 1) Degree distribution (undirected) -> wiki-degree-undir.csv
#     CSV header: degree,count
#     (Undirected has a single degree per node.)
# ============================================================
t0 = time.time()
deg = [Gu.degree(n) for n in Gu.nodes()]
deg_cnt = Counter(deg)
with open("wiki-degree-undir.csv", "w") as f:
    f.write("degree,count\n")
    for d in sorted(deg_cnt):
        f.write(f"{int(d)},{int(deg_cnt[d])}\n")
print(f"[degree] min/med/max=({np.min(deg)},{np.median(deg)},{np.max(deg)})  ({time.time()-t0:.2f}s)")

# ============================================================
# 2) Local clustering (undirected) -> wiki-clustering-undir.csv
#     CSV header: node_id,clustering_coeff
#     First row:  AVG,<value>
# ============================================================
t0 = time.time()
clust_by_node = nx.clustering(Gu)                 # dict node->float
avg_clust = nx.average_clustering(Gu)
with open("wiki-clustering-undir.csv", "w") as f:
    f.write("node_id,clustering_coeff\n")
    f.write(f"AVG,{avg_clust}\n")
    for n, c in sorted(clust_by_node.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{n},{c}\n")
print(f"[clustering] avg={avg_clust:.6f}  ({time.time()-t0:.2f}s)")

# ============================================================
# 3) Betweenness centrality (undirected, EXACT) -> wiki-betweenness-undir.csv
#     CSV header: node_id,betweenness
# ============================================================
t0 = time.time()
bc = nx.betweenness_centrality(Gu, k=None, normalized=True, endpoints=False)  # exact
with open("wiki-betweenness-undir.csv", "w") as f:
    f.write("node_id,betweenness\n")
    for n, b in sorted(bc.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{n},{b}\n")
print(f"[betweenness] undirected exact written  ({time.time()-t0:.2f}s)")

# ============================================================
# 4) Triangles (undirected, ALL) -> wiki-triangles-undir.csv
#     CSV header: metric,value
#     Single row: undirected_triangle_count,<int>
# ============================================================
t0 = time.time()
tri_per_node = nx.triangles(Gu)                   # node -> incident triangle count
total_tri = sum(tri_per_node.values()) // 3       # each triangle counted at all 3 vertices
with open("wiki-triangles-undir.csv", "w") as f:
    f.write("metric,value\n")
    f.write(f"undirected_triangle_count,{total_tri}\n")
print(f"[triangles] undirected triangles (exact) = {total_tri}  ({time.time()-t0:.2f}s)")

# ============================================================
# 5) Connected components & exact diameter (undirected)
#     -> wiki-components-diameter-undir.csv
#     CSV header: num_cc,largest_cc_nodes,diameter_largest_cc
# ============================================================
t0 = time.time()
ccs = list(nx.connected_components(Gu))
largest_cc = max(ccs, key=len)
H = Gu.subgraph(largest_cc).copy()
diam = nx.diameter(H)  # exact diameter on the LCC
with open("wiki-components-diameter-undir.csv", "w") as f:
    f.write("num_cc,largest_cc_nodes,diameter_largest_cc\n")
    f.write(f"{len(ccs)},{len(largest_cc)},{diam}\n")
print(f"[components] CCs={len(ccs)} (largest={len(largest_cc)}), "
      f"diameter_largest_cc={diam}  ({time.time()-t0:.2f}s)")

print(f"[done] total time {time.time()-START:.2f}s")
