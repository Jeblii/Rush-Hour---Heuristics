from copy import deepcopy
import numpy as np
def breadthfirstsearch(board, maxDepth=100):
    """
    An implementation of breadth first search; checks states on the order FIFO
    function terminates, when solution is found or max depth is reached
    :param board: call function with a boardstate
    :param maxDepth: max depth of the tree till search terminates
    :return:
    """
    queue = [board]
    visit = dict()
    key = board.get_board()
    visit[key.tostring()]= 1

    for depth in range(0, maxDepth):
        new_generation = []
        visited = set()

        for individual in range(len(queue)):
            print("depth is", depth + 1)
            print("checking node:", individual ,"/", len(queue),"\n")
            next_board = queue[individual]

            #visit_count += 1                                                #number of visited states in the breadthfirstsearch
            #visit[visit_count] = queue[individual].get_board()              #create key for a visited state in visit dictionary

            new_gen = next_board.calculate_next_move()
                                                                     #save the states of new_gen that are already in visit dictionary
            # for i in new_gen:
            #     for o in visit.values():
            #         if np.array_equal(i.get_board(), o) == True:
            #             ng.append(i)
            # for i in ng:                                                    #remove the visited states from new_gen -> will not show a visited state as child
            #     if i in new_gen:
            #         new_gen.remove(i)


            for child in new_gen:
                new_key = child.get_board()
                if new_key.tostring() in visit:
                    continue
                else:
                    visit[new_key.tostring()] = 1
                    if child.vehicles[0].x == 4: #if solution is found

                        visit[len(visit)+1] = child.get_board()                 #add last visited state to visit dictionary

                        print("Total visited states:",len(visit))
                        # for i in visit.values():                            #prints all the visited states in breatdhfirst search
                        #     print(i)                                        #<- uncomment this section if you want to seethe visited states in the breadthfirstsearch

                        print("\nReversed solution route")
                        get_parents(child)

                        return
                    new_generation.append(child)
                    print(child.get_board(), "\n")
                visited.add(child)
        queue = new_generation
    return visited

def get_parents(winning_state):
    solution_steps = []
    parent = winning_state.parent
    while parent:
        solution_steps.append(parent.get_board())
        parent = parent.parent

    for i in reversed(solution_steps):
        print(i, "\n")

    print(winning_state.get_board())

import numpy as np
from copy import deepcopy
from vehicle import Vehicle
from operator import attrgetter

class board(object):
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.parent = None


    def get_board(self):
        """
        draws a matrix and fill it with ..
        goes through all the vehicles and draw it in the matrix
        :return:
        """
        dimension = max(self.vehicles, key = attrgetter('x')).x + 1

        board = np.full((dimension,dimension), '..')

        for vehicle in self.vehicles:
            x, y = vehicle.x, vehicle.y
            if vehicle.orientation == 0:
                for i in range(vehicle.length):
                    board[y][x + i] = vehicle.id
                    if vehicle.length == 2:
                        board[y][x + i] += "."
            else:
                for i in range(vehicle.length):
                    board[y + i][x] = vehicle.id
                    if vehicle.length == 2:
                        board[y + i][x] += "."
        return board


    def calculate_next_move(self):
        """
        calculates a next move
        """
        new_boards = []
        copied = dict()

        for vehicle_id in range(len(self.vehicles)):
            vehicle = self.vehicles[vehicle_id]
            state = self.get_board()
            if vehicle.orientation == 0: #horizontal
                if vehicle.x > 0: #left
                    if state[vehicle.y][vehicle.x-1] == "..":
                        self.vehicles[vehicle_id].x -= 1
                        if self.get_board().tostring() not in copied:
                            # if not get_board(self.vehicles[vehicle_id].x -= 1) in dict ???
                            new_board = deepcopy(self)
                            new_board.vehicles[vehicle_id].x -= 1
                            new_board.parent = self
                            new_boards.append(new_board)

                if vehicle.x + vehicle.length <= (len(state)-1): #right
                    if state[vehicle.y][vehicle.x+vehicle.length] == "..":
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id].x += 1
                        new_board.parent = self
                        new_boards.append(new_board)

            else:    #vertical
                if vehicle.y - 1 >= 0: #up
                    if state[vehicle.y-1][vehicle.x] == "..":
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id].y -= 1
                        new_board.parent = self
                        new_boards.append(new_board)

                if vehicle.y + vehicle.length <= (len(state)-1):
                    if state[vehicle.y + vehicle.length][vehicle.x] == "..":#down
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id].y += 1
                        new_board.parent = self
                        new_boards.append(new_board)
        return new_boards