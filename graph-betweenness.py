import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import munkres

def draw(G, pos, measures, measure_name):

    nodes = nx.draw_networkx_nodes(G, pos, node_size=250, cmap=plt.cm.plasma, 
                                   node_color=[mv for mv in measures.values()],
                                   nodelist=[mk for mk in measures.keys()])
    nodes.set_norm(mcolors.SymLogNorm(linthresh=0.01, linscale=1))
    
    labels = nx.draw_networkx_labels(G, pos)
    edges = nx.draw_networkx_edges(G, pos)

    plt.title(measure_name)
    plt.colorbar(nodes)
    plt.axis('off')
    plt.show()

###############################################################################

G = nx.Graph()

G.add_edges_from([('hol1','hol2'), ('hol1','sala1'), ('hol1','sala4'),
                 ('hol2','sala2'), ('hol2','wc'), ('hol2','hol3'),
                 ('hol3','sala3'), ('hol3','sala5'),
                 ('sala2', 'closet'), ('sala3', 'closet')])

bet_cen = nx.betweenness_centrality(G)
print()
print("Betwenness centrality: {}".format(bet_cen))

pos = nx.spring_layout(G)
draw(G, pos, bet_cen, 'Betweenness Centrality')

###############################################################################

central_dict = {}
leaf_dict = {}

for (node, val) in bet_cen.items():
    # if betwenness is high enough, it's probably a central node
    if val > 0.3:
        central_dict[node] = {}
        central_dict[node]['centrality'] = val
    else:
        leaf_dict[node] = {} # maybe we'll need centrality here, too
del bet_cen #should probably keep it for comparison with original ground truth floor plan - NOPE, just add centrality to central_dict

print()
print("Leaf nodes dictionary: {}".format(leaf_dict))
print("Central nodes dictionary: {}".format(central_dict))

Bi = nx.Graph()
Bi.add_nodes_from([cnode for cnode in central_dict], bipartite=0)
Bi.add_nodes_from([lnode for lnode in leaf_dict], bipartite=1)
Bi.add_edges_from(G.edges)

print()
print("Bipartite sets: {}".format(nx.bipartite.sets(Bi, [node for node in central_dict])))

for (node, dsts) in dict(nx.shortest_path_length(Bi)).items():
    if node in leaf_dict.keys():
        leaf_dict[node]['weight'] = sum(dsts.values())

print()
print("Leaf nodes dict with weights: {}".format(leaf_dict))