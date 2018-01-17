from copy import deepcopy
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
    for depth in range(0, maxDepth):
        new_generation = []
        visited = set()

        for individual in range(len(queue)):
            print(len(queue))
            print("depth is", depth + 1)
            print("checking:", individual ,"/", len(queue) )
            next_board = queue[individual]
            new_gen = next_board.calculate_next_move()
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



