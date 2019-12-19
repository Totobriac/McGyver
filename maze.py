import pygame
from pygame.locals import *

import random

class Maze :
    
    def __init__ (self, level, window):
        
        self.level = level 
        self.walls = []
        self.paths = []
        self.guard_position = []
        self.hero_position = []
        self.window = window
           

    def create_maze (self):
        
        with open (self.level) as f:
            for y, line in enumerate (f):                       
                for x, c in enumerate (line):
                    if c == 'x': self.walls.append([x,y])
                    elif c == '0': self.paths.append([x,y])
                    elif c == 'G': self.paths.append([x,y]), self.guard_position.append([x,y])
                    elif c == 'H': 
                        self.paths.append([x,y]) 
                        self.hero_position.append([x,y])
                        self.position = [self.hero_position[0][0], self.hero_position[0][1]]                   
            return self.walls, self.paths, self.guard_position, self.hero_position, self.position

    def items (self):

        self.items_position = []      
        while len(self.items_position) < 3:
            item_position = random.choice(self.paths)
            if item_position not in self.items_position and item_position not in self.guard_position and item_position not in self.hero_position:
                self.items_position.append(item_position)
        return self.items_position

    def draw (self, window):

        wall = pygame.image.load('wall.png').convert()
        for i in self.walls:
            x = i[0] * 30
            y = i[1] * 30
            window.blit(wall,(x,y))
          
        guard = pygame.image.load('guard.png').convert()
        x = self.guard_position [0][0] * 30
        y = self.guard_position [0][1] * 30
        window.blit(guard,(x,y))

        items_draw = []
        needle = pygame.image.load('needle.png').convert()
        ether = pygame.image.load('ether.png').convert()
        tube = pygame.image.load('tube.png').convert()
        for i in self.items_position:
            x = i[0] * 30
            y = i[1] * 30
            items_draw.append([x,y])
        
        window.blit(needle,(items_draw[0][0],items_draw[0][1]))
        window.blit(ether,(items_draw[1][0],items_draw[1][1]))
        window.blit(tube,(items_draw[2][0],items_draw[2][1]))







