<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Temperature Class Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            color: #2c3e50;
        }
        pre {
            background-color: #fff;
            border: 1px solid #ccc;
            padding: 10px;
            overflow-x: auto;
        }
        .content {
            margin-bottom: 20px;
        }
        .note {
            background-color: #e7f3fe;
            border-left: 6px solid #2196F3;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Python Temperature Class Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Temperature</code> that represents a temperature in Celsius. The class uses a property to manage the temperature value, ensuring that it stays within a valid range.</p>
        
        <h3>Why?</h3>
        <p>Using properties allows for encapsulation of data and validation logic. This ensures that any temperature value assigned to the instance is checked for validity, preventing invalid states.</p>
        
        <h3>What?</h3>
        <p>The <code>celsius</code> property provides a way to get and set the temperature value. The setter method includes validation to ensure that the temperature is within the range of -273.15°C (absolute zero) to 5000°C.</p>
        
        <h3>How?</h3>
        <p>When an instance of the <code>Temperature</code> class is created, the initial temperature is set using the setter. If an invalid temperature is assigned later, a <code>ValueError</code> is raised, which can be caught and handled appropriately.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius  # Uses the setter

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if not (-273.15 <= value <= 5000):
            raise ValueError("Temperature out of range")
        self._celsius = value

# Create an instance
temp = Temperature(25)
print(f"Temperature: {temp.celsius}°C")

# Attempt to set an invalid temperature
try:
    temp.celsius = -300
except ValueError as e:
    print(e)  # Output: Temperature out of range
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to use properties in Python to manage class attributes with validation, ensuring that the temperature value remains within a specified range.
    </div>

</body>
</html>