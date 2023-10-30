# Vorto-Algorithmic-Challenge

Vehicle Routing Problem (VRP) Solver
This program provides a basic solution to a version of the Vehicle Routing Problem (VRP) as described in the Vorto Algorithmic Challenge. The solution uses a simple greedy approach to assign loads to drivers.

Problem Description
A set of loads needs to be completed efficiently by an unbounded number of drivers.
Each load has a pickup and dropoff location specified by Cartesian points.
Driving time between points is the Euclidean distance between them.
Each driver starts and ends at a depot located at (0,0).
A driver may not exceed 12 hours of total drive time.
The total cost of a solution is given by: total_cost = 500*number_of_drivers + total_number_of_driven_minutes.
Usage
To use the program, save it as vrp_solver.py and run it with the input file as an argument:

