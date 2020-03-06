# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 19:48:12 2020

@author: baotr
"""
#class Vertex(object):
#    def __init__(self, name):
#        self.name=name
#        self.neighbors=[]
#        
#    def add_neighbor(self, new_neighbor):
#        if new_neighbor not in self.neighbors:
#            self.neighbors.append(new_neighbor)
#            self.neighbors.sort()
            
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
    
    

# finds shortest path between 2 nodes of a graph using BFS
    def bfs_shortest_path(self, start, end):
        # keep track of explored nodes
        visited = []
        # keep track of all the paths to be checked
        queue = [[start]]
        print("initial list of paths: ", queue)
     
        # return path if start is goal
        if start == end:
            return "That was easy! Start = goal"
     
        # keeps looping until all possible paths have been checked
        while queue:
            # pop the first path from the queue
            path = queue.pop(0)
            # get the last node from the path
            node = path[-1]
            if node not in visited:
                neighbours = self.graph_dict[node]
                # go through all neighbour nodes, construct a new path and
                # push it into the queue
                for neighbour in neighbours:
                    new_path = list(path)
                    print("new path:", new_path)
                    
                    new_path.append(neighbour)
                    print("new path 2:", new_path)
                    queue.append(new_path)
                    print("queue: ", queue)
                    # return path if neighbour is goal
                    if neighbour == end:
                        return new_path
     
                # mark node as explored
                visited.append(node)
     
        # in case there's no path between the 2 nodes
        return "So sorry, but a connecting path doesn't exist :("
            
    
#######################################################################        
graph_dict = { "a" : ["b", "c"],
              "b" : ["a"],
              "c" : ["b", "a", "e", "d"],
              "d" : ["b", "c","e"],
              "e" : ["d", "b"],
              "f" : [] }

graph = Graph(graph_dict)
print(graph.bfs_shortest_path("a", "d"))



    
    

            
            
            
            
            
    
