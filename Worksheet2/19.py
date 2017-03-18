def checkRight(board, row, col):
	try:
		if board[row][col+1]:
			return False
		else:
			return True
	except:
		return False
		
def checkLeft(board, row, col):
	try:
		if board[row][col-1]:
			return False
		else:
			return True
	except:
		return False
		
def checkUp(board, row, col):
	try:
		if board[row-1][col]:
			return False
		else:
			return True
	except:
		return False
		
def checkDown(board, row, col):
	try:
		if board[row+1][col]:
			return False
		else:
			return True
	except:
		return False

def display(maze):
	for i in maze:
		print(i)
		
def move(maze, cur_row, cur_col):
	if (cur_row == end_row_index) and (cur_col == end_col_index):
		return True
	else:
		if checkLeft(maze, cur_row, cur_col):
			return move(maze, cur_row, cur_col - 1)
		
		if checkRight(maze, cur_row, cur_col):
			return move(maze, cur_row, cur_col + 1)
			
		if checkUp(maze, cur_row, cur_col):
			return move(maze, cur_row - 1, cur_col)
			
		if checkDown(maze, cur_row, cur_col):
			return move(maze, cur_row + 1, cur_col)
		else:
			return False


import random

rows = 20
cols = 20

while True:
	start_row_index = random.randint(0, rows-1)
	start_col_index = random.randint(0, cols-1)
	end_row_index = random.randint(0, rows-1)
	end_col_index = random.randint(0, cols-1)
	if start_row_index != end_row_index or start_col_index != end_col_index:
		break
		
maze = []

for i in range(rows):
	maze.append([])
	for j in range(cols):
		maze[i].append(random.randint(0, 1))
		
maze[start_row_index][start_col_index] = 0
maze[end_row_index][end_col_index] = 0

display(maze)
print(start_row_index, start_col_index)
print(end_row_index, end_col_index)
print(move(maze, start_row_index, start_col_index))