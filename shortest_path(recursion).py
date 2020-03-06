# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:45:58 2020

@author: baotr
"""

class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict={}
        self.graph_dict=graph_dict
    
    def neighbors(self, node):
        return self.graph_dict[node]

        
    def add_vertex(self, vertex):
        if vertex not in self.graph_dict.keys():
            self.graph_dict[vertex]=[]
            
    def vertices(self):
        return list(self.graph_dict.keys())
            
    def add_edge(self, edge):
        vert1, vert2 = edge[0], edge[1]
        if vert1 in self.graph_dict.keys():
            self.graph_dict[vert1].append(vert2)
        else:
            self.graph_dict[vert1]=[vert2]
    
# finds shortest path between 2 nodes of a graph using DFS        
    def shortest_path(self, start_vertex, end_vertex, path=None, paths=None):
        """ find shortest path from start_vertex to end_vertex  in graph """
        if path == None:
            path = []
        self.path=path
        
        if paths==None:
            paths=[]
        self.paths=paths
          
        shortest = None
        path = path + [start_vertex]
        
        if start_vertex == end_vertex:   
            return path
        
        for vertex in self.graph_dict[start_vertex]:
            if vertex not in path:
                new_path = self.shortest_path(vertex, end_vertex, path, paths) 
                if new_path:
                    if not shortest or len(new_path)<len(shortest):
                        shortest=new_path                        
        return  shortest
    
    
graph_dict = { "a" : ["b", "c"],
              "b" : ["a"],
              "c" : ["b", "a", "e", "d"],
              "d" : ["b", "c","e"],
              "e" : ["d", "b"],
              "f" : [] }

graph = Graph(graph_dict)
print(graph.shortest_path("a", "d"))