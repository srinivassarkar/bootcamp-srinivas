<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Transport Network Example</title>
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

    <h1>Python Transport Network Example</h1>

    <div class="content">
        <h2>Problem Approach</h2>
        <p>This Python code defines a class called <code>TransportNetwork</code> that manages routes, schedules, and passengers. The class provides methods to add routes, update schedules, add passengers, and analyze the network.</p>
        
        <h3>Why?</h3>
        <p>Managing a transport network requires efficient handling of routes, schedules, and passenger data. This implementation provides a structured way to manage these elements and perform various analyses.</p>
        
        <h3>What?</h3>
        <p>The <code>TransportNetwork</code> class can add routes, update schedules, add passengers to stations, calculate the total number of unique stations, find the most frequented station, sort routes by the number of stops, and merge with another transport network.</p>
        
        <h3>How?</h3>
        <p>The class uses a list to store routes, a dictionary to map routes to schedules, and a <code>defaultdict</code> to manage passengers per station. Various methods are defined to perform the required operations on the transport network.</p>
    </div>

    <h2>Python Code</h2>
    <pre>
from collections import defaultdict, Counter

class TransportNetwork:
    def __init__(self):
        self.routes = []  # List of routes
        self.schedules = {}  # Dictionary mapping routes to schedules
        self.passengers = defaultdict(list)  # Defaultdict for passengers per station

    def add_route(self, route):
        self.routes.append(route)

    def update_schedule(self, route, schedule):
        self.schedules[route] = schedule

    def add_passenger(self, station, passenger):
        self.passengers[station].append(passenger)

    def total_unique_stations(self):
        stations = set()
        for schedule in self.schedules.values():
            for stop in schedule:
                stations.add(stop.station)
        return len(stations)

    def most_frequented_station(self):
        station_counts = Counter()
        for passengers in self.passengers.values():
            station_counts.update(passengers)
        return station_counts.most_common(1)[0]

    def sort_routes_by_stops(self):
        return sorted(self.routes, key=lambda x: len(self.schedules.get(x, [])))

    def merge_network(self, other_network):
        self.routes.extend(other_network.routes)
        for route, schedule in other_network.schedules.items():
            self.schedules[route] = schedule
        for station, passengers in other_network.passengers.items():
            self.passengers[station].extend(passengers)

# Example Usage
# Create instances and use the TransportNetwork class as needed
    </pre>

    <div class="note">
        <strong>Note:</strong> This code demonstrates how to manage a transport network in Python, including the ability to analyze and merge different networks.
    </div>

</body>
</html>