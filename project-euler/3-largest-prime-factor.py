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
Found this alternate solution online and it's so stupidly simple that I'm upset.
The overall idea is the same as mine, but you don't even have to restrict the
	divisions to primes.
This works because since each successive prime is fully divided out, it's
	guaranteed that later nonprimes will not be factors.
For example: n = 185130
	// 2 -> 92565 (no longer divisible by 2)
	// 3 -> 30855
	// 3 -> 10285 (no longer divisible by 3)
	// 5 -> 2057 (no longer divisible by 5)
		not divisible by 6 since 2 and 3 are already divided out
		not divisible by 7
		not divisible by 8 since 2 is already divided out
		not divisible by 9 since 3 is already divided out
		not divisible by 10 since 2 and 5 are already divided out
	// 11 -> 187
	// 11 -> 17 (no longer divisible by 11)
		not divisible by 12, 13, 14, 15, or 16...
	// 17 -> 1 (DONE)
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