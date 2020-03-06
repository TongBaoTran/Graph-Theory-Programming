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
    

    
    ## DFS with only startnode
    def dfs(self, start, visited=None):
        if visited==None:
            visited=[]
        self.visited=visited
        self.visited += [start]        
        neighbors = self.neighbors(start)
        for i in neighbors:
            if i not in visited:
                self.dfs(i, visited)
        return self.visited
    
    def connectedComponents(self):
        visited=[]
        cc=[]
        for node in self.graph_dict.keys():
            if node not in visited:
                cc.append(self.dfs(node))
                visited+=self.dfs(node)
        return cc
        
        
  
# Driver Code 
if __name__=="__main__": 
    
    graph_dict={"A": ["B", "C"],
                "B": ["A", "C", "D", "E"],
                "C": ["A", "B", "E"],
                "D": [],
                "E": ["B", "C"],
                "M": ["N", "F"],
                "N": ["M", "F"],
                "F": ["M", "N"]
                  }
      
    g=Graph(graph_dict)
    cc = g.connectedComponents() 
    print("Following are connected components") 
    print(cc) 