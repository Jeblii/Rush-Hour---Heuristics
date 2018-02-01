from vehicle import Vehicle
from vehicle_2 import Vehicle_2
from boards import Board
from algorithms.breadth_first import breadth_first_search
from algorithms.best_first import best_first_search
from algorithms.random import random_search
from setup import *
from visualization import visualization
from datetime import datetime


def run_algorithm(algorithm):
    start_time = datetime.now()
    result = algorithm(init_board)
    stop_time = datetime.now()
    elapsed_time = stop_time - start_time
    print('Elapsed Time:', elapsed_time)
    return result, elapsed_time


def create_board(grid, size):
    """
    This function puts the four attributes of each vehicle in an array and loads
    them into the class board
    """
    vehicles = []
    for count in range(len(grid)):
        if size > 20: #with this number of cars, we can assume that we are dealing with a 9x9 or 12x12
            x = Vehicle_2(int(grid[count][0]), int(grid[count][1]),
                          int(grid[count][2]), int(grid[count][3]))
            vehicles.append(x)
        else:
            x = Vehicle(int(grid[count][0]), int(grid[count][1]),
                        int(grid[count][2]), int(grid[count][3]))
            vehicles.append(x)
    new_board = Board(vehicles)
    return new_board


grid = user_setup()
size = len(grid)                          #reads the number of lines of mylist
init_board = create_board(grid, size)     #puts all the vehicles into a generated board

algorithm = int(input("What Algorithm would you like to use: "
                      "\nType Number 1 for Breadth First\nType Number 2 for Best First\nType Number 3 for Random\n"))


if algorithm == 1:
    result, elapsed_time = run_algorithm(breadth_first_search)
    if len(result[0].get_board()) == 6:
        visualization(result[0], result[1], elapsed_time, 'Breadth First Search')
elif algorithm == 2:
    result, elapsed_time = run_algorithm(best_first_search)
    if len(result[0].get_board()) == 6:
        visualization(result[0], result[1], elapsed_time, 'Best First Search')
elif algorithm == 3:
    run_algorithm(random_search)
else:
    print("Invalid value, please try again")
