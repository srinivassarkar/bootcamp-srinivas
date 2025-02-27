# Python Passenger Count Example

<div class="content">

## Problem Approach

This Python code uses a `defaultdict` from the `collections` module to manage the number of passengers at various stations. The `defaultdict` allows for automatic initialization of dictionary values.

### Why?

Using a `defaultdict` simplifies the process of counting items, as it automatically initializes the count to zero for any new key. This eliminates the need for checking if a key exists before updating its value.

### What?

The code initializes a `defaultdict` to keep track of the number of passengers at each station. It then updates the passenger counts for specific stations and prints the total number of passengers at each station.

### How?

The code increments the passenger count for each station by using the `+=` operator. Finally, it iterates through the dictionary to print the number of passengers at each station.

</div>

## Python Code

<pre>from collections import defaultdict

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

<div class="note">**Note:** This code demonstrates how to efficiently count occurrences using `defaultdict` in Python, making it easier to manage and update counts without additional checks.</div>