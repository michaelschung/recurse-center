from math import prod

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

# Process user input - not bothering with choice validation
def make_turn(board, x_turn):
	player = 'X' if x_turn else 'O'
	choice = int(input(f'It\'s {player}\'s turn. Choose your space: '))
	r = (choice-1) // 3
	c = (choice-1) % 3
	board[r][c] = 2 if x_turn else 3
	print('\n' * 5)

# Check board for win state. Return:
# 	0 if nothing
# 	1 if X wins
# 	2 if O wins
# 	(cats game left as default at the end)
def game_over(board):
	# Hold all valid trios
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

	# Check for X or Y win
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