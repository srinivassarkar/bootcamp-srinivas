import json

class MyCollection:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def to_json(self):
        return json.dumps(self.items)

    @classmethod
    def from_json(cls, json_string):
        collection = cls()
        collection.items = json.loads(json_string)
        return collection

# Create a MyCollection
collection = MyCollection()
collection.add("Apple")
collection.add("Banana")

# Serialize to JSON
json_string = collection.to_json()
print("JSON representation of MyCollection:")
print(json_string)

# Deserialize from JSON
loaded_collection = MyCollection.from_json(json_string)
print("Deserialized MyCollection items:")
print(loaded_collection.items)



# 11. Serialization of Custom Collections:
#     - Serialized a custom MyCollection class.
#     - Used JSON for flexibility.

