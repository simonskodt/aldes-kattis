class Graph:
    def __init__(self):
        self.graph = {}
        self.SOURCE = 's'
        self.SINK = 't'
        self.add_node(self.SOURCE)
        self.add_node(self.SINK)

    def add_node(self, node):
        if node in self.graph:
            return
        
        self.graph[node] = []

        if node.startswith("C"):
            self.add_edge(self.SOURCE, node)

    def add_edge(self, n1, n2, capacity=1):
        if n1 in self.graph and n2 in self.graph:
            self.graph[n1].append((n2, capacity))

    def get_path_capacity(self, n1, n2):
        if n1 not in self.graph or n2 not in self.graph:
            raise ValueError("Node(s) not in graph")
        
        adjacent_nodes = self.graph[n1]
        for edge in adjacent_nodes:
            if n2 == edge[0]:
                return edge[1]
            
    def update_path_weight(self, n1, n2, new_weight):
        if n1 not in self.graph or n2 not in self.graph:
            raise ValueError("Node(s) not in graph")
        
        adjacent_nodes = self.graph[n1]
        for i, edge in enumerate(adjacent_nodes):
            if n2 == edge[0]:
                adjacent_nodes[i] = (n2, new_weight)
                break   

    def get_adjacent_nodes(self, node):
        return self.graph[node]
    
    def node_has_no_adjacent_nodes(self, node):
        if node not in self.graph:
            return False
        
        return not self.graph[node]