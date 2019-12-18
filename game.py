from classes import *
import random

maze = Maze('maze.txt')
maze.create_maze()
objects = maze.items()
print (objects)

position = [maze.hero_position[0][0], maze.hero_position[0][1]]
mac = Player('mac',position)

keep_playing = True

while keep_playing:
    print (mac.position)
    print (mac.collected_items)
    direction = input("Where are you heading to?")
    if direction == "quit":
        keep_playing = False
    elif mac.calculate_move(direction) in maze.paths:
        mac.do_move(direction)
        print('ok')
        if mac.position in objects:                    
            mac.collect(mac.position)                        
        elif mac.position in maze.guard_position:
            mac.win (mac.collected_items) 
    else : print ('No way!!')  