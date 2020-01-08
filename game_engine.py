import pygame
from maze import Maze
from player import Player


class GameEngine:

    def start_game(self):
        pygame.init()
        self.window = pygame.display.set_mode((450, 450))  
        self.maze = Maze('arts/maze.txt', self.window)
        self.maze.create_maze()
        self.maze.draw(self.window)
        self.mac = Player('mac', self.maze.start_position, self.window)
        self.mac.draw_player(self.window)
        self.collected = self.mac.collected_items
        self.maze.items_placement()
        self.maze.items_draw(self.window, self.collected)

    def refresh_game(self):
        self.maze.draw(self.window)
        self.maze.items_draw(self.window, self.collected)
        self.maze.text_items(self.collected)
        self.mac.draw_player(self.window)

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
                if self.mac.calculate_move(direction) in self.maze.paths:
                    self.mac.do_move(direction)
                    '''
                    Collects the objects
                    '''
                    if self.mac.position in self.maze.items_position:
                        self.mac.collect(self.mac.position)
                    '''
                    Checks if the player win or lose.
                    '''
                    if self.mac.position in self.maze.guard_position:
                        self.mac.win(self.mac.collected_items)
        