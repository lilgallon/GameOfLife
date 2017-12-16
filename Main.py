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
    grid_lines = 8
    cell_width = 50
    cell_height = 50
    cell_thickness = 1
    cell_color = (0, 150, 0)
    cells = [Cell(5, 4), Cell(5, 5), Cell(5, 6)]

    grid = Grid(cells, grid_lines, grid_columns, cell_width, cell_height, cell_thickness, cell_color)

    screen = pygame.display.set_mode(
        (2 * grid_x + (grid_columns - 1) * cell_width, 2 * grid_y + (grid_lines - 1) * cell_height))
    screen.fill((255, 255, 255))

    it = 0
    font = pygame.font.Font(None, 40)
    text = font.render(str(it), 1, (0, 0, 0))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
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
