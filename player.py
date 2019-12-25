import pygame
from pygame.locals import *



class Player :

    def __init__ (self, name, start_position, window):

        self.name = name
        self.position = start_position
        self.collected_items = []
        self.window = window

    def calculate_move(self, direction):

        posible_position = self.position [:]
        if direction == "right":    posible_position[0] += 1
        elif direction == "left":   posible_position[0] -= 1
        elif direction == "up":     posible_position[1] -= 1
        elif direction == "down":   posible_position[1] += 1
        return posible_position

    def do_move(self, direction):

        self.position = self.calculate_move(direction)

    def collect (self, position):

        if position not in self.collected_items:
            self.collected_items.append(position)                        
            return self.collected_items

    def win (self, collected_items):

        if len(collected_items) == 3: print ('Good job!!!')
        else: print ('Dead!!!')

    def draw_player (self, window):
        mac_sprite = pygame.image.load('arts/mac_gyver.png').convert()
        x = self.position [0] * 30
        y = self.position [1] * 30
        window.blit(mac_sprite,(x,y))
