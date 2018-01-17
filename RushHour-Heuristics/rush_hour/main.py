from vehicle import Vehicle
from vehicle_2 import Vehicle_2
from Boards import board
from Algorithms.BreadthFirstSearch import breadthfirstsearch
from Algorithms.Random import randomsearch
from setup import *

def create_board(txt, size):
    vehicles = []
    for count in range(len(mylist)):
        if size > 20:
            x = Vehicle_2(int(mylist[count][0]), int(mylist[count][1]), int(mylist[count][2]), int(mylist[count][3]))
            vehicles.append(x)
        else:
            x = Vehicle(int(mylist[count][0]), int(mylist[count][1]), int(mylist[count][2]), int(mylist[count][3]))
            vehicles.append(x)
    new_board = board(vehicles)
    return new_board

mylist = user_setup()
size = len(mylist)
init_board = create_board(mylist, size)

print("initial board")
for i in range(len(init_board.get_board())):
    print(init_board.get_board()[i])
print("")

#use x algorithm to solve board
result = breadthfirstsearch(init_board)
