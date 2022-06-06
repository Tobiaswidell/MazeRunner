import sys
import os

from numpy import char, character

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

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
        for fileInCurrentFolder in os.listdir():
            if(fileInCurrentFolder.startswith('maze')
               and fileInCurrentFolder.endswith('.txt')):
                print(' ', fileInCurrentFolder)
        continue
    if filename.upper() == 'QUIT':
        sys.exit()
        
    if os.path.exists(filename):
          print('There are no file named ',filename)
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
    for x, character in emulate(line.rstrip()):
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


