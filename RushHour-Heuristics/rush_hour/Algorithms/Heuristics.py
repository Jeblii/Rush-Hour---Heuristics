#alles kan iets geoptimized worden als we weten in welke rijen de rode auto staat voor elk board en die index vervolgens gebruiken

def get_heuristic(board):
    "calculate number of cars between 00 and the exit"
    blocking_cars = 0
    for v in board.vehicles:
        if v.x > board.vehicles[0].x:
            blocking_cars += 1
    return blocking_cars


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
            set_i = set(i)
            if '..' in set_i: #weet niet of deze syntax klopt
                set_i.remove('..')
            return len(set_i)-1


def ThreeLanesHeuristic(board):
    grid = board.get_board()
    for i in range(len(grid)):
        if 0 in grid[i]:
            merged_list = grid[i+1] + grid[i] + grid[i-1]
            merged_set = set(merged_list)
            if '..' in merged_set: #weet niet of deze syntax klopt
                merged_set.remove('..')
            return len(set(merged_list))-1


