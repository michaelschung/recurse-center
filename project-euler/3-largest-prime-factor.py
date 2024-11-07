# https://projecteuler.net/problem=3

def is_prime(n):
	for i in range(2, n//2+1):
		if n % i == 0:
			return False
	return True

def primes_up_to(n):
	primes = []
	for i in range(2, n):
		i_is_prime = True
		for prime in primes:
			if prime > i//2+1 or i % prime == 0:
				i_is_prime = False
				break
		if i_is_prime:
			primes.append(i)
	return primes

def largest_prime_factor(n):
	return primes_up_to(n)[-1]

# print(largest_prime_factor(600851475143))
print(largest_prime_factor(40_000_000))