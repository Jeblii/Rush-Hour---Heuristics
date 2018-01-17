from copy import deepcopy
import numpy as np
def breadthfirstsearch(board, maxDepth=6):
    """
    An implementation of breadth first search; checks states on the order FIFO
    function terminates, when solution is found or max depth is reached
    :param board: call function with a boardstate
    :param maxDepth: max depth of the tree till search terminates
    :return:
    """
    queue = [board]
    visited = []
    visit = dict()
    visit_count = 0

    for depth in range(0, maxDepth):
        new_generation = []
        visited = set()

        for individual in range(len(queue)):
            print(len(queue))
            print("depth is", depth + 1)
            print("checking:", individual ,"/", len(queue) )
            next_board = queue[individual]

            visit_count += 1                                                #number of visited states
            visit[visit_count] = queue[individual].get_board()              #create key in visit dictionary

            new_gen = next_board.calculate_next_move()


            ng = []                                             #save the states of new_gen that are already in visit dictionary
            for i in new_gen:
                for o in visit.values():
                    if np.array_equal(i.get_board(), o) == True:
                        ng.append(i)

            for i in ng:                                        #remove the visited states from new_gen
                if i in new_gen:
                    new_gen.remove(i)
            #print("nr of children" , len(new_gen))

            for child in new_gen:
                if child in visited:
                    continue
                else:
                    if child.vehicles[0].x == 4:
                        get_parents(child)
                        #print("depth is", depth + 1)
                        return
                    new_generation.append(child)
                    #print(child.get_board()))
                visited.add(child)
        queue = new_generation

    return visited

def get_parents(winning_state):
    print(winning_state.get_board(), "\n")
    parent = winning_state.parent
    while parent:
        print(parent.get_board(), "\n")
        parent = parent.parent
