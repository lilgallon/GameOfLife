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


# TODO:
# Big optimization
# https://docs.python.org/2/tutorial/datastructures.html
#
# tuple = list that can't be modified
# dictionary ~= c++ map http://apprendre-python.com/page-apprendre-dictionnaire-python

class Grid:
    def __init__(self, alive_entities, columns, lines, cell_width, cell_height, cell_thickness, cell_color):
        self.alive_entities = alive_entities
        self.dead_entities = []
        self.columns = columns
        self.lines = lines
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.cell_thickness = cell_thickness
        self.cell_color = cell_color
        self.column_origin = 0
        self.line_origin = 0
        self.last_updated_cell = Cell(-6000, -6000)

    def draw(self, screen, pygame, x, y):
        """
        Draws the grid with all its entities (not implemented)
        :param screen: screen on which draw the grid
        :param pygame: graphic lib
        :param x: x position of the grid
        :param y: y position of the grid
        """
        Graphics.draw_grid(screen, pygame, x, y, self.columns, self.lines, self.cell_width, self.cell_height,
                           self.cell_thickness, self.cell_color)
        for cell in self.alive_entities:
            Graphics.draw_entity_in_grid(screen, pygame, x, y, self.column_origin, self.line_origin, self.cell_width,
                                         self.cell_height, self.cell_color, cell.line, cell.column)

    def check_rules(self):
        """
        Updates the grid according to the rules.
        """
        new_alive_entities = []
        # pass parameter by reference??
        new_alive_entities.extend(self.check_r123())
        new_alive_entities.extend(self.check_r4())
        self.alive_entities = new_alive_entities

    def check_r123(self):
        """
        Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
        Any live cell with two or three live neighbours lives on to the next generation.
        Any live cell with more than three live neighbours dies, as if by overpopulation.
        """
        new_alive_entities = []
        for cell in self.alive_entities:
            if self.count_neighbours(cell.column, cell.line) == 2 or self.count_neighbours(cell.column, cell.line) == 3:
                new_alive_entities.append(Cell(cell.column, cell.line))

        return new_alive_entities

    def check_r4(self):
        """
        Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        """
        dead_entities = []
        # Optimized algorithm for small grid
        for column in range(0, self.columns):
            for line in range(0, self.lines):
                if not self.is_alive(column, line):
                    dead_entities.append(Cell(column, line))

        # Optimized algorithm for huge grid
        # For every alive cell, we look at all their neighbours to
        # see if they are dead.
        # for cell in self.alive_entities:
        #     for l_inc in range(-1, 2):
        #         for c_inc in range(-1, 2):
        #             if not self.is_alive(cell.line + l_inc, cell.column + c_inc):
        #                 dead_entities.append(cell)

        new_alive_entities = []
        for cell in dead_entities :
            if self.count_neighbours(cell.column, cell.line) == 3:
                new_alive_entities.append(cell)

        return new_alive_entities

    def is_alive(self, column, line):
        """
        Returns if the
        :param column:
        :param line:
        :return:
        """
        try:
            self.alive_entities.index(Cell(column, line))
            return True
        except ValueError:
            return False

    def count_neighbours(self, column, line):
        """
        Count the neighbours of the cell. Returns -1 if there is an error.
        :param line: line of the cell
        :param column: column of the cell
        :return: number of neighbours of the specified cell
        """
        if line < 0 or line >= self.lines:
            print("The line #" + str(line) + " is not in the defined range. (0;" + str(self.lines - 1) + ")")
            return -1
        if column < 0 or column >= self.columns:
            print("The column #" + str(column) + " is not in the defined range. (0;" + str(self.lines - 1) + ")")
            return -1
        counter = 0
        for cell in self.alive_entities:
            # X and Y and not Z
            # X : line neighbour | Y : column neighbour | Z : case when the cell is counting itself as a neighbour
            if (cell.line == line - 1 or cell.line == line or cell.line == line + 1) and (
                    cell.column == column - 1 or cell.column == column or cell.column == column + 1) and \
                    not (cell.line == line and cell.column == column):
                counter = counter + 1
        return counter

    def set_size(self, columns, lines):
        """
        Change the size (lines / columns) of the grid and adapt automatically the size of the grid (height / width)
        :param lines: new lines
        :param columns: new columns
        """

        # if we already have reached the minimum size OR we want to reduce the size, we cancel
        if (self.columns == 2 or self.lines == 2) and (self.lines > lines or self.columns > columns):
            return

        if self.lines > lines:
            line_inc = -1
        elif self.lines < lines:
            line_inc = 1
        else:
            line_inc = 0
        if self.columns > columns:
            column_inc = -1
        elif self.columns < columns:
            column_inc = 1
        else:
            column_inc = 0

        if self.lines != lines:
            # % vertical  =         incremented height         * 100 /           initial height
            vertical_perc = ((self.lines - lines) * self.cell_height) * 100.0 / \
                            ((self.lines + line_inc) * self.cell_height)
        if self.columns != columns:
            # % horizontal  =         incremented width         * 100 /           initial width
            horizontal_perc = ((self.columns - columns) * self.cell_width) * 100.0 / \
                              ((self.columns + column_inc) * self.cell_width)

        self.cell_width = self.cell_width + (self.cell_width * horizontal_perc) / 100.0
        self.cell_height = self.cell_height + (self.cell_height * vertical_perc) / 100.0

        self.lines = lines
        self.columns = columns

    def move(self, d_columns, d_lines):
        """
        Used to navigate in the grid by moving the entities.
        :param d_lines: y movement (lines)
        :param d_columns: x movement (columns)
        """
        self.column_origin += d_columns
        self.line_origin += d_lines

    def convert_to_grid_pos(self, x, y):
        """
        Convert a x;y position to a c;l position regardless of the grid
        :param x:
        :param y:
        :return:
        """
        column = int(x / self.cell_width)
        line = int(y / self.cell_height)
        return column, line

    # TODO: remove
    def check_cells(self, cells):
        """
        Just a debug method...
        :param cells:
        """
        for cell in cells:
            print(str(cell.column) + ";" + str(cell.line))

    def update_cell(self, x, y):
        """
        Update the cell : if it is alive , then it dies, and if it is dead, it gets alive
        And this, according to the x / y position in the window
        :param x: x position in the window
        :param y: y position in the window
        """
        column = int(x / self.cell_width)
        line = int(y / self.cell_height)

        if self.last_updated_cell == Cell(column, line):
            return

        if 0 < column < self.columns and 0 < line < self.lines:
            self.last_updated_cell = Cell(column, line)
            if self.is_alive(column - self.column_origin, line - self.line_origin):
                self.alive_entities.remove(Cell(column - self.column_origin, line - self.line_origin))
            else:
                self.alive_entities.append(Cell(column - self.column_origin, line - self.line_origin))
