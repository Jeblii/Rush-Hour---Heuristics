from copy import deepcopy
import random

def randomsearch(board):
    new_board = board
    i=1
    counter=0
    while i == 1:
        new_board = random.choice(new_board.calculate_next_move())
        if new_board.vehicles[0].x == 4:
            #get_parents(child)
            # print("depth is", depth + 1)
            print('win')
            print(counter)
            break
        counter += 1



def astarsearch(board, maxDepth=6):
    """
    
    """


    board = random.choice(board.calculate_next_move())
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



