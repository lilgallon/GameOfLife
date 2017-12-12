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

import NeroGrid.Cell as Cell
import NeroUtils.Graphics as Graphics


class Grid:
    def __init__(self, lines, columns, cell_width, cell_height, cell_thickness, cell_color):
        self.cells = [Cell]
        self.lines = lines
        self.columns = columns
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_thickness = cell_thickness
        self.cell_color = cell_color

    def draw(self, screen, pygame, x, y):
        Graphics.draw_grid(screen, pygame, x, y, self.lines, self.columns, self.cell_width, self.cell_height,
                           self.cell_thickness, self.cell_color)