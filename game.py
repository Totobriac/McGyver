import pygame
from pygame.locals import *
from maze import Maze
from player import Player

pygame.init()

window = pygame.display.set_mode((450, 450))


maze = Maze('maze.txt', window)
maze.create_maze()
maze.items()
maze.draw(window)



mac = Player('mac',maze.start_position, window)


keep_playing = True
pygame.display.flip()
collected = mac.collected_items
mac.draw_player(window)
maze.item_draw(window, collected)

while keep_playing:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            raise SystemExit

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "up"
            elif event.key == pygame.K_LEFT:
                direction = "left"
            elif event.key == pygame.K_DOWN:
                direction = "down"
            elif event.key == pygame.K_RIGHT:
                direction = "right"

            if mac.calculate_move(direction) in maze.paths:
                mac.do_move(direction)

                if mac.position in maze.items_position:
                    mac.collect(mac.position)

                elif mac.position in maze.guard_position:
                    mac.win(mac.collected_items)

    maze.draw(window)
    maze.item_draw(window, collected)
    mac.draw_player(window)

    pygame.display.flip()
