import numpy as np
from copy import deepcopy
from vehicle import Vehicle
from operator import attrgetter

class board(object):
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.parent = None


    def get_board(self):
        """
        draws a matrix and fill it with ..
        goes through all the vehicles and draw it in the matrix
        :return:
        """
        dimension = max(self.vehicles, key = attrgetter('x')).x + 1

        board = np.full((dimension,dimension), '..')

        for vehicle in self.vehicles:
            x, y = vehicle.x, vehicle.y
            if vehicle.orientation == 0:
                for i in range(vehicle.length):
                    board[y][x + i] = vehicle.id
                    if vehicle.length == 2:
                        board[y][x + i] += "."
            else:
                for i in range(vehicle.length):
                    board[y + i][x] = vehicle.id
                    if vehicle.length == 2:
                        board[y + i][x] += "."
        return board


    def calculate_next_move(self):
        """
        calculates a next move
        """
        new_boards = []
        for vehicle_id in range(len(self.vehicles)):
            vehicle = self.vehicles[vehicle_id]
            state = self.get_board()
            if vehicle.orientation == 0: #horizontal
                if vehicle.x > 0: #left
                    if state[vehicle.y][vehicle.x-1] == "..":
                        # if not get_board(self.vehicles[vehicle_id].x -= 1) in dict ???
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id].x -= 1
                        new_board.parent = self
                        new_boards.append(new_board)

                if vehicle.x + vehicle.length <= (len(state)-1): #right
                    if state[vehicle.y][vehicle.x+vehicle.length] == "..":
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id].x += 1
                        new_board.parent = self
                        new_boards.append(new_board)

            else:    #vertical
                if vehicle.y - 1 >= 0: #up
                    if state[vehicle.y-1][vehicle.x] == "..":
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id].y -= 1
                        new_board.parent = self
                        new_boards.append(new_board)

                if vehicle.y + vehicle.length <= (len(state)-1):
                    if state[vehicle.y + vehicle.length][vehicle.x] == "..":#down
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id].y += 1
                        new_board.parent = self
                        new_boards.append(new_board)
        return new_boards