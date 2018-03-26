from __future__ import division

import time

class digraph:
    def __init__(self, edgeList):
        """
        Input: a list of pairs (a, b), denoting directed edges a -> b
        
        Attributes:
        V = list of all vertices
        E = list of all edges
        n = number of vertices
        m = number of edges
        A = dictionary of lists of outgoing vertices; keys are vertices, values are lists of outgoing vertices
        """

        self.V = list(set([edge[0] for edge in edgeList] + [edge[1] for edge in edgeList]))
        self.E = edgeList
        self.n = len(self.V)
        self.m = len(edgeList)

        out_neighbors = {}
        for vertex in self.V:
            out_neigh_set = set()
            for edge in self.E:
                if edge[0] == vertex:
                    out_neigh_set.add(edge[1])
            out_neighbors[vertex] = list(out_neigh_set)
        self.A = out_neighbors

class weighted_digraph:
    def __init__(self, edgeDict):
        """
        Input: a dictionary where the keys are pairs (a, b) denoting directed edges a -> b, and the values are the edge weights

        Attributes:
        V = list of all vertices
        E = list of all edges
        n = number of vertices
        m = number of edges
        adjacent = dictionary of lists of outgoing vertices; keys are vertices, values are lists of outgoing vertices
        weight = dictionary representation of weight function; w[(a, b)] = weight of directed edge a -> b
        """

        edgeList = edgeDict.keys()
        
        self.V = list(set([edge[0] for edge in edgeList] + [edge[1] for edge in edgeList]))
        self.E = edgeList
        self.n = len(self.V)
        self.m = len(edgeList)

        out_neighbors = {}
        for vertex in self.V:
            out_neigh_set = set()
            for edge in self.E:
                if edge[0] == vertex:
                    out_neigh_set.add(edge[1])
            out_neighbors[vertex] = list(out_neigh_set)
        self.adjacent = out_neighbors

        self.weight = edgeDict

def bellman_ford(wdg, source):
    """
    Inputs:
    wdg = weighted digraph
    source = source vertex from which the shortest paths to all other vertices are desired
    """
    start = time.time()
    
    distance = {}
    predecessor = {}

    for vertex in wdg.V:
        # Initialize the distances and predecessors
        distance[vertex] = 1e309
        predecessor[vertex] = None
        distance[source] = 0

    # Update the distances and predecessors
    for i in range(wdg.n - 1):
        for edge in wdg.E:                
            if distance[edge[0]] + wdg.weight[edge] < distance[edge[1]]:
                distance[edge[1]] = distance[edge[0]] + wdg.weight[edge]
                predecessor[edge[1]] = edge[0]

    # Check for negative cycles
    for edge in wdg.E:
        if distance[edge[0]] + wdg.weight[edge] < distance[edge[1]]:
            raise Exception("The digraph contains a cycle with negative weight! :(")

    print "Bellman-Ford took {} seconds.".format(time.time() - start)

    return (distance, predecessor)
        

        
