# Wiki-Votes — README (concise)

**Dataset:** `Wiki-Vote.txt` from SNAP. A directed edge `i j` means user _i_ voted on user _j_ in a Wikipedia adminship (RfA) election.

## Folder layout

```
wiki-votes/
├─ Wiki-Vote.txt
├─ directed/
│  ├─ wiki-vote-data-dir.py
│  ├─ *.csv                # five outputs (directed view)
│  └─ time-metrics.txt     # optional timings
└─ undirected/
   ├─ wiki-vote-data-undir.py
   ├─ *.csv                # five outputs (undirected view)
   └─ time-metrics.txt     # optional timings
```

## How to run

From `wiki-votes/`:

```bash
python directed/wiki-vote-data-dir.py
python undirected/wiki-vote-data-undir.py
```

---

## What each property is and what each CSV contains

### 1) Degree distribution

- **Meaning:** In a directed graph, **in-degree** = votes **received**; **out-degree** = votes **cast**. In undirected, degree is a single count of neighbors.
- **Directed file:** `directed/wiki-degree-dir.csv`  
  Columns: `degree,in_count,out_count`. Each row `d` says how many nodes have in-degree `d` and out-degree `d`. Use this to see popularity (in-degree) vs. voter activity (out-degree).
- **Undirected file:** `undirected/wiki-degree-undir.csv`  
  Columns: `degree,count`. Each row `d` is how many nodes have degree `d` (overall connectivity).

### 2) Local clustering coefficient

- **Meaning:** How likely a node’s neighbors are connected to each other (standard definition is **undirected**). High values indicate tightly knit local groups.
- **Directed file:** `directed/wiki-clustering-dir.csv` (computed on the undirected view)
- **Undirected file:** `undirected/wiki-clustering-undir.csv`  
  Columns: `node_id,clustering_coeff`. The first data row is `AVG,<value>` (the graph-wide average). Use per-node values to find locally dense regions; the average gives overall local cohesion.

### 3) Betweenness centrality

- **Meaning:** Fraction of shortest paths that pass through a node (bridge/broker role). In **directed**, paths must follow edge direction; in **undirected**, direction is ignored.
- **Directed file:** `directed/wiki-betweenness-dir.csv`
- **Undirected file:** `undirected/wiki-betweenness-undir.csv`  
  Columns: `node_id,betweenness`. Larger values imply nodes that mediate many shortest paths (potential influence/bridging points).

### 4) Triangles

- **Meaning:** Small 3-node motifs that indicate closure/community.
  - **Directed:** counts **3-cycles** `u→v→w→u` (feedback loop).
  - **Undirected:** counts 3-cliques (all three nodes mutually connected).
- **Directed file:** `directed/wiki-triangles-dir.csv`  
  Columns: `metric,value` with a single row: `directed_3cycle_count,<int>`.
- **Undirected file:** `undirected/wiki-triangles-undir.csv`  
  Columns: `metric,value` with a single row: `undirected_triangle_count,<int>`.  
  Use these counts to compare motif abundance (directed is stricter, usually fewer than undirected).

### 5) Components & diameter

- **Meaning:** Connectivity at the whole-graph scale.
  - **Undirected:** **connected components (CCs)** and **diameter** on the **largest CC** (longest shortest path inside it).
  - **Directed:** **weakly connected components (WCCs)** (ignore direction), **strongly connected components (SCCs)** (mutual reachability), and **diameter** on the **largest SCC**.
- **Directed file:** `directed/wiki-components-diameter-dir.csv`  
  Columns: `num_wcc,largest_wcc_nodes,num_scc,largest_scc_nodes,diameter_largest_scc`.
- **Undirected file:** `undirected/wiki-components-diameter-undir.csv`  
  Columns: `num_cc,largest_cc_nodes,diameter_largest_cc`.  
  Use these to judge global cohesion: a very large largest CC/WCC implies broad connectivity; SCC size shows the mutual-reachability core; diameter reflects “how many hops apart” nodes are inside the core.

---

## Notes

- All computations are **exact** (no sampling/approximation).
- Timings (if recorded) are in each folder’s `time-metrics.txt`.
- CSV headers are consistent across directed/undirected for easy comparison.
