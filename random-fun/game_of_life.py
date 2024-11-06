from random import randint
from time import sleep

def display_board(board):
	for r in range(len(board)):
		for c in range(len(board[r])):
			if board[r][c] == 1:
				print('@', end=' ')
			else:
				print('.', end=' ')
		print('')
	print('-' * (len(board[0])*2-1))

def count_neighbors(board, r, c):
	count = 0
	for n_r in range(r-1, r+2):
		# Ignore out of bounds
		if n_r < 0 or n_r >= len(board):
			continue
		for n_c in range(c-1, c+2):
			# Ignore out of bounds
			if n_c < 0 or n_c >= len(board[r]):
				continue
			# Ignore self
			if n_r != r or n_c != c:
				count += board[n_r][n_c]
	return count

def compute_next(board, r, c):
	n_neighbors = count_neighbors(board, r, c)

	# If currently alive
	if board[r][c]:
		if n_neighbors < 2:
			return 0
		if n_neighbors < 4:
			return 1
		return 0
	# If currently dead
	if n_neighbors == 3:
		return 1
	return 0

def next_gen(board):
	return [[compute_next(board, r, c) for c in range(len(board[r]))] for r in range(len(board))]

def run_game():
	n_rows = 50
	n_cols = 100

	board = [[randint(0, 1) for c in range(n_cols)] for r in range(n_rows)]

	while True:
		display_board(board)
		board = next_gen(board)
		sleep(0.1)

if __name__ == '__main__':
	run_game()