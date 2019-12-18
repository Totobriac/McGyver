from classes import *

maze = Maze ('maze.txt')

maze.create_maze()

mac = Player('mac',[2,2])


print(maze.guard_position)

keep_playing = True
print (mac.position)
while keep_playing:
    print (mac.position)
    direction = input("Where are you heading to?")
    if mac.calculate_move(direction) in maze.paths:
        mac.do_move(direction)        
        print('ok')
        if mac.position in maze.guard_position:
            print('It is a win')
    else:
        print('No way!')