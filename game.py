import pygame
from maze import Maze
from player import Player

"""
initialize pygame
"""
pygame.init()
window = pygame.display.set_mode((450, 450))

"""
Creates and draws the maze on the window
"""
maze = Maze('arts/maze.txt', window)
maze.create_maze()
maze.draw(window)

"""
Creates and draws the player on the window
"""
mac = Player('mac', maze.start_position, window)
mac.draw_player(window)

"""
Creates and draws the objects on the window
"""
collected = mac.collected_items
maze.items_placement()
maze.items_draw(window, collected)
keep_playing = True


pygame.display.flip()

"""
Main Loop
"""
while keep_playing:

    for event in pygame.event.get():
        """
        Get the players keyboard inputs
        """
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

            """
            Checks if move is posible or not.
            """
            if mac.calculate_move(direction) in maze.paths:
                mac.do_move(direction)
                '''
                Collects the objects
                '''
                if mac.position in maze.items_position:
                    mac.collect(mac.position)
                '''
                Checks if the player win or lose.
                '''
                if mac.position in maze.guard_position:
                    mac.win(mac.collected_items)

    """
    Refresh the window
    """
    maze.draw(window)
    maze.items_draw(window, collected)
    maze.text_items(collected)
    mac.draw_player(window)

    pygame.display.flip()
