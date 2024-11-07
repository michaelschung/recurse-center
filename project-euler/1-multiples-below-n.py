# https://projecteuler.net/problem=1

# factors: list of desired values to compute all multiples of
# n: upper bound - find all multiples of factors below n
def sum_of_multiples(factors, n):
	# Use set to avoid overlap
	all_multiples = set()
	for fact in factors:
		all_multiples.update(set([x for x in range(1, n) if x % fact == 0]))
	return sum(all_multiples)

print(sum_of_multiples([3, 5], 1000))