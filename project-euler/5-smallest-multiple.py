# https://projecteuler.net/problem=5

from math import prod
from typing import Iterator

# Prime number iterator
def prime() -> Iterator[int]:
	all_primes: [int] = []
	i: int = 1
	while True:
		i += 1
		i_is_prime: bool = True
		# Loop through current known primes
		for prime in all_primes:
			# Being divisible by a prime disqualifies i from being a prime
			if i % prime == 0:
				i_is_prime = False
				break
		# If i is not divisible by any known primes, then i is prime
		if i_is_prime:
			all_primes.append(i)
			yield i

# Get all prime numbers below n
def primes_below(n: int) -> [int]:
	primes_below: [int] = []
	prime_gen: Iterator[int] = prime()
	next_prime: int = next(prime_gen)
	while next_prime < n:
		primes_below.append(next_prime)
		next_prime = next(prime_gen)
	return primes_below

# Main solution - see below for example
def smallest_multiple(n: int) -> int:
	final_vals = []
	for prime in primes_below(n):
		exp: int = 1
		while pow(prime, exp) < n:
			exp += 1
		final_vals.append(pow(prime, exp-1))
	return prod(final_vals)

print(smallest_multiple(10))

'''
EXAMPLE: n = 10
	final_vals: []
	unaccounted: [2, 3, 4, 5, 6, 7, 8, 9, 10]
	PRIME: 2
		Find largest power of 2 less than n: 8
		final_vals: [8] - accounts for powers of 2, reduces all multiples of 2
		unaccounted: [3, 5, 3, 7, 9, 5]
	PRIME: 3
		Find largest power of 3 less than n: 9
		final_vals: [8, 9] - accounts for powers of 3, reduces all multiples of 3
		unaccounted: [5, 7, 5]
	PRIME: 5
		Find largest power of 5 less than n: 5
		final_vals: [8, 9, 5] - accounts for powers of 5, reduces all multiples of 5
		unaccounted: [7]
	PRIME: 7
		Find largest power of 7 less than n: 7
		final_vals: [8, 9, 5, 7] - accounts for powers of 7, reduces all multiples of 7
		unaccounted: []
	prod([8, 9, 5, 7]) = 2520
'''


'''
# Didn't end up using these but extra prime-related functions below:

def prime_factors_below(n: int) -> [int]:
	prime_factors_below: [int] = []
	prime_gen = prime()
	next_prime: int = next(prime_gen)
	while next_prime < n:
		if n % next_prime == 0:
			prime_factors_below.append(next_prime)
		next_prime = next(prime_gen)
	return prime_factors_below

def prime_factorization(n: int) -> [int]:
	prime_factors: [int] = []
	prime_gen = prime()
	while n > 1:
		next_prime = next(prime_gen)
		while n % next_prime == 0:
			prime_factors.append(next_prime)
			n //= next_prime
	return prime_factors
'''
