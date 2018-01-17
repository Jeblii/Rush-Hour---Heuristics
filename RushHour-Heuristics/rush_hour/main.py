from vehicle import Vehicle
from Boards import board
from Algorithms.BreadthFirstSearch import breadthfirstsearch
from Algorithms.Random import randomsearch

from setup import *

def create_board(txt):
    vehicles = []
    for count in range(len(mylist)):
        x = Vehicle(int(mylist[count][0]), int(mylist[count][1]), int(mylist[count][2]), int(mylist[count][3]))
        vehicles.append(x)
    new_board = board(vehicles)
    return new_board


mylist = load_text("4000")

print("initial board")
for i in range(len(init_board.get_board())):
    print(init_board.get_board()[i])
print("")

#use x algorithm to solve board
result = breadthfirstsearch(init_board)
#result = randomsearch(init_board)