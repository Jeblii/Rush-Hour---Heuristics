import numpy as np
from operator import attrgetter
from random import shuffle


def RightCarsHeuristic(board):
    "calculate number of vehicles right of the red car"
    blocking_cars = 0
    for v in board.vehicles:
        if v.x > board.vehicles[0].x:
            blocking_cars += 1
    return blocking_cars


def LeftCarsHeuristic(board):
    "calculate number of vehicles left of the red car, used in ReverseHeuristic"
    blocking_cars = 0
    for v in board.vehicles:
        if v.x <= board.vehicles[0].x:
            blocking_cars += 1
    return blocking_cars


def DistanceHeuristic(board):
    "calculates distance from red car to exit"
    grid = board.get_board()
    distance = len(grid) - board.vehicles[0].x - 1
    return distance


def BlockingHeuristic(board):
    "calculate number of vehicles blocking the red car"
    grid = board.get_board()
    for i in grid:
        if '0.' in i:
            while not i[0] == 0:
                np.delete(i, 0)
            set_i = set(i)
            if '..' in set_i:
                set_i.remove('..')
            return len(set_i)-1


def ThreeLanesHeuristic(board):
    "calculate number of vehicles in 3 lanes"
    grid = board.get_board()
    for i in range(len(grid)):
        if '0.' in grid[i]:
            mergedlist = []
            for k in range(len(grid[i])):
                mergedlist.append(grid[i - 1][k])
                mergedlist.append(grid[i][k])
                mergedlist.append(grid[i + 1][k])
            merged_set = set(mergedlist)
            if '..' in merged_set:
                merged_set.remove('..')
            return len(merged_set) - 1


def EdgeHeuristic(board):
    "calculates the amount of cars on the edges of the grid except the right one"
    grid = board.get_board()
    merged_list = []
    for i in range(len(grid[0])):
        merged_list.append(grid[0][i])
        merged_list.append(grid[-1][i])
    counter = 0
    for i in board.vehicles:
        if i.x == 0:
            counter += 1
    return len(set(merged_list))+counter


def ReverseHeuristic(board):
    "randomly prioritizes the LeftCarsHeuristic instead of the RightCarsHeuristic in certain cases"
    grid = board.get_board()
    if board.vehicles[0].x + 1 > len(grid)/2:
        val1 = RightCarsHeuristic(board)
        val2 = LeftCarsHeuristic(board)
        val_list = [val1, val1, val2]
        shuffle(val_list)
        return val_list[0]
    else:
        return RightCarsHeuristic(board)


def get_heuristic(board):
    "select a heuristic by uncommenting"
    #return RightCarsHeuristic(board)*4 + DistanceHeuristic(board) + (board.depth /10)
    return RightCarsHeuristic(board)
    #return DistanceHeuristic(board)
    #return BlockingHeuristic(board)
    #return ThreeLanesHeuristic(board)
    #return EdgeHeuristic(board)
    #return ReverseHeuristic(board)


def best_first(board, maxDepth=10000):
    """
    An implementation of breadth first search; checks states on the order FIFO
    function terminates, when solution is found or max depth is reached
    :param board: call function with a boardstate
    :param maxDepth: max depth of tfhe tree till search terminates
    :return:
    """
    priority_queue = []
    priority_queue.append((0, board))

    visit = dict()
    key = board.get_board()
    visit[key.tostring()]= 1
    dimension = max(board.vehicles, key=attrgetter('x')).x + 1

    while priority_queue:
        new_generation = []
        next_board = priority_queue[0][1]
        new_gen = next_board.calculate_next_move(visit)

        for child in new_gen:
            new_key = child.get_board()
            if new_key.tostring() in visit:
                continue
            else:
                visit[new_key.tostring()] = 1
                new_generation.append((get_heuristic(child), child))
                if child.vehicles[0].x == dimension - 2:                #if solution is found
                    visit[len(visit)+1] = child.get_board()             #add last visited state to visit dictionary
                    # for i in visit.keys():                            #prints all the visited states in breatdhfirst search
                    #     print(i)                                      #<- uncomment this section if you want to seethe visited states in the breadthfirstsearch
                    get_parents(child)
                    print("Total visited nodes:", len(visit))
                    return child
        for i in new_generation:
            priority_queue.append(i)
        priority_queue.pop(0)
        priority_queue = sorted(priority_queue, key=lambda x: x[0])


def get_parents(winning_state):
    solution_steps = []
    parent = winning_state.parent
    while parent:
        solution_steps.append(parent.get_board())
        parent = parent.parent

    print("Solution route")
    for i in reversed(solution_steps):
        print(i, "\n")
    print(winning_state.get_board())
    print("Total moves:", len(solution_steps))
