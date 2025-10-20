# wiki_vote_directed_five_props_csv.py
# Directed Wiki-Vote (exact, no sampling/approx), writes exactly 5 CSVs with headers.
# Input path kept as requested: ../Wiki-Vote.txt

import time
from collections import Counter
import numpy as np
import networkx as nx

START = time.time()

# ---------- Load directed graph ----------
G = nx.read_edgelist(
    "../Wiki-Vote.txt",            # keep your original path
    nodetype=int,
    create_using=nx.DiGraph(),
    comments="#",
)
print(f"[load] V={G.number_of_nodes()} E={G.number_of_edges()}  ({time.time()-START:.2f}s)")

# ============================================================
# 1) Degree distribution (directed) -> wiki-degree-dir.csv
#     CSV header: degree,in_count,out_count
# ============================================================
t0 = time.time()
in_deg  = [G.in_degree(n) for n in G.nodes()]
out_deg = [G.out_degree(n) for n in G.nodes()]
in_cnt  = Counter(in_deg)
out_cnt = Counter(out_deg)
all_degrees = sorted(set(in_cnt) | set(out_cnt))

with open("wiki-degree-dir.csv", "w") as f:
    f.write("degree,in_count,out_count\n")
    for d in all_degrees:
        f.write(f"{int(d)},{int(in_cnt.get(d,0))},{int(out_cnt.get(d,0))}\n")

print(f"[degree] in(min,med,max)=({np.min(in_deg)},{np.median(in_deg)},{np.max(in_deg)}) "
      f"out(min,med,max)=({np.min(out_deg)},{np.median(out_deg)},{np.max(out_deg)})  ({time.time()-t0:.2f}s)")

# ============================================================
# 2) Local clustering (standard = undirected) -> wiki-clustering-dir.csv
#     CSV header: node_id,clustering_coeff
#     First data row: AVG,<value>
# ============================================================
t0 = time.time()
Gu = G.to_undirected()
clust_by_node = nx.clustering(Gu)                 # dict node->float
avg_clust = nx.average_clustering(Gu)

with open("wiki-clustering-dir.csv", "w") as f:
    f.write("node_id,clustering_coeff\n")
    f.write(f"AVG,{avg_clust}\n")
    for n, c in sorted(clust_by_node.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{n},{c}\n")

# (console-only helper)
recip = nx.reciprocity(G)
print(f"[clustering] avg={avg_clust:.6f} reciprocity(dir)={recip:.6f}  ({time.time()-t0:.2f}s)")

# ============================================================
# 3) Betweenness centrality (directed, EXACT) -> wiki-betweenness-dir.csv
#     CSV header: node_id,betweenness
# ============================================================
t0 = time.time()
bc = nx.betweenness_centrality(G, k=None, normalized=True, endpoints=False)  # exact
with open("wiki-betweenness-dir.csv", "w") as f:
    f.write("node_id,betweenness\n")
    for n, b in sorted(bc.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{n},{b}\n")
print(f"[betweenness] directed exact written  ({time.time()-t0:.2f}s)")

# ============================================================
# 4) Directed triangles (ALL 3-cycles u->v->w->u) -> wiki-triangles-dir.csv
#     CSV header: metric,value ; single row with exact count.
#     We dedup by only counting when u is the smallest id in (u,v,w).
# ============================================================
t0 = time.time()
succ = {u: set(G.successors(u)) for u in G.nodes()}
tri_count = 0
for u in G.nodes():
    Nu = succ[u]
    if not Nu:
        continue
    for v in Nu:
        if v == u:
            continue
        Nv = succ[v]
        if not Nv:
            continue
        for w in Nv:
            if w == u or w == v:
                continue
            if u in succ[w]:            # closes 3-cycle
                if u <= v and u <= w:   # canonical start => no duplicates
                    tri_count += 1

with open("wiki-triangles-dir.csv", "w") as f:
    f.write("metric,value\n")
    f.write(f"directed_3cycle_count,{tri_count}\n")

print(f"[triangles] directed 3-cycles (exact) = {tri_count}  ({time.time()-t0:.2f}s)")

# ============================================================
# 5) Components (WCC/SCC) & exact diameter on largest SCC
#     -> wiki-components-diameter-dir.csv
#     CSV header: num_wcc,largest_wcc_nodes,num_scc,largest_scc_nodes,diameter_largest_scc
# ============================================================
t0 = time.time()
wccs = list(nx.weakly_connected_components(G))
sccs = list(nx.strongly_connected_components(G))
largest_wcc = max(wccs, key=len)
largest_scc = max(sccs, key=len)
H = G.subgraph(largest_scc).copy()
diam = nx.diameter(H)  # exact diameter on largest SCC

with open("wiki-components-diameter-dir.csv", "w") as f:
    f.write("num_wcc,largest_wcc_nodes,num_scc,largest_scc_nodes,diameter_largest_scc\n")
    f.write(f"{len(wccs)},{len(largest_wcc)},{len(sccs)},{len(largest_scc)},{diam}\n")

print(f"[components] WCCs={len(wccs)} (largest={len(largest_wcc)}), "
      f"SCCs={len(sccs)} (largest={len(largest_scc)}), "
      f"diameter_largest_scc={diam}  ({time.time()-t0:.2f}s)")

print(f"[done] total time {time.time()-START:.2f}s")
