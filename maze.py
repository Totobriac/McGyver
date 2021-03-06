import pygame
import random


class Maze:
    """
    This class creates the maze.
    """
    def __init__(self, level, window):
        """
        The maze constructor.

        Parameters:
           level (.txt): A .txt file. Creates the whole maze from it.
        """
        self.level = level
        self.walls = []
        self.paths = []
        self.guard_position = []
        self.hero_position = []
        self.window = window

    def create_maze(self):
        """
        Reads the level.txt and create the maze skeleton.

        Returns:
            lists with paths, walls, hero and guard starting position.
        """
        with open(self.level) as f:
            for y, line in enumerate(f):
                for x, c in enumerate(line):
                    if c == 'x':
                        self.walls.append([x, y])
                    elif c == '0':
                        self.paths.append([x, y])
                    elif c == 'G':
                        self.paths.append([x, y]),
                        self.guard_position.append([x, y])
                    elif c == 'H':
                        self.paths.append([x, y])
                        self.hero_position.append([x, y])
                        self.start_position = [self.hero_position[0][0],
                                               self.hero_position[0][1]]
            return (self.walls, self.paths, self.guard_position,
                    self.start_position)

    def items_placement(self):
        """
        Function that checks for random posible positions for the objects.

        Returns:
            a list with the position of the objects
        """

        self.items_position = []
        while len(self.items_position) < 3:
            item_position = random.choice(self.paths)
            if item_position not in self.items_position and\
               item_position not in self.guard_position and \
               item_position not in self.hero_position:
                self.items_position.append(item_position)
        return self.items_position

    def draw(self, window):
        """
        Function that draws the background, walls and guard in the game window.
        """

        background = pygame.image.load('arts/floor.png').convert()
        window.blit(background, (0, 0))

        wall = pygame.image.load('arts/wall.png').convert()
        for i in self.walls:
            x = i[0] * 30
            y = i[1] * 30
            window.blit(wall, (x, y))

        guard = pygame.image.load('arts/guard.png').convert()
        x = self.guard_position[0][0] * 30
        y = self.guard_position[0][1] * 30
        window.blit(guard, (x, y))

    def items_draw(self, window, collected):
        """
        Function that draws the objects in the game window.

        Parameters:
            collected : a list of the objects already collected by the player
        """

        sprite = [pygame.image.load('arts/needle.png').convert(),
                  pygame.image.load('arts/ether.png').convert(),
                  pygame.image.load('arts/tube.png').convert_alpha()]

        for i in range(len(self.items_position)):
            x = self.items_position[i][0] * 30
            y = self.items_position[i][1] * 30
            if self.items_position[i] not in collected:
                window.blit(sprite[i], (x, y))

    def text_items(self, collected):
        """
        Function that draws how many objects are colleced in the game window.

        Parameters:
            collected : a list of the objects already collected by the player
        """
        inventory_count = len(collected)
        font = pygame.font.SysFont('Comic Sans MS', 28)
        items_count = "Items collected : {}".format(inventory_count)
        text = font.render(items_count, 2, (42, 42, 42))
        self.window.blit(text, (0, 0))
