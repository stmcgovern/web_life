#reproduce Conway's game of Life

import numpy as np
import random as r
import sys
import pdb


class Board(object):
	def __init__(self, size, attr2, attr3):
		self.size=size
		self.time_steps=attr2
		self.initial_density =attr3
 		self.grid = [[0]*size]*size#np.zeros(shape=(n_size,n_size),dtype=np.int)
 		self.

#TODO:pass as parameters
print sys.argv

if len(sys.argv)==4:

	n_size=int(sys.argv[1])
	time_steps=int(sys.argv[2])
	initial_density =float(sys.argv[3])
else:
	n_size =25
	time_steps=1
	initial_density = 0.8



def main():
	grid=init()
	seed(grid, initial_density)
	print grid

	for i in xrange(time_steps):
		next_grid=Update(grid)
		print next_grid
		grid=next_grid

		
	# print "Game OVER"


#initialize the grid / all 0s
def init():
	
	grid = np.zeros(shape=(n_size,n_size),dtype=np.int)
	return grid

# shoots for initial density (not guaranteed since random might repeat)
def seed(grid, initial_density):
	grains=int(initial_density*(n_size*n_size))
	for x in xrange(grains):
		row=r.randint(1,n_size-2) #leaves edges at 0 during seeding
		col=r.randint(1,n_size-2)
		grid[row][col]=1

def Update(grid):

	next_grid=init()

#just scan through the whole thing
	for row in xrange(1,n_size-1):
		for col in xrange(1,n_size-1):
			
			status=grid[row][col]
			cell = (row,col)
			neighbors = get_neighbors(grid, cell)
			alive_neighbors=sum_neighbors(grid, neighbors)
			i,j=cell
			if(grid[i][j]==0):
				next_grid[i][j]=evolution_0(alive_neighbors)
			else:
				next_grid[i][j]=evolution_1(alive_neighbors)

	return next_grid


def get_neighbors(grid, cell):
	neighbors=[]
	i,j=cell
	#print "i,j", i,j
	neighbors.append((i-1,j-1))
	neighbors.append((i-1,j))
	neighbors.append((i-1,j+1))
	neighbors.append((i,j-1))
	neighbors.append((i,j+1))
	neighbors.append((i+1,j-1))
	neighbors.append((i+1,j))
	neighbors.append((i+1,j+1))
	#print "index", index
	#print "cell", live[index]
	#print "neighbors", neighbors
	return neighbors

def sum_neighbors(grid, neighbors):
	alive_neighbors=0
	for neighbor in neighbors:
		i, j = neighbor
		#print "i,j", i,j
		#print "grid_value", grid[i][j]
		alive_neighbors += grid[i][j]

	# print "alive_neighbors", alive_neighbors
	assert alive_neighbors == sum(grid[i][j] for i, j in neighbors)
	return alive_neighbors

def evolution_0(alive_neighbors): #return 0 or 1 based on rules for dead cell
	if  alive_neighbors== 3:
		return 1
	else:
		return 0

def evolution_1(alive_neighbors): #return 0 or 1 based on rules for alive cell
	if alive_neighbors<2:
		return 0
	elif alive_neighbors <4:
		return 1
	else:
		return 0


# RUNNING THE DARN THING
if __name__ == '__main__':
	main()


