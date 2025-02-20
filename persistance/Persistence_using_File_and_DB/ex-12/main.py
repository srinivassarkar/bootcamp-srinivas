import pickle

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbor = None

# Create two nodes
node1 = Node("Node 1")
node2 = Node("Node 2")

# Create a cyclic reference
node1.neighbor = node2
node2.neighbor = node1

# Serialize to a file
with open("cyclic_nodes.pkl", "wb") as file:
    pickle.dump(node1, file)

# Deserialize from the file
with open("cyclic_nodes.pkl", "rb") as file:
    loaded_node1 = pickle.load(file)

print("Deserialized cyclic nodes:")
print(f"Node 1: {loaded_node1.name}, Neighbor: {loaded_node1.neighbor.name}")


# 12. Serializing Cyclic References:
#     - Handled objects with cyclic references.
#     - Pickle automatically manages cyclic references.