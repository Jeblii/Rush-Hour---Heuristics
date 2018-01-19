def DistanceHeuristic(board):
    grid = board.get_board()
    for i in grid:
        if 0 in i:
            while not i[0] == 0:
                i.pop(0)
            i.pop(0)
            i.pop(0)
            return len(i)

def BlockingHeuristic(board):
    grid = board.get_board()
    for i in grid:
        if 0 in i:
            while not i[0] == 0:
                i.pop(0)
            i.pop(0)
            i.pop(0)
            return len(set(i))


