def random_search(board):
    getal = 1
    while getal == 1:
        new_board = board
        counter = 0
        vehicle_amount = len(board.vehicles)
        visit = dict()
        key = board.get_board()
        visit[key.tostring()] = 1
        limit = len(board.get_board())-2
        while counter < 1000000:
            new_board = new_board.calculate_random_move(vehicle_amount, visit)
            if new_board.vehicles[0].x == limit:
                getal = 2
                print('Solution found: \n', new_board.get_board())
                break
            counter += 1
            print(counter)


def random_search_path(board):
    getal = 1
    while getal == 1:
        new_board = [board]
        counter = 0
        vehicle_amount = len(board.vehicles)
        visit = dict()
        key = board.get_board()
        visit[key.tostring()] = 1
        limit = len(board.get_board())-2
        while counter < 1000000:
            new_board.append(new_board[-1].calculate_random_move(vehicle_amount, visit))
            if new_board[-1].vehicles[0].x == limit:
                getal = 2
                print(new_board[-1].get_board())
                for i in new_board:
                    print(i.get_board())
                break
            counter += 1
            print(counter)


