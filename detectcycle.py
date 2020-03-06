from collections import defaultdict 

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
    
    def num_node(self):
        return len(self.graph_dict.keys())
            
            
            
    def dfs_parent(self, startnode, visited=None, parent_dict=None):
        if parent_dict==None:
            parent_dict=defaultdict(list)
        self.parent_dict=parent_dict
            
        if visited==None: 
            visited=[]
        self.visited=visited
        
        visited+=[startnode]
        next_list=self.graph_dict[startnode]
        
        for next in next_list:
            if next not in visited:
                parent_dict[next]=startnode
                self.dfs_parent(next, visited, parent_dict)      
        return visited, parent_dict
 
    
    def detect_cycle(self, startnode):  ## neighbors in visited but not parent->cycle
        x=self.dfs_parent(startnode)
        path= x[0]
        parent_dict=x[1]
        visited=[]
        isCycle=False
        for node in path:
            if node==startnode:
                visited.append(node)
            else:
                visited.append(node)
                neighbors=self.graph_dict[node]
                neighbors_visited=[x for x in neighbors if x in visited]
                for i in neighbors_visited:
                    if i != parent_dict[node]:
                        isCycle=True
            print(node, isCycle)
        return isCycle
        

    
graph_dict = { "a" : ["b", "c"],
              "b" : ["d"],
              "c" : ["e"],
              "d" : [],
              "e" : ["b"] }

graph = Graph(graph_dict)


print(graph.dfs_parent("a")[0])
print(graph.dfs_parent("a")[1])   
print(graph.detect_cycle("a"))
            
                

        
        
            

