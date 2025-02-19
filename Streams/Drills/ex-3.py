# A generator is a special type of iterator that uses the yield keyword to produce values one at a time. It is more concise than writing a custom iterator class.


# Why use Generators?
# Generators are simpler to write and more memory-efficient for large datasets.

def file_line_generator(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# Using the generator
for line in file_line_generator('sample.txt'):
    print(line)
    
    
