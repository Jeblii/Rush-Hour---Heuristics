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
        draws a 6x6 matrix and fill it with ..
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
                        board[y][x + i] += " "
            else:
                for i in range(vehicle.length):
                    board[y + i][x] = vehicle.id
        return board


    def calculate_next_move(self):
        """
        calculates a next move
        """
        new_boards = []
        for vehicle_id in range(len(self.vehicles)):
            vehicle = self.vehicles[vehicle_id]
            if vehicle.orientation == 0: #horizontal
                if vehicle.x > 0: #left
                    if self.get_board()[vehicle.y][vehicle.x-1] == "..":
                        child_v = deepcopy(vehicle)
                        child_v.x -= 1
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id] = child_v
                        new_board.parent = self
                        new_boards.append(new_board)

                if vehicle.x <= 5 - vehicle.length: #right
                    if self.get_board()[vehicle.y][vehicle.x+vehicle.length] == "..":
                        child_v = deepcopy(vehicle)
                        child_v.x += 1
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id] = child_v
                        new_board.parent = self
                        new_boards.append(new_board)

            else:    #vertical
                if vehicle.y - 1  >= 0: #up
                    if self.get_board()[vehicle.y-1][vehicle.x] == "..":
                        child_v = deepcopy(vehicle)
                        child_v.y -= 1
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id] = child_v
                        new_board.parent = self
                        new_boards.append(new_board)

                if vehicle.y +vehicle.length <= 5:
                    if  self.get_board()[vehicle.y + vehicle.length][vehicle.x] == "..":#down
                        child_v = deepcopy(vehicle)
                        child_v.y += 1
                        new_board = deepcopy(self)
                        new_board.vehicles[vehicle_id] = child_v
                        new_board.parent = self
                        new_boards.append(new_board)
        return new_boards


