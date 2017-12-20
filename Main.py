"""
 Coded by Lilian GALLON (please check the licence before doing anything)
 github.com/N3ROO

                                  _.====.._
             _____              ,:._       ~-_
       _ __ |___ / _ __ __          `\        ~-_
      | '_ \  |_ \| '__/ _ \          `\        ~-_
      | | | |___) | | | (_) |           |         `.
      |_| |_|____/|_|  \___/ 	       ,/            ~-_
                             -..__..-''                ~~--..__...----...
"""

import pygame
from NeroGrid.Cell import Cell
from NeroGrid.Grid import Grid


# http://www.nerdparadise.com/programming/pygame/part1
def main():
    pygame.init()
    done = False

    grid_x = 5
    grid_y = 5
    grid_columns = 20
    grid_lines = 20
    cell_width = 50
    cell_height = 50
    cell_thickness = 1
    cell_color = (0, 150, 0)
    alive_entities = [Cell(10, 10), Cell(11, 10), Cell(9, 10), Cell(10, 9), Cell(9, 11)]

    grid = Grid(alive_entities, grid_columns, grid_lines, cell_width, cell_height, cell_thickness, cell_color)

    screen = pygame.display.set_mode(
        (2 * grid_x + grid_columns * cell_width, 2 * grid_y + grid_lines * cell_height))
    screen.fill((255, 255, 255))

    it = 0
    font = pygame.font.Font(None, 40)
    text = font.render(str(it), 1, (0, 0, 0))

    left_clicking = False
    right_clicking = False
    start_x = 0
    start_y = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    grid.set_size(grid.columns + 1, grid.lines + 1)
                elif event.button == 5:
                    grid.set_size(grid.columns - 1, grid.lines - 1)
                elif event.button == 1:
                    left_clicking = True
                    start_x, start_y = pygame.mouse.get_pos()
                elif event.button == 3:
                    right_clicking = True
                    x, y = pygame.mouse.get_pos()
                    grid.update_cell(x - grid_x, y - grid_y)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if left_clicking:
                        end_x, end_y = pygame.mouse.get_pos()
                        d_x = start_x - end_x
                        d_y = start_y - end_y
                        d_column, d_line = grid.convert_to_grid_pos(d_x, d_y)
                        grid.move(d_column, d_line)
                    left_clicking = False
                if event.button == 3:
                    right_clicking = False

            if event.type == pygame.MOUSEMOTION:
                if left_clicking:
                    end_x, end_y = pygame.mouse.get_pos()
                    d_x = start_x - end_x
                    d_y = start_y - end_y
                    d_column, d_line = grid.convert_to_grid_pos(d_x, d_y)
                    if d_column != 0 or d_line != 0:
                        grid.move(d_column, d_line)
                        start_x = end_x
                        start_y = end_y
                if right_clicking:
                    x, y = pygame.mouse.get_pos()
                    grid.update_cell(x - grid_x, y - grid_y)

            if event.type == pygame.KEYDOWN:
                # up
                if event.key == 273:
                    grid.move(- 1, 0)
                # left
                elif event.key == 276:
                    grid.move(0, - 1)
                # down
                elif event.key == 274:
                    grid.move(1, 0)
                #right
                elif event.key == 275:
                    grid.move(0, 1)
                #space
                elif event.key == pygame.K_SPACE:
                    # Grid
                    grid.check_rules()
                    # Text
                    it = it + 1
                    font = pygame.font.Font(None, 40)
                    text = font.render(str(it), 1, (0, 0, 0))

        # Draw
        screen.fill((255, 255, 255))
        grid.draw(screen, pygame, grid_x, grid_y)
        screen.blit(text, (5, 5))
        pygame.display.flip()


main()
