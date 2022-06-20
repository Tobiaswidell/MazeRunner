import sys
import os

from numpy import char, character

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
MAZES_DIRECTORY = 'F:\PythonProjects\MazeRunner\Mazes'

PLAYER = '@'
BLOCK = chr(9617) 

def displayMaze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if(x,y) == (playerX, playerY):
                print(PLAYER, end='')
            elif(x,y) == (exitX, exitY):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print( maze[(x, y)], end='')
            print()
            
while True:
    print('Enter filename of MAZE')
    filename = input('> ')
    
    if filename.upper == 'LIST':
        for fileInCurrentFolder in os.listdir(MAZES_DIRECTORY):
            if(fileInCurrentFolder.startswith('Maze')
               and fileInCurrentFolder.endswith('.txt')):
                print('FileInCurrentFolder- ', fileInCurrentFolder)
        continue
    if filename.upper() == 'QUIT':
        sys.exit()
    if filename.upper() == 'CD':
        os.chdir(MAZES_DIRECTORY)   
        print('Changed directory - ',{MAZES_DIRECTORY})
    if filename.upper() == 'DIR':
        print('dir - '+os.getcwd())
    if os.path.exists(filename):
        print('There are no file named',filename)
        break
      
# Load maze from file

mazeFile = open(filename)
maze = {}
lines = mazeFile.readlines()
playerX = None
playerY = None
exitY = None
exitX = None
y = 0

for line in lines:
    WIDTH = len(line.rstrip())
    for x, character in enumerate(line.rstrip()):
        assert character in (WALL, EMPTY, START, EXIT,), 'invalid character at column {}, line {}'.format(x + 1, y + 1)
        if character in (WALL, EMPTY):
           maze[(x, y)] = character
        elif character == START:
            playerX, playerY = x, y
            maze[(x, y)] = EMPTY
        elif character == EXIT:
            exitX, exitY = x, y
            maze[(x, y)] = EMPTY
    y += 1
HEIGHT = y

assert playerX != None and playerY != None, 'No start in maze file.'
assert exitX != None and exitY != None, 'No exit in maze file.'

while True: # Main loop
    displayMaze(maze)
    
    while True:
        print('Enter Direction')
        move = input('> ').upper()
        
        if move == 'QUIT':
            print('Good bye!')
            sys.exit()
        if move not in ['W','A','S','D',]:
                print('Invalid direction')
                continue
            
        if move == 'W' and maze[(playerX, playerY - 1)] == EMPTY:
            break
        elif move == 'S' and maze[(playerX, playerY + 1)] == EMPTY:
            break
        elif move == 'A' and maze[(playerX - 1, playerY)] == EMPTY:
            break
        elif move == 'D' and maze[(playerX + 1, playerY)] == EMPTY:
            break
        
        print('Cant move in that direction')
        
    # Keep moving in this direction until you encounter a branch point.
    if move == 'W':
        while True:
            playerY -= 1
    if (playerX, playerY) == (exitX, exitY):
        break
    if maze[(playerX, playerY - 1)] == WALL:
        break # Break if we've hit a wall.
    if (maze[(playerX - 1, playerY)] == EMPTY
    or maze[(playerX + 1, playerY)] == EMPTY):
        break # Break if we've reached a branch point.
    elif move == 'S':
        while True:
            playerY += 1
    if (playerX, playerY) == (exitX, exitY):
        break
    if maze[(playerX, playerY + 1)] == WALL:
        break # Break if we've hit a wall.
    if (maze[(playerX - 1, playerY)] == EMPTY
    or maze[(playerX + 1, playerY)] == EMPTY):
        break # Break if we've reached a branch point.
    elif move == 'A':
        while True:
            playerX -= 1
    if (playerX, playerY) == (exitX, exitY):
        break
    if maze[(playerX - 1, playerY)] == WALL:
        break # Break if we've hit a wall.
    if (maze[(playerX, playerY - 1)] == EMPTY
    or maze[(playerX, playerY + 1)] == EMPTY):
        break # Break if we've reached a branch point.
    elif move == 'D':
        while True:
            playerX += 1
    if (playerX, playerY) == (exitX, exitY):
        break
    if maze[(playerX + 1, playerY)] == WALL:
        break # Break if we've hit a wall.
    if (maze[(playerX, playerY - 1)] == EMPTY
    or maze[(playerX, playerY + 1)] == EMPTY):
        break
    if (playerX, playerY) == (exitX, exitY):
        displayMaze(maze)
        print('You have reached the exit! Good job!')
        print('Thanks for playing!')
        sys.exit()
