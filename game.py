walls = []
paths = []

class Maze :

    def __init__ (self, level):
        self.level = level

    def create_maze (self):
        with open (self.level) as f:
            for x, line in enumerate (f):                       
                for y, c in enumerate (line):
                    if c == 'x':
                        walls.append((x,y))
                    elif c == '0':
                        paths.append((x,y))

maze = Maze ('maze.txt')

maze.create_maze()


position = (2,2)

if position in walls:
    print ('ok')
else: print('no')