import random

def randomsearch(board):
    getal=1
    while getal==1:
        new_board = board
        i = 1
        counter = 0
        vehicleamount = len(board.vehicles)
        visit = dict()
        key = board.get_board()
        visit[key.tostring()] = 1
        while counter < 1000000:
            new_board = new_board.calculate_random_move(vehicleamount, visit)
            #visit[new_board.get_board().tostring()] = 1
            if new_board.vehicles[0].x == len(board.get_board())-2:
                for vehicle in new_board.vehicles:
                    print (vehicle.id,',', vehicle.x, ',', vehicle.y, ',', vehicle.orientation)
                print(counter)
                getal=2
                break
            counter += 1
            print(counter)


