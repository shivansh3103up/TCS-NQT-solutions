bus_stops = [ "TH", "GA", "IC", "HA", "TE", "LU", "NI","CA" ]
fare = 5
path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
source = input("Enter the souce from the given bus stops:")
destination = input("Enter the destination from bus stops:")
source_index = bus_stops.index(source)
dest_index = bus_stops.index(destination)
distance = 0
for i in range(source_index, len(path)):
    distance += path[i]
print(distance)