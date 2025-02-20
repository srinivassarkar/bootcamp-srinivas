import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# Create an instance of Car
car = Car("Toyota", "Corolla", 2020)

# Serialize to YAML
yaml_string = yaml.dump(car.__dict__)
print("YAML representation of Car:")
print(yaml_string)



# 5. YAML Serialization:
#    - Serialized a Car object to YAML.
#    - YAML is great for configuration files.

