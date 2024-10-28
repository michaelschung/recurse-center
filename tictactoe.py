from math import prod
from random import randint

# Interpret numbers into Xs and Os
def display_board(board):
	print('=' * 30)
	print('Here is the board:\n')
	for r in range(len(board)):
		for c in range(len(board[r])):
			if board[r][c] == 2:
				print('X\t', end='')
			elif board[r][c] == 3:
				print('O\t', end='')
			else:
				print('-\t', end='')
		print('\n')

# Show space numbers for reference
def instructions():
	print('Here are the spaces.\n')
	print('1\t2\t3\n')
	print('4\t5\t6\n')
	print('7\t8\t9\n')

def comp_turn(board):
	# If X is about to win, stop them
	trios = get_trios(board)
	for i, trio in enumerate(trios):
		if sum(trio) == 4:
			print('X about to win')
			# Rows
			if i < 3:
				for c in range(len(board[i])):
					if board[i][c] == 0:
						board[i][c] = 3
						return
			# Cols
			if i < 6:
				for r in range(len(board)):
					if board[r][i-3] == 0:
						board[r][i-3] = 3
						return
			# Major diagonal
			if i == 6:
				for j in range(len(trio)):
					if trio[j] == 0:
						board[j][j] = 3
						return
			# Minor diagonal
			for j in range(len(trio)):
				if trio[j] == 0:
					board[j][2-j] = 3
					return

	# Otherwise, make random choice
	r = randint(0, 2)
	c = randint(0, 2)
	while board[r][c] != 0:
		r = randint(0, 2)
		c = randint(0, 2)
	board[r][c] = 3

# Process user input - not bothering with choice validation
def make_turn(board, x_turn):
	player = 'X' if x_turn else 'O'

	if x_turn:
		choice = int(input(f'It\'s {player}\'s turn. Choose your space: '))
		r = (choice-1) // 3
		c = (choice-1) % 3
		while board[r][c] != 0:
			choice = int(input(f'That space is already taken. Please choose another: '))
			r = (choice-1) // 3
			c = (choice-1) % 3
		board[r][c] = 2
	else:
		comp_turn(board)
	print('\n' * 5)

def get_trios(board):
	trios = []

	# Include all rows
	trios.extend(board)

	# Include all cols
	for c in range(len(board[0])):
		col = [board[0][c], board[1][c], board[2][c]]
		trios.append(col)

	# Include diagonals (major, then minor)
	trios.append([board[0][0], board[1][1], board[2][2]])
	trios.append([board[0][2], board[1][1], board[2][0]])

	return trios

# Check board for win state. Return:
# 	0 if nothing
# 	1 if X wins
# 	2 if O wins
# 	(cats game left as default at the end)
def game_over(board):
	# Hold all valid trios
	trios = get_trios(board)

	# Check for X or O win
	for trio in trios:
		if prod(trio) == 8:
			return 1
		elif prod(trio) == 27:
			return 2

	# Default if no win state
	return 0

# Display end state
def display_winner(board):
	display_board(board)
	winner = game_over(board)
	if winner == 1:
		print('X wins!')
	elif winner == 2:
		print('O wins!')
	else:
		print('Cats game')

# Main game loop
def play_game():
	# 0 = blank, 2 = X, 3 = O
	board = [[0, 0, 0],
			 [0, 0, 0],
			 [0, 0, 0]]

	# True = X, False = O
	x_turn = True

	n_turns = 0

	while n_turns < 9 and not game_over(board):
		display_board(board)
		instructions()
		make_turn(board, x_turn)
		x_turn = not x_turn
		n_turns += 1

	display_winner(board)

if __name__ == '__main__':
	play_game()