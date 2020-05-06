import pygame

images = {}

class Cell:
	empty = True
	value = "blank" # Can be blank, o or x

	def __init__(self, x, y, width, height):
		# Initiate the properties for a cell
		self.x = x
		self.y = y
		self.width = width
		self.height = height


		self.xPos = self.x * self.width 
		self.yPos = self.y * self.height 

	def drawLines(self, screen):
		pygame.draw.rect(screen, (25,25,25),(self.xPos, self.yPos, self.width, self.height), 5)
		if not self.empty:
			screen.blit(images[self.value], (self.xPos, self.yPos))

	def emptyCell(self, value): # This function actually just changes the value of the cell.
		if not self.empty :
			return False
		self.value = value # If cell is empty we add a value.
		self.empty = False
		self.image = images[self.value] # Storage the image
		return True

	def checkPosition(self, xPos, yPos):
		initialX = self.xPos
		initialY = self.yPos
		endX = self.xPos + self.width
		endY = self.yPos + self.height

		if xPos < initialX or xPos > endX :
			return False
		if yPos < initialY or yPos > endY :
			return False

		return True

def checkWin(table):
	# Check for an horizontal win.
	for y in range(0,3):
		currentValue = table[0][y].value
		pieces = 0
		for x in range(0,3):
			
			if table[x][y].value == currentValue : 
				pieces += 1

		if pieces == 3 and currentValue != "blank": # WIN
			if currentValue == 'x' : victoryValue = 'greenX'
			elif currentValue == 'o' : victoryValue = 'greenO'
			for x in range(0,3):
				table[x][y].value = victoryValue
			return True

	# Check for a vertical win
	for x in range(0,3):
		currentValue = table[x][0].value
		pieces = 0
		for y in range(0,3):
			if table[x][y].value == currentValue : 
				pieces += 1
		if pieces == 3 and currentValue != "blank": # WIN
			if currentValue == 'x' : victoryValue = 'greenX'
			elif currentValue == 'o' : victoryValue = 'greenO'
			for y in range(0,3):
				table[x][y].value = victoryValue
			return True

	# Check diagonal wins
	if table[1][1].value != "blank" :
		currentValue = table[1][1].value
		if table[0][0].value == currentValue and table[2][2].value == currentValue : # WIN
			if currentValue == 'x' :
				for i in range(0,3):
					table[i][i].value = 'greenX'
			elif currentValue == 'o' :
				table[1][1].value = 'greenO'
				table[0][0].value = 'greenO'
				table[2][2].value = 'greenO'
			return True
		elif table[0][2].value == currentValue and table[2][0].value == currentValue : # WIN
			if currentValue == 'x' : victoryValue = 'greenX'
			elif currentValue == 'o' : victoryValue = 'greenO'

			table[1][1].value = victoryValue
			table[0][2].value = victoryValue
			table[2][0].value = victoryValue
			return True

	# Arrived at this point there is no win		
	return False # NOT WIN

def initTable(rows, columns, cellWidth, cellHeight):
	# Create table
	table = []
	for x in range(0, rows):
		row = []
		table.append(row)
		for y in range(0, columns):
			# Create every cell.
			cell = Cell(x, y, cellWidth, cellHeight)
			table[x].append(cell)
	return table


