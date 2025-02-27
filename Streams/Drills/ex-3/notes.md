<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Line Generator Example</title>
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

    <h1>File Line Generator in Python</h1>
    <p>This example demonstrates a generator function in Python that reads lines from a file. Generators are a more concise and memory-efficient way to produce values one at a time compared to custom iterator classes.</p>

    <h2>Code Implementation</h2>
    <pre>
def file_line_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Using the generator
for line in file_line_generator('sample.txt'):
    print(line)
    </pre>

    <h2>Explanation</h2>
    <p>The <code>file_line_generator</code> function is a generator that yields lines from a specified file:</p>
    <ul>
        <li><code>yield</code>: This keyword is used to produce a value and pause the function's execution, allowing it to be resumed later. This makes the function a generator.</li>
        <li><code>with open(filename, 'r')</code>: This context manager ensures that the file is properly opened and closed, even if an error occurs.</li>
    </ul>

    <h2>Approach to the Problem</h2>
    <p>The approach taken in this example is to create a generator that reads lines from a specified file. This is particularly useful for handling large files where you want to process one line at a time without consuming too much memory.</p>

    <h2>Why, What, and How</h2>
    <p><strong>Why:</strong> Generators are simpler to write and more memory-efficient for large datasets, making them a preferred choice for many applications.</p>
    <p><strong>What:</strong> This code defines a generator function that yields lines from a file until the end of the file is reached.</p>
    <p><strong>How:</strong> By using the <code>yield</code> keyword, we enable the function to produce values one at a time, allowing for easy traversal of the file's lines in a for loop.</p>

    <div class="note">
        <strong>Note:</strong> This example was created using Blackbox AI.
    </div>

</body>
</html>