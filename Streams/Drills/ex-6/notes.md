<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Processing Pipeline Example</title>
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

    <h1>File Processing Pipeline in Python</h1>
    <p>This example demonstrates a file processing pipeline that reads lines from a file, filters them based on a keyword, and counts the number of words in each filtered line. This approach allows for efficient processing of text data.</p>

    <h2>Code Implementation</h2>
    <pre>
def count_words(line):
    return len(line.split())

def file_processing_pipeline(filename, keyword):
    lines = filtered_file_generator(filename, keyword)
    for line in lines:
        word_count = count_words(line)
        print(f"Line: {line} | Word Count: {word_count}")


file_processing_pipeline('sample.txt', 'Python')
    </pre>

    <h2>Explanation</h2>
    <p>The <code>file_processing_pipeline</code> function processes lines from a specified file:</p>
    <ul>
        <li><code>filtered_file_generator(filename, keyword)</code>: This line uses the previously defined generator to filter lines containing the specified keyword.</li>
        <li><code>word_count = count_words(line)</code>: This line counts the number of words in the current line using the <code>count_words</code> function.</li>
        <li><code>print(f"Line: {line} | Word Count: {word_count}")</code>: This line prints the filtered line along with its word count.</li>
    </ul>

    <h2>Approach to the Problem</h2>
    <p>The approach taken in this example is to create a processing pipeline that filters lines from a file based on a keyword and counts the words in each of those lines. This is useful for analyzing text data efficiently.</p>

    <h2>Why, What, and How</h2>
    <p><strong>Why:</strong> A processing pipeline allows for modular and efficient handling of data, making it easier to analyze and transform text.</p>
    <p><strong>What:</strong> This code defines a pipeline that filters lines from a file and counts the words in each filtered line.</p>
    <p><strong>How:</strong> By using generators and helper functions, we enable efficient processing of the file's content, yielding results one line at a time.</p>

    <div class="note">
        <strong>Note:</strong> This example was created using Blackbox AI.
    </div>

</body>
</html>