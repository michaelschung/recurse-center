# https://projecteuler.net/problem=4

def check_palindrome(word: str) -> bool:
	if len(word) <= 1:
		return True
	if word[0] != word[-1]:
		return False
	return check_palindrome(word[1:-1])

def is_palindrome(n: int) -> bool:
	return check_palindrome(str(n))

# n = # digits in each factor
def largest_palindrome_product(n: int) -> int:
	max_palindrome = 1
	max_val: int = int('9' * n)
	for a in range(max_val, 0, -1):
		for b in range(max_val, 0, -1):
			candidate: int = a * b
			if is_palindrome(candidate) and candidate > max_palindrome:
				max_palindrome = candidate
	return max_palindrome

print(largest_palindrome_product(3))