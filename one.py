#Python code applying Node2Vec and t-SNE to the college football network and graphs from the stochastic block model

import numpy as np
import networkx as nx
from node2vec import Node2Vec
from sklearn.manifold import TSNE
from sklearn.cluster import KMeans
from sklearn import metrics
from itertools import combinations_with_replacement, product
import matplotlib.pyplot as plt

#some interesting functions here, let me know if you have questions!
def sbm(C, P):
  G =nx.Graph()
  G.add_nodes_from(range(sum(C)))
  for (a, b) in combinations_with_replacement(range(len(P)), 2):
    aStart, aEnd = sum(C[:a]), sum(C[:a+1])
    bStart, bEnd = sum(C[:b]), sum(C[:b+1])
    for (u, v) in product(range(aStart, aEnd), range(bStart, bEnd)):
      if u!=v and np.random.ranf() < P[a][b]: G.add_edge(u, v)
  return G

#
if __name__=='__main__':
  #use node2vec to embed the football network, cluster the nodes, evaluate the clusters
  #consider different parameters for node2vec, how do these affect the results?
  if True:
    G = nx.read_gml('lesmis.gml')
    print(G.number_of_nodes(), G.number_of_edges())

    node2vec = Node2Vec(G, dimensions=20, walk_length=15, num_walks=200, p=1, q=0.5, workers=1, seed=1234)
    model = node2vec.fit(window=15, min_count=1)
    embedding = [model.wv[str(v)] for v in sorted(G.nodes())]

    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos=pos, node_size=100, font_size=5, width=0.5)
    plt.savefig('temp_node2vec.eps', bbox_inches='tight', format="eps")
    plt.clf()

    tsne = TSNE(n_components=2, init='pca')
    pos = tsne.fit_transform(np.array(embedding))
    pos = {v:pos[i] for i,v in enumerate(sorted(G.nodes()))}
    nx.draw_networkx(G, pos=pos, edgelist=[], alpha=0.5, node_size=100, font_size=5,
    nodelist=sorted(G.nodes()), node_color="red")
    # [G.nodes[v]['value'] for v in sorted(G.nodes())]
    plt.savefig('temp_node2vec_2.png', bbox_inches='tight')
    plt.clf()
    plt.show()

    

    # numClusters = 6
    # len(set(nx.get_node_attributes(G, 'value').values()))
    # kmeans = KMeans(numClusters)
    # kmeans.fit(embedding)
    # yHat = kmeans.labels_
    # y = [G.nodes[v]['value'] for v in sorted(G.nodes())]

    # print(y)

#     print('adjusted rand index:', metrics.adjusted_rand_score(y, yHat))
#     print('silhouette coefficient:', metrics.silhouette_score(embedding, yHat))


#   #generate random graphs according to the SBM, embed the nodes with node2vec, cluster the nodes, evaluate the clusters
#   #consider different kinds of community structure based on the SBM
#   if False:
#     C = [5,10,5]
#     P = [[1,0.1,0],[0.1,1,0.1],[0,0.1,1]]
#     G = sbm(C, P)
#     print(G.number_of_nodes(), G.number_of_edges())
#     nx.draw_networkx(G, node_size=100, width=0.5)
#     plt.savefig('temp_sbm_cluster.png', bbox_inches='tight')
#     plt.clf()

#     node2vec = Node2Vec(G, dimensions=10, walk_length=15, num_walks=200, p=1, q=1, workers=1)
#     model = node2vec.fit(window=15, min_count=1)
#     embedding = [model.wv[str(v)] for v in sorted(G.nodes())]

#     tsne = TSNE(n_components=2, init='pca', perplexity=5)
#     pos = tsne.fit_transform(np.array(embedding))
#     print(pos)
#     pos = {v:pos[i] for i,v in enumerate(sorted(G.nodes()))}
#     nx.draw_networkx(G, pos=pos, edgelist=[], alpha=0.5, node_size=100, font_size=5, nodelist=sorted(G.nodes()))
#     plt.savefig('temp_sbm_cluster_2.png', bbox_inches='tight')
#     plt.clf()

#     #cluster with kmeans
#     kmeans = KMeans(3)
#     kmeans.fit(embedding)

#     print(metrics.silhouette_score(embedding, kmeans.labels_))