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
            print("checking:", individual ,"/", len(queue),"\n")

            next_board = queue[individual]
            new_gen = next_board.calculate_next_move()

            for child in new_gen:
                new_key = child.get_board()
                if new_key.tostring() in visit:
                    continue
                else:
                    visit[new_key.tostring()] = 1
                    if child.vehicles[0].x == 4: #if solution is found

                        visit[len(visit)+1] = child.get_board()                 #add last visited state to visit dictionary

                        print("Total visited states:",len(visit))
                        # for i in visit.keys():                            #prints all the visited states in breatdhfirst search
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
    print(winning_state.get_board(), "\n")
    parent = winning_state.parent
    while parent:
        print(parent.get_board(), "\n")
        parent = parent.parent
