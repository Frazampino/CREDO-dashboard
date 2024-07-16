#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt

# Define the original graph G
G1 = nx.DiGraph()
nodes_sequence = ["Task1", "Task2", "Task3", "Task4", "Task5"]
G1.add_nodes_from(nodes_sequence)
edges = [("Task1", "Task2"), ("Task2", "Task3"), ("Task3", "Task4")]
G1.add_edges_from(edges)

#

# Aggiungi il nodo del gateway e i flussi
gateway_node = "OR"
incoming_flows = ["Task1"]
outgoing_flows = ["Task2", "Task3"]
G1.add_node(gateway_node)
for source_node in incoming_flows:
    G1.add_edge(source_node, gateway_node)
for target_node in outgoing_flows:
    G1.add_edge(gateway_node, target_node)

# Visualizzazione del grafo
plt.figure(figsize=(15, 10))
plt.subplot(121)
pos = nx.spring_layout(G1, k=0.9)
nx.draw(G1, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=12)
plt.title("Structural Graph 1 with Gateway")
plt.tight_layout()
plt.show()

# Visualize the total graph
plt.figure(figsize=(16, 8))


# In[2]:


import networkx as nx
import matplotlib.pyplot as plt

# Define the original graph G2
G2 = nx.DiGraph()
nodes_sequence = ["Task1", "Task2", "Task3", "Task4", "Task51"]
G2.add_nodes_from(nodes_sequence)
edges = [("Task1", "Task2"), ("Task2", "Task3"), ("Task3", "Task4"),
         ( "Task4","Task51")]
G2.add_edges_from(edges)

# Aggiungi il nodo del gateway e i flussi
gateway_node = "XOR"
incoming_flows = ["Task1"]
outgoing_flows = ["Task2", "Task3"]
G2.add_node(gateway_node)
for source_node in incoming_flows:
    G2.add_edge(source_node, gateway_node)
for target_node in outgoing_flows:
    G2.add_edge(gateway_node, target_node)

# Visualizzazione del grafo
plt.figure(figsize=(15, 10))
plt.subplot(121)
pos = nx.spring_layout(G2, k=0.9)
nx.draw(G2, pos, with_labels=True, node_size=1000, node_color="lightgreen", font_size=12)
plt.title("Structural Graph 2 with Gateway")
plt.tight_layout()
plt.show()


# In[3]:


import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET
import networkx as nx
from networkx.algorithms.similarity import graph_edit_distance

ged = graph_edit_distance(G1, G2)

max_possible_ged = max(len(G1), len(G2))
similarity = 1 - (ged / max_possible_ged)  # Normalizing GED to a similarity measure


print("Structural Similarity (GED):", similarity)


# In[4]:


import networkx as nx
import matplotlib.pyplot as plt



# Calculate SEM similarity
intersection_size = len(set(G1.nodes()).intersection(set(G2.nodes())))

synonym_penalty = 0
for s in set(G1.nodes()).difference(set(G2.nodes())):
    for l in set(G2.nodes()).difference(set(G1.nodes())):
        if s == l:  # Checking for synonymous pairs
            synonym_penalty += 1

max_set_size = max(len(G1.nodes()), len(G2.nodes()))

sem_similarity = 1.0 * intersection_size + 0.75 * synonym_penalty
max_similarity = max(len(G1.nodes()), len(G2.nodes()))

normalized_sem_similarity = sem_similarity / max_similarity


print("Normalized SEM Similarity:", normalized_sem_similarity)


# In[10]:


import networkx as nx
from networkx.algorithms.similarity import graph_edit_distance

# Definisci PES e PSP per i modelli di processo

# PES per il System Model
system_model_pes = [
    "Start", "Task1_start", "Task1_end", 
    "XOR", "Task2_start", "Task2_end", "Task4_start", "Task4_end", "Task5_start", "Task5_end", "End",
    "XOR", "Task3_start", "Task3_end", "Task4_start", "Task4_end", "Task5_start", "Task5_end", "End"
]

# PES per il Process Model
process_model_pes = [
    "Start", "Task1_start", "Task1_end",
    "XOR", "Task2_start", "Task2_end", "Task4_start", "Task4_end", "End",
    "XOR", "Task3_start", "Task3_end", "Task4_start", "Task4_end", "End"
]

# Definisci PSP come grafi
G1 = nx.DiGraph()
G2 = nx.DiGraph()

# Aggiungi nodi e archi per il System Model PSP
G1.add_edges_from([
    ("Start", "Task1"), ("Task1", "XOR1"),
    ("XOR1", "Task2"), ("Task2", "Task4"), ("Task4", "Task5"), ("Task5", "End"),
    ("XOR1", "Task3"), ("Task3", "Task4")
])

# Aggiungi nodi e archi per il Process Model PSP
G2.add_edges_from([
    ("Start", "Task1"), ("Task1", "XOR1"),
    ("XOR1", "Task2"), ("Task2", "Task4"), ("Task4", "End"),
    ("XOR1", "Task3"), ("Task3", "Task4")
])

# Costruisci il Partially Synchronized Product (PSP)
def partially_synchronized_product(G1, G2):
    P = nx.DiGraph()
    
    # Crea un prodotto cartesiano degli archi
    for (u1, v1) in G1.edges():
        for (u2, v2) in G2.edges():
            if u1 == u2 and v1 == v2:  # condizione di sincronizzazione parziale
                P.add_edge((u1, u2), (v1, v2))
    
    return P

# Costruisci il PSP
P = partially_synchronized_product(G1, G2)

# Calcola la distanza di modifica del grafo per il PSP
psp_similarity = graph_edit_distance(G1, G2)

# Helper function per calcolare la similarità di Jaccard per le liste di eventi
def jaccard_similarity(list1, list2):
    set1, set2 = set(list1), set(list2)
    return len(set1 & set2) / len(set1 | set2)

# Calcola la similarità di Jaccard per PES
pes_similarity = jaccard_similarity(system_model_pes, process_model_pes)

# Combina le similarità
weights = [0.33, 0.33, 0.34]
behavioural_similarity = (pes_similarity * weights[0]) + (psp_similarity * weights[1])

print(f"PES Similarity: {pes_similarity}")
print(f"PSP Structural Similarity (edit distance): {psp_similarity}")
print(f"Behavioural Similarity: {behavioural_similarity}")


# In[ ]:




