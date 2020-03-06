# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:58:22 2020

@author: baotr
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 21:47:16 2020

@author: baotr
"""
import heapq

class Vertex:
    def __init__(self, name):
        self.name=name
        self.neighbors={}
    
    def add_neighbor(self, newneighbor, dist):
        if newneighbor not in self.neighbors.keys():
            self.neighbors[newneighbor]=dist    
            
    def get_neighbors(self):
        return self.neighbors
        
    def __str__(self):
       return "{}: {}".format(self.name, self.neighbors)
    
    
    
        
class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict==None:
            graph_dict={}
        self.graph_dict=graph_dict
        self.num_node=0
        
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.graph_dict.keys():
            self.graph_dict[vertex.name]=vertex.neighbors
            self.num_node+=1 

    def __str__(self):
        return "{}".format(self.graph_dict)
   
        
        
    def dijikstra(self, start, goal):
        visited=[]
        distance_dict={v: 10000 for v  in self.graph_dict}
        queue=[(0, start)]
        heapq.heapify(queue)
        
        result_list=[]

        while len(queue):            
            s=heapq.heappop(queue)
            result_list.append(s)
            mindist=s[0]
            chosen_node=s[1][-1]
            for i, j in queue:
                if j[-1]==chosen_node:
                    queue.remove((i,j))
            visited.append(chosen_node)
            print(visited)
            neighbors=self.graph_dict[chosen_node]
            for next in neighbors:
                if next not in visited:
                    if mindist+neighbors[next]<=distance_dict[next]:
                        distance_dict[next]=mindist+neighbors[next]              
                    heapq.heappush(queue, (distance_dict[next], s[1]+next))
            heapq.heapify(queue)
            print(queue) 
            
        for i, j in result_list:
            if j[-1]==goal:
                return  "shortest path: {} with distance: {}".format(j, i)
            

            
        
 

    
#a=Vertex("a")
#a.add_neighbor("b", 7)
#a.add_neighbor("c", 9) 
#a.add_neighbor("f", 14) 
# 
#b=Vertex("b")
#b.add_neighbor("c", 10)
#b.add_neighbor("d", 15)  
#b.add_neighbor("a", 7)  
#
#
#c=Vertex("c")
#c.add_neighbor("d", 11)
#c.add_neighbor("f", 2)
#c.add_neighbor("a", 9)
#c.add_neighbor("b", 10)
#
#
#
#d=Vertex("d")
#d.add_neighbor("e", 6)
#d.add_neighbor("c", 11)
#d.add_neighbor("b", 15)
#
#
#e=Vertex("e")
#e.add_neighbor("f", 9)
#e.add_neighbor("d", 6)
#
#
#f=Vertex("f") 
#f.add_neighbor("e", 9)
#f.add_neighbor("a", 14)
#f.add_neighbor("c", 2)
#
#    
#a=Vertex("a")
#a.add_neighbor("b", 2)
#a.add_neighbor("c", 4) 
#
# 
#b=Vertex("b")
#b.add_neighbor("c", 1)
#b.add_neighbor("d", 5)  
#b.add_neighbor("f", 1) 
#
#c=Vertex("c")
#c.add_neighbor("e", 3)
#c.add_neighbor("d", 2)
#
#d=Vertex("d")
#d.add_neighbor("f", 0.5)
#
#
#e=Vertex("e")
#e.add_neighbor("f", 2)
#
#
#f=Vertex("f")    
    
    
    
#a=Vertex("a")
#a.add_neighbor("b", 7)
#a.add_neighbor("c", 9) 
#a.add_neighbor("f", 14)
# 
#b=Vertex("b")
#b.add_neighbor("c", 10)
#b.add_neighbor("d", 15)  
#
#c=Vertex("c")
#c.add_neighbor("d", 11)
#c.add_neighbor("f", 2)
#
#d=Vertex("d")
#d.add_neighbor("e", 6)
#
#
#e=Vertex("e")
#e.add_neighbor("f", 9)
#
#
#f=Vertex("f")


a=Vertex("a")                        
a.add_neighbor("b", 5)
a.add_neighbor("c", 8) 
a.add_neighbor("d", 3) 
a.add_neighbor("e", 4) 
a.add_neighbor("f", 9)
 
b=Vertex("b")
b.add_neighbor("c", 6)       
b.add_neighbor("d", 1)
b.add_neighbor("e", 5) 
b.add_neighbor("f", 4)  

c=Vertex("c")
c.add_neighbor("d", 3)
c.add_neighbor("e", 9) 
c.add_neighbor("f", 2)

d=Vertex("d")
d.add_neighbor("e", 4)
d.add_neighbor("f", 6)


e=Vertex("e")
e.add_neighbor("f", 3)

f=Vertex("f")



g=Graph()
g.add_vertex(a)
g.add_vertex(b)
g.add_vertex(c)
g.add_vertex(d)
g.add_vertex(e)
g.add_vertex(f)

print(g.dijikstra("a","b"))
        