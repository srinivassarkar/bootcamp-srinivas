# File Processing Pipeline in Python

This example demonstrates a file processing pipeline that reads lines from a file, filters them based on a keyword, and counts the number of words in each filtered line. This approach allows for efficient processing of text data.

## Code Implementation

<pre>def count_words(line):
    return len(line.split())

def filtered_file_generator(filename, keyword):
    """Generator that yields lines from the file containing the specified keyword."""
    with open(filename, 'r') as file:
        for line in file:
            if keyword in line:
                yield line.strip()  

def file_processing_pipeline(filename, keyword):
    lines = filtered_file_generator(filename, keyword)
    for line in lines:
        word_count = count_words(line)
        print(f"Line: {line} | Word Count: {word_count}")

file_processing_pipeline('sample.txt', 'Python')
    </pre>

## Explanation

The code consists of three main functions:

*   `count_words(line)`: This function takes a line of text as input and returns the number of words in that line by splitting the line into words.
*   `filtered_file_generator(filename, keyword)`: This generator function reads lines from a specified file and yields only those lines that contain the specified keyword.
*   `file_processing_pipeline(filename, keyword)`: This function orchestrates the processing by using the filtered generator to get lines containing the keyword and counting the words in each of those lines.

## Approach to the Problem

The approach taken in this example is to create a processing pipeline that filters lines from a file based on a keyword and counts the words in each of those lines. This is useful for analyzing text data efficiently.

## Why, What, and How

**Why:** A processing pipeline allows for modular and efficient handling of data, making it easier to analyze and transform text.

**What:** This code defines a pipeline that filters lines from a file and counts the words in each filtered line.

**How:** By using generators and helper functions, we enable efficient processing of the file's content, yielding results one line at a time.

<div class="note">**Note:** This example was created using Blackbox AI.</div>