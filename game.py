from classes import *

maze = Maze ('maze.txt')

maze.create_maze()

mac = Player('mac',[2,2])


keep_playing = True
print (mac.position)
while keep_playing:
    print (mac.position)
    direction = input("Where are you heading to?")
    if mac.move(direction) in maze.paths:
        print ('ok')
    else: print('No way!')
