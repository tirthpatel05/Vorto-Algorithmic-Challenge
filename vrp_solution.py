import math
import sys
from turtle import distance
time_required = distance

def euclidean_distance(x1, x2):
    # Calculate Euclidean distance between points
    return math.sqrt((x2[0] - x1[0])**2 + (x2[1] - x1[1])**2)

def total_distance_for_load(pickup, dropoff):
    """
    Calculate total distance.
    """
    # Set the depot location to the origin
    depot = (0, 0)
    # Calculate distance from depot to pickup, pickup to dropoff, dropoff to depot and sum of all distances 
    return euclidean_distance(depot, pickup) + euclidean_distance(pickup, dropoff) + euclidean_distance(dropoff, depot)

def assign_loads_to_drivers(loads):
    """Assign loads to drivers.

    Iterates through loads, appends load_id to current_driver's list if
    the driver can handle the load. If not, creates a new driver with the load.
    Returns a list of drivers, where each driver is a list of load_ids.
    """
    MAX_MINUTES = 12 * 60
    drivers = []
    current_driver = []
    current_time = 0

    for load in loads:
        load_id, pickup, dropoff = load
        distance = total_distance_for_load(pickup, dropoff)
        time_required = distance

        if current_time + time_required <= MAX_MINUTES:
            current_driver.append(load_id)
            current_time += time_required
        else:
            drivers.append(current_driver)
            current_driver = [load_id]
            current_time = time_required

    if current_driver:
        drivers.append(current_driver)

    return drivers

def calculate_total_cost(drivers, loads):
    """Calculate total cost based on drivers and loads."""

    # Calculate total number of drivers
    number_of_drivers = len(drivers)

    # Calculate total driven minutes for all loads
    total_driven_minutes = 0
    for driver in drivers:
        for load_id in driver:
            _, pickup, dropoff = loads[load_id - 1]  # adjusting for 0-based index
            total_driven_minutes += total_distance_for_load(pickup, dropoff)

    # Calculate total cost using drivers' rate and driven minutes
    return 500 * number_of_drivers + total_driven_minutes

def parse_input_file(input_file):
    """
    Parses an input file containing various key-value pairs separated by spaces or tabs.
    Each line represents a distinct set of key-value pairs. The key-value pairs are separated
    by the equals sign (=). 
    """
    loads = []
    with open(input_file, 'r') as f:
        next(f)  # skip header
        for line in f:
            parts = line.strip().split()
            load_id = int(parts[0])
            pickup = tuple(map(float, parts[1][1:-1].split(',')))
            dropoff = tuple(map(float, parts[2][1:-1].split(',')))
            loads.append((load_id, pickup, dropoff))
    return loads

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python vrp_solution.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    loads = parse_input_file(input_file)
    driver_assignments = assign_loads_to_drivers(loads)

    for driver_loads in driver_assignments:
        print(driver_loads)
    total_cost = calculate_total_cost(driver_assignments, loads)
    print(f"Total Cost: {total_cost}")