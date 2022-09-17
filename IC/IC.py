import random
from networkx.readwrite import json_graph
import networkx as nx
import statistics



def facebook_graph():
    FielName="facebook.txt"
    Graphtype=nx.Graph()
    g= nx.read_edgelist(FielName,create_using=Graphtype,nodetype=int)
    
    return graphe_TO_json(g)

def facebook_direct_graph():
    FielName="facebook.txt"
    Graphtype=nx.DiGraph()
    g= nx.read_edgelist(FielName,create_using=Graphtype,nodetype=int)
    
    return graphe_TO_json(g), g.number_of_edges()


def graphe_TO_json(g):
    						#(1/g.degree[i])
    data =  json_graph.node_link_data(g,{"link": "links", "source": "source", "target": "target","weight":"weight"})
    data['nodes'] = [ {"id": i, "Infetime":0,"degree":g.degree[i], "activation_prob": random.random(), "try_activate_a_neighbor":{n:"false" for n in g.neighbors(i)}, "neighbors":[n for n in g.neighbors(i)]} for i in range(len(data['nodes'])) ]
    data['links'] = [ {"source":u,"target":v, "weight":(g.degree[u]+g.degree[v])/2} for u,v in g.edges ]
    return data




def IC (Graph, number_of_edges):
	
    # the initial infected set is 5 % of the hole population 
	NodesCanActive_neighbors = set()
	
	## select the initial set of active nodes##########################
	ListActiveNodes = set()
	for each in range(len(Graph.nodes)):	
		NodesCanActive_neighbors.add(each)
		if random.random() < 0.05 :
			Graph.nodes[each]['state'] = "active"
			ListActiveNodes.add(each)
		else:
			Graph.nodes[each]['state'] = "inactive"
			#print(Graph.nodes[each]["teta"])

	##################################################################
	number_of_nodes = Graph.number_of_nodes()
	#print( Graph.nodes[1]['try_activate_a_neighbor'][119])
	print(number_of_nodes)
	print(len(ListActiveNodes))
	


	#########################################################################""
	while  NodesCanActive_neighbors:
		
		for each in NodesCanActive_neighbors:
			if Graph.nodes[each]['state'] == 'active':

				for key in Graph.nodes[each]['neighbors'] :
					
					# check if there is at least one neighor that this current node doesn't try to activate. # key is the neighbor and : value is the boolean
					if Graph.nodes[each]['try_activate_a_neighbor'][key]=='false' and Graph.nodes[key]['state'] == "inactive" and Graph.nodes[each]['state'] == "active" : 
					
						Graph.nodes[each]['try_activate_a_neighbor'][key] = 'true'
						# then the node will try to activate this neighbor
						#print('i am vefore random')
						if random.random() < statistics.mean((Graph.nodes[each]['activation_prob'], Graph.nodes[key]['activation_prob'])):
							#print('i am after radommmmmmmmmmmmmmmmm')
							Graph.nodes[key]['state'] == "active"
							
							if key in Graph.nodes:
								ListActiveNodes.add(key)
							

			
		for each in range(len(Graph.nodes))	:
			cant_activate_neghbors = 'true'

			for key in Graph.nodes[each]['try_activate_a_neighbor'].keys():
				if Graph.nodes[each]['try_activate_a_neighbor'][key] == 'false':
					
					cant_activate_neghbors = 'false'

			if cant_activate_neghbors and each in NodesCanActive_neighbors:
				NodesCanActive_neighbors.remove(each)					
				#print('i did got it removed yeah : ')
		print("element active: ", len(ListActiveNodes))			
		

		
if __name__ == '__main__':
	facebook_direct_graph, number_of_edges = facebook_direct_graph()
	g=json_graph.node_link_graph(facebook_direct_graph)
	IC(g, number_of_edges)