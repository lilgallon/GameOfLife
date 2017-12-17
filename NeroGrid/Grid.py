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

import NeroUtils.Graphics as Graphics
from NeroGrid.Cell import Cell


class Grid:
    def __init__(self, cells, lines, columns, cell_width, cell_height, cell_thickness, cell_color):
        self.cells = cells
        self.lines = lines
        self.columns = columns
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_thickness = cell_thickness
        self.cell_color = cell_color

    def draw(self, screen, pygame, x, y):
        """
        Draws the grid with all its entities (not implemented)
        :param screen: screen on which draw the grid
        :param pygame: graphic lib
        :param x: x position of the grid
        :param y: y position of the grid
        """
        Graphics.draw_grid(screen, pygame, x, y, self.lines, self.columns, self.cell_width, self.cell_height,
                           self.cell_thickness, self.cell_color)
        for cell in self.cells:
            Graphics.draw_entity_in_grid(screen, pygame, x, y, self.lines, self.columns, self.cell_width,
                                         self.cell_height,
                                         self.cell_thickness, self.cell_color, cell.line, cell.column)

    def check_rules(self):
        new_cells = []
        # pass parameter by reference??
        # new_cells.extend(self.check_r1())
        new_cells.extend(self.check_r2())
        # new_cells.extend(self.check_r3())
        new_cells.extend(self.check_r4())
        self.cells = new_cells

    def check_r1(self):
        """
        Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
        """
        new_cells = []
        # useless
        return new_cells

    def check_r2(self):
        """
        Any live cell with two or three live neighbours lives on to the next generation.
        """
        new_cells = []
        for cell in self.cells:
            if self.count_neighbours(cell.line, cell.column) == 2 or self.count_neighbours(cell.line, cell.column) == 3:
                new_cells.append(Cell(cell.line, cell.column))

        return new_cells

    def check_r3(self):
        """
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        """
        new_cells = []
        # useless
        return new_cells

    def check_r4(self):
        """
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        print(" ")
        dead_cells = []
        for line in range(0, self.lines - 1):
            for column in range(0, self.columns - 1):
                if not self.is_alive(line, column):
                    dead_cells.append(Cell(line, column))

        new_cells = []
        for cell in dead_cells:
            if self.count_neighbours(cell.line, cell.column) == 3:
                new_cells.append(Cell(cell.line, cell.column))

        return new_cells

    def is_alive(self, line, column):
        i = 0
        found = False
        while not found and i < len(self.cells):
            if self.cells[i].line == line and self.cells[i].column == column:
                found = True
            else:
                i = i + 1
        return found

    def count_neighbours(self, line, column):
        """
        Count the neighbours of the cell. Returns -1 if there is an error.
        :param line: line of the cell
        :param column: column of the cell
        :return: number of neighbours of the specified cell
        """
        if line < 0 or line >= self.lines:
            print("The line #" + line + " is not in the defined range. (0;" + self.lines - 1 + ")")
            return -1
        if column < 0 or column >= self.columns:
            print("The column #" + column + " is not in the defined range. (0;" + self.lines - 1 + ")")
            return -1
        counter = 0
        for cell in self.cells:
            # X and Y and not Z
            # X : line neighbour | Y : column neighbour | Z : case when the cell is counting itself as a neighbour
            if (cell.line == line - 1 or cell.line == line or cell.line == line + 1) and (
                    cell.column == column - 1 or cell.column == column or cell.column == column + 1) and \
                    not (cell.line == line and cell.column == column):
                counter = counter + 1
        return counter

    def set_size(self, lines, columns):
        """
        Change the size (lines / columns) of the grid and adapt automatically the size of the grid (height / width)
        :param lines: new lines
        :param columns: new columns
        """
        if self.lines != lines:
            # % vertical  =         incremented height         * 100 /           initial height
            vertical_perc = ((self.lines - lines) * self.cell_height) * 100.0 / (self.lines * self.cell_height)
        if self.columns != columns:
            # % horizontal  =         incremented width         * 100 /           initial width
            horizontal_perc = ((self.columns - columns) * self.cell_width) * 100.0 / (self.columns * self.cell_width)

        print(horizontal_perc)
        self.cell_width = self.cell_width + (self.cell_width * horizontal_perc) / 100.0
        self.cell_height = self.cell_height + (self.cell_height * vertical_perc) / 100.0

        self.lines = lines
        self.columns = columns

    def move(self, d_lines, d_columns):
        """
        Used to navigate in the grid by moving the entities.
        :param d_lines: y movement (lines)
        :param d_columns: x movement (columns)
        """
        new_cells = []
        for cell in self.cells:
            new_cells.append(Cell(cell.line + d_lines, cell.column + d_columns))
        self.cells = new_cells

    def convert_to_grid_pos(self, x, y):
        column = int(x / self.cell_width)
        line = int(y / self.cell_height)
        return column, line
