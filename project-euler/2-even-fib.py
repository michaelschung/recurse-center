# https://projecteuler.net/problem=2

def fib():
	a, b = 1, 2
	while True:
		yield a
		a, b = b, a + b

def sum_even_fib_below(n):
	fibber = fib()
	all_fib_below = []
	next_fib = next(fibber)

	while next_fib < n:
		if next_fib % 2 == 0:
			all_fib_below.append(next_fib)
		next_fib = next(fibber)

	return sum(all_fib_below)

print(sum_even_fib_below(4000000))