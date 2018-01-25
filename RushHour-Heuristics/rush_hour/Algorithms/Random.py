import random

def randomsearch(board):
    new_board = board
    i=1
    counter=0
    vehicleamount=len(board.vehicles)
    visit = dict()
    key = board.get_board()
    visit[key.tostring()] = 1
    while i == 1:
        new_board = new_board.calculate_random_move(vehicleamount, visit)
        #visit[new_board.get_board().tostring()] = 1
        if new_board.vehicles[0].x == len(board.get_board())-2:
            print(new_board.get_board())
            print(counter)
            break
        counter += 1

        print (counter)

