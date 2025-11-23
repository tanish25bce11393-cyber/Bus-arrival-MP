import random

# Sample bus routes with distances (in km)
routes = {
    "South MP": {
        "stops": ["Indore", "Ashta", "Sehore", "VIT Bhopal"],
        "distance": [115,45,38]  # distances between stops
    },
    "Central MP": {
        "stops": ["VIT Bhopal", "Vidisha", "Sagar", "Khajuraho", "Satna"],
        "distance": [57, 111, 203, 115]
    },
    "North MP": {
        "stops": ["Jhansi", "Shivpuri", "Gwalior"],
        "distance": [99, 116]
    }
}

AVERAGE_SPEED = 55  # km/h


def show_routes():
    print("\nAvailable Bus Routes:")
    route_names = list(routes.keys())
    index = 0
    while index < len(route_names):
        print(str(index + 1) + ". " + route_names[index])
        index += 1


def get_next_bus_time():
    """Simulates next bus arrival (random between 1–10 minutes)."""
    return random.randint(1, 10)


def calculate_travel_time(distance):
    """Returns travel time in minutes."""
    return round((distance / AVERAGE_SPEED) * 60)


def show_stops(stops):
    i = 0
    while i < len(stops):
        print(str(i + 1) + ". " + stops[i])
        i += 1


def transport_system():
    print("=== BUS ARRIVAL MP ===")

    show_routes()

    # User selects a route
    choice = int(input("\nSelect a route number: "))
    route_names = list(routes.keys())
    route_name = route_names[choice - 1]
    route_data = routes[route_name]

    print("\nYou selected:", route_name)
    print("Stops:", " → ".join(route_data['stops']))

    # User selects start and end stops
    print("\nChoose your boarding stop:")
    show_stops(route_data['stops'])
    start = int(input("Start stop number: ")) - 1

    print("\nChoose your destination stop:")
    show_stops(route_data['stops'])
    end = int(input("Destination stop number: ")) - 1

    if end <= start:
        print("\n❌ Destination must be AFTER the start stop.")
        return

    # Calculate total distance
    total_distance = 0
    i = start
    while i < end:
        total_distance += route_data['distance'][i]
        i += 1

    # Estimated travel time
    travel_time = calculate_travel_time(total_distance)

    # Next bus arrival
    next_bus = get_next_bus_time()

    print("\n=== RESULT ===")
    print("Next bus arrives in:", next_bus, "minutes")
    print("Distance between stops:", total_distance, "km")
    print("Estimated travel time:", travel_time, "minutes")

    print("\nHave a safe journey!")


# Run the system
transport_system()