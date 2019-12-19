import pygame
from pygame.locals import *
from maze import Maze
from player import Player

pygame.init()

window = pygame.display.set_mode((450, 450))
background = pygame.image.load('floor.png').convert()
window.blit(background,(0,0))


maze = Maze('maze.txt', window)
maze.create_maze()
maze.items()
maze.draw(window)

position = [maze.hero_position[0][0], maze.hero_position[0][1]]
mac = Player('mac',position)

keep_playing = True
pygame.display.flip()
while keep_playing:
    
    direction = input("Where are you heading to?")
    if direction == "quit":
        keep_playing = False
    elif mac.calculate_move(direction) in maze.paths:
        mac.do_move(direction)     
        if mac.position in maze.items_position:                    
            mac.collect(mac.position)                        
        elif mac.position in maze.guard_position:
            mac.win(mac.collected_items) 
   
    pygame.display.flip()
   