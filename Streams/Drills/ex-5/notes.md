<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multiply by Two Generator Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        pre {
            background-color: #eaeaea;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .note {
            background-color: #d9edf7;
            border-left: 5px solid #31708f;
            padding: 10px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Multiply by Two Generator in Python</h1>
    <p>This example demonstrates a generator function in Python that takes an iterator and yields each item multiplied by two. This approach allows for efficient processing of sequences without creating additional lists in memory.</p>

    <h2>Code Implementation</h2>
    <pre>
def multiply_by_two(iterator):
    for item in iterator:
        yield item * 2

# Using the function
numbers = range(1, 6)  
processed_numbers = multiply_by_two(numbers)
for num in processed_numbers:
    print(num)
    </pre>

    <h2>Explanation</h2>
    <p>The <code>multiply_by_two</code> function is a generator that processes each item from the provided iterator:</p>
    <ul>
        <li><code>for item in iterator</code>: This line iterates through each item in the input iterator.</li>
        <li><code>yield item * 2</code>: This line yields the result of multiplying the current item by two, allowing the function to produce values one at a time.</li>
    </ul>

    <h2>Approach to the Problem</h2>
    <p>The approach taken in this example is to create a generator that processes an input iterator and yields modified values. This is particularly useful for transforming data in a memory-efficient manner.</p>

    <h2>Why, What, and How</h2>
    <p><strong>Why:</strong> Using a generator for transformations allows for efficient memory usage, especially when dealing with large datasets.</p>
    <p><strong>What:</strong> This code defines a generator function that yields each number from the input iterator multiplied by two.</p>
    <p><strong>How:</strong> By using the <code>yield</code> keyword, we enable the function to produce transformed values one at a time, allowing for easy traversal in a for loop.</p>

    <div class="note">
        <strong>Note:</strong> This example was created using Blackbox AI.
    </div>

</body>
</html>