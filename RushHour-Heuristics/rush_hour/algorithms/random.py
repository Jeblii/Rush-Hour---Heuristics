def random_search(board):
    getal = 1
    while getal == 1:
        new_board = board
        counter = 0
        vehicleamount = len(board.vehicles)
        visit = dict()
        key = board.get_board()
        visit[key.tostring()] = 1
        limit = len(board.get_board())-2
        while counter < 1000000:
            new_board = new_board.calculate_random_move(vehicleamount, visit)
            if new_board.vehicles[0].x == limit:
                getal = 2
                print('Solution found: \n', new_board.get_board())
                break
            counter += 1
            print(counter)


