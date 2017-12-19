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
        """
        Updates the grid according to the rules.
        """
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
        dead_cells = []
        # Optimized algorithm for small grid
        for line in range(0, self.lines):
            for column in range(0, self.columns):
                if not self.is_alive(line, column):
                    dead_cells.append(Cell(line, column))

        # Optimized algorithm for huge grid
        # For every alive cell, we look at all their neighbours to
        # see if they are dead.
        # for cell in self.cells:
        #     for l_inc in range(-1, 2):
        #         for c_inc in range(-1, 2):
        #             if not self.is_alive(cell.line + l_inc, cell.column + c_inc):
        #                 dead_cells.append(cell)

        new_cells = []
        for cell in dead_cells:
            if self.count_neighbours(cell.line, cell.column) == 3:
                new_cells.append(cell)

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
        """
        Convert a x;y position to a c;l position regardless of the grid
        :param x:
        :param y:
        :return:
        """
        column = int(x / self.cell_width)
        line = int(y / self.cell_height)
        return column, line

    def check_cells(self, cells):
        """
        Just a debug method...
        :param cells:
        """
        for cell in cells:
            print(str(cell.column) + ";" + str(cell.line))

    def update_cell(self, x, y, gapx, gapy):
        """
        Update the cell : if it is alive , then it dies, and if it is dead, it gets alive
        And this, according to the x / y position in the window
        :param x: x position in the window
        :param y: y position in the window
        :param gapx: initial x position of the grid
        :param gapy: initial y position of the grid
        """
        column = int((x - gapx) / self.cell_width)
        line = int((y - gapy) / self.cell_height)

        if 0 < column < self.columns and 0 < line < self.lines:
            if self.is_alive(line, column):
                new_cells = []
                for cell in self.cells:
                    if cell != Cell(line, column):
                        new_cells.append(cell)
                self.cells = new_cells
            else:
                self.cells.append(Cell(line, column))
