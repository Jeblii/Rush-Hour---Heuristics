import pygame as pg
import sys
import numpy as np
import time

class Visualization(object):
    def __init__(self, steps):
        self.steps = steps
        # self.win = win

        path = self.steps[0]
        win = self.steps[1]
        print(path)
        w = np.array(win)
        print(w)

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
        red_car = pg.image.load('Blocks/Car0.png')

        #Initializes Background Image
        DISPLAYSURF.blit(board, (0,0))

        #Load cars into board
        car_0 = np.where(win == '0.')
        print (car_0)
        for i in car_0[0]:
            y = (dif_heigth * i) + 25

        for i in car_0[1]:
            x = (dif_width *i) - 100
        print (y)
        print(x)

        DISPLAYSURF.blit(red_car, (x,y))

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                pg.display.update()



colorcoding = []
imagelist = []

for number in range(0,16):
    imagelist.append(pg.image.load('Blocks/' + "Car" + number + ".png"))
for number in range(1,16):
    imagelist.append(pg.image.load('Blocks/' + "Car-rotated" + number + ".png"))

horizontalcars = imagelist[0:12]
horizontaltrucks = imagelist[12:16]
verticalcars = imagelist[16:25]
verticaltrucks = imagelist[25:]

for vehicle in board.vehicles:
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

for state in winning_route:
    clean board init
    for vehicle in range(len(state.vehicles)):
        x = (dif_width * state.vehicles[vehicle].x) - 100
        y = (dif_heigth * state.vehicles[vehicle].y) + 25
        DISPLAYSURF.blit(colorcoding[vehicle], (x, y))
    pg.display.update
    time.sleep(.5)