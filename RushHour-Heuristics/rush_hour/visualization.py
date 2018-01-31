import pygame as pg
import sys


def visualization(winning_state, visit, elapsed_time):
        #initializes board
        pg.init()
        width = 600
        height = 600
        DISPLAYSURF = pg.display.set_mode((width, height), 0, 32)
        pg.display.set_caption('Rush Hour')
        myfont = pg.font.SysFont('Garamond', 16)

        dif_width = width/6
        dif_height = height/6

        #loads Background Images
        board = pg.image.load('blocks/RushHour.png')
        results = pg.image.load('blocks/Pop_up.png')

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
            imagelist.append(pg.image.load('blocks/' + "Car" + str(number) + ".png"))
        for number in range(1, 16):
            imagelist.append(pg.image.load('blocks/' + "Car-rotated" + str(number) + ".png"))

        horizontalcars = imagelist[0:12]
        horizontaltrucks = imagelist[12:15]
        verticalcars = imagelist[16:27]
        verticaltrucks = imagelist[27:]

        for vehicle in winning_state.vehicles:
            if vehicle.orientation == 0:
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

        maximum = (len(solution_steps))-1
        counter = maximum

        num_moves = "Total Number of Moves: " + str(counter)
        number_of_moves = myfont.render(num_moves, True, (0, 0, 0))
        num_nodes = "Total Number of Nodes Visited: " + str(visit)
        number_of_nodes = myfont.render(num_nodes, True, (0, 0, 0))
        el_time = "Elapsed Time: " + str(elapsed_time)
        elapsed_time = myfont.render(el_time, True, (0, 0, 0))


        state = (solution_steps[counter])
        for vehicle in range(len(state.vehicles)):
            x = (dif_width * state.vehicles[vehicle].x)
            y = (dif_height * state.vehicles[vehicle].y)
            DISPLAYSURF.blit(colorcoding[vehicle], (x, y))
        counter -= 1
        pg.display.update()

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                    pg.display.update()
                if event.type == pg.KEYDOWN:
                    # if event.key == pg.K_LEFT:
                    #     if counter < maximum:
                    #         DISPLAYSURF.blit(board, (0, 0))
                    #         state = (solution_steps[counter])
                    #         for vehicle in range(len(state.vehicles)):
                    #             x = (dif_width * state.vehicles[vehicle].x)
                    #             y = (dif_height * state.vehicles[vehicle].y)
                    #             DISPLAYSURF.blit(colorcoding[vehicle], (x, y))
                    #         counter +=1
                    #         pg.display.update()
                    if event.key == pg.K_RIGHT:
                        if counter >= 0:
                            DISPLAYSURF.blit(board, (0, 0))
                            state = solution_steps[counter]
                            for vehicle in range(len(state.vehicles)):
                                x = (dif_width * state.vehicles[vehicle].x)
                                y = (dif_height * state.vehicles[vehicle].y)
                                DISPLAYSURF.blit(colorcoding[vehicle], (x, y))
                            counter -= 1
                            pg.display.update()
                        if counter <= -1:
                            DISPLAYSURF.blit(results, (200, 200))
                            DISPLAYSURF.blit(number_of_moves, (210, 250))
                            DISPLAYSURF.blit(number_of_nodes, (210, 300))
                            DISPLAYSURF.blit(elapsed_time, (210, 350))
                            pg.display.update()
