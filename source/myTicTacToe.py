import pygame
import numpy as np
import time
from cell import Cell, images, checkWin, initTable


pygame.init() # Initiate the game.
pygame.display.set_caption("Tic Tac Toe: ugly version")
# Determinate and apply screen basic properties.
screenHeight = 900
screenWidth = 900
infoBarHeight = 0
screen = pygame.display.set_mode((screenWidth,screenHeight+infoBarHeight))
backgroundColor = 255,155,0
screen.fill(backgroundColor)
rows = 3
columns = 3
cellWidth = screenWidth / rows
cellHeight = screenHeight / columns

turns = ["x","o"] # Specify the possible turns.
currentTurn = 0
#currentTurnTest = np.random.randint(0, len(turns), 1)
#print(currentTurnTest[0])

# Load the images and resize them.
# Save the images in our images dictionary, understandable assignation:
xImage = pygame.image.load('images/x.png')
xImage = pygame.transform.scale(xImage, (cellWidth, cellHeight))
images['x'] = xImage
# Mental boom assignation:
images['o'] = pygame.transform.scale(pygame.image.load('images/o.png'), (cellWidth, cellHeight))
images['greenX'] = pygame.transform.scale(pygame.image.load('images/x_green.png'), (cellWidth, cellHeight))
images['greenO'] = pygame.transform.scale(pygame.image.load('images/o_green.png'), (cellWidth, cellHeight))

# Create table
table = []
for x in range(0, rows):
	row = []
	table.append(row)
	for y in range(0, columns):
		# Create every cell.
		cell = Cell(x, y, cellWidth, cellHeight)
		table[x].append(cell)

victory = False
runGame = True
while runGame: # Game execution
	
	# Display the whole table on screen
	for x in range(0,rows):
		for y in range(0,columns):
			table[x][y].drawLines(screen)

	pygame.display.flip() # Refresh screen content.

	# Check for keyboard and mouse clicks.
	for event in pygame.event.get():
		mouseClick = pygame.mouse.get_pressed() # This will return a three positions vector.
		
		if mouseClick[0] == 1 and not victory : # Check if left click is pressed.
			# Get position in pixels of the mouse.
			mouseXpos, mouseYpos = pygame.mouse.get_pos() # This function returns a two positions vector.
			xPos = mouseXpos
			yPos = mouseYpos
			
			# Find the cell clicked 
			for x in range(0, rows):
				for y in range(0, columns):
					if table[x][y].checkPosition(xPos, yPos) : # Check if the mouse position is in one of the cells.
						if table[x][y].emptyCell(turns[currentTurn]) : # Check if cell is empty.
							if checkWin(table):
								victory = True
								print(turns[currentTurn] +" WINS!")
								#table = initTable(rows, columns, cellWidth, cellHeight)
							else : 
								currentTurn +=1
							if currentTurn >= len(turns):
								currentTurn = 0
		# Check if ESC key or X button from the game window has been pressed		
		if event.type == pygame.QUIT:
			runGame = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				runGame = False