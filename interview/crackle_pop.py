def main():
	for i in range(1, 101):
		if not i % 15:
			print('CracklePop')
		elif not i % 3:
			print('Crackle')
		elif not i % 5:
			print('Pop')
		else:
			print(i)

if __name__ == '__main__':
	main()