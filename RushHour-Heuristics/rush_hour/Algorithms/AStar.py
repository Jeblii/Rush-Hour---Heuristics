from copy import deepcopy
def astarsearch(board, maxDepth=6):
    """

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



