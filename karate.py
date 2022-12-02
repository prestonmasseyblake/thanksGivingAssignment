import numpy as np
import networkx as nx
from node2vec import Node2Vec
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn import metrics
from itertools import combinations_with_replacement, product
import matplotlib.pyplot as plt
from networkx.algorithms.community import greedy_modularity_communities

from hiveplotlib import Axis, Node, HivePlot
from hiveplotlib.converters import networkx_to_nodes_edges
from hiveplotlib.viz import axes_viz_mpl, node_viz_mpl, edge_viz_mpl
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# matplotlib inline
G = nx.karate_club_graph()
# print(karate_graph)


    


# color the nodes by faction
# color = []
# for node in G.nodes():
#     if G.nodes.data()[node]['club'] == "Mr. Hi":
#         color.append("C0")
#     else:
#         color.append("C1")

# fig, ax = plt.subplots(figsize=(10, 10))
# plt.axis("equal")
# nx.draw(G, with_labels=True, node_color=color, ax=ax,
#                  font_color="white", node_size=1000)
# ax.set_title("Zachary's Karate Club\nCircular Network Plot", fontsize=20)

# # legend
# john_a_legend = Line2D([], [], markerfacecolor="C1", markeredgecolor='C1',
#                        marker='o', linestyle='None', markersize=10)

# mr_hi_legend = Line2D([], [], markerfacecolor="C0", markeredgecolor='C0',
#                        marker='o', linestyle='None', markersize=10)

# ax.legend([mr_hi_legend, john_a_legend],
#           ["Mr. Hi", "John A."],
#           loc='upper left', bbox_to_anchor=(1, 1), title="Faction")
# plt.show()

# for node in G.nodes():
#     if node in result[0]:
#         G.nodes.data()[node]['club'] = "0"
#     elif node in result[1]:
#         G.nodes.data()[node]['club'] = "1"
#     elif node in result[2]:
#         G.nodes.data()[node]['club'] = "2"
    
# #     if G.nodes.data()[node]['club'] == "Mr. Hi":


# color = []
# for node in G.nodes():
#     if G.nodes.data()[node]['club'] == "0":
#         color.append("C0")
#     elif G.nodes.data()[node]['club'] == "1":
#         color.append("C1")
#     elif G.nodes.data()[node]['club'] == "2":
#         color.append("C2")

# fig, ax = plt.subplots(figsize=(10, 10))
# plt.axis("equal")
# nx.draw(G, with_labels=True, node_color=color, ax=ax,
#                  font_color="white", node_size=1000)
# ax.set_title("Zachary's Karate Club\nCircular Network Plot", fontsize=20)

# # legend
# john_a_legend = Line2D([], [], markerfacecolor="C1", markeredgecolor='C1',
#                        marker='o', linestyle='None', markersize=10)

# mr_hi_legend = Line2D([], [], markerfacecolor="C0", markeredgecolor='C0',
#                        marker='o', linestyle='None', markersize=10)

# mr_hi_legends = Line2D([], [], markerfacecolor="C2", markeredgecolor='C2',
#                        marker='o', linestyle='None', markersize=10)

# ax.legend([mr_hi_legend, john_a_legend, mr_hi_legends],
#           ["Group 1", "Group 2", "Group 3"],
#           loc='upper left', bbox_to_anchor=(1, 1), title="Faction")
# plt.show()