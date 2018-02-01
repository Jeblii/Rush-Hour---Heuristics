from operator import attrgetter


def breadth_first_search(board, max_depth=100):
    """
    An implementation of breadth first search; checks states on the order FIFO
    function terminates, when solution is found or max depth is reached
    :param board: call function with a board state
    :param max_depth: max depth of the tree until search terminates
    :return:
    """
    queue = [board]
    visit = dict()
    key = board.get_board()
    visit[key.tostring()]= 1
    dimension = max(board.vehicles, key=attrgetter('x')).x + 1

    for depth in range(0, max_depth):
        new_generation = []
        #print("depth is", depth + 1)
        for individual in range(len(queue)):
            #print("depth is", depth + 1)
            #print("checking node:", individual ,"/", len(queue),"\n")
            next_board = queue[individual]
            new_gen = next_board.calculate_next_move(visit)

            for child in new_gen:
                new_key = child.get_board()
                if new_key.tostring() in visit:
                    continue
                else:
                    visit[new_key.tostring()] = 1
                    new_generation.append(child)
                    #print(child.get_board(), "\n")             #<- uncomment to print the children of visited states
                    if child.vehicles[0].x == dimension - 2:    #if solution is found
                        # for i in visit.keys():                #prints all the visited states
                        #      print(i)                         #<- uncomment this section for visited states
                        if dimension > 6:
                            child.display_route()
                        print("Total visited nodes:", len(visit))
                        return child, len(visit)
        queue = new_generation
