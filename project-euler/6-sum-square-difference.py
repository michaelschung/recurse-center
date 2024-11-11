# https://projecteuler.net/problem=6

def sum_square_diff(n):
	sum_of_squares = 0
	square_of_sums = 0
	for i in range(n+1):
		sum_of_squares += pow(i, 2)
		square_of_sums += i
	square_of_sums = pow(square_of_sums, 2)
	return square_of_sums - sum_of_squares

print(sum_square_diff(100))