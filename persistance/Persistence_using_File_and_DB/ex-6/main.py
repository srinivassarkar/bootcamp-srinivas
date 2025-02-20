import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

# YAML string
yaml_string = """
make: Toyota
model: Corolla
year: 2020
"""

# Deserialize from YAML
data = yaml.safe_load(yaml_string)
car = Car(**data)
print("Deserialized Car object:")
print(f"Make: {car.make}, Model: {car.model}, Year: {car.year}")





# 6. YAML Deserialization:
#    - Restored a Car object from its YAML representation.
#    - Used PyYAML for parsing.

