from collections import defaultdict

passengers_per_station = defaultdict(int)

# Example: Adding passengers to stations
passengers_per_station['Station1'] += 10  # Station1 now has 10 passengers
passengers_per_station['Station2'] += 5   # Station2 now has 5 passengers
passengers_per_station['Station1'] += 3   # Station1 now has 13 passengers

# Output the number of passengers at each station
for station, count in passengers_per_station.items():
    print(f"{station}: {count} passengers")