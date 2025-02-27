<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YAML Deserialization</title>
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

    <h1>YAML Deserialization</h1>

    <h2>Why Use YAML Deserialization?</h2>
    <p>
        YAML deserialization is the process of restoring a <code>Car</code> object from its 
        YAML representation. This allows you to easily reconstruct objects from data that has 
        been stored or transmitted in YAML format, making it convenient for data exchange 
        between applications.
    </p>

    <h2>What We Will Do</h2>
    <p>
        We will deserialize a YAML string back into a <code>Car</code> object, enabling us 
        to easily convert YAML data back into a usable Python object.
    </p>

    <h2>How to Deserialize YAML</h2>
    <p>
        Use the <code>yaml.safe_load()</code> function to parse the YAML string and create a 
        <code>Car</code> object.
    </p>

    <h2>Example Code</h2>
    <pre>
import yaml

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def to_yaml(self):
        return yaml.dump(self.__dict__)

    @classmethod
    def from_yaml(cls, yaml_string):
        data = yaml.safe_load(yaml_string)
        return cls(**data)

# Example YAML string
car_yaml = """
make: Tesla
model: Model S
year: 2025
"""

# Create a Car instance from the YAML string
car_instance = Car.from_yaml(car_yaml)
print(car_instance.make)   # Output: Tesla
print(car_instance.model)  # Output: Model S
print(car_instance.year)   # Output: 2022
    </pre>

    <footer>
        <p>Note: This document was created using Blackbox AI.</p>
    </footer>

</body>
</html>