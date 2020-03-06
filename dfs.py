# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:43:07 2020

@author: baotr
"""


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


visited=[]

def dfs(graph, startnode):
    global visited
    visited+=[startnode]
    for neighbor in graph[startnode]:
        if neighbor not in visited:
            dfs(graph, neighbor)
    return visited


print(dfs(graph,"G"))
    