# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 18:59:58 2020

@author: baotr
"""

from GraphTheory import Graph
import unittest

class Graphtheory_Test(unittest.TestCase):
    

    def setUp(self):
        graph_dict={ "a" : ["b", "c"],
                             "b" : ["a"],
                             "c" : ["b", "a","e", "d"],
                             "d" : ["b", "c","e"],
                             "e" : ["d", "b"],
                             "f" : [] }
        self.graph=Graph(graph_dict)
        print("set up")
        
    def tearDown(self):
        print("tear Down \n")
    
    def test_bfs(self):
        print("Testing bfs")
        self.assertEqual(self.graph.bfs("a"),['a', 'b', 'c', 'e', 'd'] )
    
    def test_dfs(self):
        print("Testing dfs")
        self.assertEqual(self.graph.dfs("a"),['a', 'b', 'c', 'e', 'd'] )
        
    def test_findpath(self):
        print("Testing find path")
        self.assertEqual(self.graph.find_path("a", "d"),[['a', 'c', 'e', 'd'], ['a', 'c', 'd']] )  
        
    def test_shortest(self):
        print("Testing shortest path")
        self.assertEqual(self.graph.shortest_path("a", "d"), ['a', 'c', 'd'])  


if __name__ == '__main__':
    unittest.main()        
        
        
        
        