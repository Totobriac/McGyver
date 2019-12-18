import random

class Maze :
    
    def __init__ (self, level):
        
        self.level = level 
        self.walls = []
        self.paths = []
        self.guard_position = []
        self.hero_position = []
     
    def create_maze (self):
        
        with open (self.level) as f:
            for y, line in enumerate (f,1):                       
                for x, c in enumerate (line,1):
                    if c == 'x': self.walls.append([x,y])
                    elif c == '0': self.paths.append([x,y])
                    elif c == 'G': self.paths.append([x,y]), self.guard_position.append([x,y])
                    elif c == 'H': self.paths.append([x,y]), self.hero_position.append([x,y])                   
            return self.walls, self.paths, self.guard_position, self.hero_position

    def items (self):

        items_position = []      
        while len(items_position) < 3:
            item_position = random.choice(self.paths[1:-1])
            if item_position not in items_position and item_position not in self.guard_position and item_position not in self.hero_position:
                items_position.append(item_position)
        return items_position



class Player :

    def __init__ (self, name, position):

        self.name = name
        self.position = position
        self.collected_items = []
        
    def calculate_move(self, direction):
        
        posible_position = self.position [:] 
        if direction == "right":    posible_position[0] += 1
        elif direction == "left":   posible_position[0] -= 1
        elif direction == "up":     posible_position[1] -= 1
        elif direction == "down":   posible_position[1] += 1
        return posible_position

    def do_move(self, direction):
        
        self.position = self.calculate_move(direction)

    def collect (self, position):
        
        if position not in self.collected_items:            
            self.collected_items.append(position)
            print ('You get an object!')  
            return self.collected_items 

    def win (self, collected_items):

        if len(collected_items) == 3: print ('Good job!!!')
        else: print ('Dead!!!')


