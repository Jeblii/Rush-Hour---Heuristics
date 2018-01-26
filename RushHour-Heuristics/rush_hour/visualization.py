import pygame as pg
import sys
import numpy as np

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
