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


def draw_grid(screen, pygame, x, y, lines, columns, width, height, thickness, color):
    """
    Draws a grid composed of empty rectangles. Uses pygame as graphic lib.
    :param screen: screen on which draw the grid
    :param pygame: graphic lib
    :param x: x position of the grid
    :param y: y position of the grid
    :param lines: number of lines of the grid
    :param columns: number of column of the grid
    :param width: width of a cell in the grid
    :param height: height of a cell in the grid
    :param thickness: thickness of a cell in the grid (outlines)
    :param color: color of the outline of the cells
    """
    for line in range(0, lines - 1):
        for column in range(0, columns - 1):
            draw_empty_rectangle(screen, pygame, x + (column * width), y + (line * height), width, height, thickness,
                                 color)


def draw_empty_rectangle(screen, pygame, x, y, width, height, thickness, color):
    """
    Draws an empty rectangle (only the outlines of a rectangle). Uses pygame as graphic lib.
    The outlines are generated from the middle of the outline.
    :param screen: screen on which draw the rectangle
    :param pygame: graphic lib
    :param x: x position of the rectangle
    :param y: y position of the rectangle
    :param width: width of a cell in the rectangle
    :param height: height of a cell in the rectangle
    :param thickness: thickness of the rectangle outline
    :param color: color of the rectangle outline
    """
    # top
    pygame.draw.rect(screen, color, pygame.Rect(x - thickness / 2, y - thickness / 2, width + thickness, thickness))
    # bottom
    pygame.draw.rect(screen, color, pygame.Rect(x - thickness / 2, y + height - thickness / 2, width + thickness,
                                                thickness))
    # left
    pygame.draw.rect(screen, color, pygame.Rect(x - thickness / 2, y, thickness, height))
    # right
    pygame.draw.rect(screen, color, pygame.Rect(x + width - thickness / 2, y, thickness, height))
