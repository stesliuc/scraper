# Script to create a Graph class
# This script should allow you to initiate an empty graph
# Add nodes and edges to it
# And define some method of traversing the graph

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append(to_node)

    def get_edges(self, node):
        return self.graph.get(node, [])
