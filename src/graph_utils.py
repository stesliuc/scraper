# Script to create a Graph class
# This script should allow you to initiate an empty graph
# Add nodes and edges to it
# And define some method of traversing the graph


class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if not node:
            raise TypeError
        if node not in self.graph:
            self.graph[node] = {'edges': [],
                                'content': []}

    def add_edge(self, from_node, to_node):
        # Check that the from node is not None
        self.add_node(from_node)
        # If To node isn't already connected, create edge
        if to_node not in self.graph[from_node]['edges']:
            self.graph[from_node]['edges'].append(to_node)

    def get_edges(self, node):
        return self.graph.get(node, {'edges': [],
                                     'content': []})['edges']

    def get_content(self, node):
        return self.graph.get(node, {'edges': [],
                                     'content': []})['content']

    def add_content(self, node, content):
        if node:
            self.graph[node]['content'].append(content)
