from operator import attrgetter
from random import shuffle


def right_cars_heuristic(board):
    "calculate number of vehicles right of the red car"
    blocking_cars = 0
    for v in board.vehicles:
        if v.x > board.vehicles[0].x:
            blocking_cars += 1
    return blocking_cars


def left_cars_heuristic(board):
    "calculate number of vehicles left of the red car, used in ReverseHeuristic"
    blocking_cars = 0
    for v in board.vehicles:
        if v.x <= board.vehicles[0].x:
            blocking_cars += 1
    return blocking_cars


def distance_heuristic(board):
    "calculates distance from red car to exit"
    grid = board.get_board()
    distance = len(grid) - board.vehicles[0].x - 1
    return distance


def three_lanes_heuristic(board):
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


def edge_heuristic(board):
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


def reverse_heuristic(board):
    "randomly prioritizes the LeftCarsHeuristic instead of the RightCarsHeuristic in certain cases"
    grid = board.get_board()
    if board.vehicles[0].x + 1 > len(grid)/2:
        val1 = right_cars_heuristic(board)
        val2 = left_cars_heuristic(board)
        val_list = [val1, val1, val2]
        shuffle(val_list)
        return val_list[0]
    else:
        return right_cars_heuristic(board)


def get_heuristic(heuristic, board):
    #return right_cars_heuristic(board)*4 + distance_heuristic(board) + (board.depth /10)
    if heuristic == 1:
        return right_cars_heuristic(board)
    elif heuristic == 2:
        return distance_heuristic(board)
    elif heuristic == 3:
        return three_lanes_heuristic(board)
    elif heuristic == 4:
        return edge_heuristic(board)
    elif heuristic == 5:
        return right_cars_heuristic(board)
    else:
        print("Invalid value, please try again")


def best_first_search(board):
    """
    An implementation of breadth first search; checks states on the order FIFO
    function terminates, when solution is found or max depth is reached
    :param board: call function with a board state
    :return:
    """
    priority_queue = [(0, board)]
    heuristic = int(input("What Heuristic would you like to use with Best First Search: "
                          "\nType Number 1 for Right Car Heuristic\nType Number 2 for Distance Heuristic"
                          "\nType Number 3 for Three Lanes Heuristic\nType Number 4 for Edge Heuristic"
                          "\nType Number 5 for Reverse Heuristic\n"))
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
                new_generation.append((get_heuristic(heuristic, child), child))
                if child.vehicles[0].x == dimension - 2:                #if solution is found
                    visit[len(visit)+1] = child.get_board()             #add last visited state to visit dictionary
                    # for i in visit.keys():                            #prints all the visited states
                    #     print(i)                                      #<- uncomment this section for  visited states
                    if dimension > 6:
                        child.display_route()
                    print("Total visited nodes:", len(visit))
                    return child, len(visit)
        for i in new_generation:
            priority_queue.append(i)
        priority_queue.pop(0)
        priority_queue = sorted(priority_queue, key=lambda x: x[0])