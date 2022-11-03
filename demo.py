# %%
from neo4j import GraphDatabase
import nxneo4j as nx
uri = 'bolt://localhost'
user = 'neo4j'
password = 'esb1313'
driver = GraphDatabase.driver(uri=uri, auth=(user, password))
G = nx.Graph(driver)
# %%
G.delete_all()
G.add_node(1)                   #single node
G.add_nodes_from([2,3,4])       #multiple nodes
G.add_edge(1,2)                 #single edge
G.add_edges_from([(2,3),(3,4)]) #multiple edges
# %%
from karateclub.utils.walker import RandomWalker
worker = RandomWalker(2, 10)
worker.do_walks(G)
# %% 
from karateclub import Estimator
Estimator()._check_graph(G)
# %%
Estimator()._check_connectivity(G) 
# %%
Estimator()._check_directedness(G)
# %%
Estimator()._check_indexing(G)
# %%
from karateclub import DeepWalk
model = DeepWalk()
model.fit(G)
# %% 
# Problem: 
# What are the methods that are missing on networkx-neo4j? 
# 1) G.neighbors()
# 2) G.number_of_nodes_query()
# 3) G.is_directed()