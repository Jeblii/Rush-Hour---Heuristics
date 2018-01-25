import numpy as np
from copy import deepcopy
from vehicle import Vehicle
from operator import attrgetter
import random
from random import *

class board(object):
    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.parent = None
        self.depth = 0


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


    def calculate_next_move(self, visit):
        """
        calculates a next move
        """
        self.depth += 1
        new_boards = []
        for vehicle_id in range(len(self.vehicles)):
            vehicle = self.vehicles[vehicle_id]
            state = self.get_board()
            if vehicle.orientation == 0: #horizontal
                if vehicle.x > 0: #left
                    if state[vehicle.y][vehicle.x-1] == "..":
                        self.vehicles[vehicle_id].x -=1
                        if not self.get_board().tostring() in visit:
                            if not self.get_board().all in new_boards:
                                new_board = deepcopy(self)
                                self.vehicles[vehicle_id].x += 1
                                new_board.parent = self
                                new_boards.append(new_board)
                        else:
                            self.vehicles[vehicle_id].x += 1

                if vehicle.x + vehicle.length <= (len(state)-1): #right
                    if state[vehicle.y][vehicle.x+vehicle.length] == "..":
                        self.vehicles[vehicle_id].x += 1
                        if not self.get_board().tostring() in visit:
                            if not self.get_board().all in new_boards:
                                new_board = deepcopy(self)
                                self.vehicles[vehicle_id].x -= 1
                                new_board.parent = self
                                new_boards.append(new_board)
                        else:
                            self.vehicles[vehicle_id].x -= 1

            else:    #vertical
                if vehicle.y - 1 >= 0: #up
                    if state[vehicle.y-1][vehicle.x] == "..":
                        self.vehicles[vehicle_id].y -= 1
                        if not self.get_board().tostring() in visit:
                            if not self.get_board().all in new_boards:
                                new_board = deepcopy(self)
                                self.vehicles[vehicle_id].y += 1
                                new_board.parent = self
                                new_boards.append(new_board)
                        else:
                            self.vehicles[vehicle_id].y += 1

                if vehicle.y + vehicle.length <= (len(state)-1):
                    if state[vehicle.y + vehicle.length][vehicle.x] == "..":#down
                        self.vehicles[vehicle_id].y += 1
                        if not self.get_board().tostring() in visit:
                            if not self.get_board().all in new_boards:
                                new_board = deepcopy(self)
                                self.vehicles[vehicle_id].y -= 1
                                new_board.parent = self
                                new_boards.append(new_board)
                        else:
                            self.vehicles[vehicle_id].y -= 1
        self.depth -= 1
        return new_boards

    def calculate_random_move(self, vehicleamount):
        """
        calculates a next move
        """
        self.depth += 1

        while True:
            number = (randint(0, 1))
            vehicle_id = (randint(0, vehicleamount-1))
            vehicle = self.vehicles[vehicle_id]
            state = self.get_board()
            if vehicle.orientation == 0: #horizontal
                if number == 0:
                    if vehicle.x > 0: #left
                        if state[vehicle.y][vehicle.x-1] == "..":
                            self.vehicles[vehicle_id].x -=1
                            return self
                else:
                    if vehicle.x + vehicle.length <= (len(state)-1): #right
                        if state[vehicle.y][vehicle.x+vehicle.length] == "..":
                            self.vehicles[vehicle_id].x += 1
                            return self
            else:    #vertical
                if number == 0:
                    if vehicle.y - 1 >= 0: #up
                        if state[vehicle.y-1][vehicle.x] == "..":
                            self.vehicles[vehicle_id].y -= 1
                            return self
                else:
                    if vehicle.y + vehicle.length <= (len(state)-1):
                        if state[vehicle.y + vehicle.length][vehicle.x] == "..":#down
                            self.vehicles[vehicle_id].y += 1
                            return self

