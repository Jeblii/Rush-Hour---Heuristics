from vehicle import Vehicle
from vehicle_2 import Vehicle_2
from Boards import board
from Algorithms.BreadthFirstSearch import breadthfirstsearch
from Algorithms.AStar import Astar
from Algorithms.Heuristics import *
from Algorithms.Random import randomsearch
from setup import *
import time
from time import sleep
from datetime import datetime

def run_algorithm(algorithm):
    start_time = datetime.now()
    result = algorithm(init_board) #calls on the breadthfirstsearch algorithm
    stop_time = datetime.now()
    elapsed_time = stop_time - start_time
    print('Elapsed Time:', elapsed_time)
    return result

def create_board(txt, size):
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
mylist = load_text("72") #runs the setup file
size = len(mylist) #reads the number of lines of mylist
init_board = create_board(mylist, size) #puts all the vehicles into a generated board

# print(file)
# for i in range(len(init_board.get_board())):
#     print(init_board.get_board()[i]) #prints all the states the algorithm vistis
# print("")

#use x algorithm to solve board
run_algorithm(breadthfirstsearch)
run_algorithm(Astar)