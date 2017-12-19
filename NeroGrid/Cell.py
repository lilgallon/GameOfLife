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

    def __eq__(self, other):
        if isinstance(other, Cell):
            return other.column == self.column and other.line == self.line
        else:
            return False
