# NEO Karate Playground

Playground of networkx-neo4j and karate-club. The goal is to build unsupervised node embedding for graph in neo4j. 

# networkx-neo4j

## Setup: 
```bash
# Install networkx-neo4j
git clone https://github.com/neo4j-graph-analytics/networkx-neo4j.git
cd networkx-neo4j
python setup.py install
# Start neo4j DB 4.4.6 & setup password
# - NOTE: It is installed on the Graph image on Aicloud Primehub
neo4j console
cypher-shell
> username: neo4j 
> password: neo4j
> change the password
```
## Install GDS 2.1.6 (support neo4j 4.4.6)
1. download GDS jar file from: https://github.com/neo4j/graph-data-science/releases/download/2.1.6/neo4j-graph-data-science-2.1.6.jar
2. move the jar file to /var/lib/neo4j/plugins/
3. [?] Uncommand `dbms.security.procedures.allowlist=apoc.coll.*,apoc.load.*,gds.*` in neo4j.conf

# Run: 
```python
from neo4j import GraphDatabase
uri = 'bolt://localhost'
user = 'neo4j'
password = 'esb1313'
driver = GraphDatabase.driver(uri=uri, auth=(user, password))
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
# karateclub 

## Install: 
```
pip install karateclub==1.0.0
```
## Run:
```
from neo4j import GraphDatabase
uri = 'bolt://localhost'
user = 'neo4j'
password = 'esb1313'
driver = GraphDatabase.driver(uri=uri, auth=(user, password))
import nxneo4j as nx
G = nx.Graph(driver)
G.add_node(1)                   #single node
G.add_nodes_from([2,3,4])       #multiple nodes
G.add_edge(1,2)                 #single edge
G.add_edges_from([(2,3),(3,4)]) #multiple edges
from karateclub import DeepWalk
model = DeepWalk()
model.fit(G)
embedding = model.get_embedding()

splitter = EgoNetSplitter(1.0)
splitter.fit(G)

```


REF: https://buildmedia.readthedocs.org/media/pdf/neonx/stable/neonx.pdf

