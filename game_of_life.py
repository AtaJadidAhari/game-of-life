import random

def decision(probability):
    return random.random() < probability

def show_board(board):
	for i in range(2 * (X + 1) + 1):
		for j in range(2 * (Y + 1) + 1):
			if i % 2 == 0:
				print('-', end='')
			else:
				if j % 2 == 0:
					print('|', end='')
				else:
					if board[i//2][j//2] == 1:
						print('#', end='')
					else:
						print(' ', end='')
		print()

def alive_neighbors(board, x, y):
	num = 0
	neighbor = neighbors(x, y) + edge_neighbors(x, y)
	for i in neighbor:
		
		num += board[i[0]][i[1]]
	
	return num



	


def edge_neighbors(x, y):
	neighs = []
	if x == X and y == 0:
		return([(0, 0), (0, Y), (0, 1), (X - 1, Y), (X, Y)])
	elif x == 0 and y == Y:
		return([(0, 0), (1, 0), (X, Y), (X, Y - 1), (X, 0)])
	
	elif x == X and y == Y:
		return([(0, 0), (0, Y), (0, Y - 1), (X, 0), (X - 1, 0)])
	elif x == 0 and y == 0:
		return([(X, Y), (X, 0), (X, 1), (0, Y), (1, Y)])
	if x == X :
		
		neighs.append((0, y))
		if 0 < y < Y:
			neighs.append((0, y + 1))
			neighs.append((0, y - 1))
		elif y == 0:
			neighs.append((0, Y))
			neighs.append((1, Y))
		else:
			neighs.append((0, 0))
			neighs.append((0, 1))
	elif x == 0:
		
		neighs.append((X, y))
		if 0 < y < Y:
			neighs.append((X, y + 1))
			neighs.append((X, y - 1))
		elif y == 0:
			neighs.append((X, Y))
			neighs.append((X, 1))
		else:
			neighs.append((X, 0))
			
	
	if y == 0:
		neighs.append((x, Y))
		if 0 < x < X:
			neighs.append((x - 1, Y))
			neighs.append((x + 1, Y))
		elif x == 0:
			neighs.append((X, Y))
			neighs.append((1, Y))
		else:
			neighs.append((0, Y))

	elif y == Y :
		neighs.append((x, 0))
		if 0 < x < X:
			neighs.append((x - 1, 0))
			neighs.append((x + 1, 0))
		elif x == 0:
			neighs.append((X, 0))
			neighs.append((X, 0))
		else:
			neighs.append((0, 0))
			neighs.append((1, 0))
	return list(set(neighs))
	
neighbors = lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= X and
                                   -1 < y <= Y and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= X) and
                                   (0 <= y2 <= Y))]


def print_done(xy, rule_num):
	
	print("Rule number",  rule_num ,"was applied on" , xy, ".")

def print_undone(xy, rule_num):
	
	print("Rule number",  rule_num ,"was not applied on" , xy , "because of low probability.")




def evolution(board, p):

	new_board = [[0 for i in range(10)] for j in range(10)]
	
	for i in range(X + 1):
		for j in range(Y + 1):
			neighs = alive_neighbors(board, i, j) 
			if board[i][j] == 1:
				

				if neighs < 2: #rule number 1
					if decision(p):
						new_board[i][j] = 0
						print_done([i+1, j+1], 1)
					else:
						new_board[i][j] = 1
						print_undone([i+1, j+1], 1)
				elif neighs > 3: #rule number 3
					if decision(p):
						new_board[i][j] = 0
						print_done([i+1, j+1], 3)
					else:
						new_board[i][j] = 1
						print_undone([i+1, j+1], 3)
				else: #rule number 2
					if decision(p):
						new_board[i][j] = 1
						print_done([i+1, j+1], 2)
					else:
						new_board[i][j] = 1
						print_undone([i+1, j+1], 2)
			else:
				if neighs == 3: #rule number 4
					if decision(p):					
						new_board[i][j] = 1
						print_done([i+1, j+1], 4)
					else:
						new_board[i][j] = 0
						print_undone([i+1, j+1], 4)
				

	return new_board
	





X , Y = map(int, input("Please enter the number of rows and columns of the world.\n").split())

X -= 1
Y -= 1
p = float(input("Please enter probability of p.\n"))






board = [[0 for i in range(10)] for j in range(10)]



num_of_alives = int(input("Please number of entries you want to add.\n"))
for i in range(num_of_alives):
	x, y = map(int, input("Please enter x and y of the cell, seperated by space.\n").split(' '))
	x = x - 1
	y = y -1
	board[x][y] = 1


num_of_iteration = int(input("Please enter number of iterations.\n"))
		

show_board(board)

print("Universe state in step: ", 0)

for i in range(num_of_iteration):
	
	
	input("Press enter to go to next step. \n\n")

	board = evolution(board, p)
	
	show_board(board)
	print("Universe state in step: ", i + 1)
	
	
	









































