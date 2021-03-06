# DO NOT EDIT THIS FILE

from Problem import *

from copy import *
#from cs1graphics import *
from time import sleep

class FifteenPuzzle(Problem):
	"""A problem representing a 15 tile sliding puzzle.
	
	The representation will be a two-d array of which tile is
	in a given postion.  0 represents the empty space."""
	
	def getSolved(self):
		return ((0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14,15))
	
	def actions(self, state):
		"""Return the possible moves, represented by the integer that
		can be moved into the empty space."""
		
		for i in range(4):
			for j in range(4):
				if state[i][j] == 0:
					row = i
					col = j
					
		actions = []		
		if row > 0:
			actions.append('U')
		if row < 3:
			actions.append('D')
		if col > 0:
			actions.append('L')
		if col < 3:
			actions.append('R')

		return actions
		
	def result(self, state, action):
		"""Apply the action to the state."""
		
		for i in range(4):
			for j in range(4):
				if state[i][j] == 0:
					blankRow = i
					blankCol = j
				
		if action == 'U':
			tileRow = blankRow - 1
			tileCol = blankCol
		elif action == 'D':
			tileRow = blankRow + 1
			tileCol = blankCol
		elif action == 'L':
			tileRow = blankRow
			tileCol = blankCol - 1
		else:
			tileRow = blankRow
			tileCol = blankCol + 1
					
		newState = [ [ x for x in y ] for y in state ]
		newState[blankRow][blankCol] = state[tileRow][tileCol]
		newState[tileRow][tileCol] = 0
		newState = tuple([ tuple([ x for x in y ]) for y in newState ])		
		
		return newState
				
	def cost(self, state, action):
		"""Calculate the cost of transitioning from one state to the next."""
		
		return 1

	def tileMoved(self, state, action):
		for i in range(4):
			for j in range(4):
				if state[i][j] == 0:
					blankRow = i
					blankCol = j

				
		if action == 'U':
			return state[blankRow-1][blankCol]
		elif action == 'D':
			return state[blankRow+1][blankCol]
		elif action == 'L':
			return state[blankRow][blankCol-1]
		else:
			return state[blankRow][blankCol+1]
			
	def text(self, state):
		return '\n'.join( [ ' '.join(["%2s"%y if y>0 else "  " for y in x]) for x in state ] )
		
	def initializeDraw(self):
		self._canvas = Canvas(200,200)
		self._canvas.setBackgroundColor('gray')
		self._tiles = [None]
		for i in range(1,16):
			t = TextBox(50,50)
			t.setMessage(str(i))
			t.setFontSize(30)
			t.setFillColor('tan')
			t.setBorderColor('black')
			t.setBorderWidth(3)
			t.moveTo(-500,-500)
			self._tiles.append(t)
			self._canvas.add(t)
			
	def draw(self, state):
		for i in range(4):
			for j in range(4):
				t = state[i][j]
				if t > 0:
					self._tiles[t].moveTo(50*j+25,50*i+25)
		
	def drawAction(self, state, action):
		self.draw(state)
		for i in range(4):
			for j in range(4):
				if state[i][j] == action:
					y,x = i,j	# Where the tile is
				elif state[i][j] == 0:
					b,a = i,j	# Where the blank spot is
					
		for i in range(50):
			self._tiles[action].move( (a-x), (b-y) )
			sleep(.02)
		
		
	def closeDraw(self, state):
		self._canvas.close()

