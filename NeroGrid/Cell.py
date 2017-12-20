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


class Cell:
    def __init__(self, column, line):
        self.column = column
        self.line = line

    # str(self)
    def __str__(self):
        return str(self.column) + ";" + str(self.line)

    # self + other
    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(self.column + other.column, self.line + other.line)
        else:
            return Cell(self.column + other, self.line + other)

    # self - other
    def __sub__(self, other):
        if isinstance(other, Cell):
            return Cell(self.column - other.column, self.line - other.line)
        else:
            return Cell(self.column - other, self.line - other)

    # self / other
    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(self.column/ other.column, self.line / other.line)
        else:
            return Cell(self.column / other, self.line / other)

    # self ^ power
    def __pow__(self, power, modulo=None):
        if isinstance(power, Cell):
            raise ValueError("You should not use pow between two cells.")
        else:
            return Cell(self.column ** power, self.line ** power)

    # self < other
    def __lt__(self, other):
        if isinstance(other, Cell):
            return other.column < self.column and other.line < self.line
        else:
            return False

    # self <= other
    def __le__(self, other):
        if isinstance(other, Cell):
            return other.column <= self.column and other.line <= self.line
        else:
            return False

    # self != other
    def __ne__(self, other):
        return not self.__eq__(self, other)

    # self == other
    def __eq__(self, other):
        if isinstance(other, Cell):
            return other.column == self.column and other.line == self.line
        else:
            return False

    # self > other
    def __gt__(self, other):
        if isinstance(other, Cell):
            return other.column > self.column and other.line > self.line
        else:
            return False

    # self >= other
    def __ge__(self, other):
        if isinstance(other, Cell):
            return other.column >= self.column and other.line >= self.line
        else:
            return False