#alles kan iets geoptimized worden als we weten in welke rijen de rode auto staat voor elk board en die index vervolgens gebruiken

def RightCarsHeuristic(board): #works
    "calculate number of cars between 00 and the exit"
    blocking_cars = 0
    for v in board.vehicles:
        if v.x > board.vehicles[0].x:
            blocking_cars += 1
    return blocking_cars


def DistanceHeuristic(board):#works
    grid = board.get_board()
    for i in grid:
        if '0.' in i:
            while not i[0] == 0:
                np.delete(i, 0)
            return len(i)-2

def BlockingHeuristic(board):  #works
    grid = board.get_board()
    for i in grid:
        if '0.' in i:
            while not i[0] == 0:
                i.pop(0)
            print(i)
            set_i = set(i)
            if '..' in set_i:
                set_i.remove('..')
            return len(set_i)-1


def ThreeLanesHeuristic(board): #works
    grid = board.get_board()
    for i in range(len(grid)):
        if '0.' in grid[i]:
            mergedlist = []
            for k in range(len(grid[i])):
                mergedlist.append(grid[i - 1][k])
                mergedlist.append(grid[i][k])
                mergedlist.append(grid[i + 1][k])
            merged_set = set(mergedlist)
            if '..' in merged_set:
                merged_set.remove('..')
            return len(merged_set) - 1


