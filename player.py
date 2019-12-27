import pygame


class Player:
    """
    This class creates the player.
    """
    def __init__(self, name, start_position, window):
        """
        The player constructor.

        Parameters:
           name: a string with player name
           start_position: a liste given by Maze.create_maze
        """
        self.name = name
        self.position = start_position
        self.collected_items = []
        self.window = window

    def calculate_move(self, direction):
        """
        Function that calculate if a move is posible or no.

        Parameters:
           direction: a string given by the main loop

        Returns:
          a list with a new directon
        """

        posible_position = self.position[:]
        if direction == "right":
            posible_position[0] += 1
        elif direction == "left":
            posible_position[0] -= 1
        elif direction == "up":
            posible_position[1] -= 1
        elif direction == "down":
            posible_position[1] += 1
        return posible_position

    def do_move(self, direction):
        """
        Function that moves the player around.

        Parameters:
           direction: a string given by the main loop

        Returns:
            the player new position.
        """
        self.position = self.calculate_move(direction)

    def collect(self, position):
        """
        Function that collects the objects.

        Parameters:
           position: a list with the player position.

        Returns:
            a list with the collected items.
        """

        if position not in self.collected_items:
            self.collected_items.append(position)
            return self.collected_items

    def win(self, collected_items):
        """
        Function that checks if the player wan.

        Parameters:
           collected_items: a list with the collected items.

        Returns:
            a print if it's a win or a loss.
        """

        if len(collected_items) == 3:
            print('Good job!!!')
        else:
            print('Dead!!!')

    def draw_player(self, window):
        """
        Function that draws the player on the game window.
        """
        mac_sprite = pygame.image.load('arts/mac_gyver.png').convert()
        x = self.position[0] * 30
        y = self.position[1] * 30
        window.blit(mac_sprite, (x, y))
