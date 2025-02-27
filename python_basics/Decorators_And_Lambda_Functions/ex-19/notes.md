<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Total Ordering Example</title>
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

    <h1>Python Total Ordering Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>Point</code> that represents a point in a 2D space. The class uses the <code>functools.total_ordering</code> decorator to automatically generate the rich comparison methods based on the defined <code>__lt__</code> (less than) and <code>__eq__</code> (equal to) methods.</p>
        
        <h3>Why?</h3>
        <p>Implementing all comparison methods (<code>__lt__</code>, <code>__le__</code>, <code>__gt__</code>, <code>__ge__</code>, <code>__eq__</code>, and <code>__ne__</code>) can be tedious and error-prone. The <code>total_ordering</code> decorator simplifies this by allowing you to define only the necessary methods, while it automatically provides the rest.</p>
        
        <h3>What?</h3>
        <p>The <code>Point</code> class defines the <code>__lt__</code> method to compare points based on their distance from the origin (calculated as the square root of the sum of the squares of their coordinates) and the <code>__eq__</code> method to check for equality based on their coordinates.</p>
        
        <h3>How?</h3>
        <p>The <code>total_ordering</code> decorator is applied to the <code>Point</code> class, which requires the implementation of at least one less-than method and one equality method. The decorator then generates the other comparison methods automatically.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from functools import total_ordering

@total_ordering
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)

# Example Usage
p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1 < p2)  # Output: True
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to use the <code>total_ordering</code> decorator in Python to simplify the implementation of comparison methods in a class, making it easier to work with custom objects in sorting and comparisons.
    </div>

</body>
</html>