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
    for line in range(0, lines - 1):
        for column in range(0, columns - 1):
            draw_empty_rectangle(screen, pygame, x + (column * width), y + (line * height), width, height, thickness,
                                 color)


def draw_empty_rectangle(screen, pygame, x, y, width, height, thickness, color):
    # haut
    pygame.draw.rect(screen, color, pygame.Rect(x - thickness / 2, y - thickness / 2, width + thickness, thickness))
    # bas
    pygame.draw.rect(screen, color, pygame.Rect(x - thickness / 2, y + height - thickness / 2, width + thickness,
                                                thickness))
    # gauche
    pygame.draw.rect(screen, color, pygame.Rect(x - thickness / 2, y, thickness, height))
    # droite
    pygame.draw.rect(screen, color, pygame.Rect(x + width - thickness / 2, y, thickness, height))
