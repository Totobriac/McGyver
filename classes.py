
class Maze :
    
    def __init__ (self, level):
        
        self.level = level 
        self.walls = []
        self.paths = []
        self.guard_position = []

    def create_maze (self):

        with open (self.level) as f:
            for y, line in enumerate (f,1):                       
                for x, c in enumerate (line,1):
                    if c == 'x':
                        self.walls.append([x,y])
                    elif c == '0':
                        self.paths.append([x,y])
                    elif c == 'G':
                        self.paths.append([x,y])
                        self.guard_position.append([x,y])
            return self.walls, self.paths



class Player :

    def __init__ (self,name, position):
        self.name = name
        self.position = position
        
    def calculate_move(self, direction):
        
        posible_position = self.position [:] 
        if direction == "right":    posible_position[0] += 1
        elif direction == "left":   posible_position[0] -= 1
        elif direction == "up":     posible_position[1] -= 1
        elif direction == "down":   posible_position[1] += 1
        return posible_position

    def do_move(self, direction):
        """Actually move in the given direction"""
        self.position = self.calculate_move(direction)

