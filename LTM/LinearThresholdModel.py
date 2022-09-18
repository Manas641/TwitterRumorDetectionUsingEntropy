import random
from networkx.readwrite import json_graph
import networkx as nx




def facebook_graph():
    FielName="facebook.txt"
    Graphtype=nx.Graph()
    g= nx.read_edgelist(FielName,create_using=Graphtype,nodetype=int)

    return graphe_TO_json(g)

def graphe_TO_json(g):
    						#(1/g.degree[i])
    data =  json_graph.node_link_data(g,{"link": "links", "source": "source", "target": "target","weight":"weight"})
    data['nodes'] = [ {"id": i, "Infetime":0,"delta_t":0,"energy":0,"activation_time":0,"degree":g.degree[i], "teta": (1/g.degree[i]), "tried_to_be_infected":"false", "neighbors":[n for n in g.neighbors(i)]} for i in range(len(data['nodes'])) ]
    data['links'] = [ {"source":u,"target":v, "weight":(g.degree[u]+g.degree[v])/2} for u,v in g.edges ]
    return data

g=json_graph.node_link_graph(facebook_graph())

def LT (Graph):
    # the initial infected set is 5 % of the hole population
	ListInactiveNodes_not_tried_to_be_activated = []
	ListActiveNodes = []
	for each in range(len(Graph.nodes)):
		if random.random() < 0.25 :
			Graph.nodes[each]['state'] = "active"
			ListActiveNodes.append(each)
		else:
			Graph.nodes[each]['state'] = "inactive"
			ListInactiveNodes_not_tried_to_be_activated.append(each)
			#print(Graph.nodes[each]["teta"])
	while ListInactiveNodes_not_tried_to_be_activated:
		pass
		for each in ListInactiveNodes_not_tried_to_be_activated:
			if Graph.nodes[each]['tried_to_be_infected'] == "true":
				continue
			else:
				Graph.nodes[each]['tried_to_be_infected'] = "true"

				sum_bi = 0
				for neighbor in Graph.nodes[each]['neighbors'] :
					if Graph.nodes[neighbor]['state'] == "active" and Graph.nodes[each]['state'] == "inactive" :
						sum_bi += (1/(Graph.nodes[neighbor]['degree'])) # + Graph.nodes[each]['degree']

				if sum_bi > Graph.nodes[each]['teta'] :
					Graph.nodes[each]['state'] == "active"
					ListActiveNodes.append(each)
				ListInactiveNodes_not_tried_to_be_activated.remove(each)

			print("element inactive and not tried to be activated: ", len(ListInactiveNodes_not_tried_to_be_activated))
			print("element active: ", len(ListActiveNodes))









if __name__ == '__main__':
	LT(json_graph.node_link_graph(facebook_graph()))
