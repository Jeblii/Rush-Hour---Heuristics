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
