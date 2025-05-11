import random
import string
class Graph:
    def __init__(self, directed=False):
        self.adj_list = {}
        self.directed = directed

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, src, dest, weight=1):
        self.add_node(src)
        self.add_node(dest)
        self.adj_list[src].append((dest, weight))
        if not self.directed:
            self.adj_list[dest].append((src, weight))

    def remove_edge(self, src, dest):
        self.adj_list[src] = [pair for pair in self.adj_list[src] if pair[0] != dest]
        if not self.directed:
            self.adj_list[dest] = [pair for pair in self.adj_list[dest] if pair[0] != src]

    def remove_node(self, node):
        self.adj_list.pop(node, None)
        for src in self.adj_list:
            self.adj_list[src] = [pair for pair in self.adj_list[src] if pair[0] != node]

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

    def __str__(self):
        return '\n'.join(f"{node}: {neighbors}" for node, neighbors in self.adj_list.items())
    
    def get_nodes(self):
        return list(self.adj_list.keys())
    
    def get_edges(self):
        edges = []
        seen = set()
        for src in self.adj_list:
            for dest, weight in self.adj_list[src]:
                if self.directed or (src, dest) not in seen and (dest, src) not in seen:
                    edges.append((src, dest, weight))
                    if not self.directed:
                        seen.add((src, dest))
        return edges
        
    @staticmethod
    def create_random_graph(num_nodes, num_edges, directed=False):
        if num_nodes > 26:
            raise ValueError("Number of nodes cannot exceed 26 (A-Z).")

        graph = Graph(directed)
        nodes = list(string.ascii_uppercase[:num_nodes])

        # Ensure all nodes are added
        for node in nodes:
            graph.add_node(node)

        edge_set = set()
        while len(edge_set) < num_edges:
            src, dest = random.sample(nodes, 2)
            if directed:
                edge = (src, dest)
            else:
                edge = tuple(sorted((src, dest)))

            if edge not in edge_set:
                edge_set.add(edge)
                weight = random.randint(1, 10)  # Random weight between 1 and 10
                graph.add_edge(src, dest, weight)

        return graph