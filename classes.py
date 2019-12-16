
class Maze :
    
    def __init__ (self, level):
        
        self.level = level 
        self.walls = []
        self.paths = []

    def create_maze (self):

        with open (self.level) as f:
            for y, line in enumerate (f,1):                       
                for x, c in enumerate (line,1):
                    if c == 'x':
                        self.walls.append([x,y])
                    elif c == '0':
                        self.paths.append([x,y])
            return self.walls, self.paths



class Player :

    def __init__ (self,name, position):
        self.name = name
        self.position = position
        
    def move (self, direction):

        if direction == "right":
            
            self.position [0] += 1
            return self.position
            
        elif direction == "left":
            
            self.position [0] -= 1
            return self.position
            
        elif direction == "up":
           
            self.position [1] -= 1
            return self.position
            
        elif direction == "down":
           
            self.position [1] += 1
            return self.position
            


