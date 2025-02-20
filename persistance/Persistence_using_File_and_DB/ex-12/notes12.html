<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Serializing Cyclic References</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1, h2 {
            color: #2c3e50;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-left: 5px solid #3498db;
            overflow-x: auto;
        }
        footer {
            margin-top: 20px;
            font-size: 0.9em;
            color: #777;
        }
    </style>
</head>
<body>

    <h1>Serializing Cyclic References</h1>

    <h2>Why Handle Cyclic References?</h2>
    <p>
        Handling cyclic references is important when dealing with objects that reference each 
        other. If not managed properly, serialization can lead to infinite loops or errors. 
        Using a serialization method that supports cyclic references ensures that the data 
        structure can be accurately represented and restored.
    </p>

    <h2>What We Will Do</h2>
    <p>
        We will create two objects that reference each other and serialize them, demonstrating 
        how to handle cyclic references using Pickle.
    </p>

    <h2>How to Serialize Cyclic References</h2>
    <p>
        We will use Pickle’s built-in ability to handle cyclic references, which allows it to 
        track objects that have already been serialized and avoid duplication.
    </p>

    <h2>Example Code</h2>
    <pre>
import pickle

class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

# Create two nodes that reference each other
node1 = Node("Node 1")
node2 = Node("Node 2")
node1.next_node = node2
node2.next_node = node1  # Creating a cyclic reference

# Serialize the nodes
with open('cyclic_nodes.pkl', 'wb') as file:
    pickle.dump(node1, file)

# Deserialize the nodes
with open('cyclic_nodes.pkl', 'rb') as file:
    loaded_node1 = pickle.load(file)
    loaded_node2 = loaded_node1.next_node

print(f"Node 1 Value: {loaded_node1.value}")  # Output: Node 1 Value: Node 1
print(f"Node 2 Value: {loaded_node2.value}")  # Output: Node 2 Value: Node 2
print(f"Node 1's Next Node Value: {loaded_node1.next_node.value}")  # Output: Node 1's Next Node Value: Node 2
print(f"Node 2's Next Node Value: {loaded_node2.next_node.value}")  # Output: Node 2's Next Node Value: Node 1
    </pre>

    <footer>
        <p>Note: This document was created using Blackbox AI.</p>
    </footer>

</body>
</html>