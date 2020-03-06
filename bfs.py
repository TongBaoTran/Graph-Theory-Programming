## -*- coding: utf-8 -*-
#"""
#Created on Tue Feb 18 22:49:24 2020
#
#@author: baotr
#"""

graph = {
    'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}





## BFS for unweighted path with only startnode
def bfs(self, node, visited=None):
    if visited==None:
        visited=[]
    self.visited=visited
    queue=[node]
    visited+=[node]
    while queue:
        s=queue.pop(0)
        neighbors=self.neighbors(s) 
        for neighbor in neighbors:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    return visited

print(bfs(graph,"G"))



