import pygame
from pygame.locals import *
from constants import *

class Level:

    def __init__ (self ):
        self.map = 0

    def generate (self):
        with open('/home/pi/Documents/McGyver/maze.txt', "r") as maze:
            level_design = []
            for line in maze:
                level_line = []
                for sprite in line:
                    if sprite != '\n':
                        level_line.append(sprite)
                level_design.append(level_line)
                self.map = level_design

    def draw (self,window):

        wall_texture = pygame.image.load(wall).convert()
        floor_texture = pygame.image.load(floor).convert()

        num_line = 0
        for line in self.map:
            num_column =0
            for sprite in line:
                x = num_column * 60
                y = num_line * 60
                if sprite == 'x':
                    window.blit(wall_texture,(x,y))
                elif sprite == '0':
                    window.blit(floor_texture,(x,y))
                num_column += 1
            num_line += 1


# def start ():
#     window = pygame.display.set_mode((900, 900), RESIZABLE)
#     jeu = Level()
#     jeu.generate()
#     jeu.draw(window)

class Player:
    def __init__(self):
        self.player = Player
        self.case_x = 1
        self.case_y = 1
        self.x = 60
        self.y = 60


