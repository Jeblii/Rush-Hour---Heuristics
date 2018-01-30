from operator import attrgetter


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
    dimension = max(board.vehicles, key=attrgetter('x')).x + 1

    for depth in range(0, maxDepth):
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
                    #print(child.get_board(), "\n")                         #<- uncomment to print the children of visited states
                    if child.vehicles[0].x == dimension - 2: #if solution is found
                        # for i in visit.keys():                            #prints all the visited states in breatdhfirst search
                        #      print(i)                                     #<- uncomment this section if you want to seethe visited states in the breadthfirstsearch
                        print("Total visited nodes:", len(visit))
                        return child
        queue = new_generation


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

    return winning_state

