import json

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def to_json(self):
        return json.dumps({
            "nodes": list(self.nodes),
            "edges": self.edges
        })

# Create a Graph
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_edge("A", "B")

# Serialize to JSON
json_string = graph.to_json()
print("JSON representation of Graph:")
print(json_string)





# 7. Custom Serialization for Complex Objects:
#    - Implemented custom logic to serialize a Graph object.
#    - Used dictionaries to represent nodes and edges.

