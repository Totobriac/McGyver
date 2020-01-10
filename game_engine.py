import pygame
from maze import Maze
from player import Player


class GameEngine:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((450, 450))
        self.maze = Maze('arts/maze.txt', self.window)
        self.maze.create_maze()
        self.maze.draw(self.window)
        self.player = Player('mac', self.maze.start_position, self.window)
        self.player.draw_player(self.window)
        self.collected = self.player.collected_items
        self.maze.items_placement()
        self.maze.items_draw(self.window, self.collected)

    def refresh_game(self):
        self.maze.draw(self.window)
        self.maze.items_draw(self.window, self.collected)
        self.maze.text_items(self.collected)
        self.player.draw_player(self.window)

    def game_loop(self):
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

                """
                Checks if move is posible or not.
                """
                if self.player.calculate_move(direction) in self.maze.paths:
                    self.player.do_move(direction)
                    '''
                    Collects the objects
                    '''
                    if self.player.position in self.maze.items_position:
                        self.player.collect(self.player.position)
                    '''
                    Checks if the player win or lose.
                    '''
                    if self.player.position in self.maze.guard_position:
                        self.player.win(self.player.collected_items)
