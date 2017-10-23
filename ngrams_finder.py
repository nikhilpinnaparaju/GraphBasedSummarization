import networkx as nx
from tokenizer import tokenized
import matplotlib.pyplot as plt

def ngrams(input_list,n):
     return zip(*[input_list[i:] for i in range(n)])

print("Please enter the grams size for this problem:")
x = int(input())

grams = []

for input_list in tokenized:
    grams.append(list(ngrams(input_list,x)))

# print(grams)

tags = []

for arr in grams:
    for gram in arr:
        # print(gram)
        temp = []
        for i in range(x):
            sent_tags = gram[i].split("_")
            temp.append(sent_tags)
        tags.append(temp)

# print(tags)

edges_list = []

for gram in tags:
    # print(gram,"\n")
    for i in range(x):
        for j in range( x):
            if (gram[i][1][0] == "N" and gram[i][1][1] == "N") and (gram[j][1][0] == "J" and gram[j][1][1] == "J"):
                edge = []
                edge.append(gram[i])
                edge.append(gram[j])
                edges_list.append(edge)

#print(edges_list)

G = nx.Graph()

for edge in edges_list:
    #print(edge[0][0],edge[1][0])
    G.add_node(edge[0][0].lower())
    G.add_node(edge[1][0].lower())
    G.add_edge(edge[0][0].lower(),edge[1][0].lower())

print(G.nodes(),G.edges())
nx.draw(G)
plt.show()

all_nodes = G.nodes()

# scores = {}

# for node in all_nodes:
#     vals = [1,1]
#     scores[node] = vals

# print(scores)

print("Set damping factor (0-1), normally 0.85")

d = float(input())

word_scores = nx.pagerank(G,d)

print(word_scores)

# for i in range(30):
#     cumul = 0
#     for node in all_nodes:
#         # print(node,list(nx.all_neighbors(G,node)))
#         neigh = list(nx.all_neighbors(G,node))
#         for j in neigh:
#             cumul = cumul + 1/(len(neigh))*scores[j][1]
#         scores[node][0] = scores[node][1]
#         scores[node][1] = (1-d) + d*cumul

# print(scores)

f = open('wordscores.txt', 'w')

s = [(k, word_scores[k]) for k in sorted(word_scores, key=word_scores.get, reverse=True)]
for k, word_scores[k] in s:
    v = word_scores[k]
    print(k,v)
    f.write("%s %.18f\n" % (k,v))

f.close()