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
    def __init__(self, line, column):
        self.line = line
        self.column = column

    def __eq__(self, other):
        if isinstance(other, self):
            return other.line == self.line and other.column == self.column
        else:
            return False
