import random

def randomsearch(board):
    new_board = board
    i=1
    counter=0
    vehicleamount=len(board.vehicles)
    while i == 1:
        new_board = new_board.calculate_random_move(vehicleamount)
        if new_board.vehicles[0].x == 4:
            print('win')
            print(counter)
            break
        counter += 1
        print (counter)

