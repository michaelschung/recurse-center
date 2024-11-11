# https://projecteuler.net/problem=7

# Prime number generator
def prime():
	all_primes = []
	i = 1
	while True:
		i += 1
		i_is_prime = True
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

def get_prime(n):
	prime_gen = prime()
	for _ in range(n-1):
		next(prime_gen)
	return next(prime_gen)

print(get_prime(10001))