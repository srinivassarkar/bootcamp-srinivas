import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_json(self):
        data = self.__dict__.copy()
        data.pop("password")  # Skip password
        return json.dumps(data)

# Create a User
user = User("alice", "secret123")

# Serialize to JSON
json_string = user.to_json()
print("JSON representation of User (excluding password):")
print(json_string)




# 8. Skipping Attributes During Serialization:
#    - Excluded sensitive data (e.g., password) during serialization.
#    - Overrode the __dict__ attribute.

