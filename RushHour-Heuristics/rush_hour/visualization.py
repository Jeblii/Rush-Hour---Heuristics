import pygame as pg
import sys
import numpy as np
import time

def visualization(winning_state):
        #initializes board
        pg.init()
        width = 600
        heigth = 600
        DISPLAYSURF = pg.display.set_mode((width, heigth), 0, 32)
        pg.display.set_caption('Rush Hour')

        dif_width = width/6
        dif_heigth = heigth/6

        #loads Background Image
        board = pg.image.load('Blocks/Background.jpg')

        #Initializes Background Image
        DISPLAYSURF.blit(board, (0,0))

        solution_steps = [winning_state]
        parent = winning_state.parent
        while parent:
            solution_steps.append(parent)
            parent = parent.parent

        colorcoding = []
        imagelist = []

        for number in range(0, 16):
            imagelist.append(pg.image.load('Blocks/' + "Car" + str(number) + ".png"))
        for number in range(1, 16):
            imagelist.append(pg.image.load('Blocks/' + "Car-rotated" + str(number) + ".png"))

        horizontalcars = imagelist[0:12]
        horizontaltrucks = imagelist[12:16]
        verticalcars = imagelist[16:25]
        verticaltrucks = imagelist[25:]

        for vehicle in winning_state.vehicles:
            if vehicle.orientation == 1:
                if vehicle.id < 12:
                    colorcoding.append(horizontalcars[0])
                    horizontalcars.append(horizontalcars[0])
                    horizontalcars.pop(0)
                else:
                    colorcoding.append(horizontaltrucks[0])
                    horizontaltrucks.append(horizontaltrucks[0])
                    horizontaltrucks.pop(0)
            else:
                if vehicle.id < 12:
                    colorcoding.append(verticalcars[0])
                    verticalcars.append(verticalcars[0])
                    verticalcars.pop(0)
                else:
                    colorcoding.append(verticaltrucks[0])
                    verticaltrucks.append(verticaltrucks[0])
                    verticaltrucks.pop(0)

        counter = 0
        max = (len(solution_steps))

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    pg.display.update()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        if counter > 0:
                            DISPLAYSURF.blit(board, (0, 0))
                            state = reversed(solution_steps[counter])
                            for vehicle in range(len(state.vehicles)):
                                x = (dif_width * state.vehicles[vehicle].x) - 100
                                y = (dif_heigth * state.vehicles[vehicle].y) + 25
                                DISPLAYSURF.blit(colorcoding[vehicle], (x, y))
                            counter -=1
                            pg.display.update
                    if event.key == pg.K_RIGHT:
                        if counter < max:
                            DISPLAYSURF.blit(board, (0, 0))
                            state = solution_steps[counter]
                            for vehicle in range(len(state.vehicles)):
                                x = (dif_width * state.vehicles[vehicle].x) - 100
                                y = (dif_heigth * state.vehicles[vehicle].y) + 25
                                DISPLAYSURF.blit(colorcoding[vehicle], (x, y))
                            counter += 1
                            pg.display.update
