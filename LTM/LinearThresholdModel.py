import random
from networkx.readwrite import json_graph
import networkx as nx

def facebook_graph():
    FileName="facebook.txt"
    Graphtype=nx.Graph()
    g= nx.read_edgelist(FileName,create_using=Graphtype,nodetype=int)

    return graphe_TO_json(g)

def graphe_TO_json(g):
    data =  json_graph.node_link_data(g,{"link": "links", "source": "source", "target": "target","weight":"weight"})
    data['nodes'] = [ {"id": i, "delta_t":0,"energy":0,"activation_time":0,"degree":g.degree[i], "teta": (1/g.degree[i]), "neighbors":[n for n in g.neighbors(i)]} for i in range(len(data['nodes']))]
    data['links'] = [ {"source":u,"target":v, "weight":(g.degree[u]+g.degree[v])/2} for u,v in g.edges]
    return data

g=json_graph.node_link_graph(facebook_graph())

def LT (Graph):
    # the initial infected set is 5 % of the hole population
    t = 0
    for each in range(len(Graph.nodes)):
        if random.random() < 0.25 :
            Graph.nodes[each]['state'] = "active"
            Graph.nodes[each]['energy'] = 3
            Graph.nodes[each]['activation_time'] = t
            Graph.nodes[each]['delta_t'] = t - Graph.nodes[each]['activation_time']
        else:
            Graph.nodes[each]['state'] = "inactive"

    tick = 0
    while tick<10:
        t += 1
        for each in range(len(Graph.nodes)):
            if Graph.nodes[each]["state"] == "inactive":
                sum_bi = 0
                for neighbor in Graph.nodes[each]['neighbors']:
                    if Graph.nodes[neighbor]['state'] == "active" and Graph.nodes[each]['state'] == "inactive" :
                        sum_bi += (1/(Graph.nodes[neighbor]['degree']))

                if sum_bi > Graph.nodes[each]['teta']:
                    if random.random() < 0.10:
                        node_id = Graph.nodes[each]
                        print(f"Rumor Stopped at Node id: {each}")
                        break
                    Graph.nodes[each]['state'] = "active"
                    Graph.nodes[each]['energy'] = 3
                    Graph.nodes[each]['activation_time'] = t
                    Graph.nodes[each]['delta_t'] = t - Graph.nodes[each]['activation_time']

        for each in range(len(Graph.nodes)):
            if Graph.nodes[each]['energy'] > 0:
                Graph.nodes[each]['energy'] -= 1
                if Graph.nodes[each]['energy'] == 0:
                    Graph.nodes[each]['state'] = "inactive"
                    Graph.nodes[each]['delta_t'] = 0
        tick += 1

if __name__ == '__main__':
    LT(json_graph.node_link_graph(facebook_graph()))
