<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Passenger Count Example</title>
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

    <h1>Python Passenger Count Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code uses a <code>defaultdict</code> from the <code>collections</code> module to manage the number of passengers at various stations. The <code>defaultdict</code> allows for automatic initialization of dictionary values.</p>
        
        <h3>Why?</h3>
        <p>Using a <code>defaultdict</code> simplifies the process of counting items, as it automatically initializes the count to zero for any new key. This eliminates the need for checking if a key exists before updating its value.</p>
        
        <h3>What?</h3>
        <p>The code initializes a <code>defaultdict</code> to keep track of the number of passengers at each station. It then updates the passenger counts for specific stations and prints the total number of passengers at each station.</p>
        
        <h3>How?</h3>
        <p>The code increments the passenger count for each station by using the <code>+=</code> operator. Finally, it iterates through the dictionary to print the number of passengers at each station.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from collections import defaultdict

# Initialize a defaultdict to count passengers
passengers_per_station = defaultdict(int)

# Example: Adding passengers to stations
passengers_per_station['Station1'] += 10  # Station1 now has 10 passengers
passengers_per_station['Station2'] += 5   # Station2 now has 5 passengers
passengers_per_station['Station1'] += 3   # Station1 now has 13 passengers

# Output the number of passengers at each station
for station, count in passengers_per_station.items():
    print(f"{station}: {count} passengers")
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to efficiently count occurrences using <code>defaultdict</code> in Python, making it easier to manage and update counts without additional checks.
    </div>

</body>
</html>