# https://projecteuler.net/problem=3

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

def largest_prime_factor(n):
	prime_gen = prime()
	# Loop until number has been reduced to 1
	while n > 1:
		# Get next prime
		next_prime = next(prime_gen)
		# Divide that prime out fully (may be a duplicate factor)
		while n % next_prime == 0:
			n //= next_prime
	# Last prime to be used is the largest prime factor
	return next_prime

print(largest_prime_factor(600851475143))

'''
Found this alternate solution online, and I'm honestly confused about how it works.
Why isn't x restricted to primes? How, then, is it guaranteed that the last factor
	will always be prime?
I'm assuming there's a super simple explanation here, but my brain is dead.
'''

# from itertools import count

# n = 600851475144  
# for x in count(2):
# 	# print(x)
# 	while n % x == 0:
# 		n //= x
# 	if n == 1:
# 		print(x) # largest factor will be the last one
# 		break