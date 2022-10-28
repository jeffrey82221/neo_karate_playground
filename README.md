# NEO Karate Playground

Playground of networkx-neo4j and karate-club. The goal is to build unsupervised node embedding for graph in neo4j. 

# networkx-neo4j

## Setup: 
```bash
pip install networkx-neo4j==0.0.2
neo4j console
cypher-shell
> username: neo4j 
> password: neo4j
> change the password
```
# Run: 
```python
from neo4j import GraphDatabase
uri = 'bolt://localhost'
user = 'xxxx'
password = 'xxxx'
driver = GraphDatabase.driver(uri=uri, auth=(uri, password))
import nxneo4j as nx
G = nx.Graph(driver)

G.add_node(1)                   #single node
G.add_nodes_from([2,3,4])       #multiple nodes
G.add_edge(1,2)                 #single edge
G.add_edges_from([(2,3),(3,4)]) #multiple edges

list(G.nodes())
list(G.edges())

G.add_node('Mike',gender='M',age=17)
G.add_edge('Mike','Jenny',type='friends',weight=3)

G.nodes[‘Mike’]
G.nodes['Mike']['gender']

G.delete_all()
```
