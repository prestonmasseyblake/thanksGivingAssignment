import json
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import networkx.algorithms.community as nx_comm
import itertools
from networkx.algorithms.community import greedy_modularity_communities
from itertools import combinations
# import sys

#1 







minimum_int = -2400000
# 2 Determine the modularity of the network below. Show your work.

G = nx.Graph()
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 3)
G.add_edge(2, 4)
G.add_edge(3,4)
G.add_edge(3, 5)
G.add_edge(3, 8)
G.add_edge(5, 6)
G.add_edge(6, 7)
G.add_edge(6, 9)
G.add_edge(7, 9)
G.add_edge(7, 8)
G.add_edge(8, 9)
nx.draw_networkx(G)

# plt.show()
# result = nx_comm.modularity(G, [{0,1,2,3,4},{5,6,7,8,9}])
# print("result ", result)
# 3 Write a function modularity(G, C) to calculate the modularity of the graph G 
# where C is a dictionary with nodes as keys and community number as values.
# example C 
c_example =  {
0 : 1,
1: 1,
2: 1,
3: 1,
4: 1,
5: 2,
6: 2,
7: 2

}  

def my_modularity(G, communities, weight="weight", resolution=1):

    def parseCommunities(communities):
        vals = []
        arr = []
        for i in range(len(communities)):
            index_val = False 
            compare_val = -1
            temp_arr = []
            for key in communities:
                if not index_val and communities[key] not in vals:
                    index_val = True
                    compare_val = communities[key]
                    vals.append(compare_val)
                if index_val and communities[key] == compare_val:
                    temp_arr.append(key)
            if len(temp_arr) > 0:
                temp_arr = set(temp_arr)
                # print("this is temp_arr",temp_arr,"this is vals", vals)
                arr.append(temp_arr)
        # print(arr)
        return arr
            
    communities = parseCommunities(communities)
    # print(communities)
    directed = False
    
    out_degree = in_degree = dict(G.degree(weight=weight))
    deg_sum = sum(out_degree.values())
    m = deg_sum / 2
    norm = 1 / deg_sum**2

    def community_contribution(community):
        comm = set(community)
        # print("this is comm", community)
        L_c = sum(wt for u, v, wt in G.edges(
            comm, data=weight, default=1) if v in comm)

        out_degree_sum = sum(out_degree[u] for u in comm)
        in_degree_sum = sum(in_degree[u]
                            for u in comm) if directed else out_degree_sum

        return L_c / m - resolution * out_degree_sum * in_degree_sum * norm
    sums = 0

    for c in communities:
        sums += community_contribution(c)
    # print(map(community_contribution, communities))
    return sums


def greedy_modularity(G,C,  weight="weight", resolution=1):

    print(" this is the C ",C[0]," ",C[1])
    # loop until 1 com  
    m = minimum_int
    # while len(C) != 1:
    temp_C = []
    for (a, b) in zip(C[0],C[1]):
        temp_C.append(a)
        temp_C.append(b)
    idx = 2
    for (a, b) in zip(C[0],C[1]):
        pair_temp = {a,b}
        right_arr =    temp_C[idx:] 
        idx += 2
        M = my_modularity(G,[pair_temp, right_arr ]) 
        print(M)

result = greedy_modularity_communities(G)
# print(result)
def greedy_modularity(G,C,weight="weight",resolution=1):
    # loop until 1 comm 
    while C != len(C):
    # max_m = - infiniti
        max_val = float('-inf')
    # for all pa\irs of coms C1 & C2 
    for (c1,c2) in combinations(C,2):
        C1 = [c1,c2]
    # combine C1, & C2 
        M = my_modularity(G,C1)  
        if M > max_val:
            M = max_val
    # update max M 
    return max_val

karate_graph = nx.karate_club_graph()
result = greedy_modularity_communities(G)
print(result)
print(karate_graph)




# print(nx.greedy_modularity_communities(G) )
# GGG = nx.karate_club_graph()
# c = greedy_modularity_communities(GGG)
# print(c)
    # max m = -infiniti 
    # for all pairs of coms c1 of c2 

    # combine c1 & c2 
    # M = my_modularity(G,C) 
       
    # update maxM 
    # for () 




# C_example = {
#     0: "1",
#     1: "1",
# }
# cc =[{0, 1, 2, 3, 4}, {5, 6, 7, 8, 9}]
# result = my_modularity(G, c_example)
# greedy_modularity(G,cc)
# example_dict = {
#     0: 1,
#     1: 1,
#     2: 1,
#     3: 1,
#     4: 1,
#     5: 2,
#     6: 2,
#     7: 2,
#     8: 2,
#     9: 2,
  

# }
# result = my_modularity(G, example_dict)
# print(result)

# def my_greedyModularity(G):
#     print(G)



# print("result from my function", result)
# 4 


# 5 What is the probability that a random node has degree 95 in G1000,0.1?

# amounts = []
# for i in range(0, 100):
#     G = nx.gnp_random_graph(1000, 0.1)
#     amount = 0
#     for g in  range(len(G.nodes)):
#         val = G.degree[g]
#         if val == 95:
#             amount += 1
#     print(amount)
#     amounts.append(amount)

# print(amounts)
# sum = 0
# for i in range(len(amounts)):  
#     sum += amounts[i] 
# average = sum / len(amounts)
# print(average/1000)


# print(G.degree[g])
# print(G.nodes)

#6

#7 
# ps = [.05,.1,.15,.2,.25,.3,.35,.4,.45,.5,.55,.6,.65,.7,.75,.8,.85,.9,.95]
# values = []
# start = .05
# end = .95
# while start <= end:
#     G = nx.erdos_renyi_graph(1000, start)
#     result = nx.harmonic_centrality(G)
#     sum = 0
#     for r in range(len(result)):
#         print(result[r])
#         sum += result[r]
#     average = sum / 1000
#     values.append(average)
#     print("////////////////////////////////////////////////////////////////")
#     print(average)
#     start += .05
# print(values)
# vv =[511.10466666666684, 549.5716666666665, 574.408, 599.468, 624.277, 649.378, 674.475, 699.621,
#     724.885, 749.395, 774.923, 799.04, 824.535, 849.117, 874.291, 898.649, 924.349, 949.174, 951.234]
# plt.scatter(ps, vv, color='b', label=r'$\alpha=0$', alpha=0.3)
# plt.show()

#8

#9 


#10 


