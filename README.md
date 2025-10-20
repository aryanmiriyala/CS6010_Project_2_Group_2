# Project 2 - Group 2
This is the README file for Project 2 of CS 6010 Data Science Programming
Written by: Jashhvanth Tamilselvan Kunthavai, Aryan Miriyala, Emily Massie, Joshua Gabriel, and Kyle Cusimano

# Introduction and Requirements

Contained in this series of folders are the base code for the programs executed, the datasets as txts, and the output files from the programs. The main goal for this project was to select two graph networks, find five graph properties using unsupervised machine learning from both networks, and then compare and contrast the properties and derive conclusions from them. Both of the databases were pulled from https://snap.stanford.edu/data/. The datasets used were the directed wiki-Vote dataset from https://snap.stanford.edu/data/wiki-Vote.html, which had 7,115 nodes and 103,689 edges, and the undirected roadNet-TX dataset from https://snap.stanford.edu/data/wiki-Vote.html, which had 1,379,917 nodes and 1,921,660 edges.

The processing code scripts require:

     - python==3.11
     - contourpy==1.3.2
     - cycler==0.12.1
     - fonttools==4.60.1
     - kiwisolver==1.4.9
     - matplotlib==3.10.7
     - networkx==3.4.2
     - numpy==2.2.6
     - packaging==25.0
     - pillow==12.0.0
     - pyparsing==3.2.5
     - python-dateutil==2.9.0.post0
     - six==1.17.0

# File Path Locations

## road-network
    - Contains the dataset, program, and the output of the program related to the roadNet-TX dataset

    - The actual roadNet-TX network dataset can be found in /CS6010_Project2_Group_2/road-network/roadNet_TX.txt. It contains the Texas road network (edge list, undirected).

    - The program file for calculating and finding the graph properties can be found in /CS6010_Project2_Group_2/road-network/roadnet_data.py. The program file analyzes the road network as undirected (degrees, clustering, betweenness centrality, connected components, triangles, largest CC and diameter).

## wiki-votes
    - Contains the dataset, program, and the output of the program related to the wiki-Vote dataset after it was converted to an undirected graph.

    - The actual wiki-Vote network dataset can be found in /CS6010_Project2_Group_2/wiki-votes/Wiki-Vote.txt. It contains the Wikipedia vote network (edge list, directed).

### directed
    - The program file for calculating and finding the graph properties can be found in /CS6010_Project2_Group_2/wiki-votes/directed/wiki-vote-data-dir.py. The program file analyzes the road network as directed (degrees, clustering, betweenness centrality, strongly connected components, simple circles, largest CC and diameter).

## undirected
    - The program file for calculating and finding the graph properties can be found in /CS6010_Project2_Group_2/wiki-votes/undirected/wiki-vote-data-undir.py. The program file analyzes the road network as undirected (degrees, clustering, betweenness centrality, connected components, triangles, largest CC and diameter).


# Graph Properties

Our group decided to choose five different graph properties. The definition of each graph property and the reasoning for why the properties were chosen are listed below:

    - Degree Distribution: Shows how many nodes have a certain number of connection. We chose this property so it can highlight the overall connectivity of the network 

    - Local Clustering Coefficient: How likely a node’s neighbors are connected to each other. We chose this show local community structure and closely knit they are 

    - Betweenness Centrality: measures how often a node lies on the shortest path between other nodes. We chose this to see which nodes are most important when it comes to hte shortest path, and to see which nodes are the “bridge” 

    - Number of triangles: a triangle in a graph network is when three nodes connect to each other, to form a triangle. We chose this to show how many groups there are in each network 

    - Connected Components and diameter: a subset of nodes where every node is reachable from any other node in the same subnet. Diameter is the maximum shortest path within the network. We chose this to show how unified or disconnected the network is and coupled them together because they go hand-in-hand with each other 

# Methodology


# Runtime

    - roadnet_data.py: 
    - wiki-vote-data-undir.py: 
    - wiki-vote-data-dir.py: 


# Setup and Execution

## Creating the venv (venv named 'proj2-env')

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

## Run (from root, with venv active)

First, you must cd into the respective folders to execute the Python programs. The steps to do so can be seen below:
    - To execute the roadnet_data.py file, use the following command: cd road-network
    - To execute the wiki-vote-data-undir.py file, use the following command: cd wiki-votes/undirected
    - To execute the wiki-vote-data-dir.py file, use the following command: cd wiki-votes/directed

Once you cd into the respective folders, you can use one of the three bash commands below to run the respective files:

    ```bash
    python roadnet_data.py              # uses road-network/roadNet-TX.txt
    python wiki-vote-data-undir.py      # uses wiki-votes/Wiki-Vote.txt (undirected)
    python wiki-vote-data-alt-dir.py    # uses wiki-votes/Wiki-Vote.txt (directed)
    ```

**Outputs:** PNGs (degree histograms) and TXT reports (components, largest CC/SCC, etc.) in the repo.


# Results and Conclusions

The programs for both the datasets run. The execution time was measured for each program and can be found above. The outputs for each program (including the PNGs and the TXT reports) were used to analyze, compare, and contrast the two graph network datasets. 