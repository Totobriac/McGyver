import pygame
from game_engine import GameEngine

"""
initialize maze
"""
new_game = GameEngine()
new_game.start_game()

keep_playing = True

"""
Main Loop
"""
while keep_playing:
    new_game.game_loop()

    """
    Refresh the window
    """
    new_game.refresh_game()
    pygame.display.flip()
