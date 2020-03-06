# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:41:44 2020

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
            
    ## All paths between two nodes
    def find_path(self, start_vertex, end_vertex, path=None, paths=None):
        """ find a path from start_vertex to end_vertex  in graph """
        if path == None:
            path = []
        
        if paths==None:
            paths=[]
        self.paths=paths
    
        if start_vertex not in self.graph_dict.keys():
            return None
    
        path = path + [start_vertex]
        
        if start_vertex == end_vertex:   
            return path
        
        if start_vertex not in self.graph_dict.keys():
            return None
        
        for vertex in self.graph_dict[start_vertex]:
            if vertex not in path:
                new_path = self.find_path(vertex, end_vertex, path, paths) 
                if new_path  and isinstance(new_path[0], str):
                    self.paths.append(new_path)                           
        return  self.paths
    
    
graph_dict = { "a" : ["b", "c"],
              "b" : ["a"],
              "c" : ["b", "a", "e", "d"],
              "d" : ["b", "c","e"],
              "e" : ["d", "b"],
              "f" : [] }

graph = Graph(graph_dict)
print(graph.find_path("a", "d"))