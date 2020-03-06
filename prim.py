from collections import defaultdict
import heapq


class Vertex:
    def __init__(self, name, neighbors=None):
        self.name=name
        if neighbors==None:
            neighbors={}
        self.neighbors=neighbors
    
    def add_neighbor(self, newneighbor, dist):
        if newneighbor not in self.neighbors.keys():
            self.neighbors[newneighbor]=dist
            
    
    def __str__(self):
       return "{}: {}".format(self.name, self.neighbors)
    
    
        
class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict==None:
            graph_dict={}
        self.graph_dict=graph_dict
        
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.graph_dict.keys():
            self.graph_dict[vertex.name]=vertex.neighbors
            
    
    def __str__(self):
       return "{}".format(self.graph_dict)
   
        
    def prim(self, startnode):
       mst=defaultdict(set)
       print(mst)
       visited=set([startnode])
       edges=[(cost, startnode, to) 
           for  to, cost in self.graph_dict[startnode].items() ]
       heapq.heapify(edges)
       print(edges)
   
       while edges:
           cost, fromnode, to = heapq.heappop(edges)
   
           if to not in visited:
                visited.add(to)
                mst[fromnode].add(to)
                for  to_next, cost in self.graph_dict[to].items():
                      if to_next not in visited:
                           heapq.heappush(edges, (cost, to, to_next))
   
       return mst





example_graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'C': 1, 'D': 1, 'E': 4},
    'C': {'A': 3, 'B': 1, 'F': 5},
    'D': {'B': 1, 'E': 1},
    'E': {'B': 4, 'D': 1, 'F': 1},
    'F': {'C': 5, 'E': 1, 'G': 1},
    'G': {'F': 1},
}


g=Graph(example_graph)
print(g)

print(dict(g.prim('A')))