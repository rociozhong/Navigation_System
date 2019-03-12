import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

edgelist = pd.read_csv("/Users/rociozhong/PycharmProjects/A7_graphs_nav/edge_data.csv")

edgelist.head(10)

nodelist = pd.read_csv("/Users/rociozhong/PycharmProjects/A7_graphs_nav/nodes.csv")

nodelist.head(5)
# Create empty graph
g = nx.DiGraph()

# Add edges and edge attributes
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())

# Add node attributes
for i, nlrow in nodelist.iterrows():
    g.node[nlrow['id']].update(nlrow[1:].to_dict())

print(nlrow)


# Preview first 5 edges
list(g.edges(data=True))[0:5]

# Preview first 10 nodes
list(g.nodes(data=True))[0:10]

print('# of edges: {}'.format(g.number_of_edges()))
print('# of nodes: {}'.format(g.number_of_nodes()))

edge_type = dict([((e[0], e[1]), e[2]['attr_dict']['distance']) for e in g.edges(data=True)])

edge_colors = [e[2]['attr_dict']['color'] for e in g.edges(data=True)]

#edge_weights = dict([((e[0], e[1]), e[2]['attr_dict']['distance']) for e in g.edges(data=True)])

# Define node positions data structure (dict) for plotting
node_positions = {node[0]: (node[1]['left'], -node[1]['top']) for node in g.nodes(data=True)}

dict(list(node_positions.items())[0:5])


# calculate distance between two nodes using nodelist dataframe

dist_result1 =[]
for i in range(1, nodelist.shape[0]):
    for j in range(1, nodelist.shape[0]):
        temp_dict = {}
        if i !=j:
            temp = np.sqrt(np.square(nodelist.iloc[i]['left'] - nodelist.iloc[j]['left']) + \
            np.square(nodelist.iloc[i]['top'] - nodelist.iloc[j]['top']))
            temp = round(temp/100, 2)
            temp_dict['distance'] = temp
            t = ((nodelist.iloc[i]['id'], nodelist.iloc[j]['id']), )
            t += (temp_dict, )
            dist_result1.append(t)


plt.figure(figsize=(8, 6))
nx.draw(g, pos=node_positions, edge_color=edge_colors, node_size=1000, node_color='skyblue', alpha=0.8)
graph_pos = nx.spring_layout(g, weight=3)
nx.draw_networkx_edges(g, graph_pos, edge_color=edge_colors)
nx.draw_networkx_labels(g, pos=node_positions, font_size=8)
nx.draw_networkx_edge_labels(g, pos=node_positions, edge_labels=edge_type, font_size=6)

#labels = [(e[2]['attr_dict']['Type_of_road'], e[2]['attr_dict']['color']) for e in g.edges(data=True)]
plt.title('Zoo Map', size=20)
line1, = plt.plot([1,2,3], label='Not for Disabled', color='red', linewidth=2)
line2, = plt.plot([3,2,1], label='Accessible route – ADA', color='gray', linewidth=2)
plt.legend(handles=[line1, line2])
#plt.show()
plt.savefig('St Louis Zoo.png')








#
# g.add_edges_from(list(g.edges(data=True)))
# initialpos = node_positions
# pos = nx.spring_layout(g,weight='distance', pos = initialpos)
#
# nx.draw_networkx(g,pos)
#
# import pylab as plt
# plt.savefig('test.png')


