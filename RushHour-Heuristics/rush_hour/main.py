from vehicle import Vehicle
from vehicle_2 import Vehicle_2
from Boards import board
from Algorithms.BreadthFirstSearch import breadthfirstsearch
from Algorithms.BestFirst import BestFirst
from Algorithms.Random import randomsearch
from setup import *
from visualization import visualization
from datetime import datetime

def run_algorithm(algorithm):
    start_time = datetime.now()
    result = algorithm(init_board) #calls on the breadthfirstsearch algorithm
    stop_time = datetime.now()
    elapsed_time = stop_time - start_time
    print('Elapsed Time:', elapsed_time)
    return result

def create_board(mylist, size):
    """
    This function puts the four attributes of each vehicle in an array and loads
    them into the class board
    """
    vehicles = []
    for count in range(len(mylist)):
        if size > 20: #with this number of cars, we can assume that we are dealing with a 9x9 or 12x12
            x = Vehicle_2(int(mylist[count][0]), int(mylist[count][1]), int(mylist[count][2]), int(mylist[count][3]))
            vehicles.append(x)
        else:
            x = Vehicle(int(mylist[count][0]), int(mylist[count][1]),
                        int(mylist[count][2]), int(mylist[count][3]))
            vehicles.append(x)
    new_board = board(vehicles)
    return new_board

mylist = user_setup()
size = len(mylist)                          #reads the number of lines of mylist
init_board = create_board(mylist, size)     #puts all the vehicles into a generated board

algorithm = int(input("What Algorithm would you like to use: "
                      "\nType Number 1 for Breadthfirst\nType Number 2 for Best First\nType Number 3 for Random\n"))
if algorithm == 1:
    winning_state = run_algorithm(breadthfirstsearch)
    if len(winning_state.get_board()) == 6:
        visualization(winning_state)
elif algorithm == 2:
    winning_state = run_algorithm(BestFirst)
    if len(winning_state.get_board()) == 6:
        visualization(winning_state)
elif algorithm == 3:
    run_algorithm(randomsearch)
else:
    print("Invalid value, please try again")
