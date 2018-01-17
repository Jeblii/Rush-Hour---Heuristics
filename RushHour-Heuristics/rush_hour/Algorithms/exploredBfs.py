from copy import deepcopy
import numpy as np
def breadthfirstsearch(board, maxDepth=4):
    """
    An implementation of breadth first search; checks states on the order FIFO
    function terminates, when solution is found or max depth is reached
    :param board: call function with a boardstate
    :param maxDepth: max depth of the tree till search terminates
    :return:
    """
    queue = [board]
    explored = [board]
    for depth in range(0, maxDepth):
        new_generation = []
        visited = dict()

        for individual in range(len(queue)):
            print(len(queue))
            print("depth is", depth + 1)
            print("checking:", individual ,"/", len(queue) )
            next_board = queue[individual]

            #visited[individual] = queue[individual].get_board()

            new_gen = next_board.calculate_next_move()
            for child in new_gen:
                for i in range(5):
                    if not np.array_equal(explored[i].get_board(), child.get_board()):
                        if child.vehicles[0].x == 4:
                            print(child.get_board())
                            print("depth is", depth + 1)
                            return

                        new_generation.append(child)
                        explored.append(child)

                        #print(child.get_board())
                        #print("")
                    else:
                        break


            queue = new_generation

    return visited