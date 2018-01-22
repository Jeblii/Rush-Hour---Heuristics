from copy import deepcopy
import numpy as np
from operator import attrgetter

def get_heuristic(self, board):
    "calculate number of cars between 00 and the exit"
    blocking_cars = 0
    for v in board.vehicles:
        if v.x > board.vehicles[0].x:
            blocking_cars += 1

def Astar(board, maxDepth=100):
    """
    An implementation of breadth first search; checks states on the order FIFO
    function terminates, when solution is found or max depth is reached
    :param board: call function with a boardstate
    :param maxDepth: max depth of the tree till search terminates
    :return:
    """
    priority_queue = [board]
    index = 0
    visit = dict()
    key = board.get_board()
    visit[key.tostring()]= 1
    dimension = max(board.vehicles, key=attrgetter('x')).x + 1

    for depth in range(0, maxDepth):
        new_generation = []

        for individual in range(len(priority_queue)):
            print("depth is", depth + 1)
            #print("checking node:", individual ,"/", len(queue),"\n")
            next_board = priority_queue[individual]

            #visit_count += 1                                                #number of visited states in the breadthfirstsearch
            #visit[visit_count] = queue[individual].get_board()              #create key for a visited state in visit dictionary
            #print("checking:", individual ,"/", len(queue),"\n")

            next_board = queue[individual]
            new_gen = next_board.calculate_next_move()


            for child in new_gen:
                new_key = child.get_board()
                if new_key.tostring() in visit:
                    continue
                else:
                    h = get_heuristic(child)
                    f = h + (depth + 1)
                    priority_queue.insert(0, position)

                    visit[new_key.tostring()] = 1
                    new_generation.append(child)
                    #print(child.get_board(), "\n")
                    if child.vehicles[0].x == dimension - 2: #if solution is found

                        visit[len(visit)+1] = child.get_board()                 #add last visited state to visit dictionary


                        # for i in visit.keys():                            #prints all the visited states in breatdhfirst search
                        #     print(i)                                        #<- uncomment this section if you want to seethe visited states in the breadthfirstsearch

                        get_parents(child)
                        print("Total visited nodes:", len(visit))

                        return
        priority_queue = new_generation
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
