<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Class Method Decorator Example</title>
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

    <h1>Python Class Method Decorator Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a decorator called <code>add_method</code> that adds a new method to a class dynamically. The decorator is applied to the <code>MyClass</code> class, allowing instances of this class to call the newly added method.</p>
        
        <h3>Why?</h3>
        <p>Using decorators to modify classes can be useful for adding functionality without altering the original class definition. This approach promotes code reusability and separation of concerns.</p>
        
        <h3>What?</h3>
        <p>The <code>add_method</code> decorator defines a new method called <code>new_method</code> and attaches it to the class it decorates. This method returns a simple string when called.</p>
        
        <h3>How?</h3>
        <p>When the <code>MyClass</code> class is defined, the <code>add_method</code> decorator is applied, adding the <code>new_method</code> to the class. An instance of <code>MyClass</code> is created, and the new method is called to demonstrate its functionality.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
def add_method(cls):
    def new_method(self):
        return "This is a new method!"
    cls.new_method = new_method
    return cls

@add_method
class MyClass:
    pass

# Create an instance and call the new method
obj = MyClass()
print(obj.new_method())  # Output: This is a new method!
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to use decorators in Python to dynamically add methods to classes, enhancing their functionality without modifying the original class definition.
    </div>

</body>
</html>