from copy import deepcopy
import numpy as np
from operator import attrgetter
import queue as Q

def get_heuristic(board):
    "calculate number of cars between 00 and the exit"
    grid = board.get_board()
    for i in range(len(grid)):
        if '0.' in grid[i]:
            mergedlist=[]
            for k in range(len(grid[i])):
                mergedlist.append(grid[i - 1][k])
                mergedlist.append(grid[i][k])
                mergedlist.append(grid[i + 1][k])
            merged_set = set(mergedlist)
            if '..' in merged_set:  # weet niet of deze syntax klopt
                merged_set.remove('..')
            return len(merged_set) - 1


def Astar(board, maxDepth=10000):
    """
    An implementation of breadth first search; checks states on the order FIFO
    function terminates, when solution is found or max depth is reached
    :param board: call function with a boardstate
    :param maxDepth: max depth of tfhe tree till search terminates
    :return:
    """
    #priority_queue = Q.PriorityQueue()
    priority_queue = []


    priority_queue.append((0, board))

    visit = dict()
    key = board.get_board()
    visit[key.tostring()]= 1
    dimension = max(board.vehicles, key=attrgetter('x')).x + 1

    while priority_queue:
        new_generation = []

        #print("depth is", depth + 1)
        #print("checking node:", individual ,"/", len(queue),"\n")

            #visit_count += 1                                                #number of visited states in the breadthfirstsearch
            #visit[visit_count] = queue[individual].get_board()              #create key for a visited state in visit dictionary
            #print("checking:", individual ,"/", len(queue),"\n")

        next_board = priority_queue[0][1]
        new_gen = next_board.calculate_next_move(visit)

        for child in new_gen:
            new_key = child.get_board()
            if new_key.tostring() in visit:
                continue
            else:
                h = get_heuristic(child)
                depth = 0
                f = h + (depth + 1)

                visit[new_key.tostring()] = 1
                new_generation.append((f, child))
                #print(child.get_board(), "\n")
                if child.vehicles[0].x == dimension - 2: #if solution is found

                    visit[len(visit)+1] = child.get_board()                 #add last visited state to visit dictionary


                    # for i in visit.keys():                            #prints all the visited states in breatdhfirst search
                    #     print(i)                                        #<- uncomment this section if you want to seethe visited states in the breadthfirstsearch

                    get_parents(child)
                    print("Total visited nodes:", len(visit))

                    return
        for i in new_generation:
            priority_queue.append(i)
        priority_queue.pop(0)
        priority_queue = sorted(priority_queue, key=lambda x: x[0])
    return visit

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
