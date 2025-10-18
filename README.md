# Graph Scripts — Quick Start

## What’s here

- **road-network/roadNet-TX.txt** — Texas road network (edge list, undirected).
- **wiki-votes/Wiki-Vote.txt** — Wikipedia vote network (edge list, _directed_).
- **roadnet_data.py** — Analyzes the road network as **undirected** (degrees, clustering, components, largest CC, diameter).
- **wiki-vote-data-undir.py** — Analyzes Wiki-Vote as **undirected** (degrees, clustering, components, largest CC, diameter).
- **wiki-vote-data-dir.py** — Analyzes Wiki-Vote as **directed** (SCCs, largest SCC, diameter).

## Setup (venv named `proj2-env`)

macOS/Linux

```bash
python3 -m venv proj2-env && source proj2-env/bin/activate
python -m pip install --upgrade pip
```

Windows (PowerShell)

```powershell
py -m venv proj2-env
.\proj2-env\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Install deps

```bash
pip install -r requirements.txt
```

## Run (from repo root, venv active)

```bash
python roadnet_data.py          # uses road-network/roadNet-TX.txt
python wiki-vote-data-dir.py        # uses wiki-votes/Wiki-Vote.txt (undirected)
python wiki-vote-data-undir.py    # uses wiki-votes/Wiki-Vote.txt (directed)
```

**Outputs:** PNGs (degree histograms) and TXT reports (components, largest CC/SCC, etc.) in the repo.
